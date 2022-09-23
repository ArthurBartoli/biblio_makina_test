from django.test import TestCase
from django.urls import reverse

from http import HTTPStatus

from reference.models import Book
from reference.forms import BookForm

class AddBookViewTest(TestCase):

    def setUp(self):
        dummyData = {}
        dummyData['title'] = "Le Test"
        dummyData['og_title'] = "The Test"
        dummyData['author'] = "Mister Test"
        dummyData['desc'] = "Ceci n'est pas un test"
        dummyData['isbn'] = "74-86-Le-Test"
        dummyData['published_year'] = 2022
        dummyData['is_lent'] = False

        self.data = dummyData

    def test_post_success(self):
        '''Is a new book correctly added to the DB ?'''
        response = self.client.post(reverse('book_new'), data=self.data)

        # We check that the data is valid
        form = BookForm(data=self.data)
        self.assertTrue(form.is_valid())

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], reverse('book_view'))

class EditBookViewTest(TestCase):

    def setUp(self):
        self.test_book = Book.objects.create(
                title='Titre',
                og_title='Title',
                author='Auteur',
                desc='Desc',
                isbn='ISBN',
                published_year=1,
                is_lent=True
            )
        
        dummyData = {}
        dummyData['title'] = "Le Test"
        dummyData['og_title'] = "The Test"
        dummyData['author'] = "Mister Test"
        dummyData['desc'] = "Ceci n'est pas un test"
        dummyData['isbn'] = "74-86-Le-Test"
        dummyData['published_year'] = 2022
        dummyData['is_lent'] = False

        self.data = dummyData

    def test_edit_success(self):
        '''Is a book correctly edited in the DB ?'''
        response = self.client.post(reverse('book_edit', args=[self.test_book.pk]), data=self.data)

        # We check that the data is valid
        form = BookForm(data=self.data)
        self.assertTrue(form.is_valid())

        # Checking status
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], reverse('book_view'))

        # Checking changes were made
        new_book = Book.objects.get(pk=self.test_book.pk)
        for k in self.data:
            val = getattr(new_book, k)
            self.assertEqual(val, self.data[k])


class DeleteBookViewTest(TestCase):

    def setUp(self):
        self.test_book = Book.objects.create(
                title='Titre',
                og_title='Title',
                author='Auteur',
                desc='Desc',
                isbn='ISBN',
                published_year=1,
                is_lent=True
            )

    def test_delete_success(self):
        '''Is a book correctly deleted from the DB ?'''
        response = self.client.get(reverse('book_delete', args=[self.test_book.pk]))

        # Checking status
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], reverse('book_view'))

        # Checking the object is deleted
        self.assertFalse(Book.objects.filter(pk=self.test_book.pk).exists())

class LendingBookViewTest(TestCase):

    def setUp(self):
        self.test_book_lent = Book.objects.create(
                title='Titre',
                og_title='Title',
                author='Auteur',
                desc='Desc',
                isbn='ISBN',
                published_year=1,
                is_lent=True
            )
        
        self.test_book_not_lent = Book.objects.create(
                title='Titre',
                og_title='Title',
                author='Auteur',
                desc='Desc',
                isbn='ISBN',
                published_year=1,
                is_lent=False
            )

    def test_unlending_success(self):
        '''Is a book's lending status correctly changed to false from the DB ?'''
        response = self.client.get(reverse('book_lending', args=[self.test_book_lent.pk]))

        # Checking status
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], reverse('book_view'))

        # Checking the object has lent status corrected
        new_book = Book.objects.get(pk=self.test_book_lent.pk)
        self.assertFalse(getattr(new_book, 'is_lent'))

    def test_lending_success(self):
        '''Is a book's lending status correctly changed to true from the DB ?'''
        response = self.client.get(reverse('book_lending', args=[self.test_book_not_lent.pk]))

        # Checking status
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], reverse('book_view'))

        # Checking the object has lent status corrected
        new_book = Book.objects.get(pk=self.test_book_not_lent.pk)
        self.assertTrue(getattr(new_book, 'is_lent'))

class AuthorsListViewTest(TestCase):

    def setUp(self):
        self.data = []

        authors = ['Bob', 'Alice', 'Zeitoun', 'Alice', 'Dan']

        for author in authors:
            self.data = Book.objects.create(
                title='Titre',
                og_title='Title',
                author=author,
                desc='Desc',
                isbn='ISBN',
                published_year=1,
                is_lent=False
            )

    def test_display_success(self):
        '''Is the list of unique authors displayed as intended ? 
        '''

        response = self.client.get(reverse('authors_list'))

        authors = ['Alice', 'Bob', 'Dan', 'Zeitoun']
        for author in authors:
            self.assertContains(response, author)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        


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
        self.assertEqual(response.status_code, HTTPStatus.OK)
        

    def test_view_response_new_book(self):
        """The new book page displays correctly"""
        response = self.client.get(reverse('book_new'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
    def test_view_response_author_list(self):
        """The lending set book page displays correctly"""
        response = self.client.get(reverse('authors_list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_view_response_books_by_author(self):
        response = self.client.get(reverse('books_by_author', args=[self.test_books[0].author]))
        self.assertEqual(response.status_code, HTTPStatus.OK) 
    

    def test_view_response_edit_book(self):
        """The book edit page displays correctly"""
        response = self.client.get(reverse('book_edit', args=[self.test_books[0].pk]))
        self.assertEqual(response.status_code, HTTPStatus.OK)
    def test_view_response_delete_book(self):
        """The delete book page displays correctly"""
        response = self.client.get(reverse('book_delete', args=[self.test_books[1].pk]))
        self.assertEqual(response.status_code, HTTPStatus.FOUND) # The user is redirected..
        self.assertEqual(response["Location"], reverse('book_view')) # ..to main page
    def test_view_response_lending_book(self):
        """The lending set book page displays correctly"""
        response = self.client.get(reverse('book_lending', args=[self.test_books[2].pk]))
        self.assertEqual(response.status_code, HTTPStatus.FOUND) # The user is redirected..
        self.assertEqual(response["Location"], reverse('book_view')) # ..to main page
    
    
