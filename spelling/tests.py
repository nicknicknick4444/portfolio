from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
# Create your tests here.

from .models import Admonish, TweetLists

def create_admonish(adm_id, adm_term, adm_text):
    return Admonish.objects.create(adm_id=adm_id, adm_term=adm_term, adm_text=adm_text)

def create_tw(twe_dict, twe_term, twe_seshn, twe_time):
    return TweetLists.objects.create(twe_dict=twe_dict, twe_term=twe_term, twe_seshn=twe_seshn, twe_time=twe_time)

class TweetsViewText(TestCase):
    def test_main_spelling_page_works(self):
        response = self.client.get(reverse("spelling:index"))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context["wordu"], "beaky")
        self.assertTemplateUsed(response, "spelling/index.html")
    
    def test_Admonish(self):
        admon = create_admonish(adm_id=1, adm_term="ghist", adm_text="Shut up")
        setto = Admonish.objects.all()
        response = self.client.get(reverse("spelling:index"))
        print(setto)
        self.assertQuerysetEqual(setto, [admon])
    
    def test_TweetLists(self):
        tweeto = create_tw(twe_dict="{\"Yes\":\"1\"}", twe_term="calvert", twe_seshn=44444, twe_time=timezone.now())
        setto = TweetLists.objects.all()
        resposne = self.client.get(reverse("spelling:index"))
        print(setto)
        self.assertQuerysetEqual(setto, [tweeto])
    
    def test_wordu(self):
        response = self.client.get(reverse("spelling:index"))
        print(response.context["wordu"])
        self.assertEqual(response.context["wordu"],"blanku")

        

#twe_dict="{\"Yes\":\"1\"}", twe_term="calvert",
