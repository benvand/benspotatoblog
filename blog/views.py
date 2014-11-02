__author__ = 'ben'
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from models import Post, Comment
from forms import PostForm, CommentForm


class PostModel(object):
    model = Post


class PostModelForm(PostModel):
    form_class = PostForm


class PostCreateView(PostModelForm, CreateView):
    
    template_name = 'blog/post_create.html'
    queryset = Post.objects.all()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.save()
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('detail_post', kwargs={'slug': self.object.slug})


class PostUpdateView(PostModelForm, UpdateView):
    
    template_name = 'blog/post_update.html'
    queryset = Post.objects.all()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug=self.kwargs['slug'])

    def get_success_url(self):
        return reverse('detail_post', kwargs={'slug': self.kwargs['slug']})


class PostDeleteView(PostModel, DeleteView):
    
    template_name = 'blog/post_delete.html'
    queryset = Post.objects.all()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug=self.kwargs['slug'])

    def get_success_url(self):
        return reverse('list_posts')


class PostDetailView(PostModel, CreateView):
    template_name = 'blog/post_detail_with_comment_form.html'
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.prefetch_related(
            'comment_set').get(slug=self.kwargs['slug'])
        return super(PostDetailView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        c = super(PostDetailView, self).get_context_data(**kwargs)
        c.update({'post': Post.objects.prefetch_related(
            'comment_set').get(slug=self.kwargs['slug'])})
        return c

    def get_success_url(self):
        return reverse('detail_post', kwargs={'slug': self.kwargs['slug']})


class PostListView(PostModel, ListView):

    def get_queryset(self, **kwargs):
        return super(PostListView, self).get_queryset(
            **kwargs).select_related('user')
