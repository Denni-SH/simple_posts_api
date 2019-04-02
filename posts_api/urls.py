"""posts_api URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

API_PATH = f"api/v1"

urlpatterns = [
    path(f'admin/', admin.site.urls),
    path(f'{API_PATH}/user/', include('apps.users.urls')),
  ]
