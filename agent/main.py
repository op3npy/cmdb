#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/2/7


import asyncio
import contextlib

import websockets

# WS_SERVER_URI = 'ws://cmdb.inner.com:8000/inner/'  # production
WS_SERVER_URI = 'ws://localhost:8000/inner/'  # dev and test


async def main():

    try:
        async with websockets.connect(WS_SERVER_URI) as websocket:
            await websocket.send('hello')
            greeting = await websocket.recv()
            print("< {}".format(greeting))
            await websocket.close()
    except ConnectionResetError:
        print('服务器主动断开连接，可能是认证失败，请确认程序所在主机和服务器处于同一内网')


if __name__ == '__main__':
    with contextlib.closing(asyncio.get_event_loop()) as loop:
        loop.run_until_complete(main())
# DeprecationWarning
