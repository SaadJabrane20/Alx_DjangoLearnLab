from rest_framework import routers
from .views import BookList
from django.urls import path


# router = routers.DefaultRouter()
# router.register(r'books', BookList)

# urlpatterns = router.urls

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]