#!/usr/bin/env python
# -*- coding: utf-8 -*-

' 项目初始化'
import functools
import hashlib
import json
import re

import flask
import werkzeug
import yaml

from flask_cachecontrol import FlaskCacheControl
from werkzeug.exceptions import PreconditionRequired

__author__ = 'Andrew Wen'


from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flasgger import Swagger

from config import config


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message = u"请登录系统后进行操作！"
login_manager.login_message_category = "info"





def create_app(config_name):

    app = Flask(__name__)

    CORS(app, supports_credentials=True)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    db.app = app

    toolbar = DebugToolbarExtension()
    toolbar.init_app(app)

    login_manager.init_app(app)

    init_swagger(app)




    # 蓝图注册
    from pyfw.system import system_blue
    app.register_blueprint(system_blue, url_prefix='/api/v1/common')



    return app


def init_swagger(app_c):
    """
    初始化swagger文档生成
    语法参考 ： https://huangwenchao.gitbooks.io/swagger/content/
    :param app_c:
    :return:
    """



    # 获取版本
    version = ''
    with open('./pyfw/__init__.py') as f:
        version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

    template = None

    with open('./swagger/template.yaml',encoding='utf-8') as f:

        template = yaml.load(f)


    template["info"]["version"]=version
    # api文档模板
    # template = {
    #     "swagger": "2.0",
    #     "info": {
    #         "title": "基础框架api",
    #         "description": "本文档描述基础开发框架相关api",
    #         "version": version
    #     }
    #     #"host": "mysite.com",  # overrides localhost:500
    #     #"basePath": "/api",  # base bash for blueprint registration
    #     # "schemes": [
    #     #     "http",
    #     #     "https"
    #     # ],
    #     # "operationId": "getmyData",
    #     # "definitions": {
    #     #     "Palette": {
    #     #       "type": "object",
    #     #       "properties": {
    #     #         "palette_name": {
    #     #           "type": "array",
    #     #           "items": {
    #     #             "$ref": "#/definitions/Color"
    #     #           }
    #     #         }
    #     #       }
    #     #     },
    #     #     "Color": {
    #     #       "type": "string"
    #     #     }
    #     #   }
    # }

    #print(template)
    template["definitions"]["user"]={
        "type": "object",
        "properties": {
             "palette_name": {
                  "type": "array",
                  "items": {
                    "$ref": "#/definitions/Color"
                  }
                }
        }
    }

    swagger = Swagger(app_c, template=template)

    return app_c