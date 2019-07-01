from flask import Blueprint

system_blue = Blueprint('system_blue', __name__)

from . import commonUserInfoViews
from . import commonHttpRequestLogsViews
from . import commonLoginViews
