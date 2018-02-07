#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/2/5

from channels.test import ChannelTestCase, WSClient

from channel_server.tests.utils import ProxyClient


class MyTests(ChannelTestCase):

    def test_a_thing(self):
        client = ProxyClient(path='/inner/', client_class=WSClient)
        try:
            client.connect()
            text = {'val': 'hello'}
            client.send_text(text)
            self.assertEqual(client.receive(), text)

        except AssertionError as e:
            raise AssertionError('认证失败') from e
        finally:
            client.disconnect()