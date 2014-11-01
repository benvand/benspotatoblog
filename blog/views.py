__author__ = 'ben'

from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from models import Post
from forms import BlogForm



class PostModel(object):
    model = Post


class PostModelForm(PostModel):
    form_class = BlogForm


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
    
    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug = self.kwargs['slug'])

    def get_success_url(self):
        return reverse('detail_post', kwargs={'slug': self.kwargs['slug']})

class PostDeleteView(PostModel, DeleteView):
    
    template_name = 'blog/post_delete.html'
    queryset = Post.objects.all()
    
    def get_object(self, queryset=None):
        return get_object_or_404(Post, slug = self.kwargs['slug'])

    def get_success_url(self):
        return reverse('list_posts')


class PostDetailView(PostModel, DetailView):

    def get_object(self):
        return get_object_or_404(Post, slug=self.kwargs.get('slug', None))


class PostListView(PostModel, ListView):


    def get_queryset(self, *args, **kwargs):
        # import pdb;pdb.set_trace()
        #model.Meta.ordering not affecting ordering on page. Work around here.
        x = super(PostListView, self).get_queryset(
            *args, **kwargs)

        return x

    def get_context_data(self, **kwargs):
        s = super(self.__class__, self).get_context_data(**kwargs)
        return s

