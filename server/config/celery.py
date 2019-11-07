from __future__ import absolute_import

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.conf.beat_schedule = {
    # Executes daily at midnight
    'sync-rate-every-day': {
        'task': 'apps.currency.tasks.get_rate',
        'schedule': crontab(minute=0, hour=0),
    },
}
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


