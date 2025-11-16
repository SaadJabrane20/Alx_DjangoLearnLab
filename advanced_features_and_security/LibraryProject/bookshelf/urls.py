from django.urls import path
from .views import book_list, test_view
urlpatterns = [
    path('booklist/',book_list,name = 'book_list'),
    path('test/', test_view, name='test'),
]