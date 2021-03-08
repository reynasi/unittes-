# coding=utf-8

import unittest

from BeautifulReport import BeautifulReport
from selenium import webdriver
import time
import traceback

from zhangjinjin.go.case.common import *

global result


class goTest(unittest.TestCase):
    def setUp(self):
        global driver
        options = webdriver.ChromeOptions()
        # options.add_experimental_option('mobileEmulation', mobileEmulation)
        options.add_argument("start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument('--disable-gpu')
        options.add_argument('window-size=1920x3000')
        # 创建驱动实例
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
        """ go :做题流程"""
        try:
            # 打开公众号测评登录页面
            driver.get("https://learnta.cn/go/#/kupei/signin")
            time.sleep(1)
            # 输入用户名
            driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[1]/input").send_keys("test")
            # 输入电话
            driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[2]/input").send_keys("18616215375")
            # 输入验证码
            driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[3]/input").send_keys("1111")
            # 点击登录
            driver.find_element_by_xpath("//*[@id='root']/div/div/form/a/span").click()
            print("----->登录")
            time.sleep(3)
            # 选择年级
            driver.find_element_by_xpath("//*[@id='root']/div/div[2]/ul/li[1]").click()
            print("----->选择年级")
            time.sleep(1)
            # 选择科目
            driver.find_element_by_xpath("//*[@id='root']/div/div[2]/ul/li[2]/span[2]").click()
            print("----->选择科目")

            # 记录题目数量
            num = 0
            # 循环做题
            while findNext(driver):
                # 点击下一题按钮
                try:
                    driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[2]/div/div[2]/a[2]").click()
                    num = num + 1
                    print("----->第 %d 道题完成" % (num))
                except:
                    # 判断是否出现审题弹框提示
                    findReview(driver)
            result = 'true'
        except:
            traceback.print_exc()
            result = 'false'
        finally:
            self.assertEqual(result, 'true')


# testsuit = unittest.TestSuite()
# testsuit.addTests(unittest.makeSuite(Testgo))
# run = BeautifulReport(testsuit)
# run.report(filename='teacher4测试报告', description='teacher4测试用例', report_dir=getreport())

# service.stop()
# 手机型号
mobile_emulation = {
    "deviceName": "Apple iPhone 3GS",
    "deviceName": "Apple iPhone 4",
    "deviceName": "Apple iPhone 5",
    "deviceName": "Apple iPhone 6",
    "deviceName": "Apple iPhone 6 Plus",
    "deviceName": "BlackBerry Z10",
    "deviceName": "BlackBerry Z30",
    "deviceName": "Google Nexus 4",
    "deviceName": "Google Nexus 5",
    "deviceName": "Google Nexus S",
    "deviceName": "HTC Evo, Touch HD, Desire HD, Desire",
    "deviceName": "HTC One X, EVO LTE",
    "deviceName": "HTC Sensation, Evo 3D",
    "deviceName": "LG Optimus 2X, Optimus 3D, Optimus Black",
    "deviceName": "LG Optimus G",
    "deviceName": "LG Optimus LTE, Optimus 4X HD",
    "deviceName": "LG Optimus One",
    "deviceName": "Motorola Defy, Droid, Droid X, Milestone",
    "deviceName": "Motorola Droid 3, Droid 4, Droid Razr, Atrix 4G, Atrix 2",
    "deviceName": "Motorola Droid Razr HD",
    "deviceName": "Nokia C5, C6, C7, N97, N8, X7",
    "deviceName": "Nokia Lumia 7X0, Lumia 8XX, Lumia 900, N800, N810, N900",
    "deviceName": "Samsung Galaxy Note 3",
    "deviceName": "Samsung Galaxy Note II",
    "deviceName": "Samsung Galaxy Note",
    "deviceName": "Samsung Galaxy S III, Galaxy Nexus",
    "deviceName": "Samsung Galaxy S, S II, W",
    "deviceName": "Samsung Galaxy S4",
    "deviceName": "Sony Xperia S, Ion",
    "deviceName": "Sony Xperia Sola, U",
    "deviceName": "Sony Xperia Z, Z1",
    "deviceName": "Amazon Kindle Fire HDX 7″",
    "deviceName": "Amazon Kindle Fire HDX 8.9″",
    "deviceName": "Amazon Kindle Fire (First Generation)",
    "deviceName": "Apple iPad 1 / 2 / iPad Mini",
    "deviceName": "Apple iPad 3 / 4",
    "deviceName": "BlackBerry PlayBook",
    "deviceName": "Google Nexus 10",
    "deviceName": "Google Nexus 7 2",
    "deviceName": "Google Nexus 7",
    "deviceName": "Motorola Xoom, Xyboard",
    "deviceName": "Samsung Galaxy Tab 7.7, 8.9, 10.1",
    "deviceName": "Samsung Galaxy Tab",
    "deviceName": "Notebook with touch",
    "deviceName": "iPhone 6"
}
