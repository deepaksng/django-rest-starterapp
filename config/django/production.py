from .base import *
from config.env import env
from .base import INSTALLED_APPS

DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS",default=[])

SECRET_KEY = env('SECRET_KEY')
# Site
# https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS += ("gunicorn", )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# http://django-storages.readthedocs.org/en/latest/index.html
INSTALLED_APPS += ('storages',)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = env('AWS_S3_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')
AWS_DEFAULT_ACL = 'public-read'
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False
MEDIA_URL = f'https://s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/'

# https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching#cache-control
# Response can be cached by browser and any intermediary caches (i.e. it is "public") for up to 1 day
# 86400 = (60 seconds x 60 minutes x 24 hours)
AWS_HEADERS = {
    'Cache-Control': 'max-age=86400, s-maxage=86400, must-revalidate',
}
