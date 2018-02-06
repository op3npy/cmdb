#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/2/6\
import contextlib

from channels.test import WSClient


class ProxyClient:
    def __init__(self, path='/', client_class=None):
        if client_class is None:
            self.client = WSClient()
        else:
            self.client = client_class()
        self.path = path

    def connect(self, content=None):
        if content is None:
            content = {}
        return self._send_and_consume(channel='websocket.connect', content=content)

    def send_text(self, text):
        return self._send_and_consume(channel='websocket.receive', content={'text': text})

    def send_byte(self, byte):
        return self._send_and_consume(channel='websocket.receive', content={'bytes': byte})

    def receive(self):
        return self.client.receive()

    def disconnect(self, content=None):
        if content is None:
            content = {}
        return self._send_and_consume(channel='websocket.disconnect', content=content)

    def _send_and_consume(self, channel, content=None, path=None):
        if content and not isinstance(content, dict):
            raise TypeError('{} is not instance of dict'.format(content))
        if path is None:
            path = self.path
        return self.client.send_and_consume(channel=channel, content=content, path=path)


@contextlib.contextmanager
def client_manager(path='/', client_class=None, content=None):
    """
    测试发送接收消息

    :param path: uri
    :param client_class: ws客户端
    :param content:  连接时发送的内容
    :return:
    """
    client = None
    try:
        client = ProxyClient(path=path, client_class=client_class)
        client.connect(content=content)
        yield client
    finally:
        if client:
            client.disconnect()
