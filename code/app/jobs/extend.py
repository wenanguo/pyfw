#!/usr/bin/env python
# -*- coding: utf-8 -*-

'marathon弹性扩缩容控制'
import threading

from flask_sqlalchemy import SQLAlchemy

from app.marathon_autoscaler.marathon import Marathon
from app.models import PassProjectContainerInfo
from .. import db
__author__ = 'Andrew Wen'



hostnamedict={
    "192.168.9.61":"mesos-master1",
    "192.168.9.62":"mesos-master1",
    "192.168.9.63":"mesos-master1",
    "192.168.9.64":"mesos-master1",
    "192.168.9.65":"mesos-master1",
    "192.168.9.66":"mesos-node1",
    "192.168.9.67":"mesos-node2",
    "192.168.9.68":"git-service1",
    "192.168.9.69":"db-service1"
}


interval=5

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

MarathonUrl="http://192.168.9.62:8080"



def queryInfluxDb(appname="gdgl",serviceport="10009",min=200,max=1000,outtime=10,containerNum=3):
    """
    查询influxdb数据库
    :param appname: 应用名称
    :param serviceport: 应用服务端口
    :param interval: 间隔时间
    :param target: 目标值
    :param outtime: 超过次数
    :return: 是否超过最大值，超过最大值数量，是否超过最小值，超过最小值数量
    """


    SQL = "select * from flowmeter where docker='"+appname+"_"+serviceport+"_BACKEND'  order by time desc limit "+str(interval*6)+""

    client = InfluxDBClient(InfluxDBHost, InfluxDBPort,InfluxDBUser,InfluxDBPass,InfluxDBDatabase)  # 初始化

    rs=client.query(SQL)  # 查询数据

    #print(type(rs.raw.get("series")[0]["values"]))
    #print(rs.raw.get("series")[0]["values"])

    x = numpy.array(rs.raw.get("series")[0]["values"])


    x2 =numpy.array(x[:,3],dtype = numpy.int64)/containerNum

    print(x2)


    print("容器数:%s,目标最小流量：%s，目标最大流量：%s ",containerNum,str(min),str(max))
    maxcount= (x2 > max).sum()
    mincount = (x2 < min).sum()

    return (maxcount > outtime),maxcount,(mincount > outtime),mincount


    # print(SQL,x2)
    # if count > outtime :
    #     return True,count
    # else:
    #     return False,count


def stertTxss(appname="gdgl",serviceport="10009",min=200,max=400,outtime=5):
    """
    启动弹性伸缩监控
    :return:
    """
    #while True:
    try:

            marathon=Marathon(MarathonUrl)
            appdetail=marathon.get_app_details(appname)

            ##获取当前容器数量
            containerNum=int(appdetail['app']['instances'])

            maxT, maxcount,minT, mincount= queryInfluxDb(appname=appname, serviceport=serviceport, min=min,max=max, outtime=outtime,containerNum=containerNum)
            print("是否超过最大值： %s，超过数量：%s，是否超过最小值：%s，超过数量：%s", maxT, maxcount,minT, mincount)

            #如果符合要求，动态扩缩容容器
            if maxT:
                print("开始扩容 %s",str(containerNum+1))
                print(marathon.update_app(appname,{"instances":containerNum+1}))
            # elif minT:
            #     if containerNum>1:
            #         print("收缩扩容 %s", str(containerNum - 1))
            #         print(marathon.update_app(appname, {"instances": containerNum - 1}))

            # 删除原有容器信息
            gdgllist=PassProjectContainerInfo.query.filter_by(container_name=appname).all()


            for app in gdgllist:
                db.session.delete(app)
                db.session.commit()

            #新增容器列表
            for app in appdetail["app"]["tasks"]:
                ppc = PassProjectContainerInfo(app_id=1, micro_service_id=1, container_name=appname,
                                               container_ip=app["ipAddresses"][0]["ipAddress"],
                                               host_ip=app["host"],
                                               hostname=hostnamedict[app["host"]],
                                               port=str(app["ports"])[1:-1],
                                               status=1
                                               )
                db.session.add(ppc)
                db.session.commit()
    except Exception as e:
        print('except:', e)
    finally:
        print('finally...')






    # 5秒调动一次
    #time.sleep(interval)



if __name__ =='__main__':
    pass








