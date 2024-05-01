from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from datetime import datetime
from .filters import PostFilter
from django.urls import reverse_lazy


class PostsList(ListView):
    model = Post
    ordering = '-post_time'
    template_name = 'Posts.html'
    context_object_name = 'Posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Новости обновляються каждую среду!"
        return context


class NewsSearch(ListView):
    model = Post
    ordering = '-post_time'
    template_name = 'Post_search.html'
    context_object_name = 'Posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    ordering = 'post_time'
    template_name = 'Post.html'
    context_object_name = 'Post'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'Post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/articles/create/':
            post.post_type = 'AR'
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('Posts')


class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'articles_create.html'
    context_object_name = 'Post'


class ArticlesUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'
    context_object_name = 'Post'


class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('Posts')
