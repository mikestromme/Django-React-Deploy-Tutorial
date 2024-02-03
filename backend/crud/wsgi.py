import os

from django.core.wsgi import get_wsgi_application
settings_module = 'crud.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'crud.settings' # used to tell application if in DEV or PROD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
