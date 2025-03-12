import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")
app = Celery("shop")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# python3 -m celery -A shop worker -l info
# celery -A shop worker --beat --scheduler django --loglevel=info