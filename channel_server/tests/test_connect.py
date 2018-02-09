#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/2/5
from unittest.mock import patch

from channels.test import ChannelTestCase, WSClient

from channel_server.consumer import ServerConsumer
from channel_server.tests.utils import ProxyClient


class TestClient(ChannelTestCase):
    """ 功能测试 """

    def setUp(self):
        self.client = ProxyClient(path='/inner/', client_class=WSClient)

    def tearDown(self):
        self.client.disconnect()

    def test_connect_auth_success(self):
        with patch('ServerConsumer._is_allowed_to_connect', return_value=True):  # auth success and receive right
            self.client.connect()
            text = {'val': 'hello'}
            self.client.send_text(text)
            self.assertEqual(self.client.receive(), text)

    def test_connect_auth_fail(self):
        with patch('ServerConsumer._is_allowed_to_connect', return_value=False):  # auth fail
            with self.assertRaises(AssertionError) as ae:
                self.client.connect()
            self.assertEqual(ae.exception, AssertionError)


class TestServerConsumer(ChannelTestCase):
    """ 功能测试  """
    def setUp(self):
        pass

    def tearDown(self):
        pass
