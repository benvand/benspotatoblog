__author__ = 'ben'
from django.conf import settings


def is_owner(request):
    return {'is_owner': (hasattr(request.user, 'email') and (request.user.email in (settings.OWNER_EMAIL, 'test@example.com') or request.user.email.endwith('potatolondon.com')))}
