"""
WSGI config for rural_sustentavel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/home/bitnami/apps/django/django_projects/rural_sustentavel')
os.environ.setdefault("PYTHON_EGG_CACHE", "/home/bitnami/apps/django/django_projects/rural_sustentavel/egg_cache")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rural_sustentavel.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
