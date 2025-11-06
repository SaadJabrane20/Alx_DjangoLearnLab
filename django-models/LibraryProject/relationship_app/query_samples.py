from models import Book, Author, Library, Librarian

author  = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

books = Library.books.all()

librarian = Librarian.objects.get(library=library)

