import sys

from django.utils.translation import gettext_lazy as _

import environ

root = environ.Path(__file__) - 3
live_dir = root.path('.live')

env = environ.Env(
    ADMINS=(list, []),
    AWS_ACCESS_KEY_ID=(str, ''),
    DEBUG=(bool, False),
    LOAD_EXTERNAL_FILES=(bool, True),
)
environ.Env.read_env(root('.env'))
sys.path.append(root('apps'))

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = (
    '127.0.0.1',
    '0.0.0.0',
)
SITE_ID = 1

PROJECT_ALIAS = 'project'
PROJECT_DISPLAY_NAME = 'Project'

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'debug_toolbar',
    'hijack',

    'webpack_loader',
    'widget_tweaks',
    'parler',
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'djangocms_text_ckeditor',
    'aldryn_apphooks_config',
    'aldryn_categories',
    'aldryn_common',
    'aldryn_newsblog',
    'aldryn_people',
    'aldryn_translation_tools',
    'sortedm2m',
    'taggit',
    'filer',
    'easy_thumbnails',
    'djangocms_link',

    'utils',
    'main',
]

MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]


# =============================================================================
# Templates
# =============================================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            root('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

ALLOWABLE_TEMPLATE_SETTINGS = ('DEBUG', 'LOAD_EXTERNAL_FILES', 'PROJECT_DISPLAY_NAME')

HTML_MINIFY = not DEBUG


# =============================================================================
# Debug toolbar
# =============================================================================

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda req: DEBUG,
}


# =============================================================================
# Database
# =============================================================================

DATABASES = {
    'default': env.db(),
}


# =============================================================================
# Auth
# =============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LOGIN_REDIRECT_URL = '/'


# =============================================================================
# i18n/l10n
# =============================================================================

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
]

LOCALE_PATHS = [root('locale')]

PARLER_LANGUAGES = {
    SITE_ID: (
        {'code': 'en',},
        {'code': 'es',},
    ),
    'default': {
        'fallbacks': ['es'],
        'hide_untranslated': False,
    }
}


# =============================================================================
# Static and media
# =============================================================================

STATICFILES_DIRS = [
    root('frontend/.build'),
]

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
if AWS_ACCESS_KEY_ID:
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
    AWS_QUERYSTRING_AUTH = False

    STATICFILES_LOCATION = 'static'
    STATIC_URL = 'https://s3.amazonaws.com/{}/{}/'.format(
        AWS_STORAGE_BUCKET_NAME, STATICFILES_LOCATION)
    STATICFILES_STORAGE = 'project.storages.StaticStorage'

    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = 'https://s3.amazonaws.com/{}/{}/'.format(
        AWS_STORAGE_BUCKET_NAME, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'project.storages.MediaStorage'
else:
    STATIC_ROOT = live_dir('static')
    STATIC_URL = '/static/'

    MEDIA_ROOT = live_dir('media')
    MEDIA_URL = '/media/'

    if not DEBUG:
        MIDDLEWARE += 'whitenoise.middleware.WhiteNoiseMiddleware',

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': '',
        'STATS_FILE': root('frontend/webpack-stats.json'),
    }
}

LOAD_EXTERNAL_FILES = env('LOAD_EXTERNAL_FILES')

THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

# =============================================================================
# Hijack
# =============================================================================

HIJACK_LOGIN_REDIRECT_URL = '/admin/'
HIJACK_LOGOUT_REDIRECT_URL = HIJACK_LOGIN_REDIRECT_URL
HIJACK_ALLOW_GET_REQUESTS = True


# =============================================================================
# Mailing
# =============================================================================

EMAIL_CONFIG = env.email_url('EMAIL_URL', default='smtp://user@:password@localhost:25')
vars().update(EMAIL_CONFIG)


# =============================================================================
# CMS
# =============================================================================

CMS_TEMPLATES = [
    ('cms_templates/main.html', 'Main template'),
]


# =============================================================================
# General
# =============================================================================

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'

ADMINS = []
admins = env('ADMINS')
for admin in admins:
    ADMINS.append(admin.split(':'))
