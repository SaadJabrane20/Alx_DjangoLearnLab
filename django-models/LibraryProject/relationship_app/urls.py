from django.contrib import admin
from django.urls import path
from .views import list_books, LibraryDetailView
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('librarydetail/', LibraryDetailView.as_view(), name='LibraryDetailView'),
    ]
