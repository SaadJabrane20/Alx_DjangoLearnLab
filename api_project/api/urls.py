from rest_framework import routers
from .views import BookList, BookViewSet, LoginAPIView
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('', include(router.urls)),  # This includes all routes registered with the router
    path('login/',LoginAPIView)
]