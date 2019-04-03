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
        'check_username/username=<username>',
        UserCreateView.as_view(),
        name='check_username',
    ),
    path('', UserRetrieveUpdateDestroyView.as_view(), name='user'),
]
