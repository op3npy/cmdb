#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/1/30
from channels.generic.websockets import WebsocketConsumer


class ServerConsumer(WebsocketConsumer):
    # Set to True to automatically port users from HTTP cookies
    # (you don't need channel_session_user, this implies it)
    channel_session = True

    # Set to True if you want it, else leave it out
    strict_ordering = False

    def connection_groups(self, **kwargs):
        """
        Called to return the list of groups to automatically add/remove
        this connection to/from.
        """
        return ['cmdb']

    def connect(self, **kwargs):
        """
        1. 主机验证：判断主机是否是内网的ip，主机是否是合法实例？
        2. 验证之后，判断是否是需要做初始化操作（ssh密钥配置）
        """
        if not self._is_allowed_to_connect():
            self.close(401)
            return
        if self._is_need_to_init():
            self._init()
        self.online()
        self.accept()

    def receive(self, text=None, bytes=None, **kwargs):
        """
        Called when a message is received with either text or bytes
        filled out.
        """
        # Simple echo
        self.send(text=text, bytes=bytes)

    def disconnect(self, message, **kwargs):
        # Called when the socket closes
        if close_code == 0:
            self.offline()

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

    def accept(self):
        """
        Perform things on connection start
        """
        # Accept the connection; this is done by default if you don't override
        # the connect function.
        self.message.reply_channel.send({"accept": True})
