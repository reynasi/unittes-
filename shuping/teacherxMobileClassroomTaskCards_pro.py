#coding=utf-8

# @Time    : 2020/2/14
# @Author  : shuping zhao
# @File    : teacherxMobileClassroomTaskCards_pro.py
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
from uitest.shuping.page.LoginPage import LoginPage
from uitest.shuping.common.Common import Common


class teacherxMobileClassroomTaskCards_pro(unittest.TestCase):
    stuName = "测试173"
    taskUsername = "17317495785"
    taskPassword = "1111"
    global orgId
    orgId = 100040  # 测服是1000369

    def setUp(self):
        global browser
        global window_teacher
        try:
            #path = os.path.dirname(os.path.abspath('./config/chromedriver/chromedriver'))
            teacherxUrl = Common.getUrl(self, "TypeUrl", "teacherxUrl")
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

            windows = LoginPage.teacherxLogin(self, browser, teacherxUrl, teacherUsername, teacherPassword)

            # 点击移动课堂模块
            Common.findElementClick(self, browser, "//div[@name='layout_container_name']/div[1]/div[2]/div")
            time.sleep(0.5)
            if self._testMethodName=="test_f_assiginMobilePhysicalCards":
                # 输入物理人教版八年级同步课 搜索课程
                browser.find_element_by_xpath("//input[@type='text']").send_keys("物理人教版八年级同步课")
            else:
                # 输入自动化测试移动课堂 搜索课程
                browser.find_element_by_xpath("//input[@type='text']").send_keys("自动化测试teacherx移动课堂用例")
            # 点击搜索按钮
            browser.find_element_by_xpath("//button[@type='button']").click()
            time.sleep(0.5)
            # 点击 自动化测试移动课堂 进入课程
            browser.find_element_by_xpath("//div[@class='listLayout']/div[1]").click()
            time.sleep(0.5)
            # 点击选择任务卡按钮
            browser.find_element_by_xpath("//div[@class='pPageHeaderTitle']/button").click()
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
        # linux存放图片路径
        browser.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))

    @BeautifulReport.add_test_img('test_a_assiginXMobileTextCard')
    def test_a_assiginXMobileTextCard(self):
        '''移动课堂完成图文卡知识点解析卡'''
        try:
            # 输入闯关卡搜索内容，点击搜索按钮
            browser.find_element_by_xpath("//input[@type='text']").send_keys("图文主观题卡")
            browser.find_element_by_xpath("//div[@class='pageBar']/button[1]").click()
            # 获取勾选框列表
            checkboxlist = browser.find_elements_by_xpath("//input[@type='checkbox']")
            # 循环点击勾选框
            for i in range(2):
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
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").send_keys("自动化测试移动课堂任务图文知识点解析卡")
            time.sleep(0.3)
            # 点击确定按钮
            browser.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
            time.sleep(0.5)
            taskImgUrl = ""
            taskImgUrl = browser.find_element_by_xpath("//div[@class='img-url']/a").get_attribute("href")
            # task登陆
            LoginPage.taskLogin(self, browser, taskImgUrl, self.stuName, self.taskUsername, self.taskPassword)
            print("======================= 图文卡开始 =========================\n")
            # 点击任务卡 pdf图文卡
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()
            textContent = browser.find_element_by_xpath("//div[@placeholder='点击此处添加文本']").text
            textflag = False
            if "测试图文卡" in textContent:
                textflag = True
            print("======================== 图文卡结束 ==========================\n")

            print("======================== 知识点解析卡开始 =====================\n")
            browser.back()
            time.sleep(1)
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()
            time.sleep(1)
            # 点击提交按钮
            Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            time.sleep(1)
            # 点击弹窗确定按钮
            Common.findElementClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
            time.sleep(0.6)
            questionNum = ""
            questionNum = browser.find_element_by_xpath("//div[@class='task-question__content']/span").text
            self.assertEqual("01.", questionNum, msg="知识点解析卡完成失败！")
            print("======================= 知识点解析卡结束 =====================\n")
        except:
            traceback.print_exc()
            print("移动课堂完成图文知识点解析卡失败！")
        self.assertEqual(True, textflag, msg="图文卡打开内容失败！")

    @BeautifulReport.add_test_img('test_b_assiginXMobileExeciseCard')
    def test_b_assiginXMobileExeciseCard(self):
        '''移动课堂完成练习卡'''
        try:
            # 输入闯关卡搜索内容，点击搜索按钮
            browser.find_element_by_xpath("//input[@type='text']").send_keys("练习卡")
            browser.find_element_by_xpath("//div[@class='pageBar']/button[1]").click()
            time.sleep(1)
            # 点击选择勾选框
            Common.findElementClick(self, browser, "//input[@type='checkbox']")
            # 点击立即分配按钮
            browser.find_element_by_xpath("//div[@class='homeworkFolderFooter']/button[1]").click()
            time.sleep(0.3)
            # 清空默认任务名称
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").clear()
            # 重命名任务名称
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").send_keys("自动化测试移动课堂任务练习卡")
            time.sleep(0.3)
            # 点击确定按钮
            browser.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
            time.sleep(0.5)
            taskImgUrl = ""
            taskImgUrl = browser.find_element_by_xpath("//div[@class='img-url']/a").get_attribute("href")
            # task登陆
            LoginPage.taskLogin(self, browser, taskImgUrl, self.stuName, self.taskUsername, self.taskPassword)
            print("======================= 练习卡开始 =========================\n")
            # 点击练习卡进入
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()
            for i in range(4):
                if i == 0:
                    browser.find_element_by_xpath("//input[@autocomplete='off']").send_keys("A")
                    time.sleep(0.5)
                elif i == 1:
                    browser.find_element_by_xpath("//input[@autocomplete='off']").send_keys("try")
                    time.sleep(0.5)
                elif i > 1:
                    # 点击选择A
                    Common.findElementClick(self, browser, "//div[@class='task-question__content']/div[2]")
                    time.sleep(0.3)
                # 点击下一步按钮
                Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
                time.sleep(0.5)
            # 点击弹窗的确定按钮
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
            time.sleep(3)
            # 获取结果页的显示答案按钮列表
            buttonlist = browser.find_elements_by_xpath("//button[@type='button']")
            # 题目按钮总数
            questioncount = 0
            questioncount = len(buttonlist)

        except:
            traceback.print_exc()
            print("移动课堂完成练习卡失败！")
        self.assertEqual(4, questioncount, msg="完成练习卡失败！")

    @BeautifulReport.add_test_img('test_c_assiginXMobileIntelligentCard')
    def test_c_assiginXMobileIntelligentCard(self):
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
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").send_keys("自动化测试移动课堂任务智能练习卡")
            time.sleep(0.3)
            # 点击确定按钮
            browser.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
            time.sleep(0.5)
            taskImgUrl = ""
            taskImgUrl = browser.find_element_by_xpath("//div[@class='img-url']/a").get_attribute("href")
            # task登陆
            LoginPage.taskLogin(self, browser, taskImgUrl, self.stuName, self.taskUsername, self.taskPassword)
            # 点击智能练习卡进入
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()

            elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div[1]")
            count = 0
            while (elementflag):
                # 点击下一题按钮
                Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div[1]")
                time.sleep(0.5)
                # 点击确定按钮
                Common.findElementClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
                time.sleep(0.7)
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
        self.assertEqual("专题：重点词汇智能练习卡", topicname, msg="完成智能练习卡失败！")

    @BeautifulReport.add_test_img('test_d_assiginXMobileTestingCard')
    def test_d_assiginXMobileTestingCard(self):
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
            taskImgUrl = ""
            taskImgUrl = browser.find_element_by_xpath("//div[@class='img-url']/a").get_attribute("href")
            # task登陆
            LoginPage.taskLogin(self, browser, taskImgUrl, self.stuName, self.taskUsername, self.taskPassword)

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

        except:
            traceback.print_exc()
            print("移动课堂完成测评卡失败！")
        self.assertEqual("专题：语法结构M2", topicname, msg="完成测评卡失败！")

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
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").send_keys("自动化测试移动课堂任务英语新题型卡")
            time.sleep(0.3)
            # 点击确定按钮
            browser.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
            time.sleep(0.5)
            taskImgUrl = ""
            taskImgUrl = browser.find_element_by_xpath("//div[@class='img-url']/a").get_attribute("href")
            # task登陆
            LoginPage.taskLogin(self, browser, taskImgUrl, self.stuName, self.taskUsername, self.taskPassword)

            print("======================= 阅读卡开始 =====================\n")
            # 点击阅读卡进入
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()
            elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div[1]")
            count = 0
            while (elementflag):
                count = count + 1
                Common.findElementClick(self, browser, "//div[@class='task-read__questions']/div[" + str(count) + "]/div/div/div/div[2]")
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

            print("======================= 完形填空卡开始 =====================\n")
            # 返回到未完成任务卡界面
            browser.back()
            # 点击选择下一个任务卡，完形卡
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()
            elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div[1]")
            count2 = 0
            while (elementflag):
                count2 = count2 + 1
                Common.findElementClick(self, browser,
                                        "//div[@class='task-read__questions']/div[" + str(count2) + "]/div/div/div/div[2]")
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

            print("======================= 听力卡开始 =====================\n")
            # 返回到未完成任务卡界面
            browser.back()
            # 点击选择下一个任务卡，听力卡
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()

            questionList = browser.find_elements_by_xpath("//div[@class='task-listen__question']")
            i = 0
            x = 200
            while i < len(questionList):
                i = i + 1
                # 滚动听力卡的题目列
                jquery = "$('.task-listen__wrapper').scrollTop(" + str(x) + ")"
                browser.execute_script(jquery)
                x = x + 350
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
            self.assertEqual(5, questioncount2, msg="完成听力卡失败！")
        except:
            traceback.print_exc()
            print("移动课堂完成英语新题型卡失败！")
        self.assertEqual(5, questioncount1, msg="完成阅读卡失败！")
        self.assertEqual(10, questioncount3, msg="完成完形卡失败！")

    @BeautifulReport.add_test_img('test_f_assiginMobilePhysicalCards')
    def test_f_assiginMobilePhysicalCards(self):
        '''移动课堂完成物理新题型卡和多选题卡'''
        try:
            # 获取输入框列表
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
            browser.find_element_by_xpath("//input[@placeholder='请编辑任务名称']").send_keys("自动化测试移动课堂物理新题型和多选题卡")
            time.sleep(0.3)
            # 点击确定按钮
            browser.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
            time.sleep(0.5)
            taskImgUrl = ""
            taskImgUrl = browser.find_element_by_xpath("//div[@class='img-url']/a").get_attribute("href")
            # task登陆
            LoginPage.taskLogin(self, browser, taskImgUrl, self.stuName, self.taskUsername, self.taskPassword)
            print("======================= 物理新题型卡开始 =====================\n")
            # 点击物理新题型卡进入
            browser.find_element_by_xpath("//div[@role='tabpanel']/div[2]/div[1]/div[1]").click()
            # 输入框列表
            inputList = browser.find_elements_by_xpath(
                "//div[@class='gapInput-mathinput gapInput-mathinput_empty']")
            count = 0
            for i in range(len(inputList)):
                count = count + 1
                if i == 0:
                    browser.find_element_by_xpath("//input[@autocomplete='off']").send_keys("大小")
                elif i == 1:
                    inputList[i].click()
                    Common.findElementClick(self, browser, "//span[@data-value='letter']")
                    Common.findElementClick(self, browser, "//span[@data-value='shift']")
                    Common.findElementClick(self, browser, "//span[@data-value='b']")
                    Common.findElementClick(self, browser, "//span[@data-value='c']")
                elif i == 2:
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
            questionList1 = Common.getElementsText(self, browser,
                                                   "//div[@class='task-multi__questions']/div/div/div/div[1]")
            rightCount1 = 0
            for i in range(len(questionList1)):
                if questionList1[i] == "答对了":
                    rightCount1 = rightCount1 + 1
                    print("======================= 第" + str(i + 1) + "道题答对了 ===========================")
                else:
                    print("======================= 第" + str(i + 1) + "道题答错了 ===========================")
                time.sleep(0.3)
            print("======================= 物理新题型卡结束 =====================\n")

            browser.back()
            # 点击物理新题型卡进入
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
                time.sleep(1)
                print("-------------------> 第" + str(count) + "道题完成<---------------------\n")
            time.sleep(1.3)
            # 点击弹窗的确定按钮
            Common.findElementClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
            time.sleep(0.6)
            questionlist2 = Common.getElementsText(self, browser, "//div[@class='task-question__content']/div[1]")
            rightCount2 = 0
            for i in range(len(questionlist2)):
                if questionlist2[i] == "答对了":
                    rightCount2 = rightCount2 + 1
                    print("======================= 第" + str(i + 1) + "道题答对了 ===========================")
                else:
                    print("======================= 第" + str(i + 1) + "道题答错了 ===========================")
            print("======================= 新题型卡结束 =====================\n")
        except:
            traceback.print_exc()
            print("移动课堂完成物理新题型卡和多选题卡失败！")
        self.assertEqual(3, rightCount1, msg="物理新题型卡的做对题数不正确！")
        self.assertEqual(2, rightCount2, msg="物理多选题卡的做对题数不正确！")

directList = Common.getDirectPath(Common)
report_dir = directList[0]
img_path = directList[1]
testsuit = unittest.TestSuite()
#testsuit.addTest(teacherxMobileClassroomTaskCards_pro("test_a_assiginXMobileTextCard"))
testsuit.addTests(unittest.makeSuite(teacherxMobileClassroomTaskCards_pro))
run = BeautifulReport(testsuit)
# 服务器存储路径
run.report(filename='TAD2.0正服_移动课堂完成所有类型任务卡', description='TAD2.0正服_移动课堂完成所有类型任务卡测试用例', report_dir=report_dir)

