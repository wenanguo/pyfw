from flask import jsonify, request, current_app, url_for
from . import api
import  json



@api.route('/devops', methods=['GET', 'POST'])
def get_devops():
    """
    获取
    :param app:
    :return:
    """



    appname = request.form['appname']
    serviceport =request.form['serviceport']
    interval = request.form['interval']
    target = request.form['target']
    outtime = request.form['outtime']



    return json.dumps({"success":True,"code":"0000","msg":"查询信息成功。"})

