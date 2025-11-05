from models import *

author = Author.objects.get(name = author_name)
books = Book.objects.filter(author=author)
books = books.all()
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(name="")
library = librarian.library