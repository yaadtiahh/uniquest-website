from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News


# Функциональное представление для домашней страницы
def index(request):
    return render(request, 'index.html')  # Убедитесь, что шаблон 'home.html' существует


# Класс-based представление для списка новостей
class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'  # Шаблон для отображения списка новостей
    context_object_name = 'news'  # Контекст, с которым будет работать шаблон


# Класс-based представление для деталей одной новости
class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'  # Шаблон для отображения новости по slug
    context_object_name = 'news'  # Контекст для шаблона
