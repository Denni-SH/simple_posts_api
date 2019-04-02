from django.urls import path

from .views import (
    PostCreateView, PostRetrieveUpdateDestroyView, PostListView,
)

urlpatterns = [
    path(
        'create_post', PostCreateView.as_view(), name='create_post'),
    path(
        'id=<int:pk>',
        PostRetrieveUpdateDestroyView.as_view(),
        name='post',
    ),
    path('', PostListView.as_view(), name='get_posts_list'),
]
