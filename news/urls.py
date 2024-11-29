from django.urls import path
from . import views


urlpatterns = [
    path('news/', views.home, name='home'),
    path('news_list/', views.NewsListView.as_view(), name='news_list'),  # Для списка новостей
    path('<slug:slug>/', views.NewsDetailView.as_view(), name='news_detail'),  # Для деталей новости
]
