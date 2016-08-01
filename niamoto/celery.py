# coding: utf-8

from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'niamoto.settings')

app = Celery(
    'niamoto',
    broker=settings.CELERY_BROKER,
    backend=settings.CELERY_BACKEND,
    include=['niamoto.tasks'],
)

app.config_from_object('niamoto.celeryconfig')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
