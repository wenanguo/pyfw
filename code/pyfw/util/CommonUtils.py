#!/usr/bin/env python
# -*- coding: utf-8 -*-

' 自定义和多号请求接口 '
import random
import time

import requests
from flask import current_app
from manage import app


from pyfw.main.models import CommonHttpRequestLogs
from pyfw.util.CommonStatusUtils import LogCatalog

__author__ = 'Andrew Wen'

def getDateRandomName():
    """
    获取时间戳+随机数，作为文件名
    :return:
    """

    rannum = random.randint(1000, 9999)
    # 生成当前时间戳
    timenum = time.time()
    # 将两个数据变成字符串
    strrannum = str(rannum)
    strtimenum = str(int(round(timenum * 1000))) #毫秒级时间戳
    #print(strrannum)
    #print(strtimenum)
    # 两个字符串链接起来

    rantime = "".join((strtimenum,strrannum))

    return rantime


