from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('news/', views.news, name='news_list'),
]
