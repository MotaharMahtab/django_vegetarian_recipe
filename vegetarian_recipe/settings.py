import os
from django.contrib import messages

ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm=aneyjp@vr#aa&7e6a%@m(qh@03=5vw0gnlyxq62ug038u&vh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'ajaximage',
    'imagekit',
    'ckeditor',
    'crispy_forms',
    'bootstrap4',
    'django_countries',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'vegetarian_recipe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
RECIPES_IN_LIST = 9
INGREDIENTS_IN_LIST = 20
RECIPES_IN_SEARCH = 20

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
SITE_MEDIA_URL = '/media/'
ADMIN_TOOLS_MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = os.path.join(STATIC_URL, "admin/")
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)
# EMAIL_HOST=os.environ.get('EMAIL_HOST')
# EMAIL_HOST_USER=os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD=os.environ.get('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS=os.environ.get('EMAIL_USE_TLS')
# EMAIL_PORT=os.environ.get('EMAIL_PORT')

# MESSAGE_TAGS={
#     messages.ERROR:'danger'
# }


# LOGIN_URL='login'
LOGIN_REDIRECT_URL='/'
# LOGOUT_URL='logout'
# LOGOUT_REDIRECT_URL='login'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

if ENVIRONMENT == 'production':
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

]

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Undo', 'Redo'],
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
             'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'removePlugins': 'elementspath',
        'resize_enabled': False,
        'height': 400,
        'width': 1000,
    },
}
DATE_FORMAT = '%d/%m/%Y'
DATE_INPUT_FORMATS = '%d/%m/%Y'

SITE_ID = 1
AJAXIMAGE_AUTH_TEST = lambda u: True

#CRISPY FORMS

CRISPY_TEMPLATE_PACK = 'bootstrap4'