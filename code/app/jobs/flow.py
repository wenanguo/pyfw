#!/usr/bin/env python
# -*- coding: utf-8 -*-

'获取marathon流量数据，存储到influxdb'

__author__ = 'Andrew Wen'





import requests
import csv
from flask import render_template, session, abort, request, redirect, url_for, current_app, flash
import time

from influxdb import InfluxDBClient


URL1="http://192.168.9.61:9090/haproxy?stats;csv"


def getll():

    print("请求："+URL1)

    response=requests.get(URL1)

    #print(response.headers)
    #print(response.text)

    msg=response.text


    #存储数据list
    flowmeterlist=[]

    reader =csv.reader(msg.split('\n'))

    #print(type(reader))

    for row in reader:
        try:
            if row[1] not in ['FRONTEND', 'BACKEND']:
                flowmeterlist.append(row)

        except Exception as e:
            pass
            #print(e)
        # do something with row, such as row[0],row[1]

    flowmeterlist.pop(0)
    flowmeterlist.pop(-1)

    #print(flowmeterlist)

    for x in range(len(flowmeterlist)):
        temp=flowmeterlist[x]
        json_body = [
            {
                "measurement": "flowmeter",
                "tags": {
                    "app": temp[0],
                    "docker":temp[1]
                },
                # "time": "2017-03-12T22:00:00Z",
                "fields": {
                    "stot": int(temp[7]),
                    "smax": int(temp[35]),
                    "scur": int(temp[33]),
                    "app": temp[0]
                }
            }
        ]
        print(json_body)
        writedata(json_body)


def writedata(json_body):
    client = InfluxDBClient('192.168.9.69', 8086,'root','','telegraf')  # 初始化

    client.write_points(json_body)  # 写入数据






if __name__ =='__main__':
    pass





    # while True:
    #      get1()
    #      print('======================')
    #      time.sleep(1)
