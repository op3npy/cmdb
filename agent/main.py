#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/2/7


import asyncio
import contextlib

import websockets


async def main():
    async with websockets.connect('ws://cmdb.inner.com:8000') as websocket:
        name = input("What's your name? ")
        await websocket.send(name)
        print("> {}".format(name))

        greeting = await websocket.recv()
        print("< {}".format(greeting))


if __name__ == '__main__':
    with contextlib.closing(asyncio.get_event_loop()) as loop:
        loop.run_until_complete(main())
# DeprecationWarning
