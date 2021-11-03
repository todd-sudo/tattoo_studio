from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('article/<str:slug>', views.ArticlesDetail.as_view(), name='article_detail'),
    path('about/', views.AboutView.as_view(), name='about'),
]
