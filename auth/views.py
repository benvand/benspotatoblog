__author__ = 'ben'

from django.views.generic import View, RedirectView
from django.core.urlresolvers import reverse
from google.appengine.api import users
from django.shortcuts import redirect

class Login(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('list_posts')
        return redirect(users.create_login_url('/'))

class Logout(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('list_posts')
        return redirect(users.create_logout_url('/'))