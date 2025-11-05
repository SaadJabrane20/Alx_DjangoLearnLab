from django.shortcuts import render, get_object_or_404
from .models import Author, Book, Library, Librarian

# List all books by a specific author
def list_books(request, author_name=None):
    if author_name:
        author = get_object_or_404(Author, name=author_name)
        books = Book.objects.filter(author=author)
    else:
        books = Book.objects.all()
        author = None
    return render(request, 'list_books.html', {'books': books, 'author': author})


# Show details for a specific library
def library_detail(request, library_name):
    library = get_object_or_404(Library, name=library_name)
    books = library.books.all()
    librarian = getattr(library, 'librarian', None)
    return render(
        request,
        'library_detail.html',
        {'library': library, 'books': books, 'librarian': librarian},
    )