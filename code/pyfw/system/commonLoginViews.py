#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from flask import current_app, jsonify
from flask import request
from pyfw.system import system_blue
from pyfw.util.CommonJsonUtils import getJsonResponse



@system_blue.route('/auth/login', methods=['post'])
def crm_ybquery_v2():
    """
    crm根据用户手机号查询subId
    :return:
    """

    resp = getJsonResponse()

    try:

        jsonStr = request.data


        # 调用业务逻辑
        resp = {"message":"","status":200,"timestamp":1534844188679,"body":{"password":"21232f297a57a5a743894a0e4a801fc3","username":"admin"},"result":{"id":"4291d7da9005377ec9aec4a71ea837f","name":"Ronald Thompson","username":"admin","password":"","avatar":"https://gw.alipayobjects.com/zos/rmsportal/jZUIxmJycoymBprLOUbT.png","status":1,"telephone":"","lastLoginIp":"127.0.0.1","lastLoginTime":1534837621348,"creatorId":"admin","createTime":1497160610259,"deleted":0,"roleId":"admin","token":"4291d7da9005377ec9aec4a71ea837f"}}



    except BaseException as e:

        current_app.logger.error("=========异常============")
        current_app.logger.error(e)
        current_app.logger.error("=========异常============")

        resp = getJsonResponse(code="101", msg="系统异常" + str(e))

    return jsonify(resp)


@system_blue.route('/user/info', methods=['post','get'])
def crm_user_info():
    """
    crm根据用户手机号查询subId
    :return:
    """

    resp = getJsonResponse()

    try:

        jsonStr = request.data


        # 调用业务逻辑
        resp = {
	"message": "",
	"timestamp": 1560347875437,
	"result": {
		"id": "4291d7da9005377ec9aec4a71ea837f",
		"name": "系统管理员",
		"username": "admin",
		"password": "",
		"avatar": "/avatar2.jpg",
		"status": 1,
		"telephone": "",
		"lastLoginIp": "27.154.74.117",
		"lastLoginTime": 1534837621348,
		"creatorId": "admin",
		"createTime": 1497160610259,
		"merchantCode": "TLif2btpzg079h15bk",
		"deleted": 0,
		"roleId": "admin",
		"role": {
			"id": "admin",
			"name": "管理员",
			"describe": "拥有所有权限",
			"status": 1,
			"creatorId": "system",
			"createTime": 1497160610259,
			"deleted": 0,
			"permissions": [{
				"roleId": "admin",
				"permissionId": "dashboard",
				"permissionName": "仪表盘",
				"actions": [{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"query","defaultCheck":False,"describe":"查询"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}],
				"actionEntitySet": [{
					"action": "add",
					"describe": "新增",
					"defaultCheck": False
				}, {
					"action": "query",
					"describe": "查询",
					"defaultCheck": False
				}, {
					"action": "get",
					"describe": "详情",
					"defaultCheck": False
				}, {
					"action": "update",
					"describe": "修改",
					"defaultCheck": False
				}, {
					"action": "delete",
					"describe": "删除",
					"defaultCheck": False
				}],
				"actionList": None,
				"dataAccess": None
			}, {
				"roleId": "admin",
				"permissionId": "exception",
				"permissionName": "异常页面权限",
				"actions": [{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"query","defaultCheck":False,"describe":"查询"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}],
				"actionEntitySet": [{
					"action": "add",
					"describe": "新增",
					"defaultCheck": False
				}, {
					"action": "query",
					"describe": "查询",
					"defaultCheck": False
				}, {
					"action": "get",
					"describe": "详情",
					"defaultCheck": False
				}, {
					"action": "update",
					"describe": "修改",
					"defaultCheck": False
				}, {
					"action": "delete",
					"describe": "删除",
					"defaultCheck": False
				}],
				"actionList": None,
				"dataAccess": None
			}, {
				"roleId": "admin",
				"permissionId": "result",
				"permissionName": "结果权限",
				"actions": [{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"query","defaultCheck":False,"describe":"查询"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}],
				"actionEntitySet": [{
					"action": "add",
					"describe": "新增",
					"defaultCheck": False
				}, {
					"action": "query",
					"describe": "查询",
					"defaultCheck": False
				}, {
					"action": "get",
					"describe": "详情",
					"defaultCheck": False
				}, {
					"action": "update",
					"describe": "修改",
					"defaultCheck": False
				}, {
					"action": "delete",
					"describe": "删除",
					"defaultCheck": False
				}],
				"actionList": None,
				"dataAccess": None
			}, {
				"roleId": "admin",
				"permissionId": "profile",
				"permissionName": "详细页权限",
				"actions": [{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"query","defaultCheck":False,"describe":"查询"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}],
				"actionEntitySet": [{
					"action": "add",
					"describe": "新增",
					"defaultCheck": False
				}, {
					"action": "query",
					"describe": "查询",
					"defaultCheck": False
				}, {
					"action": "get",
					"describe": "详情",
					"defaultCheck": False
				}, {
					"action": "update",
					"describe": "修改",
					"defaultCheck": False
				}, {
					"action": "delete",
					"describe": "删除",
					"defaultCheck": False
				}],
				"actionList": None,
				"dataAccess": None
			}, {
				"roleId": "admin",
				"permissionId": "table",
				"permissionName": "表格权限",
				"actions": [{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"import","defaultCheck":False,"describe":"导入"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"}],
				"actionEntitySet": [{
					"action": "add",
					"describe": "新增",
					"defaultCheck": False
				}, {
					"action": "import",
					"describe": "导入",
					"defaultCheck": False
				}, {
					"action": "get",
					"describe": "详情",
					"defaultCheck": False
				}, {
					"action": "update",
					"describe": "修改",
					"defaultCheck": False
				}],
				"actionList": None,
				"dataAccess": None
			}, {
				"roleId": "admin",
				"permissionId": "form",
				"permissionName": "表单权限",
				"actions": [{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"query","defaultCheck":False,"describe":"查询"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}],
				"actionEntitySet": [{
					"action": "add",
					"describe": "新增",
					"defaultCheck": False
				}, {
					"action": "get",
					"describe": "详情",
					"defaultCheck": False
				}, {
					"action": "query",
					"describe": "查询",
					"defaultCheck": False
				}, {
					"action": "update",
					"describe": "修改",
					"defaultCheck": False
				}, {
					"action": "delete",
					"describe": "删除",
					"defaultCheck": False
				}],
				"actionList": None,
				"dataAccess": None
			}, {
				"roleId": "admin",
				"permissionId": "order",
				"permissionName": "订单管理",
				"actions": [{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"query","defaultCheck":False,"describe":"查询"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}],
				"actionEntitySet": [{
					"action": "add",
					"describe": "新增",
					"defaultCheck": False
				}, {
					"action": "query",
					"describe": "查询",
					"defaultCheck": False
				}, {
					"action": "get",
					"describe": "详情",
					"defaultCheck": False
				}, {
					"action": "update",
					"describe": "修改",
					"defaultCheck": False
				}, {
					"action": "delete",
					"describe": "删除",
					"defaultCheck": False
				}],
				"actionList": None,
				"dataAccess": None
			}, {
				"roleId": "admin",
				"permissionId": "permission",
				"permissionName": "权限管理",
				"actions": [{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}],
				"actionEntitySet": [{
					"action": "add",
					"describe": "新增",
					"defaultCheck": False
				}, {
					"action": "get",
					"describe": "详情",
					"defaultCheck": False
				}, {
					"action": "update",
					"describe": "修改",
					"defaultCheck": False
				}, {
					"action": "delete",
					"describe": "删除",
					"defaultCheck": False
				}],
				"actionList": None,
				"dataAccess": None
			}, {
				"roleId": "admin",
				"permissionId": "role",
				"permissionName": "角色管理",
				"actions": [{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}],
				"actionEntitySet": [{
					"action": "add",
					"describe": "新增",
					"defaultCheck": False
				}, {
					"action": "get",
					"describe": "详情",
					"defaultCheck": False
				}, {
					"action": "update",
					"describe": "修改",
					"defaultCheck": False
				}, {
					"action": "delete",
					"describe": "删除",
					"defaultCheck": False
				}],
				"actionList": None,
				"dataAccess": None
			}, {
				"roleId": "admin",
				"permissionId": "table",
				"permissionName": "桌子管理",
				"actions": [{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"query","defaultCheck":False,"describe":"查询"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"}],
				"actionEntitySet": [{
					"action": "add",
					"describe": "新增",
					"defaultCheck": False
				}, {
					"action": "get",
					"describe": "详情",
					"defaultCheck": False
				}, {
					"action": "query",
					"describe": "查询",
					"defaultCheck": False
				}, {
					"action": "update",
					"describe": "修改",
					"defaultCheck": False
				}, {
					"action": "delete",
					"describe": "删除",
					"defaultCheck": False
				}],
				"actionList": None,
				"dataAccess": None
			}, {
				"roleId": "admin",
				"permissionId": "user",
				"permissionName": "用户管理",
				"actions": [{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"import","defaultCheck":False,"describe":"导入"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"},{"action":"export","defaultCheck":False,"describe":"导出"}],
				"actionEntitySet": [{
					"action": "add",
					"describe": "新增",
					"defaultCheck": False
				}, {
					"action": "import",
					"describe": "导入",
					"defaultCheck": False
				}, {
					"action": "get",
					"describe": "详情",
					"defaultCheck": False
				}, {
					"action": "update",
					"describe": "修改",
					"defaultCheck": False
				}, {
					"action": "delete",
					"describe": "删除",
					"defaultCheck": False
				}, {
					"action": "export",
					"describe": "导出",
					"defaultCheck": False
				}],
				"actionList": None,
				"dataAccess": None
			}, {
				"roleId": "admin",
				"permissionId": "support",
				"permissionName": "超级模块",
				"actions": [{"action":"add","defaultCheck":False,"describe":"新增"},{"action":"import","defaultCheck":False,"describe":"导入"},{"action":"get","defaultCheck":False,"describe":"详情"},{"action":"update","defaultCheck":False,"describe":"修改"},{"action":"delete","defaultCheck":False,"describe":"删除"},{"action":"export","defaultCheck":False,"describe":"导出"}],
				"actionEntitySet": [{
					"action": "add",
					"describe": "新增",
					"defaultCheck": False
				}, {
					"action": "import",
					"describe": "导入",
					"defaultCheck": False
				}, {
					"action": "get",
					"describe": "详情",
					"defaultCheck": False
				}, {
					"action": "update",
					"describe": "修改",
					"defaultCheck": False
				}, {
					"action": "delete",
					"describe": "删除",
					"defaultCheck": False
				}, {
					"action": "export",
					"describe": "导出",
					"defaultCheck": False
				}],
				"actionList": None,
				"dataAccess": None
			}]
		}
	},
	"code": 200,
	"_headers": {
		"Custom-Header": "b6B16CF5-2C9c-F5bb-6dd9-BCebaC9CCEc6"
	}
}



    except BaseException as e:

        current_app.logger.error("=========异常============")
        current_app.logger.error(e)
        current_app.logger.error("=========异常============")

        resp = getJsonResponse(code="101", msg="系统异常" + str(e))

    return jsonify(resp)


@system_blue.route('/service', methods=['get'])
def crm_service():
    """
    crm根据用户手机号查询subId
    :return:
    """

    resp = getJsonResponse()

    try:

        jsonStr = request.data


        # 调用业务逻辑

        resp = {
                    "message": "",
                    "result": {
                        "pageSize": 10,
                        "pageNo": 1,
                        "totalCount": 57,
                        "totalPage": 6,
                        "data": [{
                            "key": 1,
                            "no": "No 1",
                            "description": "这是一段描述",
                            "callNo": 898,
                            "status": 1,
                            "updatedAt": "1987-04-04 12:04:05",
                            "editable": False
                        }, {
                            "key": 2,
                            "no": "No 2",
                            "description": "这是一段描述",
                            "callNo": 47,
                            "status": 1,
                            "updatedAt": "1986-03-16 07:56:10",
                            "editable": False
                        }, {
                            "key": 3,
                            "no": "No 3",
                            "description": "这是一段描述",
                            "callNo": 25,
                            "status": 2,
                            "updatedAt": "1984-03-06 15:58:05",
                            "editable": False
                        }, {
                            "key": 4,
                            "no": "No 4",
                            "description": "这是一段描述",
                            "callNo": 216,
                            "status": 1,
                            "updatedAt": "1980-11-07 03:11:17",
                            "editable": False
                        }, {
                            "key": 5,
                            "no": "No 5",
                            "description": "这是一段描述",
                            "callNo": 678,
                            "status": 2,
                            "updatedAt": "1979-09-07 06:43:09",
                            "editable": False
                        }, {
                            "key": 6,
                            "no": "No 6",
                            "description": "这是一段描述",
                            "callNo": 603,
                            "status": 1,
                            "updatedAt": "1986-03-22 15:09:44",
                            "editable": False
                        }, {
                            "key": 7,
                            "no": "No 7",
                            "description": "这是一段描述",
                            "callNo": 653,
                            "status": 2,
                            "updatedAt": "1974-10-26 19:34:57",
                            "editable": False
                        }, {
                            "key": 8,
                            "no": "No 8",
                            "description": "这是一段描述",
                            "callNo": 531,
                            "status": 2,
                            "updatedAt": "1993-04-30 15:34:11",
                            "editable": False
                        }, {
                            "key": 9,
                            "no": "No 9",
                            "description": "这是一段描述",
                            "callNo": 629,
                            "status": 2,
                            "updatedAt": "1988-09-30 09:47:07",
                            "editable": False
                        }, {
                            "key": 10,
                            "no": "No 10",
                            "description": "这是一段描述",
                            "callNo": 7,
                            "status": 2,
                            "updatedAt": "2016-03-17 19:07:40",
                            "editable": False
                        }]
                    },
                    "status": 200,
                    "timestamp": 1534955098193
                }



    except BaseException as e:

        current_app.logger.error("=========异常============")
        current_app.logger.error(e)
        current_app.logger.error("=========异常============")

        resp = getJsonResponse(code="101", msg="系统异常" + str(e))

    return jsonify(resp)


@system_blue.route('/crm/userlist', methods=['get'])
def crm_userlist():
    """
    crm根据用户手机号查询subId
    :return:
    """

    resp = getJsonResponse()

    try:

        jsonStr = request.data


        # 调用业务逻辑
        resp ={
                    "message": "",
                    "result": {
                        "pageSize": 10,
                        "pageNo": 2,
                        "totalCount": 57,
                        "totalPage": 6,
                        "data": [
                        {
                            "key": 1,
                            "id": 1,
                            "catalog": "No 1",
                            "description": "这是一段描述",
                            "callNo": 898,
                            "status": 1,
                            "operate_time": "1987-04-04 12:04:05",
                            "editable": False
                        },
                            {
                                "key": 2,
                                "id": 2,
                                "catalog": "No 1",
                                "description": "这是一段描述",
                                "callNo": 898,
                                "status": 1,
                                "operate_time": "1987-04-04 12:04:05",
                                "editable": False
                            },
                            {
                                "key": 3,
                                "id": 3,
                                "catalog": "No 1",
                                "description": "这是一段描述",
                                "callNo": 898,
                                "status": 1,
                                "operate_time": "1987-04-04 12:04:05",
                                "editable": False
                            },
                            {
                                "key": 4,
                                "id": 4,
                                "catalog": "No 1",
                                "description": "这是一段描述",
                                "callNo": 898,
                                "status": 1,
                                "operate_time": "1987-04-04 12:04:05",
                                "editable": False
                            },
                            {
                                "key": 5,
                                "id": 5,
                                "catalog": "No 1",
                                "description": "这是一段描述",
                                "callNo": 898,
                                "status": 1,
                                "operate_time": "1987-04-04 12:04:05",
                                "editable": False
                            },
                            {
                                "key": 6,
                                "id": 6,
                                "catalog": "No 1",
                                "description": "这是一段描述",
                                "callNo": 898,
                                "status": 1,
                                "operate_time": "1987-04-04 12:04:05",
                                "editable": False
                            },
                            {
                                "key": 7,
                                "id": 7,
                                "catalog": "No 1",
                                "description": "这是一段描述",
                                "callNo": 898,
                                "status": 1,
                                "operate_time": "1987-04-04 12:04:05",
                                "editable": False
                            },
                            {
                                "key": 8,
                                "id": 8,
                                "catalog": "No 1",
                                "description": "这是一段描述",
                                "callNo": 898,
                                "status": 1,
                                "operate_time": "1987-04-04 12:04:05",
                                "editable": False
                            },
                            {
                                "key": 9,
                                "id": 9,
                                "catalog": "No 1",
                                "description": "这是一段描述",
                                "callNo": 898,
                                "status": 1,
                                "operate_time": "1987-04-04 12:04:05",
                                "editable": False
                            }
                        ]
                    },
                    "status": 200,
                    "timestamp": 1534955098193
                }



    except BaseException as e:

        current_app.logger.error("=========异常============")
        current_app.logger.error(e)
        current_app.logger.error("=========异常============")

        resp = getJsonResponse(code="101", msg="系统异常" + str(e))

    return jsonify(resp)



@system_blue.route('/test', methods=['get'])
def testReq():
    """
    api健康检查
    :return:
    """
    # print("=========/cmcc/test============")
    # print(request.url)
    # print(request.data)
    # print(request.form)
    # print("=========/cmcc/test============")

    retdict={}

    try:

        # ===============和多号服务器请求时长验证===============
        data = {
            "checkid": request.args.get("checkid", int(time.time())),
        }


        # retdict["cmcc"] = {
        #     "status": chr.response_status_code,
        #     "timeconsuming": chr.time_consuming
        # }



        retdict["result"] = {
            "code": "0000",
            "msg": "success",
        }

    except BaseException as e:
        print(e)
        retdict["result"] = {
            "code": "1001",
            "msg": str(e)
        }




    return jsonify(retdict)


