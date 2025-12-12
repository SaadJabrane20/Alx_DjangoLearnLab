from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from .views import can_add_book, can_change_book, can_delete_book

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('librarydetail/', LibraryDetailView.as_view(), name='LibraryDetailView'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('member_view/', views.member_view, name='member_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('add_book/', views.can_add_book, name='add_book'),
    path('edit_book/', views.can_change_book, name='change_book'),
    path('delete_book/', views.can_delete_book, name='delete_book'),
]
