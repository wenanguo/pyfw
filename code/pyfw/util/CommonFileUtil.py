#!/usr/bin/env python
# -*- coding: utf-8 -*-

' module description'
import os

__author__ = 'Andrew Wen'


def file_extension(filename):
    """
    获取文件后缀名
    :param path:
    :return:
    """
    #return os.path.splitext(path)[1]
    return filename.rsplit('.', 1)[1].lower()