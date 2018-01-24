#!/usr/bin/env python
# coding=utf-8
# Created on 2018/1/23

import uuid

from django.utils.deprecation import MiddlewareMixin

from . import settings
from . import local


class RequestIDMiddleware(MiddlewareMixin):
    """ 默认给所有请求都打上request_id，包括静态资源 """

    # request_id 默认的http头 可由nginx等反向代理生成,HTTP_X_REQUEST_ID
    REQUEST_ID_HEADER = getattr(settings, 'REQUEST_ID_HEADER', None)

    def process_request(self, request):
        request_id = self.get_request_id(request)
        local.request_id = request_id
        request.request_id = request_id

    def process_response(self, request, response):
        try:
            del local.request_id
        except AttributeError:
            pass
        return response

    def get_request_id(self, request):
        if hasattr(request, 'request_id'):
            return request.request_id
        elif self.REQUEST_ID_HEADER is not None:
            return request.META[self.REQUEST_ID_HEADER]
        else:
            return uuid.uuid4().hex  # 生成新request_id
