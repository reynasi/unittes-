# -*- coding:utf-8 -*-
import os
import unittest

from BeautifulReport import BeautifulReport
from selenium import webdriver
from zhangjinjin.render.case.common import *


class student4Test(unittest.TestCase):
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

    @BeautifulReport.add_test_img('test_student4')
    def test_student4(self):
        """student4：学生端登录"""
        project = "student4"
        try:
            new_tab_cn(driver, project)
            result = is_element_exist(driver, '//*[@id="root"]/div/div[1]/div/div[1]/img', project + '登录页')
            mobil_xpath = '//*[@id="username"]'
            code_xpath = '//*[@id="password"]'
            branch = is_branch_exist(driver, '//*[@id="root"]/div/div[1]/div/form', project)
            if branch == 'true':
                obvious_wait_click(driver, '//*[@id="branch"]/div/span', '选择校区')
                obvious_wait_click(driver, '/html/body/div[3]/div/div/div/ul/li[1]', '选择总校区')
                btn_xpath = '//*[@id="root"]/div/div[1]/div/form/div[4]/div/div/span/button'
            else:
                btn_xpath = '//*[@id="root"]/div/div[1]/div/form/div[3]/div/div/span/button'
            login(driver, mobil_xpath, code_xpath, btn_xpath, project, "18411100000", "100000")
            result = is_element_exist(driver, "//*[@id='root']/div/aside/div[1]/img", "TAD学生端")
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true')
            if result=='false':
                is_fail()

    @BeautifulReport.add_test_img('test_student4_customer')
    def test_student4_customer(self):
        """student4：自定义域名学生端登录"""
        url = 'http://hc.zhihuichaoren.com/student4'
        driver.get(url)
        try:
            result = is_element_exist(driver, '//*[@id="root"]/div/div[1]/div', 'TAD自定义域名学生端登录页')
            mobil_xpath = '//*[@id="username"]'
            code_xpath = '//*[@id="password"]'
            branch = is_branch_exist(driver, '//*[@id="root"]/div/div[1]/div/form', 'student4_custom')
            if branch == 'true':
                obvious_wait_click(driver, '//*[@id="branch"]/div/span', '选择校区')
                obvious_wait_click(driver, '/html/body/div[3]/div/div/div/ul/li[1]', '选择总校区')
                btn_xpath = '//*[@id="root"]/div/div[1]/div/form/div[4]/div/div/span/button'
            else:
                btn_xpath = '//*[@id="root"]/div/div[1]/div/form/div[3]/div/div/span/button'
            login(driver, mobil_xpath, code_xpath, btn_xpath, 'student4_custom', "15005201535", "201535")
            result = is_element_exist(driver, "//*[@id='root']/div/aside/div[1]/img", "TAD自定义域名学生端学生端")
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true')
            if result=='false':
                is_fail()

