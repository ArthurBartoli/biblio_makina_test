from django.shortcuts import render, redirect, get_object_or_404
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
            ### TODO: Include ISBN formatting
            book.save()
            return redirect('book_view')
    else:
        form = BookForm()
    return render(request, 'reference/book_edit.html', {'form': form})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            ### TODO: Include ISBN formatting
            book.save()
            return redirect('book_view')
    else:
        form = BookForm(instance=book)
    return render(request, 'reference/book_edit.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_view')
