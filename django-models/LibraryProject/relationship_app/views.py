from django.shortcuts import render
from models import *
from .models import Library
# Create your views here.
def list_books(request):
    book = Book.objects.all()
    return render(request, 'relationship_app/list_books.html')

def library_detail(request):
    library = Library.objects.all()
    return render(request, 'relationship_app/library_detail.html')