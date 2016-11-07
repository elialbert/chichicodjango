# Template WSGI file for Apache / WSGI.
print "hi"
import site
import os
import sys

#include virtualenv libs
site.addsitedir('/home/web/.virtualenvs/chichico/lib/python2.6/site-packages')
site.addsitedir('/home/web/chichico/chichicodjango')
site.addsitedir('/home/web/chichico/chichicodjango/chichico')

sys.stdout = sys.stderr

# Set correct settings variable.
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi

# Lastly, load handler.
application = django.core.handlers.wsgi.WSGIHandler()
