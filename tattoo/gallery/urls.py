from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


urlpatterns = [
    path('', views.GalleryView.as_view(), name='gallery')
]
