#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/2/5
import os
import pytest
from channels.testing import WebsocketCommunicator
from channel_server.consumer import ServerConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmdb.settings")


@pytest.mark.asyncio
async def test_my_consumer():
    communicator = WebsocketCommunicator(ServerConsumer, '/')
    connected, subprotocol = await communicator.connect()
    assert connected
    # Test sending text
    await communicator.send_to(text_data="hello")
    response = await communicator.receive_from()
    assert response == "hello"
    # Close
    await communicator.disconnect()
