from flask import Blueprint

api_1_1 = Blueprint('api_1_1', __name__)

from pyfw.api_1_1.system import commonUserInfoViews
