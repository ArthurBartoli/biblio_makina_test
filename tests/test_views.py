from django.test import TestCase
from django.urls import reverse

from reference.models import Book




class ViewResponseTest(TestCase):

    def setUp(self):
        self.test_books =[]
        sample = 3
        for i in range(3):
            tmp = Book.objects.create(
                    title='Titre',
                    og_title='Title',
                    author='Auteur',
                    desc='Desc',
                    isbn='ISBN',
                    published_year=1,
                    is_lent=True
                )
            self.test_books.append(tmp)


    def test_view_response_main(self):
        """The main page displays correctly"""
        response = self.client.get(reverse('book_view'))
        self.assertEqual(response.status_code, 200)

    def test_view_response_new_book(self):
        """The new book page displays correctly"""
        response = self.client.get(reverse('book_new'))
        self.assertEqual(response.status_code, 200)

    def test_view_response_edit_book(self):
        """The book edit page displays correctly"""
        response = self.client.get(reverse('book_edit', args=[self.test_books[0].pk]))
        self.assertEqual(response.status_code, 200)
    def test_view_response_delete_book(self):
        """The delete book page displays correctly"""
        response = self.client.get(reverse('book_delete', args=[self.test_books[1].pk]))
        self.assertEqual(response.status_code, 302) # The user is redirected
    def test_view_response_lending_book(self):
        """The lending set book page displays correctly"""
        response = self.client.get(reverse('book_lending', args=[self.test_books[2].pk]))
        self.assertEqual(response.status_code, 302) # The user is redirected
