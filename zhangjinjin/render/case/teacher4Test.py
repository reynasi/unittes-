# -*- coding:utf-8 -*-
import os
import unittest

from BeautifulReport import BeautifulReport
from selenium import webdriver
from zhangjinjin.render.case.common import *


class teacher4Test(unittest.TestCase):
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

    @BeautifulReport.add_test_img('test_teacher4_custom')
    def test_teacher4_custom(self):
        """teacher4：自定义域名访问内容库"""
        url = 'http://hc.zhihuichaoren.com/teacher4'
        driver.get(url)
        try:
            is_element_exist(driver, '//*[@id="root"]/div/div/div/img', 'teacher4自定义域名登录页')
            mobil_xpath = '//*[@id="username"]'
            code_xpath = '//*[@id="code"]/input'
            branch = is_branch_exist(driver, '//*[@id="root"]/div/div/div/form', 'teacher4')
            if branch == 'true':
                obvious_wait_click(driver, '//*[@id="branch"]/div/span', '选择校区')
                obvious_wait_click(driver, '//html/body/div[2]/div/div/div/ul/li[1]', '选择总校区')
                btn_xpath = '//*[@id="root"]/div/div/div/form/div[4]/div/div/span/button'
            else:
                btn_xpath = '//*[@id="root"]/div/div/div/form/div[3]/div/div/span/button'
            login(driver, mobil_xpath, code_xpath, btn_xpath, 'teacher4')
            obvious_wait_click(driver, '//*[@id="root"]/div/header/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div',
                               "内容库")
            is_element_exist(driver, "//*[@id='contentAdmin']", "内容库iframe")
            driver.switch_to.frame("contentAdmin")
            is_element_exist(driver, '//*[@id="题  库$Menu"]/li[2]/span/span[2]', '我的题库')
            obvious_wait_click(driver, '//*[@id="题  库$Menu"]/li[2]/span/span[2]', "我的题库点击")
            result = is_element_exist(driver, '//*[@id="root"]/div/div/div/div/div/div[1]/div[1]/h4', '我的题库')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true')
            if result == 'false':
                is_fail()

    @BeautifulReport.add_test_img('test_teacher4')
    def test_teacher4(self):
        """ teacher4：访问内容库 """
        project = 'teacher4'
        try:
            new_tab_cn(driver, project)
            is_element_exist(driver, '//*[@id="root"]/div/div/div/img', 'teacher4登录页')
            mobil_xpath = "//*[@id='username']"
            code_xpath = '//*[@id="code"]/input'
            branch = is_branch_exist(driver, '//*[@id="root"]/div/div/div/form', project)
            if branch == 'true':
                obvious_wait_click(driver, '//*[@id="branch"]/div/span', '选择校区')
                obvious_wait_click(driver, '//html/body/div[2]/div/div/div/ul/li[1]', '选择总校区')
                btn_xpath = '//*[@id="root"]/div/div/div/form/div[4]/div/div/span/button'
            else:
                btn_xpath = '//*[@id="root"]/div/div/div/form/div[3]/div/div/span/button'
            login(driver, mobil_xpath, code_xpath, btn_xpath, 'teacher4')
            obvious_wait_click(driver, '//*[@id="root"]/div/header/div[1]/div[1]/div[2]/div/div/div[2]/div[3]/div',
                               "内容库")
            is_element_exist(driver, "//*[@id='contentAdmin']", "内容库iframe")
            driver.switch_to.frame("contentAdmin")
            is_element_exist(driver, '//*[@id="题  库$Menu"]/li[2]/span/span[2]', '我的题库')
            obvious_wait_click(driver, '//*[@id="题  库$Menu"]/li[2]/span/span[2]', "我的题库点击")
            result = is_element_exist(driver, '//*[@id="root"]/div/div/div/div/div/div[1]/div[1]/h4', '我的题库')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true')
            if result == 'false':
                is_fail()
