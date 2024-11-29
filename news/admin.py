from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News


def home(request):
    return render(request, 'index.html')


class NewsListView(ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news"
    paginate_by = 5  # Постраничная навигация


class NewsDetailView(DetailView):
    model = News
    template_name = "news/news_detail.html"
    context_object_name = "news_item"
