import datetime

from django.test import TestCase

# Create your tests here.

from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

from .models import Entry, User

def create_entry(title, detail, date_for, user, by, mod_by, created, last_modified):
    return Entry.objects.create(title=title, detail=detail, date_for=date_for, user=user, \
                        by=by, mod_by=mod_by, created=created, last_modified=last_modified)

def this_now():
    return datetime.datetime.now().date()

class EntriesListTest(TestCase):
    def test_diary_page_works(self):
        response = self.client.get(reverse("diary:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diary/list_entries.html")
    
    def test_entry_model(self):
        entry = create_entry("V444444", "This is a diary note!", this_now(), "Nick", "Nick", "Nick", this_now(), this_now())
        setto = Entry.objects.all()
        print(setto)
        self.assertQuerysetEqual(setto, [entry])
    
    def test_edit_page(self):
        entry = create_entry("V444444", "This is a diary note!", this_now(), "Nick", "Nick", "Nick", this_now(), this_now())
        self.user = User.objects.create_user(username="testuser", password="123456", first_name="Testuser")
        login = self.client.login(username="testuser", password="123456")
        response = self.client.get(reverse("diary:edit2", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diary/edit_entry.html")
    
    def test_new_page(self):
        self.user = User.objects.create_user(username="gruff", password="slim", first_name="Gruss")
        login = self.client.login(username="gruff", password="slim")
        response = self.client.get(reverse("diary:new"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diary/new_entry.html")
    
    def test_delete_page(self):
        entry = create_entry("V444444", "This is a diary note!", this_now(), "Nick", "Nick", "Nick", this_now(), this_now())
        self.user = User.objects.create_user(username="testuser", password="123456", first_name="Testuser")
        login = self.client.login(username="testuser", password="123456")
        response = self.client.get(reverse("diary:delete", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "diary/delete_entry.html")




