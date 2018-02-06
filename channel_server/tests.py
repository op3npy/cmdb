#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/2/5
import os

from channels import route_class
from channels.test import ChannelTestCase, Client, apply_routes, WSClient

from channel_server.consumer import ServerConsumer


class MyTests(ChannelTestCase):

    def test_a_thing(self):
        # Inject a message onto the channel to use in a consumer
        with apply_routes(route_class(ServerConsumer, path='/inner')):
            client = WSClient()
            client.send_and_consume('websocket.connect', path='/inner', content={'value': 'my_value'})
            # connect/disconnect is successful or not
            self.assertEqual(client.receive(), {'value': 'my_value'})
