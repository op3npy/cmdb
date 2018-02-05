#!/usr/bin/env python
# coding=utf-8
# Created on 2018/1/30
"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmdb.settings")
django.setup()
application = get_default_application()
