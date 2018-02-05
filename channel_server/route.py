#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/1/30
from channel_server.consumer import ServerConsumer

channel_routing = [
    ServerConsumer.as_route(path=r"^/inner/"),
]
