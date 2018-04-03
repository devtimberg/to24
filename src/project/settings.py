# encoding: utf-8

# from __future__ import unicode_literals

from os.path import dirname, join, abspath

from django.core.urlresolvers import reverse_lazy

BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

SECRET_KEY = 'dev_key'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'transport_cards',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'temp', 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
AUTH_USER_MODEL = 'transport_cards.User'
LOGIN_URL = reverse_lazy('login')

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR, 'media')

# RAVEN_CONFIG = {
#     'dsn': 'https://14aba0fc016f425dad09b65950e87c9d:f47ebe54190b451d87c63b13a6eab2b1@sentry.io/249818',
#     # If you are using git, you can also automatically configure the
#     # release based on the git info.
#     'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
# }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',
    }
}

DEBUG = True

LOG_DIR = join(BASE_DIR, 'logs')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'requests': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': join(LOG_DIR, 'requests.log'),
        },
        'security': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': join(LOG_DIR, 'security.log'),
        },
        'robokassa': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': join(LOG_DIR, 'robokassa.log'),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['requests'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['security'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'robokassa': {
            'handlers': ['robokassa'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'no-reply@xn--24-emcp.xn--80asehdb'
EMAIL_HOST_PASSWORD = '521282'
EMAIL_USE_TLS = True

# Хост, для указания в поле from
DEFAULT_FROM_EMAIL = 'no-reply@xn--24-emcp.xn--80asehdb'

# Хост для отображения в письмах
EMAIL_HOST_FOR_MAILS = 'no-reply@xn--24-emcp.xn--80asehdb'


TO24_API = {
    'URL': '',
    'LOGIN': '',
    'PASSWORD': '',
    'SUCCESS': 1,
    'FAIL': 0
}

ROBOKASSA = {}

# REDIS/CELERY related settings 
REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600} 

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'



# URL для оплаты
PAYMENT_URL = 'https://auth.robokassa.ru/Merchant/index.aspx?' \
              'MerchantLogin={login}&' \
              'OutSum={outsum}&' \
              'InvId={inv}&' \
              'InvDesc={descr}&' \
              'SignatureValue={signature}&Culture=ru'

try:
    from .local_settings import *
except ImportError:
    print('Нет файла с локальными настройками')

# if EMAIL_BACKEND == 'django.core.mail.backends.smtp.EmailBackend':
#     if not (EMAIL_HOST and EMAIL_HOST_PASSWORD and EMAIL_HOST_USER and EMAIL_PORT):
#         raise NotImplementedError('Не указаны настройки SMTP')

# if not EMAIL_HOST_FOR_MAILS:
#     raise NotImplementedError('Не указан хост для отображения в письмах')

# if not TO24_API['LOGIN'] or not TO24_API['PASSWORD']:
#     raise NotImplementedError('Не указаны данные для входа на TO24_API')

if not ROBOKASSA:
    raise ImportError('Не указаны параметры ROBOKASSA')

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]
    INTERNAL_IPS = [
        '127.0.0.1',
        'localhost'
    ]

else:
    # INSTALLED_APPS.append('raven.contrib.django.raven_compat',)

    if SECRET_KEY == 'dev_key':
        raise ValueError('SECRET_KEY is not set')

    if not ALLOWED_HOSTS:
        raise ValueError("Don't have any allowed hostnames")

    
