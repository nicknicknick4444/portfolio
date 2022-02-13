import datetime

from django.test import TestCase, Client
from django.utils import timezone
from django.db.models import CharField
from django.urls import reverse
from .forms import ChoiceForm, ScoreForm

from .models import Question, Choice, Scores

# Create your tests here.
 
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
    
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
    
    def test_Was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
    
    def test_question_text_is_charfield(self):
        the_field = Question._meta.get_field("question_text")
        self.assertIs(isinstance(the_field, CharField), True)

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

def create_choice(question, choice_text):
    return Choice.objects.create(question=question, choice_text=choice_text, votes=0)

class QuestionIndexViewsTests(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse("squaresg:indexu"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
    
    def test_old_question(self):
        question = create_question(question_text="Old question", days=-30)
        choice = create_choice(question=question, choice_text="Peas")
        response = self.client.get(reverse("squaresg:indexu"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])
    
    def test_future_question_without_choice(self):
        question = create_question(question_text="Future question", days=30)
        response = self.client.get(reverse("squaresg:indexu"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
    
    def test_future_question_with_choice(self):
        question = create_question(question_text="Beans?",days=30)
        choice = create_choice(question=question, choice_text="Glusp")
        response =  self.client.get(reverse("squaresg:indexu"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
    
    def test_old_and_future_question(self):
        question1 = create_question(question_text="Future question", days=round(30,0))
        question2 = create_question(question_text="Old question", days=round(-30,0))
        choice1 = create_choice(question=question1, choice_text="Goosey1")
        choice2 = create_choice(question=question2, choice_text="Goosey2")
        response = self.client.get(reverse("squaresg:indexu"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question2])
        #print(question1.pub_date-question2.pub_date)
        #self.assertEqual(question1.pub_date-question2.pub_date, datetime.timedelta(days=60))
    
    def test_two_old_questions(self):
        question1 = create_question(question_text="Old question 1", days=-30)
        question2 = create_question(question_text="Old question 2", days=-5)
        choice1 = create_choice(question=question1, choice_text="Gist1")
        choice2 = create_choice(question=question2, choice_text="Gist2")
        response = self.client.get(reverse("squaresg:indexu"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question2, question1])
    
    def test_choiceless_questions_banned(self):
        question = create_question(question_text="Tixt", days=-30)
        choice = create_choice(question=question, choice_text="Grass")
        response = self.client.get(reverse("squaresg:indexu"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])
    
    def test_choicey_question_included(self):
        question = create_question(question_text="Gas", days=-5)
        choice = create_choice(question=question, choice_text="Peas!")
        response = self.client.get(reverse("squaresg:indexu"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])
    
class QuestionDetailViewTests(TestCase):
    
    def test_future_question_with_choice_detail(self):
        future_question1 = create_question(question_text="Goose", days=30)
        future_choice = create_choice(question=future_question1, choice_text="Syrup")
        url = reverse("squaresg:detail", args=(future_question1.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_future_question_without_choice_detail(self):
        future_question2 = create_question(question_text="Future question", days=30)
        url = reverse("squaresg:detail", args=(future_question2.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_old_question_with_choice_detail(self):
        old_question = create_question(question_text="Old question", days=-5)
        old_choice = create_choice(question=old_question, choice_text="She's A River")
        url = reverse("squaresg:detail", args=(old_question.id,))
        response = self.client.get(url)
        goose = old_question.choice_set.all()
        print(goose)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, old_question.question_text)
    
    def test_choiceless_old_question_without_choice_detail(self):
        old_question = create_question(question_text="Old question", days=-5)
        url = reverse("squaresg:detail", args=(old_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

class QuestionResultsViewTest(TestCase):
    
    def test_future_results_with_choice(self):
        future_question1 = create_question(question_text="Future question 1", days=30)
        future_choice1 = create_choice(question=future_question1, choice_text="Spoons eh?")
        url = reverse("squaresg:results", args=(future_question1.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_future_results_without_choice(self):
        future_question2 = create_question(question_text="Future question 2", days=30)
        url = reverse("squaresg:results", args=(future_question2.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_old_results_with_choice(self):
        old_question = create_question(question_text="Old question", days=-5)
        old_choice = create_choice(question=old_question, choice_text="Geese?")
        url = reverse("squaresg:results", args=(old_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_old_results_without_choice(self):
        old_question2 = create_question(question_text="Old question2", days=-30)
        url = reverse("squaresg:results", args=(old_question2.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

class VotesViewTest(TestCase):
    
    def test_votes_increment(self):
        question = create_question(question_text="Gusp", days=-30)
        choice = create_choice(question=question, choice_text="Grast")
        selected_choice = question.choice_set.get(pk=1)
        selected_choice.votes += 1
        print(selected_choice)
        print(selected_choice.votes)
        url = reverse("squaresg:results", args=(question.id,))
        response = self.client.get(url)
        print(response)
        print(question.choice_set.get())
        self.assertEqual(selected_choice.votes, 1)
        self.assertEqual(response.status_code, 200)

class NewChoiceFormTest(TestCase):
    
    def test_new_choice_form(self):
        question = create_question(question_text="Gart", days=-5)
        choiceo = create_choice(choice_text="choicey gorks text", question=question)
        fields={"addey":"True", "choice_text":"Choooooorssssse", "question":"question"}
        formy = ChoiceForm(fields)
        self.assertIs(formy.is_valid(), True)
        response = self.client.post("/1/addey/", data=fields)
        print(response.status_code, 302)
        print(response)
        try:
            print(question.choice_set.all(), "Kelk")
            print(Choice.objects.all(), "Clix")
        except Exception as e:
            print(e, "Mini Classics")
        self.assertEqual(response.status_code, 302)
        #self.assertIn("Choooooorssssse", str(Choice.objects.all()))
        
def create_score(namey, score):
    return Scores.objects.create(namey=namey, score = score)

class SquaresViewTest(TestCase):
    
    def test_squares_page_works(self):
        response = self.client.get(reverse("squaresg:squares"))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context["nine_squares_list"][0], "square_1.png")
        self.assertTemplateUsed(response, "polls/squares.html")
    
    def test_randomise2_of_squares(self):
        self.client.post("squares_rand")
        response = self.client.get(reverse("squaresg:squares"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("token.png", str(response.context["nine_squares_list"]))
        self.assertTemplateUsed(response, "polls/squares.html")
    
    def test_reset_view(self):
        response = self.client.post("resetto")
        response = self.client.get(reverse("squaresg:squares"))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context["nine_squares_list"], ["square_1.png","square_2.png","square_3.png",
                 "square_4.png","square_5.png","square_6.png",
                 "square_7.png","square_8.png","square_9.png"] or ["square_1.png","token.png","square_3.png",
                 "square_4.png","token.png","square_6.png",
                 "square_7.png","square_8.png","square_9.png"])
        self.assertEqual(len(response.context["nine_squares_list"]), 9)
        self.assertEqual(response.context["nine_squares_list"][0][-3:], "png")
    
    def test_leaderboard(self):
        scores = create_score(namey="Franklinie", score=6)
        fields = {"saveIt":"True", "namey":"Jarth", "score":"33"}
        form = ScoreForm(fields)
        self.assertIs(form.is_valid(), True)
        response = self.client.post("/saveIt/", data=fields)
        print(response.status_code, 302)
        print("Hursh", response)
        print(Scores.objects.all())
        self.assertIn("Jarth", str(Scores.objects.all()[1]))


