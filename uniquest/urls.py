from django.contrib import admin
from django.urls import path, include  # Для использования include()

urlpatterns = [
    path('admin/', admin.site.urls),  # Страница администратора
    path('news/', include('news.urls')),  # Ссылка на приложение новостей
    path('', include('home.urls')),  # Главная страница, если есть приложение home
]
