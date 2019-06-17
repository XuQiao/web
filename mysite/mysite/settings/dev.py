from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sb*li39jz2r*us_ed7_c^u_h(c44()le@l!_x^f@xi+9k!xcom'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
#SECURE_SSL_REDIRECT = False
SECURE_SSL_REDIRECT = True

try:
    from .local import *
except ImportError:
    pass
