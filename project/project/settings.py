# Django settings for amadou-example project.
import os,sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'example_db',
        'USER': 'example_user',
        'PASSWORD': 'example_password'
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^3^orp)o&+73#l+y^@9@gyiw^$-6_#39g#f*1-drcxvk0@lr%5'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    
    # CORS Support
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    
    # CORS Support
    'corsheaders',
    
    # Rest Easy
    'rest_easy',
    'rest_framework',
    'permission',
    
    # Token
    'rest_framework.authtoken',
    
    # OAuth
    'oauth_provider',
    
    # OAuth 2
    'provider',
    'provider.oauth2',
    
    # Example
    'example',
    'simple_history',
    
    #'versions' # Cleaner Version
)

# CORS Support - https://github.com/ottoyiu/django-cors-headers/
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = () # Example ('google.com',)
CORS_ORIGIN_REGEX_WHITELIST = () # Example ('^(https?://)?(\w+\.)?google\.com$', )
CORS_URLS_REGEX = r'^/api/.*$' # Default : '^.*$'
CORS_ALLOW_METHODS = ('GET','POST','PUT','PATCH','DELETE','OPTIONS')
CORS_ALLOW_HEADERS = (
        'x-requested-with',
        'content-type',
        'accept',
        'origin',
        'authorization',
        'x-csrftoken'
)
CORS_EXPOSE_HEADERS = ()
CORS_EXPOSE_HEADERS = ()
CORS_ALLOW_CREDENTIALS = False # Disallows cookies
CORS_PREFLIGHT_MAX_AGE = 86400

REST_BASE_URL = 'http://localhost:8080/api/'

# REST_EASY Specific Settings

# Tuple of apps to be scaffolded by rest_easy
REST_EASY_APPS = ('example',)  

# 
REST_EASY_APPS_PERMISSIONS = {'example':'775',}

# Define model names to ignore, this is usefeul for ignoring models that get auto-generated
REST_EASY_IGNORE_MODELS = (r'Historical*',)

AUTHENTICATION_BACKENDS = (
    'oauth_provider.backends.XAuthAuthenticationBackend', # django-oauth-plus
    'rest_framework.authentication.OAuth2Authentication', # django-oauth2-provider
    'django.contrib.auth.backends.ModelBackend',          # django-rest-framework
    'permission.backends.PermissionBackend',              # django-permissions
)

REST_FRAMEWORK = {
    
    # !!! TODO : We need to allow these global defaults to be changed via environment os variables
    
    # Renderer
    #'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',),
    'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer','rest_framework.renderers.BrowsableAPIRenderer',),
    
    # Filters
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),

    # Authentication
    # - Default authentication (Will also need 'rest_framework.authtoken' for this
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication', # !!! NOTE: Not suitable for production in a clustered environment (stateful)
        'rest_framework.authentication.TokenAuthentication', # !!! NOTE: Must force HTTPS for this
        #'oauth2_provider.ext.rest_framework.OAuth2Authentication', # OAuth 2.0
        
    ),
    
    # Global Authorization
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.DjangoObjectPermissions',),
    #'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    
    # Throttling
    'DEFAULT_THROTTLE_CLASSES': ('rest_framework.throttling.AnonRateThrottle','rest_framework.throttling.UserRateThrottle','rest_framework.throttling.ScopedRateThrottle',),
    'DEFAULT_THROTTLE_RATES': {'anon': '100/day','user': '1000/day'} # !!! NOTE : These is dictionary will need to be appended with view_name : rate values, in addition
                                                                     # the the anon, user defaults
    
}

# Author Permission Defaults
PERMISSION_DEFAULT_APL_FIELD_NAME = 'owner'
PERMISSION_DEFAULT_APL_ANY_PERMISSION = False
PERMISSION_DEFAULT_APL_CHANGE_PERMISSION = False
PERMISSION_DEFAULT_APL_DELETE_PERMISSION = False

# Collaborator Permission Defaults
PERMISSION_DEFAULT_CPL_FIELD_NAME = 'collaborators'
PERMISSION_DEFAULT_CPL_ANY_PERMISSION = False
PERMISSION_DEFAULT_CPL_CHANGE_PERMISSION = False
PERMISSION_DEFAULT_CPL_DELETE_PERMISSION = False

# Group Permission Defaults
PERMISSION_DEFAULT_GIPL_ANY_PERMISSION = False
PERMISSION_DEFAULT_GIPL_ADD_PERMISSION = False
PERMISSION_DEFAULT_GIPL_CHANGE_PERMISSION = False
PERMISSION_DEFAULT_GIPL_DELETE_PERMISSION = False

# 
PERMISSION_DEFAULT_SPL_ANY_PERMISSION = False
PERMISSION_DEFAULT_SPL_ADD_PERMISSION = False
PERMISSION_DEFAULT_SPL_CHANGE_PERMISSION = False
PERMISSION_DEFAULT_SPL_DELETE_PERMISSION = False

# END REST_EASY Settings

# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'simple'
        },
    },
    'loggers': {
    '''
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
    '''
        'site': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'example': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'rest_easy': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}

