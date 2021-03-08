# -*- coding:utf-8 -*-
import os
import unittest

from BeautifulReport import BeautifulReport
from selenium import webdriver
from zhangjinjin.render.case.common import *


class goTest(unittest.TestCase):
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

    @BeautifulReport.add_test_img('test_go')
    def test_go(self):
        """go：go项目"""
        project = "go"
        name_xpath = '//*[@id="root"]/div/div/form/div[1]/input'
        mobile_xpath = '//*[@id="root"]/div/div/form/div[2]/input'
        code_xpath = '//*[@id="root"]/div/div/form/div[3]/input'
        btn_xpath = '//*[@id="root"]/div/div/form/a/span'
        try:
            new_tab_cn(driver, project)
            is_element_exist(driver, '//*[@id="root"]/div/div/div/div[2]', project + '登录页')
            obvious_wait_sendkeys(driver, name_xpath, '梅婕')
            obvious_wait_sendkeys(driver, mobile_xpath, '18616215375')
            obvious_wait_sendkeys(driver, code_xpath, '1111')
            obvious_wait_click(driver, btn_xpath)
            result = is_element_exist(driver, '//*[@id="root"]/div/div[2]/div', project + '登陆后元素存在判定')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true')
            if result=='false':
                is_fail()

