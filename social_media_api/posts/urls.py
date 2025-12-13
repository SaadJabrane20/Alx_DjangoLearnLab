from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedAPIView
from django.urls import path
router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('feed/', FeedAPIView.as_view(), name='feed'),
]