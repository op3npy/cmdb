#!/usr/bin/env python
# coding=utf-8
# Created on 2018/1/13


import os

module = os.environ.get('DJANGO_RUNNING_ENVIRON')
if module is None or module == 'dev':
    from cmdb.settings.dev import *
elif module == 'production':
    from cmdb.settings.production import *
elif module == 'test':
    from cmdb.settings.test import *
