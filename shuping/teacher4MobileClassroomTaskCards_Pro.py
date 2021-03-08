#coding=utf-8

# @Time    : 2020/2/13
# @Author  : shuping zhao
# @File    : teacher4MobileClassroomTaskCards_Pro.py
import sys
import time
import traceback
import unittest

from BeautifulReport import BeautifulReport
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append('/opt/')
sys.path.append('/opt/uitest/shuping/common/Common/')
sys.path.append('/opt/uitest/shuping/page/LoginPage/')
from uitest.shuping.common.Common import Common
from uitest.shuping.page.LoginPage import LoginPage

class teacher4MobileClassroomTaskCards_Pro(unittest.TestCase):

    def setUp(self):
        global browser
        global window_teacher
        global urlstr
        global orgId
        urlstr = "autotest.learnta.cn"
        orgId = 100040  # 测服是1000369
        try:
            # linux1路径
            #path = "/usr/local/python3/chromedriver"

            #path = os.path.dirname(os.path.abspath('./config/chromedriver/chromedriver'))
            teacher4url = Common.getUrl(self, "TypeUrl", "teacher4Url")
            teacherUsername = "18817572035"
            teacherPassword = "1111"
            # linux使用的静默执行方法
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument("--no-sandbox")
            options.add_argument('--disable-gpu')
            options.add_argument('window-size=1280x1024')
            # options.add_argument('--headless')
            # options.add_argument('--disable-gpu')
            # options.add_argument('--no-sandbox')

            # 设置打开浏览器不显示data; 加载本地浏览器数据，加载很慢放弃！
            #options.add_argument('--user-data-dir=/Users/shuping/Library/Application Support/Google/Chrome/Default')
            # mac、linux配置
            #browser = webdriver.Chrome(executable_path=path, options=options)
            # 服务器上写法
            browser = webdriver.Chrome(options=options)
            windows = LoginPage.teacher4Login(self, browser, teacher4url, teacherUsername, teacherPassword)
            print("-------------------> 【0】 Setup Teacher4 登录成功! <----------------------\n")
            time.sleep(1)
            # 点击移动课堂模块
            Common.findElementActionClick(self, browser, "//div[@name='layout_container_name']/div[3]/div[2]/div")
            time.sleep(0.5)
            if self._testMethodName == "test_f_assiginPhysicalCard":
                # 输入自动化测试移动课堂 搜索课程
                browser.find_element_by_xpath("//input[@type='text']").send_keys("自动化测试物理课程")
            else:
                # 输入自动化测试移动课堂 搜索课程
                browser.find_element_by_xpath("//input[@type='text']").send_keys("自动化测试移动课堂")
            # 点击搜索按钮
            Common.findElementActionClick(self, browser, "//div[@class='pageBar']/button[1]")
            time.sleep(0.5)
            # 点击 自动化测试移动课堂 进入课程
            Common.findElementActionClick(self, browser, "//div[@class='listLayout']/div[1]")
            time.sleep(0.5)
            # 点击选择任务卡按钮
            Common.findElementActionClick(self, browser, "//div[@class='pPageHeaderTitle']/button")

        except Exception as e:
            traceback.print_exc()
            print(e)

    def tearDown(self):
        try:
            browser.close()
            browser.quit()
        except:
            traceback.print_exc()
            print("close fail")

    def save_img(self, img_name):  # 错误截图方法，这个必须先定义好
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        # mac存放图片路径
        #browser.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"./img"), img_name))
        # mac存放图片路径2
        #browser.get_screenshot_as_file('{}/{}.png'.format(r"/Users/shuping/Report/img", img_name))
        # linux存放图片路径
        browser.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))

    @BeautifulReport.add_test_img('test_a_assiginMobileTextCard')
    def test_a_assiginMobileTextCard(self):
        '''移动课堂完成富文本和解析卡'''
        try:
            # 获取勾选框列表
            checkboxlist = browser.find_elements_by_xpath("//input[@type='checkbox']")
            # 循环点击勾选框
            for i in range(2):
                # if i == 4:
                #     js = "$('.lFrame main').scrollTop(2000)"
                #     browser.execute_script(js)
                action = ActionChains(browser)
                above = checkboxlist[i]
                action.move_to_element(above).perform()
                action.click(above).perform()
                time.sleep(0.3)
            # 点击立即分配按钮
            browser.find_element_by_xpath("//div[@class='homeworkFolderFooter']/button[1]").click()
            time.sleep(0.3)
            # 清空 任务名称
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").clear()
            # 重命名 任务名称
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").send_keys("自动化测试移动任务解析卡和富文本卡")
            time.sleep(0.3)
            # 点击确定按钮
            browser.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
            time.sleep(0.5)
            img_url = ""
            img_url = browser.find_element_by_xpath("//div[@class='img-url']/a").get_attribute("href")
            js2 = 'window.open("'+img_url+'");'
            browser.execute_script(js2)
            # 获取新打开页窗口
            window_new = browser.window_handles[1]
            browser.switch_to.window(window_new)
            time.sleep(3)
            # 输入账号、密码、点击登录
            browser.find_element_by_id("username").send_keys("测试学生173")
            browser.find_element_by_id("mobile").send_keys("17317495785")
            browser.find_element_by_id("code").send_keys("1111")
            browser.find_element_by_xpath("//button[@type='submit']").click()

            # 点击第一个任务卡 解析卡
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()
            browser.find_element_by_xpath("//div[@class='ant-tabs-nav-scroll']/div/div[1]/div[2]").click()
            pointname = ""
            pointname = browser.find_element_by_xpath("//div[@class='ant-tabs-nav-scroll']/div/div[1]/div[2]/span").text
            # 返回浏览器上一页
            browser.back()

            # 点击第二个任务卡 富文本卡
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()
            textContent = browser.find_element_by_xpath("//div[@class='task-html']/p[1]").text
            textflag = False
            if "测试富文本卡" in textContent:
                textflag = True

        except:
            traceback.print_exc()
            print("")
        self.assertEqual("查看讲义", pointname, msg="解析卡查看讲义名字获取失败！")
        self.assertEqual(True, textflag, msg="富文本卡打开内容失败！")

    @BeautifulReport.add_test_img('test_b_assiginMobileExeciseCard')
    def test_b_assiginMobileExeciseCard(self):
        '''移动课堂完成练习卡和闯关卡'''
        try:
            # 输入闯关卡搜索内容，点击搜索按钮
            browser.find_element_by_xpath("//input[@type='text']").send_keys("练习闯关")
            browser.find_element_by_xpath("//div[@class='pageBar']/button[1]").click()
            # 点击选择勾选框
            # 获取勾选框列表
            checkboxlist = browser.find_elements_by_xpath("//input[@type='checkbox']")
            # 循环点击勾选框
            for i in range(2):
                action = ActionChains(browser)
                above = checkboxlist[i]
                action.move_to_element(above).perform()
                action.click(above).perform()
                time.sleep(0.3)
                js = "$('.lFrame main').scrollTop(1000)"
                browser.execute_script(js)
            # 点击立即分配按钮
            browser.find_element_by_xpath("//div[@class='homeworkFolderFooter']/button[1]").click()
            time.sleep(0.3)
            # 清空默认任务名称
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").clear()
            # 重命名任务名称
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").send_keys("自动化测试移动任务练习卡闯关卡")
            time.sleep(0.3)
            # 点击确定按钮
            browser.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
            time.sleep(0.5)
            img_url = ""
            img_url = browser.find_element_by_xpath("//div[@class='img-url']/a").get_attribute("href")
            js2 = 'window.open("' + img_url + '");'
            browser.execute_script(js2)
            # 获取新打开页窗口
            window_new = browser.window_handles[1]
            browser.switch_to.window(window_new)
            time.sleep(3)
            # 输入账号、密码、点击登录
            browser.find_element_by_id("username").send_keys("测试学生173")
            browser.find_element_by_id("mobile").send_keys("17317495785")
            browser.find_element_by_id("code").send_keys("1111")
            browser.find_element_by_xpath("//button[@type='submit']").click()

            # 点击第一个 闯关卡进入
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()
            footBtnFlag = False
            footBtnFlag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            for i in range(4):
                # 点击选择A
                browser.find_element_by_xpath("//div[@class='task-question__content']/div[2]").click()
                time.sleep(0.5)
                # 点击下一步按钮
                browser.find_element_by_xpath("//div[@class='task-abstask__footer']/div[3]").click()
                time.sleep(0.5)
            # 点击弹窗的确定按钮
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
            time.sleep(3)
            # 获取结果页的题目列表
            buttonlist = browser.find_elements_by_xpath("//button[@type='button']")
            # 题目总数
            questioncount1 = 0
            questioncount1 = len(buttonlist)

            browser.back()
            # 点击第二个任务卡 练习卡
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()
            time.sleep(1)
            for i in range(5):
                # 点击下一步按钮
                browser.find_element_by_xpath("//div[@class='task-abstask__footer']/div[3]").click()
                time.sleep(0.5)
            time.sleep(0.5)
            browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button[2]").click()
            # 获取结果页的题目列表
            questionlist2 = browser.find_elements_by_xpath("//div[@class='task-report__content']/div/div")
            # 题目总数
            questioncount2 = 0
            questioncount2 = len(questionlist2)
            self.assertEqual(5, questioncount2, msg="完成练习卡失败！")
        except:
            traceback.print_exc()
            print("移动课堂完成练习闯关卡失败！")
        self.assertEqual(4, questioncount1, msg="完成闯关卡失败！")

    @BeautifulReport.add_test_img('test_c_assiginMobileIntelligentCard')
    def test_c_assiginMobileIntelligentCard(self):
        '''移动课堂完成智能练习卡'''
        try:
            # 输入闯关卡搜索内容，点击搜索按钮
            browser.find_element_by_xpath("//input[@type='text']").send_keys("智能练习卡")
            browser.find_element_by_xpath("//div[@class='pageBar']/button[1]").click()
            # 点击选择勾选框
            Common.findElementClick(self, browser, "//input[@type='checkbox']")

            # 点击立即分配按钮
            browser.find_element_by_xpath("//div[@class='homeworkFolderFooter']/button[1]").click()
            time.sleep(0.3)
            # 清空默认任务名称
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").clear()
            # 重命名任务名称
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").send_keys("自动化测试移动任务智能练习卡")
            time.sleep(0.3)
            # 点击确定按钮
            browser.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
            time.sleep(0.5)
            img_url = ""
            img_url = browser.find_element_by_xpath("//div[@class='img-url']/a").get_attribute("href")
            js2 = 'window.open("' + img_url + '");'
            browser.execute_script(js2)
            # 获取新打开页窗口
            window_new = browser.window_handles[1]
            browser.switch_to.window(window_new)
            time.sleep(3)
            # 输入账号、密码、点击登录
            browser.find_element_by_id("username").send_keys("测试学生173")
            browser.find_element_by_id("mobile").send_keys("17317495785")
            browser.find_element_by_id("code").send_keys("1111")
            browser.find_element_by_xpath("//button[@type='submit']").click()

            # 点击第一个 闯关卡进入
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()

            elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div[1]")
            count = 0
            while (elementflag):
                # 点击下一题按钮
                Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div[1]")
                time.sleep(0.5)
                # 点击确定按钮
                Common.findElementClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
                time.sleep(0.5)
                Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div[1]")
                time.sleep(0.5)
                count = count + 1
                print("-------------------> 第" + str(count) + "道题完成<---------------------")
                elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div[1]")
            time.sleep(1)
            topicname = ""
            topicname = browser.find_element_by_xpath("//div[@class='task-summary__content']/div[3]/div[1]").text

        except:
            traceback.print_exc()
            print("移动课堂完成智能练习卡失败！")
        self.assertEqual("专题：智能练习卡Text", topicname, msg="完成智能练习卡失败！")

    @BeautifulReport.add_test_img('test_d_assiginMobileTestingCard')
    def test_d_assiginMobileTestingCard(self):
        '''移动课堂完成测评卡'''
        try:
            # 输入闯关卡搜索内容，点击搜索按钮
            browser.find_element_by_xpath("//input[@type='text']").send_keys("测评卡")
            browser.find_element_by_xpath("//div[@class='pageBar']/button[1]").click()
            # 点击选择勾选框
            Common.findElementClick(self, browser, "//input[@type='checkbox']")

            # 点击立即分配按钮
            browser.find_element_by_xpath("//div[@class='homeworkFolderFooter']/button[1]").click()
            time.sleep(0.3)
            # 清空默认任务名称
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").clear()
            # 重命名任务名称
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").send_keys("自动化测试移动课堂任务测评卡")
            time.sleep(0.3)
            # 点击确定按钮
            browser.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
            time.sleep(0.5)
            img_url = ""
            img_url = browser.find_element_by_xpath("//div[@class='img-url']/a").get_attribute("href")
            js2 = 'window.open("' + img_url + '");'
            browser.execute_script(js2)
            # 获取新打开页窗口
            window_new = browser.window_handles[1]
            browser.switch_to.window(window_new)
            time.sleep(3)
            # 输入账号、密码、点击登录
            browser.find_element_by_id("username").send_keys("测试学生173")
            browser.find_element_by_id("mobile").send_keys("17317495785")
            browser.find_element_by_id("code").send_keys("1111")
            browser.find_element_by_xpath("//button[@type='submit']").click()
            # 点击测评卡进入
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()

            elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div[1]")
            count = 0
            while (elementflag):
                # 点击下一题按钮
                Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div[1]")
                time.sleep(0.5)
                count = count + 1
                print("-------------------> 第" + str(count) + "道题完成<---------------------")
                elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div[1]")
            time.sleep(1)
            topicname = ""
            topicname = browser.find_element_by_xpath("//div[@class='task-summary__content']/div[3]/div[1]").text
            weakPointTextList = Common.getElementsText(self, browser, "//div[@class='task-summary__content']/div[6]/div[1]")
            poitList = Common.getElementsText(self, browser, "//div[@class='task-summary__content']/div[6]/div[@class='task-summary__point']/div")
        except:
            traceback.print_exc()
            print("移动课堂完成测评卡失败！")
        self.assertEqual("专题：语法结构U1", topicname, msg="测评卡结果页专题名称显示错误！")
        self.assertListEqual(['薄弱知识点列表\n（共3个知识点）'], weakPointTextList, msg="测评卡结果页薄弱知识点个数显示错误！")
        self.assertListEqual(['B1 特殊疑问句的结构和用法','B2 数词的用法','B3 方位表达法'], poitList, msg="测评卡结果页薄弱知识点列表数据显示错误！")



    @BeautifulReport.add_test_img('test_e_assiginMobileEnglishCard')
    def test_e_assiginMobileEnglishCard(self):
        '''移动课堂完成阅读完形听力卡'''
        try:
            # 输入闯关卡搜索内容，点击搜索按钮
            browser.find_element_by_xpath("//input[@type='text']").send_keys("阅读完形听力")
            browser.find_element_by_xpath("//div[@class='pageBar']/button[1]").click()

            checkboxlist = browser.find_elements_by_xpath("//input[@type='checkbox']")
            # 循环点击勾选框
            for i in range(3):
                if i == 2:
                    js = "$('.lFrame main').scrollTop(2000)"
                    browser.execute_script(js)
                action = ActionChains(browser)
                above = checkboxlist[i]
                action.move_to_element(above).perform()
                action.click(above).perform()

            # 点击立即分配按钮
            browser.find_element_by_xpath("//div[@class='homeworkFolderFooter']/button[1]").click()
            time.sleep(0.3)
            # 清空默认任务名称
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").clear()
            # 重命名任务名称
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").send_keys("自动化测试移动课堂任务英语新题型卡")
            time.sleep(0.3)
            # 点击确定按钮
            browser.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
            time.sleep(0.5)
            img_url = ""
            img_url = browser.find_element_by_xpath("//div[@class='img-url']/a").get_attribute("href")
            js2 = 'window.open("' + img_url + '");'
            browser.execute_script(js2)
            # 获取新打开页窗口
            window_new = browser.window_handles[1]
            browser.switch_to.window(window_new)
            time.sleep(3)
            # 输入账号、密码、点击登录
            browser.find_element_by_id("username").send_keys("测试学生173")
            browser.find_element_by_id("mobile").send_keys("17317495785")
            browser.find_element_by_id("code").send_keys("1111")
            Common.findElementClick(self, browser, "//button[@type='submit']")

            print("======================= 阅读卡开始 =====================\n")
            # 点击阅读卡进入
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()

            elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div[1]")
            count = 0
            while (elementflag):
                count = count + 1
                Common.findElementClick(self, browser, "//div[@class='task-read__questions']/div[" + str(
                    count) + "]/div/div/div/div[2]")
                time.sleep(0.3)
                # 点击下一题按钮
                Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div[1]")
                time.sleep(0.5)
                print("-------------------> 第" + str(count) + "道题完成<---------------------\n")
                elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div[1]")
            time.sleep(1)
            questionlist1 = browser.find_elements_by_xpath("//div[@class='task-read__summary']/span")
            questioncount1 = len(questionlist1)

            print("======================= 阅读卡结束 =====================\n")

            print("======================= 听力卡开始 =====================\n")
            # 返回到未完成任务卡界面
            browser.back()
            # 点击选择下一个任务卡，听力卡
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()

            questionList = browser.find_elements_by_xpath("//div[@class='task-listen__question']")
            i = 0
            x = 300
            while i < len(questionList):
                i = i + 1
                # 滚动听力卡的题目列
                jquery = "$('.task-listen__wrapper').scrollTop(" + str(x) + ")"
                browser.execute_script(jquery)
                if i <= 7:
                    x = x + 350
                else:
                    x = x + 370
                # 输入答案
                browser.find_element_by_xpath(
                    "//div[@class='task-listen__question'][" + str(i) + "]/div/div/div/div[3]").click()
                time.sleep(0.3)
                print("-------------------> 第" + str(i) + "道题完成<---------------------\n")

            # 点击提交按钮
            Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div[1]")
            time.sleep(1)
            questionlist2 = browser.find_elements_by_xpath("//div[@class='task-listen__question']")
            questioncount2 = len(questionlist2)
            print("======================= 听力卡结束 =====================\n")

            print("======================= 完形填空卡开始 =====================\n")
            # 返回到未完成任务卡界面
            browser.back()
            # 点击选择下一个任务卡，完形卡
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()
            elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div[1]")
            count2 = 0
            while (elementflag):
                count2 = count2 + 1
                Common.findElementClick(self, browser, "//div[@class='task-read__questions']/div[" + str(
                    count2) + "]/div/div/div/div[2]")
                time.sleep(0.3)
                # 点击下一题按钮
                Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div[1]")
                time.sleep(0.5)
                print("-------------------> 第" + str(count2) + "道题完成<---------------------\n")
                elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div[1]")
            time.sleep(1)
            questionlist3 = browser.find_elements_by_xpath("//div[@class='task-read__summary']/span")
            questioncount3 = len(questionlist3)
            print("======================= 完形填空卡结束 =====================\n")
            self.assertEqual(6, questioncount3, msg="完成完形卡失败！")

        except:
            traceback.print_exc()
            print("移动课堂完成英语新题型卡失败！")
        self.assertEqual(5, questioncount1, msg="完成阅读卡失败！")
        self.assertEqual(10, questioncount2, msg="完成听力卡失败！")

    @BeautifulReport.add_test_img('test_f_assiginPhysicalCard')
    def test_f_assiginPhysicalCard(self):
        ''' 移动课堂分配物理多选题卡和新题型卡 '''
        try:
            # 输入闯关卡搜索内容，点击搜索按钮
            browser.find_element_by_xpath("//input[@type='text']").send_keys("测试")
            browser.find_element_by_xpath("//div[@class='pageBar']/button[1]").click()

            checkboxlist = browser.find_elements_by_xpath("//input[@type='checkbox']")
            # 循环点击勾选框
            for i in range(2):
                # if i == 2:
                #     js = "$('.lFrame main').scrollTop(2000)"
                #     browser.execute_script(js)
                action = ActionChains(browser)
                above = checkboxlist[i]
                action.move_to_element(above).perform()
                action.click(above).perform()

            # 点击立即分配按钮
            browser.find_element_by_xpath("//div[@class='homeworkFolderFooter']/button[1]").click()
            time.sleep(0.3)
            # 清空默认任务名称
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").clear()
            # 重命名任务名称
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").send_keys("自动化测试移动课堂任务物理新题型卡")
            time.sleep(0.3)
            # 点击确定按钮
            browser.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
            time.sleep(0.5)
            img_url = ""
            img_url = browser.find_element_by_xpath("//div[@class='img-url']/a").get_attribute("href")
            js2 = 'window.open("' + img_url + '");'
            browser.execute_script(js2)
            # 获取新打开页窗口
            window_new = browser.window_handles[1]
            browser.switch_to.window(window_new)
            time.sleep(3)
            # 输入账号、密码、点击登录
            browser.find_element_by_id("username").send_keys("测试学生173")
            browser.find_element_by_id("mobile").send_keys("17317495785")
            browser.find_element_by_id("code").send_keys("1111")
            Common.findElementClick(self, browser, "//button[@type='submit']")

            print("======================= 多选题卡开始 =====================\n")
            # 点击多选题卡进入
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()

            questionCount = browser.find_element_by_xpath("//div[@class='task-abstask__pagination']/span[2]").text
            count = 0
            for i in range(int(questionCount)):
                count = count + 1
                Common.findElementClick(self, browser, "//div[@class='task-question__content']/div[2]")
                Common.findElementActionClick(self, browser, "//div[@class='task-question__content']/div[4]")
                time.sleep(0.3)
                # 点击下一题按钮
                Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
                time.sleep(0.5)
                print("-------------------> 第" + str(count) + "道题完成<---------------------\n")
            time.sleep(1.3)
            # 点击弹窗的确定按钮
            Common.findElementClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
            time.sleep(0.6)
            questionlist1 = Common.getElementsText(self, browser, "//div[@class='task-question__content']/div[1]")
            rightCount1 = 0
            for i in range(len(questionlist1)):
                if questionlist1[i]=="答对了":
                    rightCount1 = rightCount1+1
                else:
                    print("======================= 第"+ str(i+1) +"道题答错了 ===========================")
            print("======================= 多选题卡结束 =====================\n")

            print("======================= 物理新题型卡开始 =====================\n")
            # 返回到未完成任务卡界面
            browser.back()
            # 点击选择下一个任务卡
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()

            # 输入框列表
            inputList = browser.find_elements_by_xpath("//div[@class='gapInput-mathinput gapInput-mathinput_empty']")
            count = 0
            for i in range(len(inputList)):
                count = count + 1
                if i ==0:
                    browser.find_element_by_xpath("//input[@autocomplete='off']").send_keys("大小")
                elif i ==1:
                    inputList[i].click()
                    Common.findElementClick(self, browser, "//span[@data-value='letter']")
                    Common.findElementClick(self,browser, "//span[@data-value='shift']")
                    Common.findElementClick(self, browser, "//span[@data-value='b']")
                    Common.findElementClick(self, browser, "//span[@data-value='c']")
                elif i ==2:
                    js = "$('.task-multi__questions').scrollTop(800)"
                    browser.execute_script(js)
                    time.sleep(0.5)
                    inputList[i].click()
                    Common.findElementClick(self, browser, "//span[@data-value='b']")
                    Common.findElementClick(self, browser, "//span[@data-value='d']")
                time.sleep(0.5)
                print("-------------------> 第" + str(count) + "道题完成<---------------------\n")
            # 点击左边问题区域关闭数学公式
            Common.findElementActionClick(self, browser, "//div[@class='task-multi__problem']")
            # 点击提交按钮
            Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            time.sleep(1)
            # 点击弹窗的确定按钮
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
            time.sleep(0.5)
            questionList2= Common.getElementsText(self, browser, "//div[@class='task-multi__questions']/div/div/div/div[1]")
            rightCount2 = 0
            for i in range(len(questionList2)):
                if questionList2[i]=="答对了":
                    rightCount2 = rightCount2+1
                else:
                    print("======================= 第" + str(i + 1) + "道题答错了 ===========================")
                time.sleep(0.3)
            print("======================= 物理新题型卡结束 =====================\n")
        except:
            traceback.print_exc()
            print("移动课堂完成物理新题型卡失败！")
        self.assertEqual(2, rightCount1, msg="完成物理多选题卡失败！")
        self.assertEqual(3, rightCount2, msg="完成物理新题型卡失败！")

directList = Common.getDirectPath(Common)
report_dir = directList[0]
img_path = directList[1]

testsuit = unittest.TestSuite()
#testsuit.addTest(teacher4MobileClassroomTaskCards_Pro("test_d_assiginMobileTestingCard"))
testsuit.addTests(unittest.makeSuite(teacher4MobileClassroomTaskCards_Pro))
run = BeautifulReport(testsuit)
# 服务器存储路径
run.report(filename='TAD1.0正服_移动课堂复制链接完成任务卡', description='TAD1.0_正服移动课堂完成任务卡测试用例', report_dir=report_dir)
