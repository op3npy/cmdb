#!/usr/bin/env python
# coding=utf-8
# Created on 2018/1/13
from celery import Celery

from cmdb import settings

app = Celery('cmdb')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))