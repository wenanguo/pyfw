#!/usr/bin/env python
# -*- coding: utf-8 -*-



from flask import request,  current_app
from pyfw.main.models import  CommonHttpRequestLogs
from pyfw.util.JsonUtil import  GetResult
from . import system_blue





@system_blue.route('/commonhttprequestlogslist', methods=['GET'])
def getCommonHttpRequestLogsList():
    """
    获取数据列表
    :return:
    """

    # 查询字符串
    filters = set()

    # 构建查询条件
    timestamp = request.args.get('timestamp')
    catalog = request.args.get('catalog')
    request_url = request.args.get('request_url')
    response_status_code = request.args.get('response_status_code')
    request_data = request.args.get('request_data')
    response_data = request.args.get('response_data')


    if timestamp: filters.add(CommonHttpRequestLogs.timestamp.contains(timestamp))
    if catalog: filters.add(CommonHttpRequestLogs.catalog.contains(catalog))
    if request_url: filters.add(CommonHttpRequestLogs.request_url.contains(request_url))
    if response_status_code: filters.add(CommonHttpRequestLogs.response_status_code==response_status_code)
    if request_data: filters.add(CommonHttpRequestLogs.request_data.contains(request_data))
    if response_data: filters.add(CommonHttpRequestLogs.response_data.contains(response_data))







    # 获取查询页
    page = request.args.get('currentPage', 1, type=int)

    pagination = getList(filters,page)

    resp, respdict = GetResult(pagination=pagination)

    return resp


def getList(filters=None,page=1):


    if filters==None:
        filters = set()



    pagination = CommonHttpRequestLogs.query.filter(*filters).order_by(CommonHttpRequestLogs.id.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)

    return pagination



