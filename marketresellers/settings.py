"""
Django settings for referidos project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-j_s3n3vp&r5(xakswuh$gchp)*0!rm6eg4(pd_hwo+#45k^4x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'bootstrap_admin',
    'django.contrib.admin',
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'login',
    'registro',
    'assets',
    'layouts',
    'mensaje',
    'perfil',
    'main',
    'tienda'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'marketresellers.urls'

WSGI_APPLICATION = 'marketresellers.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ES'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
#STATIC_URL = 'http://54.200.219.177:8080/referidos/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


AUTHENTICATION_BACKENDS = (
    
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    
    "django.contrib.messages.context_processors.messages",
    
    'django.core.context_processors.request',
)

SOCIAL_AUTH_PIPELINE = (

    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',


)


SOCIAL_AUTH_FACEBOOK_KEY = '1529769943978668'
SOCIAL_AUTH_FACEBOOK_SECRET = '0be02df7f133253dfacdc7ec553d54b3'


SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/perfil/'
LOGIN_ERROR_URL = 'login/fail/'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request':{
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',
        },
    },
}