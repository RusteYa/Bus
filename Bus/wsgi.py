"""
WSGI config for Bus project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from threading import Thread

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bus.settings')

application = get_wsgi_application()

import insert_data

thread_seismic = Thread(target=insert_data.insert_bus, daemon=True)

thread_seismic.start()


