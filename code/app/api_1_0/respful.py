#!/usr/bin/env python
# -*- coding: utf-8 -*-

' module description'
import json

from flask import request, jsonify
from flask_restful import Resource

from app.auth.models import CommonUserInfo, obj2dict

__author__ = 'Andrew Wen'

todos = {}


class Users(Resource):
    def get(self):
        userlist =  CommonUserInfo.query.all()


        return jsonify({
            'data': [user.to_json() for user in userlist],
            'prev': 1,
            'next': 2,
            'count': 10
        })


