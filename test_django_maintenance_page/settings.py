# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

DEBUG = False  # This has to be False. Otherwise the 500 will be swallowed by django and handler500 won't be called.
ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'test_django_maintenance_page.urls'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
            ],
            'loaders': (
                'django.template.loaders.app_directories.Loader',
            ),
        },
    },
]

SECRET_KEY = 'very-secret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/django_maintenance_page.db',
    }
}

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',

    'django_maintenance_page',
    'test_django_maintenance_page',
)
