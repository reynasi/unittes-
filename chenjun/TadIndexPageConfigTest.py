# -*- encoding=utf8 -*-
__author__ = "chenjun"

import os
import sys
import traceback
import unittest
import time
from airtest.core.api import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
from selenium.webdriver.support import expected_conditions as EC
from BeautifulReport import BeautifulReport
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

capabilities = DesiredCapabilities.CHROME
capabilities['loggingPrefs'] = { 'browser':'ALL' }

url = "https://cj.learnta.cn/teacherx"

report_dir = 'D:/learntaUitest/uitest/report/'
img_path = 'D:/learntaUitest/uitest/chenjun/img/'

class TadIndexPageConfigTest(unittest.TestCase):
    def setUp(self):
        global driver
        # url = "https://cj.learnta.cn/teacherx"
        # platf = sys.platform
        # print("platform:" + platf)
        # if platf != 'darwin':
        #     report_dir = "/opt/uitest/report"
        #     img_path = "/opt/uitest/img"
        # else:
        #     report_dir = "./report"
        #     img_path = "./img"
        # driver = WebChrome()
        options = webdriver.ChromeOptions()
        # driver = webdriver.Chrome(desired_capabilities=capabilities)
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        driver.implicitly_wait(10)
        # driver.maximize_window()

    def tearDown(self):
        try:
            driver.close()
            driver.quit()
        except:
            print("close fail")

    def save_img(self, img_name):
        driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))

    @BeautifulReport.add_test_img('testLoopClickModular')
    def testLoopClickModular(self):
        '''测试循环点击首页模块'''
        driver.find_element_by_xpath("//div[@style='display: block; user-select: none;']").click()
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/ul/li").click()
        driver.find_element_by_xpath("//input[@placeholder='请输入手机号码']").send_keys('18616015761')
        driver.find_element_by_xpath("//input[@placeholder='请输入验证码']").send_keys("5792")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        print(driver.get_log('browser'))


        def getElementNum():
            elements = driver.find_elements_by_class_name("subSystemMenuContainer")
            lists = []
            for num in elements:
                temp = num.text
                lists.append(temp)
            truelist = lists[0].splitlines()
            ElementNum = len(truelist)
            return ElementNum


        loopNum = getElementNum()
        elementTextIn = ['教学系统', '课程体系', '数据分析', '移动课堂', '题库', '招生测评', '多媒体库', '教学测评']
        elementTrueTextIn = []
        for i in range(loopNum):
            divNum = str(i+1)
            print(divNum)
            print(type(divNum))
            elementTextOut = driver.find_element_by_xpath("//*[@id=\"root\"]/div/header/div/div/div[2]/div[" + divNum + "]/div[2]").text
            print(elementTextOut)
            driver.find_element_by_xpath("//*[@id=\"root\"]/div/header/div/div/div[2]/div[" + divNum + "]/div[2]").click()
            temp2 = driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/aside/div/div[1]/ul/li/div/span").text
            elementTrueTextIn.append(temp2)
            sleep(2);
            driver.find_element_by_xpath("//img[@src='https://lcdns-pic.learnta.com/defaultLogo_02.png']").click()
            print(driver.get_log('browser'))
            self.assertEqual(elementTextIn[i], elementTextOut, msg="测试失败")
        self.assertEqual(elementTrueTextIn[3], '学习任务', msg="测试失败")

testsuite = unittest.TestSuite()
testsuite.addTests(unittest.makeSuite(TadIndexPageConfigTest))

runner = BeautifulReport(( testsuite ))
runner.report(filename='Tad首页配置测试报告.html', description='Tad首页配置测试用例', report_dir=report_dir)

