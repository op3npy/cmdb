#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/1/30
from channels.routing import route

from .serve import ws_connect, ws_disconnect, ws_message

channel_routing = [
    route("websocket.ws_connect", ws_connect),
    route("websocket.ws_message", ws_message),
    route("websocket.ws_disconnect", ws_disconnect),
]
