from django.views.generic import ListView, DetailView, CreateView

from services.views_exceptions import BaseView
from .models import Post, Comment
from .forms import CommentForm


class PostsListView(ListView, BaseView):
    """Выводит список постов"""
    queryset = Post.objects.select_related('author')\
        .prefetch_related('comment_post')\
        .defer('tags', 'author__image', 'author__about_master',
               'author__vk', 'author__telegram', 'author__instagram')
    context_object_name = 'posts'
    template_name = 'blog/posts_list.html'
    paginate_by = 9


class PostDetail(DetailView, BaseView):
    """Выводит конкретный пост"""
    queryset = Post.objects.select_related('author').prefetch_related('tags')\
        .prefetch_related('comment_post')\
        .defer(
            'tags', 'author__image', 'author__about_master', 'author__vk',
            'author__telegram', 'author__instagram',
        )
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class SearchPostsListView(ListView, BaseView):
    """Поиск постов"""
    template_name = 'blog/search_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context


class CreateComment(CreateView, BaseView):
    """Создание комментария"""
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class PostsByTagListView(ListView, BaseView):
    """Выводит записи по тегу"""
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])\
            .select_related('author')\
            .prefetch_related('tags')\
            .prefetch_related('comment_post')\
            .defer('author__image', 'author__about_master', 'author__vk',
                   'author__telegram', 'author__instagram')
