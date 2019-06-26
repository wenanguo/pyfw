#!/usr/bin/env python
# -*- coding: utf-8 -*-

' 常用状态定义'


__author__ = 'Andrew Wen'



class CommonStatus():
    """
    常用状态
    """

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


class LogCatalog():
    """
    接口日志类别
    """
    # 接收crm的http请求
    CRM_YBBIND     = {"code": '1001', "url": '/crm/ybbinding'}
    CRM_AXYBBIND   = {"code": '1002', "url": '/crm/axybbinding'}
    CRM_YBUNBIND   = {"code": '1003', "url": '/crm/ybunbinding'}
    CRM_AXYBUNBIND = {"code": '1004', "url": '/crm/axybunbinding'}
    CRM_YBQUERY    = {"code": '1005', "url": '/crm/ybquery'}
    CRM_AXYBQUERY  = {"code": '1006', "url": '/crm/axybquery'}
    CRM_PUSHDATA   = 1007

    # 向和多号发出http请求
    HDH_YBBIND     = {"code": '1101', "url": 'mid/yb/binding'}
    HDH_AXYBBIND   = {"code": '1102', "url": 'mid/axyb/binding'}
    HDH_YBUNBIND   = {"code": '1103', "url": 'mid/yb/unbinding'}
    HDH_AXYBUNBIND = {"code": '1104', "url": 'mid/axyb/unbinding'}
    HDH_YBQUERY    = {"code": '1105', "url": 'mid/'}
    HDH_AXYBQUERY  = {"code": '1107', "url": 'mid/'}

    HDH_DOWNFILE   = 1106 # 文件下载

    COMMON_TEST    = 1200 # 健康检查



    HTTP_SEND      = 2  #对外发送http请求
    HTTP_ACCEPT    = 1  #接收外部http请求
