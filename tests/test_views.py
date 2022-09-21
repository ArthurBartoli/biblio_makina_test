from django.test import TestCase
from reference.models import Book

class BookListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        nb_books = 42

        for book_id in range(nb_books):
            Book.objects.create(
                title=f'Titre {book_id}',
                og_title=f'Title {book_id}',
                author=f'Auteur {book_id}',
                desc=f'Desc {book_id}',
                isbn=f'ISBN-{book_id}',
                published_year=2020 + book_id,
                is_lent=True
            )

    def test_view_url_exists_at_desired_location(self):
        """The main page displays correctly"""
        response = self.client.get('http://0.0.0.0:8000')
        self.assertEqual(response.status_code, 200)
