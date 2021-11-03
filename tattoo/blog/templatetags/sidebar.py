from django import template


from blog.models import Post, Tag


register = template.Library()


@register.inclusion_tag('include/last_news.html')
def get_last_news(cnt=3):
    """Выводит последние посты (по умолчанию - 3)"""
    posts = Post.objects.all()[:cnt]
    return {'posts': posts}


@register.inclusion_tag('include/tags.html')
def get_tags():
    """Выводит облако тегов"""
    tags = Tag.objects.all()
    return {'tags': tags}
