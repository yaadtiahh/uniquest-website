from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('news_list/', views.NewsListView.as_view(), name='news_list'),  # Для списка новостей
    path('<slug:slug>/', views.NewsDetailView.as_view(), name='news_detail')
]
