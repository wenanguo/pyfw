import re
import threading
import time
import unittest

from pyfw import create_app
from selenium import webdriver

import os

path =os.path.join(os.path.abspath(os.path.dirname(os.path.realpath(__file__))+os.path.sep+".."),"driver/chromedriver_mac64")

class SeleniumTestCase(unittest.TestCase):
    client = None


    @classmethod
    def setUpClass(cls):
        # start Firefox
        try:

            print(webdriver)
            cls.client = webdriver.Chrome(path)
        except:
            pass

        print(cls.client)
        # skip these tests if the browser could not be started
        if cls.client:
            # create the application
            cls.app = create_app('testing')
            cls.app_context = cls.app.app_context()
            cls.app_context.push()

            # suppress logging to keep unittest output clean
            import logging
            logger = logging.getLogger('werkzeug')
            logger.setLevel("ERROR")

            # create the database and populate with some fake data
            #db.create_all()
            # Role.insert_roles()
            # User.generate_fake(10)
            # Post.generate_fake(10)

            # add an administrator user
            # admin_role = Role.query.filter_by(permissions=0xff).first()
            # admin = User(email='john@example.com',
            #              username='john', password='cat',
            #              role=admin_role, confirmed=True)
            # db.session.add(admin)
            # db.session.commit()

            # start the Flask server in a thread
            threading.Thread(target=cls.app.run).start()

            # give the server a second to ensure it is up
            time.sleep(1) 

    @classmethod
    def tearDownClass(cls):
        if cls.client:
            # stop the flask server and the browser
            cls.client.get('http://localhost:5000/shutdown')
            cls.client.close()

            # destroy database
            # db.drop_all()
            # db.session.remove()

            # remove application context
            cls.app_context.pop()

    def setUp(self):
        if not self.client:
            self.skipTest('Web browser not available')

    def tearDown(self):
        pass
    
    def test_admin_home_page(self):
        # navigate to home page
        self.client.get('http://localhost:5000/index')
        self.assertTrue(re.search('/auth/login',
                                  self.client.page_source))

        # # navigate to login page
        # self.client.find_element_by_link_text('Log In').click()
        # self.assertTrue('<h1>Login</h1>' in self.client.page_source)
        #
        # # login
        # self.client.find_element_by_name('email').\
        #     send_keys('john@example.com')
        # self.client.find_element_by_name('password').send_keys('cat')
        # self.client.find_element_by_name('submit').click()
        # self.assertTrue(re.search('Hello,\s+john!', self.client.page_source))
        #
        # # navigate to the user's profile page
        # self.client.find_element_by_link_text('Profile').click()
        # self.assertTrue('<h1>john</h1>' in self.client.page_source)
