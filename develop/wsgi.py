"""
WSGI config for develop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'develop.settings'

#from django.contrib.auth.handlers.modwsgi import check_password


from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
