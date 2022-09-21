from django.test import TestCase

from reference.forms import BookForm

class FormTestCase(TestCase):
    def test_add_book_valid(self):
            """Is the add function functionning correctly ?"""
            dummyData = {}
            dummyData['title'] = "Le Test"
            dummyData['og_title'] = "The Test"
            dummyData['author'] = "Mister Test"
            dummyData['desc'] = "Ceci n'est pas un test"
            dummyData['isbn'] = "74-86-Le-Test"
            dummyData['published_year'] = 2022
            dummyData['is_lent'] = False

            form = BookForm(data=dummyData)
            self.assertTrue(form.is_valid())