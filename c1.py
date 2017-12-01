#!/usr/bin/env python
# -*- coding: utf-8 -*-

' module description'

__author__ = 'Andrew Wen'


from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/auth/ytxtest', methods=['GET', 'POST'])
def hello_world():

    print("order_code:%s" % (request.form['order_code']))
    print("FKEY:" + request.form['FKEY'])
    print("imageFile:" + request.form['imageFile'])

    return "{'flag':'true',msg:'测试图片上传成功'}"



if __name__ == '__main__':
    app.run(host='0.0.0.0')