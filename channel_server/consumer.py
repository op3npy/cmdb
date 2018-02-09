#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/1/30
import gzip
import json
from itertools import chain

from IPy import IP, IPSet
from channels.generic.websockets import WebsocketConsumer

from channel_server import ws_logger
from channel_server.models import BlackList, WhiteList


class ServerConsumer(WebsocketConsumer):
    # Set to True to automatically port users from HTTP cookies
    # (you don't need channel_session_user, this implies it)
    channel_session = True

    # Set to True if you want it, else leave it out
    strict_ordering = False

    # 内置IPv4白名单
    WHITE_LIST = [IP('10.0.0.0/8'), IP('172.16.0.0/12'), IP('192.168.0.0/16'), IP('127.0.0.1/8', make_net=True)]
    # IP('FEC0:0000:0000:0000:0000:0000:0000:0000/10')]

    def connection_groups(self, **kwargs):
        """
        Called to return the list of groups to automatically add/remove
        this connection to/from.
        """
        return ['cmdb']

    def connect(self, message, **kwargs):
        """
        1. 主机验证：判断主机是否是内网的ip，主机是否是合法实例？
        2. 验证之后，判断是否是需要做初始化操作（ssh密钥配置）
        """
        if not self._is_allowed_to_connect():
            self.close()
            return
        if self._is_need_to_init():
            self._init()
        self._online()
        self.accept()

    def receive(self, text=None, bytes=None, **kwargs):
        if text:
            try:
                response = self.event_dispatch(text)
            except Exception as e:
                response = self.handle_exception(e)
            self.send_text(response)
        elif bytes:  # 目前客户端-服务器交互的数据协议不需要考虑二进制， 可以考虑类似http的gzip压缩，先保留
            clear_text = gzip.decompress(bytes)  # 可能抛异常
            try:
                response = self.event_dispatch(clear_text)
            except Exception as e:
                response = self.handle_exception(e)
            bin_response = gzip.compress(response)
            self.send_bytes(bin_response)
        else:
            self.send_text('pong')

    def disconnect(self, message, **kwargs):
        if message.content['code'] == 1000:  # 1000 是客户端断开， 1006 是服务器主动断开，认证失败
            self._offline()

    def send_text(self, text: str):
        self.send(text=text)

    def send_bytes(self, byte: bytes):
        self.send(bytes=byte)

    def _is_allowed_to_connect(self):
        """ 只允许内网ip，并且ip不在黑名单中。 内网的代理服务器(nginx ，apache)等要加入黑名单"""
        client = self.message.content.get('client', None)
        if client is None:
            ws_logger.warning('client ip is None!')
            return False

        client_ip, client_port = client
        ip = IP(client_ip)

        # 考虑用缓存， pickle + redis
        blacklist = IPSet([IP(item.ip_address) for item in BlackList.objects.all()])
        whitelist = IPSet(list(chain([IP(item.ip_address) for item in WhiteList.objects.all()], self.WHITE_LIST)))

        if ip in blacklist:
            ws_logger.warning('client({}:{}) connect refused!'.format(client_ip, client_port))
            return False
        elif ip in whitelist:  #
            return True
        else:
            return False

    def _is_need_to_init(self):
        pass

    def _init(self):
        pass

    def _online(self):
        """ 物理机和vm上线 """
        pass

    def _offline(self):
        """ 物理机和vm下线 """
        pass

    def accept(self):
        """
        Perform things on connection start
        """
        # Accept the connection; this is done by default if you don't override
        # the connect function.
        self.message.reply_channel.send({"accept": True})

    def event_dispatch(self, text)->str:
        # channels 1.x 不支持使用self绑定变量， 存数据只能用channel_session， 以主机的uuid来标识身份
        json.loads(text)
        pass

    def handle_exception(self, e)->str:
        pass
