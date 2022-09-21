from django import forms

from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'og_title', 'author', 'desc', 'isbn', 'published_year', 'is_lent')
        