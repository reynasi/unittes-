# -*- coding:utf-8 -*-
import os
import time
import unittest

from BeautifulReport import BeautifulReport
from selenium import webdriver
from zhangjinjin.render.case.common import *


class studentTest(unittest.TestCase):
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

    @BeautifulReport.add_test_img('test_student')
    def test_student(self):
        """student：酷培学生端登录"""
        project = "student"
        try:
            new_tab_cn(driver, project)
            is_element_exist(driver, '//*[@id="root"]/div/div/div/div[1]', project + '登录页')
            obvious_wait_click(driver, '//*[@id="root"]/div/div/div/div[1]/div[2]/div/a', project + '密码登录')
            mobil_xpath = '//*[@id="mobile"]'
            code_xpath = '//*[@id="password"]'
            btn_xpath = '//*[@class="ant-row ant-form-item"]/div/div/span/button'
            branch = is_branch_exist(driver, '//*[@id="root"]/div/div/div/div[1]/div[2]/form ', project)
            if branch == 'true':
                obvious_wait_click(driver, '//*[@id="branch"]/div/span/i', '选择校区')
                obvious_wait_click(driver, '/html/body/div[3]/div/div/div/ul/li[1]', '选择总校区')
                btn_xpath = '//*[@class="ant-row ant-form-item"]/div/div/span/button'
            else:
                btn_xpath = '//*[@class="ant-form-item-children"]/button/span'
            # driver.find_element_by_css_selector('div.ant-form-item-control>span>button').click()
            # driver.find_element_by_xpath(mobil_xpath).send_keys('18300000001')
            # driver.find_element_by_xpath(code_xpath).send_keys('000001')
            # driver.find_element_by_css_selector('div.ant-form-item-control>span>button').click()
            login(driver, mobil_xpath, code_xpath, btn_xpath, project, "18300000001", "000001")
            # 很奇怪无痕模式第一次登录时，需要点击点击两次登录才会进入系统
            driver.find_element_by_xpath(btn_xpath).click()
            result = is_element_exist(driver, '//*[@id="root"]/section/header/img', "酷培ai学生端")
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true')
            if result=='false':
                is_fail()