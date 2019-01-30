from flask import render_template, session, abort, request, redirect, url_for, current_app, flash, jsonify
from flask_login import login_required

from pyfw.main.models import CommonUserInfo
from pyfw.api_1_1 import api_1_1
from flask import request
from werkzeug import secure_filename





@api_1_1.route('/cmcc/pushtransaction', methods=['post'])
def pushtransaction():
    """
    话单推送URL
    :return:
    """



    return jsonify({
        'result': "ok"
    })




@api_1_1.route('/cmcc/pushvoicerecord', methods=['post'])
def pushvoicerecord():
    """
    录音推送URL
    :param self:
    :return:
    """
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))



    return jsonify({
            'result': "ok"
     })


