import os
import sys

path = '/home/kariluom/repo/webmail/'
if path not in sys.path:
    sys.path.append(path)

path = '/home/kariluom/repo/webmail/django_localwebmail/'
if path not in sys.path:
    sys.path.append(path)

os.chdir("/home/kariluom/repo/webmail/django_localwebmail")

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_localwebmail.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
