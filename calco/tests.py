from django.test import TestCase
from django.urls import reverse
from http.cookies import SimpleCookie
from django.shortcuts import render

from .models import Colour

# Create your tests here.

def create_colour(colour_name, colour_hex):
    return Colour.objects.create(colour_name=colour_name, colour_hex=colour_hex)

class CalcTest(TestCase):
    def test_main_calc_page_works(self):
        response = self.client.get(reverse("calco:calc1"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "calco/calc1.html")
        self.assertContains(response, "Calc 2&nbsp;&nbsp;", html=True)
        self.client.cookies = SimpleCookie({"templ8": "2"})
    
    def test_first_function_redirects(self):
        response = self.client.post(reverse("calco:first"))
        self.assertEqual(response.status_code, 302)
    
    def test_colour_in_db(self):
        colour_make = create_colour(colour_name="white", colour_hex="#ffffff")
        colour_set = Colour.objects.all()
        self.assertQuerysetEqual(colour_set, [colour_make])

