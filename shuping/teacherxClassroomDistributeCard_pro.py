#coding=utf-8

# @Time    : 2019/11/13
# @Author  : shuping zhao
# @File    : teacherxClassroomDistributeCard_pro.py
import os
import sys
import traceback
import unittest
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from BeautifulReport import BeautifulReport
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

sys.path.append('/opt/')
sys.path.append('/opt/uitest/shuping/common/Common/')
sys.path.append('/opt/uitest/shuping/page/LoginPage/')
from uitest.shuping.page.LoginPage import LoginPage
from uitest.shuping.common.Common import Common


class teacherxDistributeCard_pro(unittest.TestCase):
    def setUp(self):
        global browser
        global window_teacher
        global window_student
        try:
            #path = os.path.dirname(os.path.abspath('./config/chromedriver/chromedriver'))
            teacherUrl = Common.getUrl(self, "TypeUrl", "teacherxUrl")
            studentUrl = Common.getUrl(self, "TypeUrl", "studentxUrl")
            teacherUsername = "18817572035"
            teacherPassword = "1111"
            studentUsername = "17317495785"
            studentPassword = "495785"
            if self._testMethodName == "test_h_assignPhysicalNewCard" or self._testMethodName == "test_i_assignPhyMultiSelectCard":
                searchName = "物理人教版八年级同步课"
                courseCode = "176341"
            else:
                searchName = "自动化测试课程英语人教版七年级同步课"
                courseCode = "156609"
            # linux使用的静默执行方法
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument("--no-sandbox")
            options.add_argument('--disable-gpu')
            options.add_argument('window-size=1280x1024')
            #options.addExtensions(file("/path/to/extension.crx"))
            #options.add_argument("start-maximized")

            # options.add_argument('--headless')
            # options.add_argument('--disable-gpu')
            # options.add_argument('--no-sandbox')
            # 设置打开浏览器不显示data; 加载本地浏览器数据，加载很慢放弃！
            #options.add_argument('--user-data-dir=/Users/shuping/Library/Application Support/Google/Chrome/')
            # mac、linux配置
            #browser = webdriver.Chrome(executable_path=path, options=options)

            # 服务器上写法
            browser = webdriver.Chrome(options=options)
            windows = LoginPage.xLoginStudySystem(self, browser, teacherUrl, studentUrl, teacherUsername, teacherPassword,
                                                  studentUsername, studentPassword, searchName, courseCode)
            window_teacher = windows[0]
            window_student = windows[1]
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

        # 服务器存放图片路径
        browser.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))

    #@unittest.skip("跳过")
    @BeautifulReport.add_test_img('test_a_xassiginImgTextCard')
    def test_a_xassiginImgTextCard(self):
        '''老师和学生进入课堂学生完成图文卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)
            # 滚动任务卡排
            # js2 = "document.getElementById('cardWarp').scroll(200,0);"
            # browser.execute_script(js2)
            time.sleep(0.5)
            print("---------------------> 【1 Start】老师开始发送图文卡 <------------------------\n")
            # 点击讲义卡
            browser.find_element_by_xpath("//div[@class='stepGroup']/div[2]").click()
            # 点击发送按钮
            browser.find_element_by_xpath("//div[@class='actionBtn send']").click()
            print("---------------------> 老师点击发送图文卡按钮 <------------------------\n")
            time.sleep(1)
            # 转到学生端窗口
            browser.switch_to.window(window_student)
            time.sleep(5)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                print("--------------------->关闭录屏弹窗<------------------------")
            textname = browser.find_element_by_xpath("//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("第一单元-讲义卡片", textname, msg="学生完成图文卡失败！")
        print("-------------------> 【1 End】学生成功完成图文卡 <---------------------\n")

    # @unittest.skip("跳过")
    @BeautifulReport.add_test_img('test_b_xassiginPracticeCard')
    def test_b_xassiginPracticeCard(self):
        '''老师和学生进入课堂学生完成练习卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)
            print("-------------------> [2 Start]老师开始发送练习卡 <----------------------\n")
            # 滚动任务卡排
            js2 = "$('.pptSideBar').scrollTop(150)"
            browser.execute_script(js2)
            time.sleep(0.5)
            # 点击练习卡
            browser.find_element_by_xpath("//div[@class='stepGroup']/div[3]").click()
            #出来有延时
            time.sleep(0.5)
            inputs = browser.find_elements_by_xpath("//input[@type='checkbox']")
            inputs[0].click()
            time.sleep(2)
            # 点击发送按钮
            Common.findElementActionClick(self, browser, "//div[@class='actionBtn send']")
            # 转到学生端窗口
            browser.switch_to.window(window_student)
            # 题目出来很慢
            time.sleep(6)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if butbool == True:
                time.sleep(0.5)
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
            time.sleep(1)
            # 输入第一题填空题答案
            # inputs = browser.find_elements_by_xpath("//div[@class='task-html']/div[2]/span")
            # for i in range(len(inputs)):
            #     strNum = str(i+1)
            #     browser.find_element_by_xpath("//div[@class='task-html']/div[2]/span["+ strNum +"]/div/div/input").send_keys("M")
            # time.sleep(0.5)
            # 点击下一题按钮
            Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            #print("-------------------> 第一题答案输入完成，进入第二题 <---------------------\n")
            time.sleep(0.5)
            # 输入第二题答案
            #Common.findElementActionClick(self, browser, "//div[@class='task-question__content']/div[2]")
            # 点击下一题按钮
            Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            #print("-------------------> 第二题答案输入完成，进入第三题 <---------------------\n")
            time.sleep(1)
            # 输入第三题答案
            #Common.findElementActionClick(self, browser, "//div[@class='task-question__content']/div[2]")
            # 点击提交按钮
            Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            time.sleep(3)
            #print("-------------------> 第三题答案输入完成，提交答案完成 <---------------------\n")
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
            # 等待知道了按钮出来
            knowBtn = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button/span")
            if knowBtn == True:
                # 点击知道了按钮
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            textname = browser.find_element_by_xpath(
                "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
            browser.switch_to.window(window_teacher)
            time.sleep(2.5)
            completeStatus = " "
            # 查看学生完成状态
            completeStatus = browser.find_element_by_xpath("//tbody[@class='ant-table-tbody']/tr/td[2]").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("第一单元-练习卡", textname, msg="学生完成练习卡失败！")
        self.assertEqual("已完成", completeStatus, msg="未完成练习卡")
        print("-------------------> 【2 End】学生成功完成练习卡 <---------------------\n")
    # @unittest.skip("跳过")
    @BeautifulReport.add_test_img('test_c_xassiginSubjectCard')
    def test_c_xassiginSubjectCard(self):
        '''老师和学生进入课堂学生完成主观题卡'''
        try:
            time.sleep(0.5)
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)
            time.sleep(0.5)
            print("-------------------> 【3 Start】老师开始发送主观题卡 <----------------------\n")
            # 滚动任务卡排
            js2 = "$('.pptSideBar').scrollTop(320)"
            browser.execute_script(js2)
            time.sleep(0.5)
            # 点击主观题卡
            browser.find_element_by_xpath("//div[@class='stepGroup']/div[4]").click()
            # 出来有延时
            time.sleep(0.5)
            inputs = browser.find_elements_by_xpath("//input[@type='checkbox']")
            inputs[0].click()
            time.sleep(2)
            # 点击发送按钮
            browser.find_element_by_xpath("//div[@class='actionBtn send']").click()
            # 转到学生端窗口
            browser.switch_to.window(window_student)
            # 题目出来很慢,socket连接上要好几秒才能收到卡
            time.sleep(5.5)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                time.sleep(0.5)
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
            time.sleep(0.5)
            # 向左滚动，显示提交按钮
            js = "$('.mainLayout').scrollLeft(300)"
            browser.execute_script(js)
            time.sleep(0.5)
            # 点击提交题目按钮 （屏幕太窄看不到按钮）
            Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            time.sleep(0.5)
            # 点击提交的确认弹窗按钮
            Common.findElementClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
            print("------------------> 学生提交主观题成功 <---------------------\n")

            textname = browser.find_element_by_xpath(
                "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
            browser.switch_to.window(window_teacher)
            time.sleep(2)
            completeStatus = " "
            # 查看学生完成状态
            completeStatus = browser.find_element_by_xpath("//tbody[@class='ant-table-tbody']/tr/td[2]").text

        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("第一单元-主观题卡", textname, msg="学生完成主观题卡失败！")
        self.assertEqual("已完成", completeStatus, msg="未完成主观题卡")
        print("-------------------> 【3 End】学生成功完成主观题卡 <---------------------\n")

    @BeautifulReport.add_test_img('test_d_xassiginReadingCard')
    def test_d_xassiginReadingCard(self):
        '''老师和学生进入课堂学生完成阅读卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)

            print("-------------------> 【4 Start】老师开始发送阅读卡 <----------------------\n")
            # 滚动任务卡排
            js2 = "$('.pptSideBar').scrollTop(450)"
            browser.execute_script(js2)
            time.sleep(0.5)
            # 点击阅读卡
            browser.find_element_by_xpath("//div[@class='stepGroup']/div[5]").click()
            # 点击发送按钮
            browser.find_element_by_xpath("//div[@class='actionBtn send']").click()
            # 转到学生端窗口
            browser.switch_to.window(window_student)
            # 题目出来很慢
            time.sleep(4)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if butbool == True:
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            time.sleep(1.5)
            jquery = "$('.contentWrapper').scrollLeft(300)"
            browser.execute_script(jquery)
            time.sleep(0.5)
            questionList = browser.find_elements_by_xpath("//div[@class='task-read__question']")
            i = 0
            while i < len(questionList):
                i = i + 1
                # 输入第i题答案
                browser.find_element_by_xpath("//div[@class='task-read__questions']/div["+str(i)+"]/div/div/div/div[2]").click()
                if i!= len(questionList):
                    # 点击下一题按钮
                    Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div")
                    #browser.find_element_by_xpath("//a[@class='submitBtn submitTask']").click()
                    time.sleep(0.5)
                elif i== len(questionList):
                    # 点击提交按钮
                    Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div")
                    time.sleep(1.5)
            time.sleep(0.7)
            textname = " "
            textname = browser.find_element_by_xpath(
                "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
            browser.switch_to.window(window_teacher)
            time.sleep(1)
            completeStatus = " "
            # 查看学生完成状态
            completeStatus = browser.find_element_by_xpath("//tbody[@class='ant-table-tbody']/tr/td[2]").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("第一单元-阅读卡", textname, msg="学生完成阅读卡失败！")
        self.assertEqual("已完成", completeStatus, msg="未完成阅读卡")
        print("-------------------> 【4 End】学生成功完成阅读卡 <---------------------\n")

    @BeautifulReport.add_test_img('test_e_xassiginClozeProcedureCard')
    def test_e_xassiginClozeProcedureCard(self):
        '''老师和学生进入课堂学生完成完形填空卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)

            print("-------------------> 【5 Start]】老师开始发送完形填空卡 <----------------------\n")
            # 滚动任务卡排
            js2 = "$('.pptSideBar').scrollTop(600)"
            browser.execute_script(js2)
            time.sleep(0.5)
            # 点击完形卡
            browser.find_element_by_xpath("//div[@class='stepGroup']/div[6]").click()
            # 点击发送按钮
            browser.find_element_by_xpath("//div[@class='actionBtn send']").click()
            time.sleep(0.5)
            # 转到学生端窗口
            browser.switch_to.window(window_student)
            time.sleep(4)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if butbool == True:
                time.sleep(0.5)
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            time.sleep(1.5)
            jquery = "$('.contentWrapper').scrollLeft(300)"
            browser.execute_script(jquery)
            time.sleep(0.5)
            questionList = browser.find_elements_by_xpath("//div[@class='task-read__question']")
            i=0
            while i<len(questionList):
                i = i+1
                # 输入第一题答案
                browser.find_element_by_xpath("//div[@class='task-read__questions']/div["+str(i)+"]/div/div/div/div[2]").click()
                if i!=len(questionList):
                    # 点击下一题按钮
                    Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div")
                    time.sleep(0.6)
                elif i == len(questionList):
                    # 点击提交按钮
                    Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div")
                    time.sleep(1.5)
            time.sleep(0.7)
            clozename = " "
            clozename = browser.find_element_by_xpath(
                "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
            browser.switch_to.window(window_teacher)
            time.sleep(1)
            completeStatus = " "
            # 查看学生完成状态
            completeStatus = browser.find_element_by_xpath("//tbody[@class='ant-table-tbody']/tr/td[2]").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("第一单元-完形卡", clozename, msg="学生完成完形填空卡失败！")
        self.assertEqual("已完成", completeStatus, msg="未完成完形填空卡")
        print("-------------------> 【5 End】学生成功完成完形填空卡 <---------------------\n")

    @BeautifulReport.add_test_img('test_f_xassiginListeningCard')
    def test_f_xassiginListeningCard(self):
        '''老师和学生进入课堂学生完成听力卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)

            print("-------------------> 【6 Start】老师开始发送听力卡 <----------------------\n")
            # 滚动任务卡排
            js2 = "$('.pptSideBar').scrollTop(750)"
            browser.execute_script(js2)
            time.sleep(0.5)
            # 点击听力卡
            browser.find_element_by_xpath("//div[@class='stepGroup']/div[7]").click()
            # 点击发送按钮
            browser.find_element_by_xpath("//div[@class='actionBtn send']").click()
            # 转到学生端窗口
            browser.switch_to.window(window_student)
            # 题目出来很慢
            time.sleep(5)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if butbool==True:
                time.sleep(0.5)
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
            time.sleep(0.5)
            jquery = "$('.contentWrapper').scrollLeft(300)"
            browser.execute_script(jquery)
            questionList = browser.find_elements_by_xpath("//div[@class='task-listen__question']")
            i = 0
            x = 300
            while i < len(questionList):
                i = i + 1
                # 滚动听力卡的题目列
                jquery = "$('.dragWrapper').scrollTop(" + str(x) + ")"
                browser.execute_script(jquery)
                x = x + 360
                # 输入第i题答案
                browser.find_element_by_xpath("//div[@class='task-listen__wrapper']/div["+str(i+2)+"]/div/div/div/div[3]").click()
                time.sleep(0.5)

            # 点击提交按钮
            Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div")
            time.sleep(1.5)
            # # 等待 知道了按钮出来
            # knowBtn = self.isElementExist2("//div[@class='ant-modal-body']/div/div[2]/button/span")
            # if knowBtn == True:
            #     time.sleep(0.5)
            #     # 点击知道了按钮
            #     browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
            listenCardname = " "
            listenCardname = browser.find_element_by_xpath(
                "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text

            browser.switch_to.window(window_teacher)
            time.sleep(1)
            completeStatus = " "
            # 查看学生完成状态
            completeStatus = browser.find_element_by_xpath("//tbody[@class='ant-table-tbody']/tr/td[2]").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("第一单元-听力卡", listenCardname, msg="学生完成听力卡失败！")
        self.assertEqual("已完成", completeStatus, msg="未完成听力卡")
        print("-------------------> 【6 End】学生成功完成听力卡 <---------------------\n")

    #@unittest.skip("跳过")
    @BeautifulReport.add_test_img('test_g_xassiginKpointCard')
    def test_g_xassiginKpointCard(self):
        '''老师和学生进入课堂学生完成知识点解析卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)
            print("-------------------> 【7 Start】老师开始发送知识点解析卡 <----------------------\n")
            # 滚动任务卡排
            js2 = "$('.pptSideBar').scrollTop(850)"
            browser.execute_script(js2)
            time.sleep(0.5)
            # 点击知识点解析卡
            browser.find_element_by_xpath("//div[@class='stepGroup']/div[8]").click()
            # 点击发送按钮
            browser.find_element_by_xpath("//div[@class='actionBtn send']").click()
            # 转到学生端窗口
            browser.switch_to.window(window_student)
            time.sleep(3)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if butbool==True:
                time.sleep(0.5)
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
            time.sleep(1)
            # 学生滑动知识点解析卡
            jquery = "$('.mainSlide').scrollTop(900)"
            browser.execute_script(jquery)
            time.sleep(0.5)

            print("-------------------> 学生完成知识点解析卡第一页讲义 <---------------------\n")
            browser.switch_to.window(window_teacher)
            time.sleep(0.5)
            # 点击学习卡第二页讲义
            browser.find_element_by_xpath("//div[@id='studyCard']/div/div[2]/div[2]").click()
            browser.switch_to.window(window_student)
            print("-------------------> 学生完成知识点解析卡第二页讲义 <---------------------\n")
            browser.switch_to.window(window_teacher)
            time.sleep(1)
            # 点击学习卡第三页讲义
            Common.findElementClick(self, browser, "//div[@id='studyCard']/div/div[2]/div[3]")
            #browser.find_element_by_xpath("//div[@id='studyCard']/div/div[2]/div[3]").click()
            browser.switch_to.window(window_student)
            time.sleep(1)
            print("-------------------> 学生完成知识点解析卡第三页讲义 <---------------------\n")
            knowledgename = browser.find_element_by_xpath(
                "//div[@class='pClassroom isStudent started PstudyCard']/div[1]/h2").text
            print("-------------------> 获取学生端知识点解析卡的标题成功 <---------------------\n")

        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("第一单元-知识点解析卡重点句型教学点", knowledgename, msg="学生完成知识点解析卡失败！")  # 知识点解析卡重点句型教学点
        print("-------------------> 【7 End】学生成功完成知识点解析卡 <---------------------\n")

    # @unittest.skip("跳过")
    @BeautifulReport.add_test_img('test_h_assignPhysicalNewCard')
    def test_h_assignPhysicalNewCard(self):
        '''老师和学生进入课堂学生完成物理新题型卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)
            print("-------------------> 【8 Start】老师开始发送物理新题型卡 <----------------------\n")
            # 点击物理新题型卡
            browser.find_element_by_xpath("//div[@class='stepGroup']/div[2]").click()
            # 点击物理新题型卡的选择框
            Common.findElementActionClick(self, browser, "//div[@class='assignHeader']/label/span/input")
            time.sleep(0.5)
            # 点击发送按钮
            Common.findElementActionClick(self, browser, "//div[@class='actionBtn send']")
            time.sleep(0.5)
            # 转到学生端窗口
            browser.switch_to.window(window_student)
            time.sleep(4)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if butbool == True:
                time.sleep(0.5)
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                # browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
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
            questionList2 = Common.getElementsText(self, browser,
                                                   "//div[@class='task-multi__questions']/div/div/div/div[1]")
            rightCount2 = 0
            for i in range(len(questionList2)):
                if questionList2[i] == "答对了":
                    rightCount2 = rightCount2 + 1
                    print("======================= 第" + str(i + 1) + "道题答对了 ===========================")
                else:
                    print("======================= 第" + str(i + 1) + "道题答错了 ===========================")
                time.sleep(0.3)
            print("======================= 物理新题型卡结束 =====================\n")
            time.sleep(1)
            browser.switch_to.window(window_teacher)
            time.sleep(1.5)
            completeStatus = ""
            completeStatus = browser.find_element_by_xpath("//tbody[@class='ant-table-tbody']/tr/td[2]").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual(3, rightCount2, msg="物理新题型卡正确题数显示不对！")
        self.assertEqual("已完成", completeStatus, msg="完成多选题卡状态不是已完成！")
        print("-------------------> 【8 End】 学生成功完成物理新题型卡<----------------------\n")

    @BeautifulReport.add_test_img("test_i_assignPhyMultiSelectCard")
    def test_i_assignPhyMultiSelectCard(self):
        '''老师和学生进入课堂学生完成物理多选题卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)
            print("-------------------> 【9 Start】老师开始发送物理多选题卡 <----------------------\n")
            # 点击物理新题型卡
            browser.find_element_by_xpath("//div[@class='stepGroup']/div[3]").click()
            # 点击物理新题型卡的选择框
            Common.findElementActionClick(self, browser, "//div[@class='assignHeader']/label/span/input")
            time.sleep(0.5)
            # 点击发送按钮
            Common.findElementActionClick(self, browser, "//div[@class='actionBtn send']")
            time.sleep(0.5)
            # 转到学生端窗口
            browser.switch_to.window(window_student)
            time.sleep(4)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if butbool == True:
                time.sleep(0.5)
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                # browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
            questionCount = browser.find_element_by_xpath("//div[@class='task-abstask__pagination']/span[2]").text
            count = 0
            time.sleep(1)
            for i in range(int(questionCount)):
                count = count + 1
                Common.findElementClick(self, browser, "//div[@class='task-question__content']/div[2]")
                time.sleep(0.3)
                Common.findElementActionClick(self, browser, "//div[@class='task-question__content']/div[4]")
                time.sleep(0.3)
                # 点击下一题按钮
                Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
                time.sleep(0.5)
                print("-------------------> 第" + str(count) + "道题完成<---------------------\n")
            time.sleep(1.5)
            # 点击弹窗的确定按钮
            Common.findElementClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
            time.sleep(0.6)
            questionlist1 = Common.getElementsText(self, browser, "//div[@class='task-question__content']/div[1]")
            rightCount1 = 0
            for i in range(len(questionlist1)):
                if questionlist1[i] == "答对了":
                    rightCount1 = rightCount1 + 1
                    print("======================= 第" + str(i + 1) + "道题答对了 ===========================")
                else:
                    print("======================= 第" + str(i + 1) + "道题答错了 ===========================")
            print("======================= 物理多选题卡结束 =====================\n")
            browser.switch_to.window(window_teacher)
            time.sleep(1.5)
            completeStatus = ""
            completeStatus = browser.find_element_by_xpath("//tbody[@class='ant-table-tbody']/tr/td[2]").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual(2, rightCount1, msg="多选题卡正确题数和教师端查看报告正确题数不一致！")
        self.assertEqual("已完成", completeStatus, msg="教师端显示多选题卡状态不是已完成！")
        print("-------------------> 【9 End】 学生成功完成物理多选题卡<----------------------\n")

directList = Common.getDirectPath(Common)
report_dir = directList[0]
img_path = directList[1]

testsuit = unittest.TestSuite()
#testsuit.addTest(teacherxDistributeCard_pro("test_i_assignPhyMultiSelectCard"))
testsuit.addTests(unittest.makeSuite(teacherxDistributeCard_pro))
run = BeautifulReport(testsuit)
# 服务器存储路径
run.report(filename='TAD2.0_正服给学生端发任务卡（非智能卡）', description='TAD2.0_正服上课发任务卡测试用例', report_dir=report_dir)
