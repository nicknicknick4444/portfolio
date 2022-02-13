import datetime

from django.test import TestCase, Client
from django.utils import timezone
from django.db.models import CharField
from django.urls import reverse
from .forms import ScoreForm

from .models import Scores

# Create your tests here.
 
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


