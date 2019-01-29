import unittest
from flask import current_app
from manage import create_app, db
from flask import url_for




class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        pass
        # self.app = create_app('testing')
        # self.app_context = self.app.app_context()
        # self.app_context.push()
        #db.create_all()

    def tearDown(self):
        pass
        # db.session.remove()
        # db.drop_all()
        # self.app_context.pop()

    def test_app_exists(self):




        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        print("==="*10)
        print(current_app.config["JOBS_START"])
        print("===" * 10)
        self.assertTrue(current_app.config['TESTING'])


