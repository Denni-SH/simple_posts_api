from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token

from .views import (
    UserCreateView,
    UserLoginView,
    UserRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('auth/registration', UserCreateView.as_view(), name='register'),
    path('auth/login', UserLoginView.as_view(), name='login'),
    path('auth/refresh_token', refresh_jwt_token, name='refresh_token'),

    path(
        'get_or_update_user_info',
        UserRetrieveUpdateDestroyView.as_view(),
        name='get_or_update_user_info',
    ),
    path(
        'delete_user',
        UserRetrieveUpdateDestroyView.as_view(),
        name='delete_user',
    ),
    path(
        'check_username/username=<username>',
        UserLoginView.as_view(),
        name='check_username',
    ),
]
