"""
Development settings for portfolio project.
"""

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', '192.168.1.6', "*"]

# Add debug toolbar for development
INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Debug Toolbar Configuration
INTERNAL_IPS = [
    '127.0.0.1',
]

# Use console email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable security features for local development
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
# Database - Use SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
