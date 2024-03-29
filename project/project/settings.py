"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# load .env variables
from dotenv import load_dotenv
import os
load_dotenv()

import sys


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7v7t$cypup9ob-71mk)53s5kb15^dq%joxtb9^(36$7e!b!1=o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party libraries
    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.twitter',

    # Local apps
    'profile_account',
    'items',
    'orders',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Account middleware for third party authentication:
    "allauth.account.middleware.AccountMiddleware",
    # 'allauth.socialaccount.middleware.SocialAccountMiddleware',

]

ROOT_URLCONF = 'project.urls'


# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': os.getenv("GOOGLE_CLIENT_ID"),
            'secret': os.getenv("GOOGLE_CLIENT_SECRET"),
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'FETCH_USERINFO' : True
    },
    # 'twitter': {
    #     'APP': {
    #         'client_id': os.getenv("TWITTER_API_KEY"),
    #         'secret': 'os.getenv("TWITTER_CONSUMER_SECRET")',
    #         'key': ''
    #     }
    # },
}

AUTHENTICATION_BACKENDS = [
    # Login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'allauth.account.auth_backends.AuthenticationBackend',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

ACCOUNT_EMAIL_VERIFICATION = 'none'  # Disable email verification
SITE_ID = 1

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


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# SQLite Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# # MYSQL DB.. 
# NB : MYSQL database not working properly due to allauth package.
# DATABASES = {
#     'default': {
#         'NAME': os.getenv("MYSQL_DB_NAME"),
#         'ENGINE': 'mysql.connector.django',   # 'django.db.backends.mysql'
#         'USER': os.getenv("MYSQL_DB_USER"),
#         'PASSWORD': os.getenv("MYSQL_DB_PASSWORD"),
#         'HOST': os.getenv("MYSQL_DB_HOST"),
#         'PORT': os.getenv("MYSQL_PORT"),
#         'OPTIONS': {
#             'autocommit': True,
#         },
#     }
# }

# PostgreSQL database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("PG_DB_NAME"),
        'USER': os.getenv("PG_DB_USER"), # this is the superuser
        'PASSWORD': os.getenv("PG_DB_PASSWORD"), # this is the superuser password
        'HOST': os.getenv("PG_DB_HOST"),
        'PORT': os.getenv("PG_DB_PORT"),
    }
}


if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
