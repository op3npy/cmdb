#!/usr/bin/env python
# coding=utf-8
# Created on 2018/1/13
import os

current_env = os.environ.get('DJANGO_RUNNING_ENVIRON', 'dev')
if current_env == 'dev':
    from cmdb.settings.dev import *
elif current_env == 'production':
    from cmdb.settings.production import *
elif current_env == 'test':
    from cmdb.settings.test import *
