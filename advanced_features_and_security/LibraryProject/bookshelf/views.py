from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm
from django.http import HttpResponse
# Create your views here.


@permission_required('bookshelf.can_view',raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request,'bookshelf/book_list.html',{'books' : books})

# bookshelf/views.py

def test_view(request):
    return HttpResponse("Hello World")
