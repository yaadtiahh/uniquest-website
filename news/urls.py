from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('news_list/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
]
