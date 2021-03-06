#-*- coding: utf-8 -*-
from __future__ import with_statement
"""
Django settings for demosite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm$u%1@*iq&^q!&c2m$ecf_q2y4j07ps@nu(5dty)ws+xl4rbj#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
		os.path.join(os.path.dirname(__file__),'templates').replace('\\','/'),
)


ALLOWED_HOSTS = []

#import password and account configures
import ConfigParser as CP
configPath = os.path.dirname(__file__) + "/psw.cfg"
config = CP.ConfigParser()
with open(configPath, 'r') as cfgfile:
	config.readfp(cfgfile)
	email_host = config.get("info",'addr')
	email_psw = config.get("info",'psw')

#Email settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = email_host
print EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = email_psw 
print EMAIL_HOST_PASSWORD
EMAIL_PORT = 587

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'demosite.books',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	#'django.middleware.csrf.CsrfResponseMiddleware',
)

ROOT_URLCONF = 'demosite.urls'

WSGI_APPLICATION = 'demosite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		'ENGINE': 'django.db.backends.mysql',
		'NAME':'pydb',
		'USER':'root',
		'PASSWORD':'123456',
		#'HOST':'localhost',    #留空默认为localhost
		#'PORT':'3306',         #留空默认为3306端口
    }
}

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
