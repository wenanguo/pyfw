# -*- coding:utf-8 -*-

import unittest
from flask import current_app
from app import create_app, db
from app.models import User
from app.email import send_email
import smtplib
from email.mime.text import MIMEText
import sys


print(sys.getdefaultencoding())


class EmailTestCase(unittest.TestCase):


    def test_app_email(self):
        pass
        # user = User()
        # user.username="wenanguo"
        # send_email("79912844@qq.com", 'New User',
        #            'mail/new_user',user=user)

