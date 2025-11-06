from django.contrib import admin
from django.urls import path
from . import views
from .views import BookListView
urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('librarydetail/', BookListView.as_view(), name='library_detail'),
    ]
