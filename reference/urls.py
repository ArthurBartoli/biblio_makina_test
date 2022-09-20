from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookView.as_view(), name='book_view'),
    path('book/new/', views.book_new, name='book_new'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete')
]