# kysely/settings.py

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '...'  # oman projektin salainen avain
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'survey_app',  # sovellus
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',  
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kysely.urls'

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

WSGI_APPLICATION = 'kysely.wsgi.application'

# Tietokanta-asetukset, staattiset tiedostot yms. tänne...
LANGUAGE_QUERY_PARAMETER = 'lang'


# 1) Ota i18n ja l10n käyttöön
LANGUAGE_CODE = 'fi'   # ensisijainen kieli
USE_I18N = True
#USE_L10N = True
#USE_TZ = True

# 2) Määrittele tuetut kielet
LANGUAGES = [
    ('fi', 'Finnish'),
    ('sv', 'Swedish'),
    ('en', 'English'),
]

# 3) Määrittele, mistä .po-tiedostot haetaan
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Media-asetukset (kuvien tallennus)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
