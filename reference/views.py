from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView

from .models import Book
from .forms import BookForm


class BookView(ListView):
    # We specify the model for list view
    model = Book

def authors_list(request):
    data = Book.objects.all().values_list('author').distinct().order_by('author')
    data = [result_tuple[0] for result_tuple in data]
    return render(request, 'reference/authors_list.html', {'authors': list(data)})

def books_by_author(request, author):
    data = Book.objects.all().filter(author=author).order_by('title')
    return render(request, 'reference/book_list.html', {'object_list': data})

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

def book_lending(resquest, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.is_lent:
        book.is_lent = False
        book.save()
    else:
        book.is_lent = True
        book.save()

    # TODO: UNIT TEST !!!
    return redirect('book_view')