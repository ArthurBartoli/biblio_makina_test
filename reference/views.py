from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Book
from .forms import BookForm


class BookView(ListView):
    # We specify the model for list view
    model = Book

def book_new(request):

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_view')
    else:
        form = BookForm()
    return render(request, 'reference/book_edit.html', {'form': form})
