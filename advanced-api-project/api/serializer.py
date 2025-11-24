from rest_framework import serializers
from .models import Book, Author
from datetime import date

#this Serializer will handle the serialization of the Book model which will include all its fields, 
#and also it had validation function which validate the year of publication to not be in the future
class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = "__all__"
	def validate_publication_year(self, value):
		current_year = date.today().year
		if value > current_year:
			raise serializers.ValidationError("Publication year cannot be in the future.")
		return value
	
#this serializer will handle the Author serializer, it has a nested serializer that include the book serializer so an author,
#will be displayed with all his books, and the fields to be serialized are the author name and books
class AuthorSerializer(serializers.ModelSerializer):
	books = BookSerializer(many = True, read_only = True)
	class meta:
		model = Author
		fields = ["name", "books"]