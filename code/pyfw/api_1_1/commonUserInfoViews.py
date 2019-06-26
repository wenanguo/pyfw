#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import render_template, session, abort, request, redirect, url_for, current_app, flash, jsonify, \
    make_response
from flask_login import login_required

from pyfw import db
from pyfw.main.models import CommonUserInfo
from pyfw.util.JsonUtil import JsonStrToObj, CopyObj, GetResult
from . import api_1_1_system


#@api_1_1_system.after_request
def af_request(resp):
    """
    #请求钩子，在所有的请求发生后执行，加入headers。
    :param resp:
    :return:
    """
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp


@api_1_1_system.route('/commonuserinfos', methods=['GET'])
def getList():
    """
    获取数据列表
    :return:
    """

    # 查询字符串
    filters = set()

    # 构建查询条件
    user_name = request.args.get('name')

    if user_name: filters.add(CommonUserInfo.login_account.contains(user_name))

    # 获取查询页
    page = request.args.get('currentPage', 1, type=int)

    pagination = getUserList(filters,page)

    resp, respdict = GetResult(pagination=pagination)

    return resp


@api_1_1_system.route('/commonuserinfo', methods=['post'])
def post():
    """
    新增对象
    :param self:
    :return:
    """
    result="0000"
    msg=""

    #构建查询条件
    jsonStr=request.data

    user = CommonUserInfo();

    user,method = JsonStrToObj(jsonStr,user)


    if method=="post":

        user.password=user.login_account

        db.session.add(user);

        msg="新增成功"


    elif method == "update":

        target = CommonUserInfo.query.get_or_404(int(user.id))

        target=CopyObj(user,target)

        db.session.add(target);

        msg = "修改成功"

    elif method == "delete":

        target = CommonUserInfo.query.get_or_404(int(user.id))
        db.session.delete(target)

        msg = "删除成功"

    else:
        print("无任何操作")




    #return GetResult(code="0000",msg="操作成功",pagination=getUserList())
    pagination = getUserList()


    resp, respdict = GetResult(pagination=pagination)

    return resp




def getUserList(filters=None,page=1):


    if filters==None:
        filters = set()



    pagination = CommonUserInfo.query.filter(*filters).order_by(CommonUserInfo.id.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)

    return pagination



@api_1_1_system.route('/login', methods=['POST'])
def login():
    """
       登录方法
       :return:
       """

    #构建查询条件
    jsonStr=request.data


    ctdict = json.loads(jsonStr)


    if request.method == 'POST':

        userdb = CommonUserInfo.query.filter_by(login_account=ctdict["userName"]).first()

        # current_app.logger.info("===登录日志===")

        if userdb is not None and userdb.verify_password(ctdict["password"]):

            return jsonify({"status": "ok", "type": "account", "currentAuthority": "admin", "token": "wenanguo123456"})

        else:
           pass


    return jsonify({"status": "error", "type": "account", "currentAuthority": "guest"})



@api_1_1_system.route('/auth_routes', methods=['get'])
def auth_routes():
    """
       获得角色方法
       :return:
       """


    return jsonify({"/form/advanced-form":{"authority":["admin","user"]}})


@api_1_1_system.route('/currentUser', methods=['get'])
def currentUser():
    """
       获得当前用户数据
       :return:
       """

    return jsonify({"name":"系统管理员","avatar":"https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png","userid":"00000001","email":"wenanguo110@163.com","signature":"海纳百川，有容乃大","title":"前端小菜","group":"某某某事业群－某某平台部－某某技术部－UED","tags":[{"key":"0","label":"很有想法的"},{"key":"1","label":"专注设计"},{"key":"2","label":"辣~"},{"key":"3","label":"眼镜男"},{"key":"4","label":"汉子"},{"key":"5","label":"海纳百川"}],"notifyCount":12,"unreadCount":0,"country":"China","geographic":{"province":{"label":"浙江省","key":"330000"},"city":{"label":"杭州市","key":"330100"}},"address":"西湖区工专路 77 号","phone":"0752-xxxxxx"})



#
# @api_1_1_system.route('/commonuserinfo/<int:id>', methods=['get'])
# def get(id):
#         """
#         获得单对象
#         :param id:
#         :return:
#         """
#
#
#
#         #查询字符串
#         filters=set()
#
#         #构建查询条件
#         user_name = request.args.get('name')
#
#         if user_name :filters.add(CommonUserInfo.login_account.contains(user_name))
#
#
#         #获取查询页
#         page = request.args.get('page', 1, type=int)
#
#
#
#
#
#         pagination = CommonUserInfo.query.filter(*filters).order_by(CommonUserInfo.id.desc()).paginate(
#             page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
#             error_out=False)
#
#
#
#
#
#         return jsonify({
#             'items': [user.to_json() for user in pagination.items],
#             'page': pagination.page,
#             'prev_num': pagination.prev_num,
#             'next_num': pagination.next_num,
#             'has_next' :pagination.has_next, #如果有下一页，返回True
#             'has_prev': pagination.has_prev, #如果有上一页，返回True
#             'pages': pagination.pages, #查询得到的总页数
#             'per_page': pagination.per_page, #每页显示的记录数量
#             'total': pagination.total,
#             'iter_pages':[pages for pages in pagination.iter_pages(left_edge = 2 ,left_current=2,right_current=3,right_edge=2)]
#
#         })

#
# @api_1_1_system.route('/commonuserinfo/<int:id>', methods=['put'])
# def put( id):
#         """
#         更新对象
#         :param id:
#         :return:
#         """
#
#         login_account = request.form['login_account']
#
#
#         return jsonify({
#             'result': id,
#             'login_account':login_account,
#             'msg': '修改成功'
#         })
#
#
#
# @api_1_1_system.route('/commonuserinfo/<int:id>', methods=['delete'])
# def delete( id):
#         """
#         删除对象
#         :param id:
#         :return:
#         """
#
#
#
#
#         return jsonify({
#             'result': id,
#             'msg': '删除成功'
#         })