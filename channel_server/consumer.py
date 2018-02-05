#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/1/30
from channels.generic.websocket import WebsocketConsumer

GROUP_NAME = 'cmdb'


class ServerConsumer(WebsocketConsumer):

    def connect(self):
        """
        # todo
        1. 主机验证：判断主机是否是内网的ip，主机是否是合法实例？
        2. 验证之后，判断是否是需要做初始化操作（ssh密钥配置）
        :return:
        """
        if not self._is_allowed_to_connect():
            self.close(401)
            return
        self.accept()
        self.channel_layer.group_add(GROUP_NAME, self.channel_name)  # 加入资源组
        if self._is_need_to_init():
            self._init()
        self.online()

    def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        self.send(bytes_data="Hello world!")
        # Or add a custom WebSocket error code!
        self.close(code=0)

    def disconnect(self, close_code):
        # Called when the socket closes
        if close_code == 0:
            self.offline()
            self.channel_layer.group_discard(GROUP_NAME, self.channel_name)

    def _is_allowed_to_connect(self):
        """ 判断客户端ip是否在白名单内，并且不在黑名单中 """

    def _is_need_to_init(self):
        pass

    def _init(self):
        pass

    def online(self):
        """ 物理机和vm上线 """
        pass

    def offline(self):
        """ 物理机和vm下线 """
        pass
