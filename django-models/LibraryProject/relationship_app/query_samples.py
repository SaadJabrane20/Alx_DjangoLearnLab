from models import *
books = Book.objects.filter(author__name="")
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(name="")
library = librarian.library