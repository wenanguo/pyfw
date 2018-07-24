#!/usr/bin/env python
# -*- coding: utf-8 -*-

' module description'
from flask import request
from flask_restful import Resource



__author__ = 'Andrew Wen'

todos = {}


class Users(Resource):
    def get(self):
        return {'hello': 'world'}


