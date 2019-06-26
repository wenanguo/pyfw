#!/usr/bin/env python
# -*- coding: utf-8 -*-

' json序列化工具对象 v2版本废弃'
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

__author__ = 'Andrew Wen'

def ObjToJson(obj,isKey=True,id="id"):
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
    if isKey : targetCtdict["key"]=ctdict[id]

    return targetCtdict




def JsonStrToObj(jsonStr,targetObj):
    """
    json转换到数据库对象
    :param obj:
    :return:
    """
    ctdict = json.loads(jsonStr)

    if 'method' in ctdict:
        method = ctdict["method"]
    else:
        method = "get"

    DictToObj(ctdict,targetObj)

    return targetObj,method


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




def CopyObj(source,target):
    """
    拷贝对象属性，排除数据库相关特性
    :param source:
    :param target:
    :return: 负责完成属性的对象
    """
    sourcedict = source.__dict__

    # 去掉数据库对象
    sourcedict.pop('_sa_instance_state')

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

def ObjToJsonStr(obj):
    ctdict = deepcopy(obj.__dict__)

    # 去掉数据库对象
    ctdict.pop('_sa_instance_state')

    return json.dumps(ctdict,cls=CJsonEncoder)



def GetResult(code="100",msg="操作成功",pagination=None,result={}):
    """
    获得返回结果对象
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

    if pagination != None : page["list"]=[user.to_json() for user in pagination.items]

    if pagination != None: page["pagination"]={'total': pagination.total, 'pageSize': pagination.per_page, 'current': pagination.page}

    # {
    #     'list': [user.to_json() for user in pagination.items],
    #     'page': pagination.page,
    #     'prev_num': pagination.prev_num,
    #     'next_num': pagination.next_num,
    #     'has_next': pagination.has_next,  # 如果有下一页，返回True
    #     'has_prev': pagination.has_prev,  # 如果有上一页，返回True
    #     'pages': pagination.pages,  # 查询得到的总页数
    #     'per_page': pagination.per_page,  # 每页显示的记录数量
    #     'total': pagination.total,
    #     'iter_pages': [pages for pages in
    #                    pagination.iter_pages(left_edge=2, left_current=2, right_current=3, right_edge=2)]
    #
    # }

    return jsonify(page),page;






class CommonStatus():

    BASE_NORMAL={"code": '100', "msg": '正常'}

    BASE_DELETE={"code": '101', "msg": '删除'}

    BASE_BINDED = {"code": '102', "msg": '绑定关系已存在'}

    BASE_NONUMBER = {"code": '103', "msg": '请求消息指定地区无可用中间号'}

    BASE_STOP={"code": '104', "msg": '停用' }

    BASE_EXPIRED={"code": '105', "msg": '过期' }

    BASE_LOCKED={"code": '106', "msg": '锁定' }

    BASE_PAUSE={"code": '107', "msg": '暂停' }

    BASE_START={"code": '108', "msg": '启动' }

    BASE_UNKNOWN={"code": '110', "msg": '未知' }

    BASE_NOT_AUDIT={"code": '111', "msg": '未审核' }

    BASE_AUDITED={"code": '112', "msg": '已审核' }

    BASE_SENDING={"code": '113', "msg": '已发货' }

    BASE_DELIVERY={"code": '114', "msg": '已收货' }

    BASE_PUSH = {"code": '120', "msg": '已推送'}

    BASE_UNBIND = {"code": '121', "msg": '已解绑'}

    BASE_NODOWNLOAD = {"code": '122', "msg": '未下载'}

    BASE_DOWNLOAD = {"code": '123', "msg": '已下载'}

    BASE_REDOWNLOAD = {"code": '124', "msg": '重新下载'}

    BASE_VERIFYDOWNLOAD = {"code": '125', "msg": '验证下载文件'}

    PAY_NO={"code": '201', "msg": '未支付' }

    PAY_ING={"code": '202', "msg": '支付中' }

    PAY_YES={"code": '203', "msg": '支付成功' }

    PAY_FAIL={"code": '204', "msg": '支付失败' }

    INV_IN={"code": '301', "msg": '在库' }

    INV_SELL={"code": '302', "msg": '已售出' }

    INV_TRANSIT={"code": '303', "msg": '运输中' }

    INV_RETURN={"code": '304', "msg": '退货' }

    INV_EXCHANGE={"code": '305', "msg": '换货' }

    INV_RETURN_AUDIT={"code": '306', "msg": '退货审核中' }

    INV_EXCHANGE_AUDIT={"code": '307', "msg": '换货审核中' }


class logCatalog():

    crm_ybbind=1001
    crm_axybbind = 1002
    crm_ybunbind = 1003
    crm_axybunbind = 1004
    crm_ybquery = 1005
    crm_axybquery = 1006

    crm_pushdata = 1007

    hdh_ybbind = 1101
    hdh_axybbind = 1102
    hdh_ybunbind = 1103
    hdh_axybunbind = 1104
    hdh_ybquery = 1105
    hdh_axybquery = 1107

    hdh_downfile=1106

    common_test=1200



    HTTP_SEND=2

    HTTP_ACCEPT=1
