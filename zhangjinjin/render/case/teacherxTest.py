# -*- coding:utf-8 -*-
import os
import unittest

from BeautifulReport import BeautifulReport
from selenium import webdriver
from zhangjinjin.render.case.common import *


class teacherxTest(unittest.TestCase):
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

    @BeautifulReport.add_test_img('test_teacherx')
    def test_teacherx(self):
        """teacherx：访问题库和多媒体库"""
        project = "teacherx"
        try:
            new_tab_cn(driver, project)
            is_element_exist(driver, '//*[@id="root"]/div/div/div/img', project + '登录页')
            mobil_xpath = "//*[@id='username']"
            code_xpath = '//*[@id="code"]/input'
            branch = is_branch_exist(driver, '//*[@id="root"]/div/div/div/form', project)
            if branch == 'true':
                obvious_wait_click(driver, '//*[@id="branch"]/div/span', '选择校区')
                obvious_wait_click(driver, '//html/body/div[2]/div/div/div/ul/li[1]', '选择总校区')
                btn_xpath = '//*[@id="root"]/div/div/div/form/div[4]/div/div/span/button'
            else:
                btn_xpath = '//*[@id="root"]/div/div/div/form/div[3]/div/div/span/button'
            login(driver, mobil_xpath, code_xpath, btn_xpath, project)
            obvious_wait_click(driver, '//*[@id="root"]/div/header/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div', '题库点击')  # 进入题库
            is_element_exist(driver, "//*[@id='contentAdmin']", "题库iframe")
            driver.switch_to.frame("contentAdmin")
            obvious_wait_click(driver, '//*[@id="root"]/div/div/div/div/div/div/div[2]/div/div[1]/div[1]', "英语题库点击")
            driver.switch_to.default_content()
            obvious_wait_click(driver, '//*[@id="root"]/div/header/h1/img', '进入选择界面')
            obvious_wait_click(driver, '//*[@id="root"]/div/header/div[1]/div[1]/div[2]/div/div/div[2]/div[3]/div', '多媒体库点击')  # 进入多媒体库

            is_element_exist(driver, "//*[@id='contentAdmin']", "多媒体库iframe")
            driver.switch_to.frame('contentAdmin')
            obvious_wait_click(driver, '//*[@id="多媒体库$Menu"]/li[2]/span/span[2]', '我的视频点击')
            result = is_element_exist(driver, '//*[@id="root"]/div/div/div/div/div/div[1]/div[1]/h4', '我的视频')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true')
            if result=='false':
                is_fail()
