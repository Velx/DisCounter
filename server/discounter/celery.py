import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discounter.settings')
app = Celery('discounter')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'cron-price-with-notifications': {
        'task': 'products.tasks.cron_price',
        'schedule': 3600.0
    },
}
app.conf.timezone = 'UTC'