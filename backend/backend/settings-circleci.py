from .settings import * # noqa
# import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'circle_test',
        # postgres://USER:PASSWORD@HOST:PORT/NAME
        # 'URL': os.environ['TEST_DATABASE_URL']
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
