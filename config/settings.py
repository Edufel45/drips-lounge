import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-me")
DEBUG = os.environ.get("DEBUG", "0") == "1"   # set DEBUG=1 only on your own PC

_host = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
ALLOWED_HOSTS = ["localhost", "127.0.0.1"] + ([_host] if _host else []) + [h for h in os.environ.get("ALLOWED_HOSTS", "").split(",") if h]
CSRF_TRUSTED_ORIGINS = ["https://" + h for h in ALLOWED_HOSTS if h not in ("localhost", "127.0.0.1")]

USE_CLOUD = bool(os.environ.get("CLOUDINARY_URL"))   # product photos go to Cloudinary when set

INSTALLED_APPS = (
    ["django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes", "django.contrib.sessions", "django.contrib.messages"]
    + (["cloudinary_storage"] if USE_CLOUD else [])
    + ["django.contrib.staticfiles"]
    + (["cloudinary"] if USE_CLOUD else [])
    + ["shop"]
)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]
ROOT_URLCONF = "config.urls"
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates", "DIRS": [], "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages"]},
}]
WSGI_APPLICATION = "config.wsgi.application"
DATABASES = {"default": dj_database_url.config(default="sqlite:///" + str(BASE_DIR / "db.sqlite3"), conn_max_age=600)}
TIME_ZONE = "Africa/Nairobi"
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
STORAGES = {
    "default": {"BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage" if USE_CLOUD else "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedStaticFilesStorage"},
}
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
