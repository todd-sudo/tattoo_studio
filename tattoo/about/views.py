from django.views.generic import ListView, DetailView

from services.views_exceptions import BaseView
from .models import InformationBlock, Article


class HomeView(ListView, BaseView):
    """Выводит главную страницу"""
    model = InformationBlock
    context_object_name = 'blocks'
    template_name = 'about/home.html'


class AboutView(ListView, BaseView):
    """Выводит страницу О нас"""
    queryset = Article.objects.all()
    context_object_name = 'articles'
    template_name = 'about/about.html'


class ArticlesDetail(DetailView, BaseView):
    """Выводит полностью статью"""
    queryset = Article.objects.all()
    context_object_name = 'article'
    template_name = 'about/about_detail.html'
