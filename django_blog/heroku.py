import os
import dj_database_url
from .settings import *

DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    )
}

DEBUG = False
TEMPLATE_DEBUG = False
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ['django-blog-camila-python330-6715bc5d56eb.herokuapp.com',
    'localhost',
    '127.0.0.1',
    '.herokuapp.com',  # Allow all Heroku subdomains
]

MIDDLEWARE = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    *MIDDLEWARE,
)
