"""posts_api URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

API_PATH = "api/v1"
schema_view = get_swagger_view(title = "Posts API Doc")

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{API_PATH}/user/', include('apps.users.urls')),
    path(f'{API_PATH}/posts/', include('apps.posts.urls')),
    path(f'{API_PATH}', schema_view),
]
