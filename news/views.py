from django.shortcuts import render, get_object_or_404
from .models import News


# Функциональное представление для домашней страницы
def index(request):
    return render(request, 'index.html')  # Убедитесь, что шаблон 'index.html' существует


def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'index.html', {'news_item': news_item})


def news_list(request):
    news_list = News.objects.filter(is_visible=True).order_by('-published_date')
    return render(request, 'index.html', {'news_list': news_list})
