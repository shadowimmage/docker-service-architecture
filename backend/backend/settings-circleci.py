from .settings import * # noqa
# import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ci',
        # postgres://USER:PASSWORD@HOST:PORT/NAME
        # 'URL': os.environ['TEST_DATABASE_URL']
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'circle_test',
        'PORT': '5432',
    },
}
