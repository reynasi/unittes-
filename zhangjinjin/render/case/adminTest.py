# -*- coding:utf-8 -*-
import os
import unittest

from BeautifulReport import BeautifulReport
from selenium import webdriver
from zhangjinjin.render.case.common import *


class adminTest(unittest.TestCase):
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

    @BeautifulReport.add_test_img('test_admin')
    def test_admin(self):
        """admin：learnta管理系统"""
        project = "admin"
        try:
            new_tab_cn(driver, project)
            is_element_exist(driver, '//*[@id="root"]/div/div/h1', project + '登录页面')
            mobil_xpath = "//*[@id='username']"
            code_xpath = "//*[@id='root']/div/div/form/div[2]/div[2]/div/div/div/div[1]/input"
            btn_xpath = "//*[@id='root']/div/div/form/div[3]/div/div/button"
            login(driver, mobil_xpath, code_xpath, btn_xpath, project)
            result = is_element_exist(driver, "//*[@id='root']/div/div[1]/h1/a/span[2]", project + '登陆后元素存在判定')
            obvious_wait_click(driver, '//*[@id="root"]/div/div[2]/ul/li[2]/div', '题目管理')  # 题目管理
            obvious_wait_click(driver, '//*[@id="题目管理$Menu"]/li[1]', '题目录入')  # 题目录入
            obvious_wait_click(driver, '//*[@id="category"]/label[1]/span[2]', '数学')  # 数学
            obvious_wait_click(driver, '//*[@id="state"]/label[2]/span[2]', '练习题')  # 练习题
            obvious_wait_click(driver, '//*[@id="type"]/label[2]/span[2]', '选择题')  # 选择题
            driver.execute_script('window.scrollBy(0, 200)')  # 页面下滑200像素
            obvious_wait_click(driver, '//*[@id="isImageOptions"]', '图片选项')  # 图片选项
            obvious_wait_sendkeys(driver,
                                  '//*[@id="root"]/div/div[2]/div/div/form/div[5]/div[2]/div/div/div[1]/div[2]/div/span/div/span/input',
                                  'D:\Material\图片\8952.jpg', '图片上传')
            # obvious_wait_click('//*[@id="root"]/div/div[2]/ul/li[3]/div/span/span', '知识点管理')  # 知识点管理
            # obvious_wait_click('//*[@id="知识点管理$Menu"]/li[2]', '知识点列表')  # 知识点列表
            # obvious_wait_sendkeys('//*[@class="videoUpload"]/form/div[4]/div[2]/div/div/div/input', 'D:\Material\视频\hd.mp4',
            #                       '英语视频上传')  # 英语视频上传
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true')
            if result=='false':
                is_fail()



