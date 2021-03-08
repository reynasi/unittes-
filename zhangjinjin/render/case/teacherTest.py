# -*- coding:utf-8 -*-
import os
import unittest

from BeautifulReport import BeautifulReport
from selenium import webdriver
from zhangjinjin.render.case.common import *


class teacherTest(unittest.TestCase):
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

    @BeautifulReport.add_test_img('test_teacher')
    def test_teacher(self):
        """teacher：酷培教师端登录"""
        project = "teacher"
        try:
            new_tab_cn(driver, project)
            is_element_exist(driver, '//*[@id="root"]/div/div/div/div[1]', project + '登录页')
            mobil_xpath = '//*[@id="mobile"]'
            code_xpath = '//*[@id="captcha"]'
            branch = is_branch_exist(driver, '//*[@id="root"]/div/div/div/div[1]/div[2]/form', project)
            if branch == 'true':
                obvious_wait_click(driver, '//*[@id="branch"]/div/span', '选择校区')
                obvious_wait_click(driver, '/html/body/div[3]/div/div/div/ul/li[1]', '选择总校区')
                btn_xpath = '//*[@id="root"]/div/div/div/div[1]/div[2]/form/div[4]/div/div/span/button'
            else:
                btn_xpath = '//*[@id="root"]/div/div/div/div[2]/form/div[3]/div/div/span/button'
            login(driver, mobil_xpath, code_xpath, btn_xpath, project)
            result = is_element_exist(driver, '//*[@id="root"]/div/div[1]/div[1]/span', "酷培ai教师端")
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true')
            if result=='false':
                is_fail()



# testsuit = unittest.TestSuite()
# testsuit.addTests(unittest.makeSuite(teacher4Test))
# run = BeautifulReport(testsuit)
# print(os.path.abspath('../report'))
# run.report(filename='teacher4测试报告', description='teacher4测试用例', report_dir=os.path.abspath('../report'))
