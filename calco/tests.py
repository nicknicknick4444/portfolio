from django.test import TestCase
from django.urls import reverse
from http.cookies import SimpleCookie
from django.shortcuts import render

# Create your tests here.

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
