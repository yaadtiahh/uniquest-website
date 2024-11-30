from django.urls import path
from . import views


urlpatterns = [
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('news_list/', views.info_center, name='news_list'),
]
