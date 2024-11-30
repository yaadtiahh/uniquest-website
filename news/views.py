from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import News


# Функциональное представление для домашней страницы
def index(request):
    return render(request, 'index.html')  # Убедитесь, что шаблон 'index.html' существует


def news_list(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'news_list.html', {'news_item': news_item})


def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'news_item': news_item})


# Класс-based представление для списка новостей
class NewsListView(ListView):
    model = News
    template_name = 'news_content/news_list.html'  # Шаблон для отображения списка новостей
    context_object_name = 'news'  # Контекст, с которым будет работать шаблон


# Класс-based представление для деталей одной новости
class NewsDetailView(DetailView):
    model = News
    template_name = 'news_content/news_detail.html'  # Шаблон для отображения новости по slug
    context_object_name = 'news'  # Контекст для шаблона
