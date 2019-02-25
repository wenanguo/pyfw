#!/usr/bin/env python
# -*- coding: utf-8 -*-

' module description'
import unittest

from pyfw import create_app, db
from pyfw.main.models import CommonUserInfo, CommonRoleInfo

__author__ = 'Andrew Wen'



class FlaskdbTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        #Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        #db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_data(self):
        u1=CommonUserInfo(user_name="文安国")

        r1 = CommonRoleInfo(role_name="系统管理员")

        #r2 = CommonRoleInfo(role_name="项目经理")
        u1.roles.append(r1)


        db.session.add(u1)
        #db.session.add(r1)
        db.session.commit()


        # print(u1.roles.all())
        #
        # u1.roles.append(r2)
        # db.session.add(u1)
        #
        # print(u1.roles.all())





