__author__ = 'ben'
from django.db import models
from django.utils.text import slugify
import re
import datetime


class Post(models.Model):

    created = models.DateTimeField(auto_created=True, default=datetime.datetime.now())
    edited = models.DateTimeField(auto_now=True, default=datetime.datetime.now())
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()

    def get_unique_slug(self):
        '''get all slugs starting with slugified title.
        Try and regex the number from the end and add 1'''
        slug_prefix = slugify(self.title)
        filter_kwargs = {'slug__startswith': slug_prefix}
        query = Post.objects.filter(**filter_kwargs)
        query = query.values_list('slug')
        same_slug = [i[0] for i in query]
        if not same_slug:
            return str(slug_prefix)
        reg_matches = [re.match('^.+?-(\d+)$',slug) for slug in same_slug]
        numbers = [int(match.group(1)) for match in reg_matches if match] or [0]
        num = max(numbers) + 1
        return '-'.join([slug_prefix, str(num)])



    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    class Meta():
        ordering = ['-created']
