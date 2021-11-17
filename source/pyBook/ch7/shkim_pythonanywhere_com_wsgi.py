import os
import sys

# specify the project root(base) directory
path = '/home/shkim/pyBook/ch7'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

