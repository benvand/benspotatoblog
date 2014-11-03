__author__ = 'ben'
from datetime import datetime

from django.db import models
from django.utils.text import slugify
from django.utils.functional import cached_property
from djangae.contrib.gauth.models import GaeDatastoreUser
import re


class Post(models.Model):
    user = models.ForeignKey(GaeDatastoreUser)
    created = models.DateTimeField(auto_now_add=True,)
    edited = models.DateTimeField(auto_now=True,)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    allow_comments = models.BooleanField(default=True)

    @cached_property
    def age(self):
        return datetime.now() - self.created

    def get_unique_slug(self):
        """get all slugs starting with slugified title.
        Try and regex the number from the end and add 1"""
        slug_prefix = slugify(self.title)
        filter_kwargs = {'slug__startswith': slug_prefix}
        query = Post.objects.filter(**filter_kwargs)
        query = query.values_list('slug')
        same_slug = [i[0] for i in query]
        if not same_slug:
            return str(slug_prefix)
        reg_matches = [re.match('^.+?-(\d+)$', slug) for slug in same_slug]
        numbers = \
            [int(match.group(1)) for match in reg_matches if match] or [0]
        num = max(numbers) + 1
        return '-'.join([slug_prefix, str(num)])

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    user = models.ForeignKey(GaeDatastoreUser)
    post = models.ForeignKey(Post)
    created = models.DateTimeField(auto_now_add=True,)
    edited = models.DateTimeField(auto_now=True,)
    content = models.TextField()

    class Meta:
        ordering = ['-created']
