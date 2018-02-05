#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/2/5
from channels.test import ChannelTestCase, Client


class MyTests(ChannelTestCase):
    def test_a_thing(self):
        # Inject a message onto the channel to use in a consumer
        client = Client()
        client.send_and_consume('websocket.connect', {'value': 'my_value'})
        # connect/disconnect is successful or not
        self.assertEqual(client.receive(), {'value': 'my_value'})
