from flask import render_template, session, abort,request,redirect, url_for, current_app ,flash
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import NameForm


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
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))


@main.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':


            if request.form['username'] == "wenanguo" and request.form['password'] == "123":

                session['logged_in'] = True
                flash('登录成功！')
                return redirect(url_for('main.index'))
            else:
                session['logged_in'] = False
                flash('登录失败，请重新登录！')
                return redirect(url_for('main.login'))

    return render_template('login.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        for aa in request.form.keys():
            print(aa+"="+request.form[aa])

            if request.form['username'] == "wenanguo" and request.form['password'] == "123":

                session['logged_in'] = True
                flash('注册成功，请登录！')
                return redirect(url_for('main.login'))
            else:
                session['logged_in'] = False
                flash('注册失败，请重新注册！')
                return redirect(url_for('main.register'))

    return render_template('register.html')






@main.route('/alert', methods=['GET', 'POST'])
def alert():
    return render_template('alerts.html')



@main.route('/shutdown')
def server_shutdown():
    if not current_app.testing:
        abort(404)
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if not shutdown:
        abort(500)
    shutdown()
    return 'Shutting down...'