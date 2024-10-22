import os
from .base import *
from dotenv import load_dotenv
load_dotenv()

DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party apps
    # local apps
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

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
         "file": {
            "class": "logging.FileHandler",
            "filename": "backend.log",
            "formatter": "verbose",
        }
    },
    "formatters": {
        "verbose": {
            "format": "{asctime} [{levelname}] - {module} - {name} - [{process:d} {thread:d}] - {message}",
            "style": "{",
        }
    },
     "loggers": {
        "": {
            "handlers": ["file"],
            "level": "DEBUG",
        }
    }
}
