from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book

# Create your views here.
class BookView(ListView):
    # specify the model for list view
    model = Book
