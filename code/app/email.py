# -*- coding:utf-8 -*-

from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from . import mail
from email.mime.text import MIMEText
import sys


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to],charset='GBK')
    mmm=

    # print(type(mmm.encode('GBK')))
    # print(isinstance(mmm.encode('utf-8'),str))

    #print(mmm)
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
