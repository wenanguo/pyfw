#!/usr/bin/env python
# -*- coding: utf-8 -*-

' module description'

__author__ = 'Andrew Wen'


import requests
import csv


from influxdb import InfluxDBClient


def writedata():
    client = InfluxDBClient('192.168.9.69', 8086,'root','','telegraf')  # 初始化
    print(client.get_list_database())  # 显示所有数据库名称

    json_body = [
        {
            "measurement": "students",
            "tags": {
                "stuid": "s123"
            },
            # "time": "2017-03-12T22:00:00Z",
            "fields": {
                "value": 89
            }
        }
    ]

    client.write_points(json_body)  # 写入数据




    result = client.query('show measurements;')  # 显示数据库中的表
    print("Result: {0}".format(result))

    result = client.query('select * from students;')
    print("Result: {0}".format(result))


if __name__ =='__main__':

    for x in range(101):
        writedata()