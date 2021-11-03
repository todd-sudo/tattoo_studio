from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

import debug_toolbar

from .utils import e_handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('', include('about.urls')),
    path('blog/', include('blog.urls')),
    path('masters/', include('master.urls')),
    path('contact/', include('contact.urls')),
    path('gallery/', include('gallery.urls')),
]

handler404 = e_handler404

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
