from django.urls import path
from .views import *
urlpatterns = [
    path('books/',BookListView.as_view()),
    path('books/<int:pk>/',BookDetailView.as_view()),
    path('createbook/',BookCreateView.as_view()),
    path('updatebook/',BookUpdateView.as_view()),
    path('deletebook/',BookDeleteView.as_view()),
]