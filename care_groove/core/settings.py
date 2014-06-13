import os
import custommiddleware

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RESOURCE_DIR = os.path.abspath(os.path.join(PROJECT_DIR, "..", "resources"))

ADMINS = (
# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = []
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.abspath(os.path.join(RESOURCE_DIR, "media"))

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.abspath(os.path.join(RESOURCE_DIR, "static"))

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',)

TEMPLATE_DIRS = (
    os.path.join(RESOURCE_DIR, 'html'),
)

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

MEDIA_URL = '/media/'


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xn7usw@m!i98__yssj+^$+cu0dvn(6uc7m_^7@yov_z-rcr82u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'custommiddleware',
    'user',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'custommiddleware.middleware.host_middleware',
)

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'caredb',
        'USER': 'sarupsikha',
        'PASSWORD': 'sikha',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'user': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'caredb_user',
        'USER': 'sarupsikha',
        'PASSWORD': 'sikha',
        'HOST': '127.0.0.1',
        'PORT': '5432',

}
}

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# URL of the login page.
LOGIN_URL = '/login/'
