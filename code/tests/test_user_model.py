import json
import unittest

from pyfw import create_app, db
from pyfw.models import CommonUserInfo


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


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
        #CommonUserInfo.generate_fake(100)
        u = CommonUserInfo(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))


    def test_password_salts_are_random(self):
        u = CommonUserInfo(password='cat')
        u2 = CommonUserInfo(password='ant.design')

        u2.password="cat"
        self.assertTrue(u.login_password == u2.login_password)




    # def test_data(self):
    #     u1=CommonUserInfo(user_name="文安国")
    #
    #     r1 = CommonRoleInfo(role_name="系统管理员")
    #
    #
    #     o1 =CommonOrgInfo(org_name="项目研发室")
    #
    #     #r2 = CommonRoleInfo(role_name="项目经理")
    #     u1.roles.append(r1)
    #     u1.orgs.append(o1)
    #
    #
    #     db.session.add(u1)
    #     #db.session.add(r1)
    #     db.session.commit()
    #
    #
    #     print(u1.roles.all())
    #     print(u1.orgs.all())
    #     print(r1.users.all())
    #     print(o1.users.all())
    #     #
    #     # u1.roles.append(r2)
    #     # db.session.add(u1)
    #     #
    #     # print(u1.roles.all())

    def test_sy_data(self):
        u1=CommonUserInfo(user_name="文安国")

        ctdict=u1.__dict__
        ctdict.pop('_sa_instance_state')

        print(json.dumps(ctdict))

        #ctdict=json.dumps(u1,default=lambda obj:obj.__dict__)
        print(ctdict)
        # for key in ctdict:
        #     if hasattr(ct, key):
        #         setattr(ct, key, ctdict[key])
















