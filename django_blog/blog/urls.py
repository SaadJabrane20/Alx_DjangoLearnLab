from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import register_view
urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name="logout"),
    path('register/', register_view, name="register"),
]   