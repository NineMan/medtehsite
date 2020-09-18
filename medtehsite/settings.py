"""
Django settings for medtehsite project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys                                                                  # Взято у Хауди Хо для структуры apps'ов
import django_heroku                                                        # Для деплоя на Heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Взято у Хауди-хо с его структурой -
PROJECT_ROOT = os.path.dirname(__file__)                                    # Взято у Хауди Хо для структуры apps'ов
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))                      # Взято у Хауди Хо для структуры apps'ов

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yn3yuv!8ktv714_2^0v#m95j-6lja-v1+ys!hsdh5#_t9+k+3p'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False
# Нужно проверить !!!
# DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))     # Взято у Андрона. Проверяет переменную окружения DJANGO_DEBUG

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'mt-vlg.herokuapp.com',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bills',
    # 'cash',                   # future
    # 'order',                  # future
    # 'repair',                 # future
    # 'medtehsite.apps.core',   # future

    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'medtehsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'medtehsite/templates')
        ],
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

WSGI_APPLICATION = 'medtehsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'     # default
# LANGUAGE_CODE = 'Ru'        # for django ~2.2
LANGUAGE_CODE = 'ru-Ru'     # for django 3.1

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Volgograd'

USE_I18N = True

# USE_L10N = False
USE_L10N = True                                 # включил для использования разделителя разрядов

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
#     os.path.join(BASE_DIR, 'static/img'),
#     os.path.join(BASE_DIR, 'static/css'),
#     os.path.join(BASE_DIR, 'static/js'),
#     os.path.join(BASE_DIR, 'static/ico'),
#     # os.path.join(BASE_DIR, 'static/ckeditor'),
# ]


DATE_INPUT_FORMATS = [
    '%d/%m/%Y', '%d/%m/%y',              # '25/10/2020', '25/10/20'
    '%d-%m-%Y', '%d-%m-%y,'              # '25-10-2020', '25-10-20'
    '%d.%m.%Y', '%d.%m.%y',              # '25.06.2020', '25.06.20'
    '%d %m %Y', '%d %m %y',              # '25 06 2020', '25 06 20'
]

DATE_FORMAT = 'j E Y'

LOGIN_REDIRECT_URL = 'bills:bill_list'
LOGOUT_REDIRECT_URL = 'bills:bill_list'

# Настройка разделителя групп разрядов
THOUSAND_SEPARATOR = ' '
USE_THOUSAND_SEPARATOR = True
NUMBER_GROUPING = 3

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt' : "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'apps.bills.bills.log',
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'medtehsite': {
#             'handlers': ['file'],
#             'propagate': True,
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
#             # 'level': 'DEBUG',
#         },
#         'medtehsite.apps.bills': {
#             'handlers': ['file'],
#             'propagate': True,
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
#             # 'level': 'DEBUG',
#         },
#         'apps.bills': {
#             'handlers': ['file'],
#             'propagate': True,
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
#             # 'level': 'DEBUG',
#         },
#         'bills': {
#             'handlers': ['file'],
#             'propagate': True,
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
#         },
#     }
# }

# Настройки для деплоя на heroku

django_heroku.settings(locals())

DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': True
        }
    }
}
