from django.contrib import admin
from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
urlpatterns = [
    path('list_books', views.list_books, name='list_books'),
    path('library_detail', views.library_detail, name='library_detail'),
]
