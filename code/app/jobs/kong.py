#!/usr/bin/env python
# -*- coding: utf-8 -*-

'获取marathon流量数据，存储到influxdb'
import threading

import requests

__author__ = 'Andrew Wen'



import http.client


def getGalileo():

    conn = http.client.HTTPSConnection("api.galileo.mashape.com")

    headers = {
        'accept': "application/json",
        'service-token': "35ce5130026b11e89cd1f15ffab8da30"
        }

    conn.request("GET", "/dashboards?page=256&pageSize=256", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


def getKong():
    r = requests.get('http://192.168.9.61:8000/gdgl/api/process/list')

    print(r.status_code)

    print(r.headers['content-type'])

    print(r.encoding)

    print(r.text)

    print(r.json())



if __name__ =='__main__':
    pass
    #stertFlowMonitoring()
    getGalileo()



