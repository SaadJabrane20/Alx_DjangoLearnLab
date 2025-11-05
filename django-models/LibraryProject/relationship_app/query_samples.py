from models import *
books = Book.objects.filter(author__name="")
books = Library.books.all()
librarian = Librarian.objects.get(name=library_name)
library = librarian.library