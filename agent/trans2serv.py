#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/1/17
import sys

platform = sys.platform


def register_as_service():
    """
    首先判断是否有最高权限 windows:administrator， linux:root，如果没有则抛无权限异常
    打包成平台相关的可执行文件，注意系统位数以及linux各个操作系统的区别，兼容centos,ubuntu,debian系列

    :return:
    """
    if platform == 'win32':
        return _win()
    elif 'linux' in platform:  # todo
        return _linux()


def _win():
    pass


def _linux():
    pass
