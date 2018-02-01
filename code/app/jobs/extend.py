#!/usr/bin/env python
# -*- coding: utf-8 -*-

'marathon弹性扩缩容控制'
import threading

__author__ = 'Andrew Wen'





import requests
import csv
from flask import render_template, session, abort, request, redirect, url_for, current_app, flash
import time
import json
import numpy

from influxdb import InfluxDBClient


InfluxDBHost="192.168.9.69"
InfluxDBPort=8086
InfluxDBUser="root"
InfluxDBPass=""
InfluxDBDatabase="telegraf"



def queryInfluxDb(appname="gdgl",serviceport="10009",interval=5,target=1000,outtime=10):
    """
    查询influxdb数据库
    :param appname: 应用名称
    :param serviceport: 应用服务端口
    :param interval: 间隔时间
    :param target: 目标值
    :param outtime: 超过次数
    :return:
    """


    SQL = "select * from flowmeter where docker='"+appname+"_"+serviceport+"_BACKEND'  order by time desc limit "+str(interval*6)+""

    client = InfluxDBClient(InfluxDBHost, InfluxDBPort,InfluxDBUser,InfluxDBPass,InfluxDBDatabase)  # 初始化

    rs=client.query(SQL)  # 查询数据

    #print(type(rs.raw.get("series")[0]["values"]))
    #print(rs.raw.get("series")[0]["values"])

    x = numpy.array(rs.raw.get("series")[0]["values"])


    x2 =numpy.array(x[:,3],dtype = numpy.int64)

    count= (x2 > target).sum()

    print(SQL,x2)
    if count > outtime :
        return True,count
    else:
        return False,count







if __name__ =='__main__':
    #pass
    bl,count=queryInfluxDb(appname="gdgl", serviceport="10009", interval=5, target=2000, outtime=5)
    print(bl)
    print(count)



