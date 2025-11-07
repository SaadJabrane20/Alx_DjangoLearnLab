from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, SignUpView
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('librarydetail/', LibraryDetailView.as_view(), name='LibraryDetailView'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    ]
