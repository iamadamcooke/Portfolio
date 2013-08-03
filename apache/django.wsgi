import os
import sys

sys.path.append('/var/django/projects/')
sys.path.append('/var/django/projects/Portfolio/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'Portfolio.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
