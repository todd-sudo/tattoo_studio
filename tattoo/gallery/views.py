from django.views.generic import ListView

from services.views_exceptions import BaseView
from .models import CategoryTattoo


class GalleryView(ListView, BaseView):
    queryset = CategoryTattoo.objects.prefetch_related('gallery_category')
    context_object_name = 'categories'
    template_name = 'gallery/gallery.html'
    paginate_by = 20
