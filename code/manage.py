#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import tornado
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
import logging
from logging.handlers import RotatingFileHandler

from tornado import options
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from init import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')






manager = Manager(app)
migrate = Migrate(app, db)


"""
日志配置
定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
"""
if app.config["LOGS_START"]==True:
    basedir = os.path.abspath(os.path.dirname(__file__))
    logdir = os.path.join(basedir, 'logs/myapp.log')
    Rthandler = RotatingFileHandler(logdir, maxBytes=10*1024*1024,backupCount=5)
    Rthandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(pathname)s %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    Rthandler.setFormatter(formatter)
    app.logger.addHandler(Rthandler)




"""
配置作业
"""
if app.config["JOBS_START"]:
    pass

    #流量监控作业
    # from app.jobs.flow import stertFlowMonitoring
    #
    # t = threading.Thread(target=stertFlowMonitoring, name='getHaproxyDataThread')
    # t.start()


    # #智能扩缩容作业
    # t2 = threading.Thread(target=stertTxss, name='stertTxssThread')
    # t2.start()
    #
    # #t.join()


    # from apscheduler.schedulers.blocking import BlockingScheduler
    # from app.jobs.flow import stertFlowMonitoring
    # sched = BlockingScheduler()
    # sched.add_job(stertFlowMonitoring, 'interval', seconds=5)
    # sched.start()




def make_shell_context():
    return dict(app=app, db=db)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)




COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()



@manager.command
def profile(length=25, profile_dir=None):
    """Start the application under the code profiler."""
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length],
                                      profile_dir=profile_dir)
    app.run()



@manager.command
def test(coverage=False):
    """Run the unit tests."""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import sys
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()




# @manager.command
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)



if __name__ == '__main__':

    # 打开命令行日志显示
    logger = logging.getLogger()
    fm = tornado.log.LogFormatter(fmt='[%(asctime)s]%(color)s[%(levelname)s]%(end_color)s[(module)s:%(lineno)d] %(message)s',datefmt = '%Y-%m-%d %H:%M:%S')
    tornado.log.enable_pretty_logging(logger=logger)
    logger.handlers[0].setFormatter(fm)



    logging.info('web is starting...')

    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    IOLoop.instance().start()



