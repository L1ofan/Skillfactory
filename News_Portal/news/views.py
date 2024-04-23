from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class PostsList(ListView):
    model = Post
    ordering = '-post_time'
    template_name = 'Posts.html'
    context_object_name = 'Posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Новости обновляються каждую среду!"
        return context


class PostDetail(DetailView):
    model = Post
    ordering = 'post_time'
    template_name = 'Post.html'
    context_object_name = 'Post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Новости обновляються каждую среду!"
        return context