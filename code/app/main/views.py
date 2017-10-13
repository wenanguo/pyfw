from flask import render_template, session, abort, request, redirect, url_for, current_app, flash


from . import main
from .forms import NameForm
from .. import db
from ..email import send_email
from ..models import User



@main.route('/index', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('flask.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))


@main.route('/login', methods=['GET', 'POST'])
def login():
    """
    登录方法
    :return:
    """
    if request.method == 'POST':

        user = User.query.filter_by(username=request.form['username'],password=request.form['password']).first()

        if user is None:

            flash('用户名或密码错误，请重新登录！','danger')
        else:
            return redirect(url_for('main.index'))

    return render_template('login.html')


@main.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
       if request.form['username'] != None and request.form['password'] != None:

               user = User.query.filter_by(username=request.form['username']).first()

               if user is None:
                   user = User(username=request.form['username'],password=request.form['password'])
                   db.session.add(user)

                   #发送邮件
                   if current_app.config['FLASKY_ADMIN']:
                       send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                                  'mail/new_user', user=user)

                   flash('注册成功，请登录！','success')
                   return render_template('login.html')
               else:
                   flash('注册失败，请重新注册！','danger')

       else:
           flash('用户名或密码不能为空，请重新注册！','danger')



    return render_template('register.html')






@main.route('/alert', methods=['GET', 'POST'])
def alert():
    return render_template('index.html')



@main.route('/shutdown')
def server_shutdown():
    if not current_app.testing:
        abort(404)
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if not shutdown:
        abort(500)
    shutdown()
    return 'Shutting down...'