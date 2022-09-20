from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_view, name='book_view'),
]