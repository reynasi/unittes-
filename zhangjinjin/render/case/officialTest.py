# -*- coding:utf-8 -*-
import os
import unittest

from BeautifulReport import BeautifulReport
from selenium import webdriver
from zhangjinjin.render.case.common import *


class officialTest(unittest.TestCase):
    def setUp(self):
        global driver
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument('--disable-gpu')
        options.add_argument('window-size=1920x3000')
        driver = webdriver.Chrome(options=options)

    def tearDown(self):
        try:
            driver.close()
            driver.quit()
        except:
            traceback.print_exc()
            print("close fail")

    def save_img(self, img_name):
        driver.get_screenshot_as_file('{}/{}.png'.format(getimg(), img_name))

    @BeautifulReport.add_test_img('test_official')
    def test_official(self):
        """official：官网后台登录"""
        project = "official"
        try:
            new_tab_cn(driver, project)
            result = is_element_exist(driver, "//*[@id='root']/div/div/div/div[1]/a[2]/img", project + '登陆后元素存在判定')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true')
            if result=='false':
                is_fail()

