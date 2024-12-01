from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('news_list/', views.news_list, name='news_list'),  # Список новостей
    path('news_detail/<int:pk>/', views.news_detail, name='news_detail'),  # Детали новости
]
