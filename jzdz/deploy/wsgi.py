import os, sys

from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler

sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))

os.environ["DJANGO_SETTINGS_MODULE"] = "jzdz.settings"

application = WSGIHandler()
