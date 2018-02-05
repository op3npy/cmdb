#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/1/30
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from channel_server.consumer import ServerConsumer


class QueryAuthMiddleware:
    """
    Custom middleware (insecure) that takes user IDs from the query string.
    """

    def __init__(self, inner):
        # Store the ASGI application we were passed
        self.inner = inner

    async def __call__(self, scope):
        print(111)
        return self.inner(scope)


application = ProtocolTypeRouter({
    "websocket": QueryAuthMiddleware(URLRouter([
        path("inner/", ServerConsumer),
        # url("^inner/$", Consumer),
    ]))
})
print(111)