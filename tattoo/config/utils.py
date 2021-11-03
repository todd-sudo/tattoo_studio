from django.views.defaults import page_not_found


def e_handler404(request, exception):
    """Возвращает шаблон с 404 ошибкой - DEBUG: FALSE"""
    return page_not_found(request, exception, 'errors/404.html')
