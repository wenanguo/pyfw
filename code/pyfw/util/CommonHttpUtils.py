#!/usr/bin/env python
# -*- coding: utf-8 -*-

' 自定义和多号请求接口 '
import time

import requests
from flask import current_app
from manage import app

from pyfw import db
from pyfw.main.models import CommonHttpRequestLogs
from pyfw.util.CommonStatusUtils import LogCatalog

__author__ = 'Andrew Wen'




