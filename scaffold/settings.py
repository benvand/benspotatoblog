"""
Django settings for scaffold project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from djangae.settings_base import * #Set up some AppEngine specific stuff

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

from .boot import get_app_config
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_app_config().secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Application definition

TEMPLATE_LOADERS = (
'django.template.loaders.filesystem.Loader',
'django.template.loaders.app_directories.Loader',
#django.template.loaders.eggs.Loader',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.auth',
    'djangae.contrib.gauth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangosecure',
    'csp',
    'djangae',
    'auth',
    'blog',
    'bootstrap3',
    'markdown_deux',
)

MIDDLEWARE_CLASSES = (


    'djangae.contrib.security.middleware.AppEngineSecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'djangae.contrib.gauth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'csp.middleware.CSPMiddleware',
    'djangosecure.middleware.SecurityMiddleware',

)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    "django.core.context_processors.request",
    "blog.context_processors.is_owner",
)

ROOT_URLCONF = 'scaffold.urls'

WSGI_APPLICATION = 'scaffold.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


if DEBUG:
    CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")

BOOTSTRAP3 = {

    # The Bootstrap base URL
    'base_url': 'https://netdna.bootstrapcdn.com/bootstrap/3.2.0/',}


TEMPLATE_DIRS = [
    'templates',
]

from djangae.contrib.gauth.settings import *

AUTH_USER_MODEL = 'djangae.GaeDatastoreUser'
LOGIN_URL = 'login'
#
# DATETIME_FORMAT  = '%d/m/%Y %H:%M%a'
# SHORT_DATE_FORMAT = '%d/m/%Y %H:%M%a'
# DATE_FORMAT  = '%d/m/%Y %H:%M%a'
# TIME_FORMAT  = '%d/m/%Y %H:%M%a'

OWNER_EMAIL = 'benjamin.f.vandersteen@gmail.com'