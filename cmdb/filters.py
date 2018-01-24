#!/usr/bin/env python
# coding=utf-8
# Created on 2018/1/23


import logging
from . import local


class RequestIDFilter(logging.Filter):

    def filter(self, record):
        record.request_id = getattr(local, 'request_id', None)
        return True
