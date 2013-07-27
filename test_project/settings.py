# coding: utf-8

import os

def rel(*x):
    return os.path.normpath(os.path.join(os.path.dirname(__file__), '..', *x))


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': rel('test_project.sqlite3'),
    }
}

ALLOWED_HOSTS = '*'

TIME_ZONE = 'Europe/Helsinki'

LANGUAGE_CODE = 'en-us'

LOGIN_URL='/'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

#MEDIA_ROOT = rel('media')
#MEDIA_URL = '/media/'
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

STATIC_ROOT = ''
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '-k=yq3(7_(3#0(g+8%6%p0i+x-2-b2_dqf-qji8p7-!i2xmxzf'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
)
TEMPLATE_DIRS = (
    rel('templates'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'test_project.urls'

#WSGI_APPLICATION = 'test_project.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_ulogin',
    'customize',
    'test_project',
)

## The django-ulogin settings

ULOGIN_FIELDS = ['first_name', 'last_name', 'sex', 'email']
ULOGIN_OPTIONAL = ['photo', 'photo_big', 'city', 'country', 'bdate']

ULOGIN_SCHEMES = {
    'default':{
        'DISPLAY': 'panel',
        'PROVIDERS': ["google"],
        'HIDDEN': [],
    },
    'small_google':{
        'DISPLAY': 'small',
        'PROVIDERS': ["google"],
        'HIDDEN': [],
    }
}


