#!/usr/bin/env python
# -*- coding: utf-8 -*-

' module description'
import json

from flask import request, jsonify, current_app
from flask_restful import Resource

from app.auth.models import CommonUserInfo

__author__ = 'Andrew Wen'

todos = {}


class Users(Resource):
    def get(self):



        #查询字符串
        filters=set()

        #构建查询条件
        user_name = request.args.get('name')

        if user_name :filters.add(CommonUserInfo.login_account.contains(user_name))


        #获取查询页
        page = request.args.get('page', 1, type=int)

        #===



        pagination = CommonUserInfo.query.filter(*filters).order_by(CommonUserInfo.id.desc()).paginate(
            page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
            error_out=False)





        return jsonify({
            'items': [user.to_json() for user in pagination.items],
            'page': pagination.page,
            'prev_num': pagination.prev_num,
            'next_num': pagination.next_num,
            'has_next' :pagination.has_next, #如果有下一页，返回True
            'has_prev': pagination.has_prev, #如果有上一页，返回True
            'pages': pagination.pages, #查询得到的总页数
            'per_page': pagination.per_page, #每页显示的记录数量
            'total': pagination.total,
            'iter_pages':[pages for pages in pagination.iter_pages(left_edge = 2 ,left_current=2,right_current=3,right_edge=2)]

        })


    #
    #
    # iter_pages
    # (l e f t _ e d g e = 2,
    # left_current=2,
    # right_current=5,
    # right_edge=2)
    # 一个迭代器，返回一个在分页导航中显示的页数列表。这个列表的最左边显示left_
    # edge
    # 页，当前页的左边显示left_current
    # 页，当前页的右边显示right_current
    # 页，
    # 最右边显示right_edge
    # 页。例如，在一个100
    # 页的列表中，当前页为第50
    # 页，使用
    # 默认配置，这个方法会返回以下页数：1、2、None、48、49、50、51、52、53、54、
    # 55、None、99、100。None
    # 表示页数之间的间隔
    # prev()
    # 上一页的分页对象
    # next()
    # 下一页的分页对象

