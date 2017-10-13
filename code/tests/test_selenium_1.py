import re
import threading
import time
import unittest
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys

#
# path =os.path.join(os.path.abspath(os.path.dirname(os.path.realpath(__file__))+os.path.sep+".."),"driver/chromedriver_mac64")
#
#
# print(path)
# browser = webdriver.Chrome(path)
# browser.get('http://www.baidu.com/')
#
#
#
#
#
#
# print(browser.title)
# elem = browser.find_element_by_id("kw")
# elem.send_keys("Andrew")
# elem.send_keys(Keys.RETURN)
# print(browser.page_source)
# assert "No results found." not in browser.page_source
#
#
# browser.close()