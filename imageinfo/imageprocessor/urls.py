from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_images, name='upload_images'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('imageprocessor.urls')),  # Подключаем маршруты приложения
]
