from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book

# Create your views here.
class BookView(ListView):
    # specify the model for list view
    model = Book

def book_new(request):
    form = PostForm()
    return render(request, 'reference/book_edit.html', {'form': form})
