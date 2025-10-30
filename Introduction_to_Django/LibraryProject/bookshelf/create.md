from django.db import models

book = Book.objects.create(
    title = "1984   ",
    author = "George Orwell",
    publication_year = 1949
)

#creation successfull