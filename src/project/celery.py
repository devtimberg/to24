# encoding: utf-8

from __future__ import unicode_literals, absolute_import

import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('transport_cards')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
