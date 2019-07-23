DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ScrapperInmobiliaria',
        'USER': '',  # Your postgresql user here
        'PASSWORD': '',  # Your postgresql pass here
        'HOST': 'localhost',
        'PORT': 5432,
        'CHARSET': 'UTF-8'
    }
}
