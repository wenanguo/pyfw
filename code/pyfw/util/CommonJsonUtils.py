#!/usr/bin/env python
# -*- coding: utf-8 -*-

' json序列化工具对象'
from pyfw.util.CommonUtils import getDateRandomName

__author__ = 'Andrew Wen'

import datetime
import json
from copy import deepcopy
from flask import jsonify

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


def ObjToJson(obj,isKey=True):
    """
    对象转换为字典，排除数据库属性
    :param obj:
    :return:
    """
    ctdict = obj.__dict__.copy()

    targetCtdict = {}

    for key in ctdict:
        if key!='_sa_instance_state':targetCtdict[key]=ctdict[key]

    # 去掉数据库对象
    #ctdict.pop('_sa_instance_state')
    if isKey : targetCtdict["key"]=ctdict["id"]

    return targetCtdict

def ObjToJsonStr(obj,isPopSa=True):
    """
    对象转换给json字符串
    :param obj:
    :param isPopSa: 是否提出数据库对象，便于序列化，默认是
    :return:
    """
    ctdict = deepcopy(obj.__dict__)

    # 去掉数据库对象
    if isPopSa:ctdict.pop('_sa_instance_state')

    return json.dumps(ctdict,cls=CJsonEncoder)


def JsonStrToObj(jsonStr,targetObj):
    """
    jsonstr转换到对象
    :param obj:
    :return:
    """
    ctdict = json.loads(jsonStr)

    DictToObj(ctdict,targetObj)

    return targetObj


def DictToObj(ctdict,targetObj,force=False):
    """
    dict 转换对象
    :param ctdict: 字典
    :param targetObj: 目标对象
    :param force: 是否强制覆盖已有值的属性
    :return:
    """

    for key in ctdict:
        if hasattr(targetObj, key):
            if force :
                setattr(targetObj, key, ctdict[key])
            else:
                if getattr(targetObj,key)==None:setattr(targetObj, key, ctdict[key])

    return targetObj




def CopyObj(source,target,isPopSa=True):
    """
    拷贝对象属性，排除数据库相关特性
    :param source:
    :param target:
    :return: 负责完成属性的对象
    """
    sourcedict = source.__dict__

    # 去掉数据库对象
    if isPopSa: sourcedict.pop('_sa_instance_state')

    for key in sourcedict:
        if hasattr(target, key):
            setattr(target, key, sourcedict[key])

    return target


def FormatMobile(phone):
    """
    格式化号码为+86 形式
    :param phone:
    :return:
    """
    if (len(phone) == 11):
        phone = "86" + phone

    return phone





def getJsonResponse(code="100",msg="操作成功",result={}):
    """
    获得json返回结果对象
    :param code: 状态值
    :param msg:
    :param pagination:
    :param result:
    :return:
    """
    result1={"code":code,"msg":msg}

    result1.update(result)

    page= {
            'result':result1
          }


    return page;





def createJsonResponse(code=200,msg="操作成功",result={}):
    """
    获得json返回结果对象
    :param code: 状态值
    :param msg:
    :param pagination:
    :param result:
    :return:
    """
    result={"status":code,"message":msg,"timestamp":getDateRandomName()}

    result.update(result)



    return result;


