from django.shortcuts import render, get_object_or_404
from .models import Author, Book, Library, Librarian
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
