from django.db import models

# Create your models here.

#this model will handle the author name
class Author(models.Model):
	name = models.CharField(max_length = 225)
	def __str__(self):
		return self.name
#this model will handle the book model and it has an author field which is related to the Author class as a FK
class Book(models.Model):
	title = models.CharField(max_length = 225)
	publication_year = models.DateField()
	author = models.ForeignKey(Author, related_name='books',on_delete = models.CASCADE)
	def __str__(self):
		return self.title
