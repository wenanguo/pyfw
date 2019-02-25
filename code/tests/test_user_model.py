import unittest

from pyfw import create_app, db
from pyfw.main.models import CommonUserInfo


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        #db.create_all()


    def tearDown(self):
        db.session.remove()
        #db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        u = CommonUserInfo(password='cat')
        self.assertTrue(u.login_password is not None)

    def test_no_password_getter(self):
        u = CommonUserInfo(password='cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        CommonUserInfo.generate_fake(100)
        u = CommonUserInfo(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salts_are_random(self):
        u = CommonUserInfo(password='cat')
        u2 = CommonUserInfo(password='cat')
        self.assertTrue(u.login_password != u2.login_password)













