from .base import *

DEBUG = False

DATABASES["default"]["NAME"] = "inv_api_test"

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]