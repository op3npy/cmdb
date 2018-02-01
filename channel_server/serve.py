#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/1/30
import json

from channels import Group
from channels.sessions import channel_session
from urllib.parse import parse_qs


# Connected to websocket.connect
@channel_session
def ws_connect(message, room_name):
    """
    # todo
    1. 主机验证：判断主机是否是内网的ip，主机是否是合法实例？
    2. 验证之后，判断是否是需要做初始化操作（ssh密钥配置）

    :param message:
    :param room_name:
    :return:
    """

    # Accept connection
    message.reply_channel.send({"accept": True})
    # Parse the query string
    params = parse_qs(message.content["query_string"])
    if b"username" in params:
        # Set the username in the session
        message.channel_session["username"] = params[b"username"][0].decode("utf8")
        # Add the user to the room_name group
        Group("chat-%s" % room_name).add(message.reply_channel)
    else:
        # Close the connection.
        message.reply_channel.send({"close": True})


# Connected to websocket.receive
@channel_session
def ws_message(message, room_name):
    Group("chat-%s" % room_name).send({
        "text": json.dumps({
            "text": message["text"],
            "username": message.channel_session["username"],
        }),
    })


# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message, room_name):
    Group("chat-%s" % room_name).discard(message.reply_channel)
