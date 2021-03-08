#coding=utf-8

# @Time    : 2019/12/17
# @Author  : shuping zhao
# @File    : teacher4ClassroomDistributeCard_Pro.py

import os
import sys
import traceback
import unittest
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from BeautifulReport import BeautifulReport
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

sys.path.append('/opt/')
sys.path.append('/opt/uitest/shuping/common/ApiTestCasePro/')
sys.path.append('/opt/uitest/shuping/common/Common/')
sys.path.append('/opt/uitest/shuping/page/LoginPage/')
from uitest.shuping.page.LoginPage import LoginPage
from uitest.shuping.common.Common import Common

class ClassroomDistributeCard_Pro(unittest.TestCase):
    urlstr = "autotest.learnta.cn"
    orgId = 100040  # 测服是1000369
    searchName = "测试自动化卡"
    def setUp(self):
        global browser
        global windows
        global authorization2
        global authorization1
        try:
            # mac 路径
            #path = "/Users/shuping/chromedriver"
            # linux1路径
            #path = "/usr/local/python3/chromedriver"

            #path = os.path.dirname(os.path.abspath('./config/chromedriver/chromedriver'))

            teacher4url = Common.getUrl(self, "TypeUrl", "teacher4Url")
            studentUrl = Common.getUrl(self, "TypeUrl", "student4Url")
            teacherUsername = "18817572035"
            teacherPassword = "1111"
            studentUsername = "17317495785"
            studentPassword = "495785"
            courseCode = "154826"

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

            # mac配置
            #browser = webdriver.Chrome(executable_path=path, options=options)

            # 服务器上写法
            browser = webdriver.Chrome(options=options)
            windows = LoginPage.login(self, browser, teacher4url, studentUrl, teacherUsername, teacherPassword,
                                      studentUsername, studentPassword, self.searchName, courseCode)
            # window_teacher = windows[0]
            # window_student = windows[1]
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
        # 服务器 存放图片路径
        browser.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))

    #@unittest.skip("暂不执行")
    @BeautifulReport.add_test_img('test_a_assignPracticeCard')
    def test_a_assignPracticeCard(self):
        '''老师和学生都进入课堂学生完成练习卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(windows[0])
            print("-------------------> 【1 Start】 老师开始发送练习卡<----------------------\n")
            # 点击 Text_Lesson 1模块
            Common.findElementActionClick(self, browser, "//div[@class='cardsSelectors']/p[4]")
            js = "$('.classroomCardSubContainer').scrollTop(700)"
            browser.execute_script(js)
            time.sleep(0.5)
            # 获取练习卡的最后一个任务状态
            buttonflag = Common.isElementExist2(self, browser, "//div[@id='cardWarp']/div[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[3]/div[1]")
            print("=========================buttonflag:"+str(buttonflag)+"=======================")
            if buttonflag == True:
                # 点击更多按钮
                print("=========================准备点击更多按钮=======================")
                Common.findElementActionClick(self, browser, "//div[@id='cardWarp']/div[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]")
                print("=========================点击更多按钮完成，准备点击删除按钮=======================")
                # 点击删除按钮
                Common.findElementActionClick(self, browser, "//div[@id='cardWarp']/div[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                print("=========================点击删除按钮完成，准备点击确定按钮=======================")
                time.sleep(0.5)
                # 点击确定按钮
                Common.findElementActionClick(self, browser, "//*[@class='ant-confirm-btns']/button[2]")
                print("=========================点击确定按钮完成，准备点击分配任务按钮=======================")
                time.sleep(0.5)
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//div[@id='cardWarp']/div[@id='cardsContainer']/div[1]/div[1]/div[3]")
                print("=========================点击分配任务按钮完成=======================")
                # element = browser.find_element_by_css_selector('div[class*="loadingWhiteBox"]')
                # browser.execute_script("arguments[0].click();", element)
            elif buttonflag == False:
                time.sleep(0.5)
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//div[@id='cardWarp']/div[@id='cardsContainer']/div[1]/div[1]/div[3]")
            # 弹窗出来有延时
            time.sleep(1)
            # locator = (By.XPATH, "//input[@type='checkbox']")
            # WebDriverWait(browser, 5).until(EC.presence_of_element_located(locator))
            # inputs = browser.find_elements_by_xpath("//input[@type='checkbox']")
            # time.sleep(0.5)
            # inputs[0].click()
            # 点击选择题目框第一个勾选框按钮
            Common.findElementActionClick(self, browser, "//div[@class='assignHeader']/label/span/input")
            print("=========================老师选择完题目=======================")
            # 选择第一个教学点的所有知识点
            # if inputs[0].get_attribute('type') == 'checkbox':
            #     inputs[0].click()
            # browser.find_elements_by_css_selector('input[type=checkbox]').pop().click()

            time.sleep(1)
            # 点击确定按钮
            Common.findElementActionClick(self, browser, "//div[@class='footerSubmit fixFooter']/button[@type='button']")
            print("-------------------> 老师成功分配练习卡 <----------------------\n")
            # 转到学生端窗口
            browser.switch_to.window(windows[1])
            # 发卡后学生端倒计时5s
            time.sleep(6)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser,"//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
            time.sleep(0.5)
            Cname = " "
            cardname = " "
            Cname = browser.find_element_by_xpath("//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
            if Cname != "第一单元-语法结构_基础知识练习卡":
                browser.refresh()
                time.sleep(2)
                # 先判断有没有录屏安装弹窗   。。。
                butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                if (butbool):
                    # 点击录屏安装弹窗
                    Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                    #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
                print("-------------------> 学生未收到练习卡，重新刷新页面收到卡！刷新页面前cardname=" + Cname + " <----------------------\n")
                # 获取学生端最终收到的任务卡名字
                cardname = browser.find_element_by_xpath(
                    "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
                print("-------------------> 学生收到练习卡，cardname=" + cardname + "<----------------------\n")
            else:
                cardname = Cname
                print("-------------------> 学生收到练习卡，cardname=" + cardname + "<----------------------\n")

            # 输入第一题答案
            browser.find_element_by_xpath("//div[@class='task-html']/span/div/div/input").send_keys("making")
            # 点击下一题按钮
            Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            time.sleep(0.5)
            # 输入第二题答案
            browser.find_element_by_xpath("//div[@class='task-html']/span/div/div/input").send_keys("listening")
            # 点击下一题按钮
            Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            time.sleep(0.5)
            # 输入第三题答案
            browser.find_element_by_xpath("//div[@class='task-html']/span/div/div/input").send_keys("working")
            # 点击提交按钮
            Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            time.sleep(0.5)
            # 点击提交的弹窗确定按钮
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
            time.sleep(1)
            # 等待知道了按钮出来
            knowBtn = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button/span")
            if knowBtn == True:
                # 点击知道了按钮
                time.sleep(0.5)
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            else:
                print("===================知道了提示按钮没出现=================")
            # 获取学生对的题目列表
            student_rightList= browser.find_elements_by_xpath("//div[@class='task-gap__answer task-gap__answer_correct']")
            student_count = 0
            student_count = len(student_rightList)
            print("-------------------> 开始返回教师端查看报告 <----------------------\n")
            # 切换到教师端
            browser.switch_to.window(windows[0])
            time.sleep(1.5)
            # 点击查看报告按钮
            Common.findElementClick(self, browser, "//tbody[@class='ant-table-tbody']/tr/td[last()]/div")
            # 获取教师端查看报告对的列表、总数
            rightList = browser.find_elements_by_xpath("//span[@class='wQuestion-gap isRight']")
            teacher_rightCount = 0
            teacher_rightCount = len(rightList)
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("第一单元-语法结构_基础知识练习卡", cardname, msg="完成练习卡失败！")
        self.assertEqual(student_count, teacher_rightCount, msg="完成练习卡失败！")
        print("-------------------> 【1 End】 学生成功完成练习卡<----------------------\n")

    @BeautifulReport.add_test_img('test_b_assignBreakThroughCard')
    def test_b_assignBreakThroughCard(self):
        '''老师和学生都进入课堂学生完成闯关卡'''
        try:
            time.sleep(0.5)
            # 切换到教师端窗口
            browser.switch_to.window(windows[0])
            print("-------------------> 【2 Start]】 老师开始发送闯关卡<----------------------\n")
            # 点击 Text_Lesson 1模块 设置报错点
            Common.findElementActionClick(self, browser, "//div[@class='cardsSelectors']/p[4]")
            js = "$('.classroomCardSubContainer').scrollTop(700)"
            browser.execute_script(js)
            time.sleep(0.5)
            # 滚动任务卡排
            js2 = "document.getElementById('cardWarp').scroll(250,0);"
            browser.execute_script(js2)
            time.sleep(0.5)
            # 获取闯关卡的最后一个任务状态
            buttonflag = Common.isElementExist2(self, browser, "//div[@id='cardWarp']/div[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[3]/div[1]")
            if buttonflag == True:
                # 点击更多按钮
                Common.findElementActionClick(self, browser, "//div[@id='cardWarp']/div[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[1]")
                # 点击删除按钮
                Common.findElementActionClick(self, browser, "//div[@id='cardWarp']/div[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                time.sleep(0.5)
                # 点击确定按钮
                Common.findElementActionClick(self, browser, "//*[@class='ant-confirm-btns']/button[2]")
                time.sleep(0.5)
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//div[@id='cardWarp']/div[@id='cardsContainer']/div[2]/div[1]/div[3]")

            elif buttonflag == False:
                time.sleep(0.5)
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//div[@id='cardWarp']/div[@id='cardsContainer']/div[2]/div[1]/div[3]")
            # 弹窗出来有延时
            time.sleep(1)
            # locator = (By.XPATH, "//input[@type='checkbox']")
            # WebDriverWait(browser, 5).until(EC.presence_of_element_located(locator))
            # inputs = browser.find_elements_by_xpath("//input[@type='checkbox']")
            #inputs[0].click()
            # 点击闯关卡的第一个勾选框
            Common.findElementActionClick(self, browser, "//div[@class='assignHeader']/label/span/input")
            time.sleep(1)
            # 点击立即分配按钮
            Common.findElementActionClick(self, browser, "//button[@type='button']")
            time.sleep(0.5)
            print("-------------------> 老师成功分配闯关卡 <----------------------\n")
            # 转到学生端窗口
            browser.switch_to.window(windows[1])
            # 发卡后学生端倒计时5s
            time.sleep(6.5)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
            time.sleep(0.5)
            Cname = " "
            cardname = " "
            Cname = browser.find_element_by_xpath("//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
            if Cname != "第一单元-语法结构_基础知识闯关卡":
                browser.refresh()
                time.sleep(2)
                # 先判断有没有录屏安装弹窗   。。。
                butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                if (butbool):
                    # 点击录屏安装弹窗
                    Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                    #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
                print("-------------------> 学生未收到闯关卡，重新刷新页面收到卡！刷新页面前cardname=" + Cname + " <----------------------\n")
                # 获取学生端最终收到的任务卡名字
                cardname = browser.find_element_by_xpath(
                    "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
                print("-------------------> 学生收到闯关卡，cardname=" + cardname + "<----------------------\n")
            else:
                cardname = Cname
                print("-------------------> 学生收到闯关卡，cardname=" + cardname + "<----------------------\n")
            js = "$('.task-abstask__content').scrollTop(300)"
            browser.execute_script(js)
            time.sleep(0.7)
            # 输入第一题答案 D
            Common.findElementActionClick(self, browser, "//div[@class='task-question__content']/div[5]")
            # 点击下一题按钮
            Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            time.sleep(0.5)
            # 输入第二题答案 A
            Common.findElementActionClick(self, browser, "//div[@class='task-question__content']/div[2]")
            # 点击下一题按钮
            Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            #browser.find_element_by_xpath("//a[@class='btn right']").click()
            time.sleep(0.7)
            browser.execute_script(js)
            time.sleep(0.5)
            # 输入第三题答案 D
            Common.findElementActionClick(self, browser, "//div[@class='task-question__content']/div[5]")
            # 点击提交按钮
            Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            time.sleep(0.5)
            # 点击提交的弹窗确定按钮
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
            time.sleep(0.5)
            # 等待知道了按钮出来
            # knowBtn = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            # if knowBtn == True:
            #     time.sleep(0.5)
            #     # 点击知道了按钮
            #     Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            # else:
            #     print("====================未出现知道了按钮===================")
            # 获取对的列表、总数
            stu_rightlist = browser.find_elements_by_xpath("//div[@class='task-option task-option_selected task-option_disabled task-option_correct']")
            student_count = 0
            student_count = len(stu_rightlist)
            print("-------------------> 开始返回教师端查看报告 <----------------------\n")
            # 切换到教师端
            browser.switch_to.window(windows[0])
            time.sleep(1.5)
            textCompleteStatus = " "
            textCompleteStatus = browser.find_element_by_xpath(
                "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[3]/div[1]").text
            # 点击查看报告按钮
            Common.findElementClick(self, browser, "//tbody[@class='ant-table-tbody']/tr/td[last()]/div")
            # 获取对的列表、总数
            tea_rightlist = browser.find_elements_by_xpath("//a[@class='qBtn small success']")
            teacher_count = 0
            teacher_count = len(tea_rightlist)
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("第一单元-语法结构_基础知识闯关卡", cardname, msg="学生端完成任务卡后显示端标题不正确！")
        self.assertEqual("已完成", textCompleteStatus, msg="完成闯关卡状态不正确！")
        self.assertEqual(student_count, teacher_count, msg="学生端正确的题数和教师端查看报告的题数不等！")
        print("-------------------> 【2 End】 学生成功完成闯关卡<----------------------\n")

    #@unittest.skip("暂不执行")
    @BeautifulReport.add_test_img('test_c_assignAnalysisCard')
    def test_c_assignAnalysisCard(self):
        '''老师和学生都进入课堂学生完成解析卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(windows[0])
            print("-------------------> 【3 Start】老师开始发送解析卡<----------------------\n")
            # 点击 Text_Lesson 1模块
            Common.findElementActionClick(self, browser, "//div[@class='cardsSelectors']/p[5]")
            js = "$('.classroomCardSubContainer').scrollTop(700)"
            browser.execute_script(js)
            time.sleep(0.5)
            # 滚动任务卡排
            js2 = "document.getElementById('cardWarp').scroll(250,0);"
            browser.execute_script(js2)
            time.sleep(0.5)
            # 获取解析卡的最后一个任务状态
            buttonflag = Common.isElementExist2(self, browser, "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[3]/div[1]")
            if buttonflag == True:
                # 点击更多按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[1]")
                #Common.findElementClick("//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[1]")
                # 点击删除按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                #Common.findElementClick("//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                time.sleep(0.5)
                # 点击确定按钮
                Common.findElementActionClick(self, browser, "//*[@class='ant-confirm-btns']/button[2]")
                time.sleep(1)
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[2]/div[1]/div[3]")
            elif buttonflag == False:
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[2]/div[1]/div[3]")

            time.sleep(1)
            print("-------------------> 老师成功分配解析卡 <----------------------\n")
            # 转到学生端窗口
            browser.switch_to.window(windows[1])
            # 发卡后学生端倒计时5s
            time.sleep(5.5)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()

            # 获取学生端的任务卡标题
            Cname = " "
            cardname = " "
            Cname = browser.find_element_by_xpath("//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
            if Cname!= "第一单元-测试解析卡":
                browser.refresh()
                time.sleep(2)
                # 先判断有没有录屏安装弹窗   。。。
                butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                if (butbool):
                    # 点击录屏安装弹窗
                    Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                    #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
                print("-------------------> 学生未收到解析卡，重新刷新页面收到卡！刷新页面前cardname=" + Cname +" <----------------------\n")
                # 获取学生端最终收到的任务卡名字
                cardname = browser.find_element_by_xpath(
                    "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
                print("-------------------> 学生收到解析卡，cardname=" + cardname + "<----------------------\n")
            else:
                cardname = Cname
                print("-------------------> 学生收到解析卡，cardname=" + cardname +"<----------------------\n")
            # 获取学生端最终收到的任务卡名字
            cardname = browser.find_element_by_xpath("//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
            print("-------------------> 开始返回教师端查看报告<----------------------\n")
            # 切换到教师端窗口
            browser.switch_to.window(windows[0])
            time.sleep(1)
            # 点击查看报告按钮
            Common.findElementClick(self, browser, "//tbody[@class='ant-table-tbody']/tr/td[last()]/div")
            time.sleep(0.6)
            hasReader = ""
            hasReader = browser.find_element_by_xpath("//div[@class='right-arrow-collapse']/div[2]/div/div[1]/span").text
            time.sleep(0.5)
            # 点击教师端关闭任务卡详情弹窗按钮
            Common.findElementActionClick(self, browser, "//button[@class='ant-modal-close']")
            analysisCompleteStatus = ""
            analysisCompleteStatus = browser.find_element_by_xpath(
                "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[3]/div[1]").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("已读（1人）", hasReader, msg="已读解析卡人数不正确！")
        self.assertEqual("第一单元-测试解析卡", cardname, msg="完成解析卡失败！")
        self.assertEqual("已完成", analysisCompleteStatus, msg="完成解析卡失败！")
        print("-------------------> 【3 End】 学生成功完成解析卡<----------------------\n")

    #@unittest.skip("暂不执行")
    @BeautifulReport.add_test_img('test_d_assignTextCard')
    def test_d_assignTextCard(self):
        '''老师和学生都进入课堂学生完成富文本卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(windows[0])
            print("-------------------> 【4 Start】 老师开始发送富文本卡<----------------------\n")
            # 点击 Ability_Lesson 1模块
            Common.findElementActionClick(self, browser, "//div[@class='cardsSelectors']/p[6]")
            js = "$('.classroomCardSubContainer').scrollTop(700)"
            browser.execute_script(js)
            time.sleep(0.5)
            # 滚动任务卡排
            js2 = "document.getElementById('cardWarp').scroll(250,0);"
            browser.execute_script(js2)
            time.sleep(0.5)
            # 获取富文本卡的最后一个任务状态
            buttonflag = Common.isElementExist2(self, browser,
                "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[3]/div[1]")
            if buttonflag == True:
                # 点击更多按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[1]")
                #Common.findElementClick("//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[1]")
                # 点击删除按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                # Common.findElementClick(self, browser,
                #     "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                time.sleep(0.5)
                # 点击确定按钮
                Common.findElementActionClick(self, browser, "//*[@class='ant-confirm-btns']/button[2]")
                time.sleep(0.5)
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[2]/div[1]/div[3]")
            elif buttonflag == False:
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[2]/div[1]/div[3]")

            time.sleep(1)
            print("-------------------> 老师成功分配富文本卡 <----------------------\n")
            # 转到学生端窗口
            browser.switch_to.window(windows[1])
            # 发卡后学生端倒计时5s
            time.sleep(5.5)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
            # 获取学生端的任务卡标题
            Cname = " "
            cardname = " "
            Cname = browser.find_element_by_xpath("//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
            if Cname != "第一单元-测试富文本卡":
                browser.refresh()
                time.sleep(2)
                # 先判断有没有录屏安装弹窗   。。。
                butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                if (butbool):
                    # 点击录屏安装弹窗
                    Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                    #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
                print("-------------------> 学生未收到富文本卡，重新刷新页面收到卡！刷新页面前cardname=" + Cname + " <----------------------\n")
                # 获取学生端最终收到的任务卡名字
                cardname = browser.find_element_by_xpath(
                    "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
                print("-------------------> 学生收到任务卡，cardname=" + cardname + "<----------------------\n")
            else:
                cardname = Cname
                print("-------------------> 学生收到富文本卡，cardname=" + cardname + "<----------------------\n")
            print("-------------------> 开始返回教师端查看报告<----------------------\n")
            # 切换到教师端窗口
            browser.switch_to.window(windows[0])
            time.sleep(0.6)
            # 点击查看报告按钮
            Common.findElementClick(self, browser, "//tbody[@class='ant-table-tbody']/tr/td[last()]/div")
            time.sleep(0.6)
            hasReader = ""
            hasReader = browser.find_element_by_xpath(
                "//div[@class='right-arrow-collapse']/div[2]/div/div[1]/span").text
            time.sleep(0.5)
            # 点击查看详情按钮弹窗关闭按钮
            browser.find_element_by_xpath("//button[@aria-label='Close']").click()
            textCompleteStatus = " "
            textCompleteStatus = browser.find_element_by_xpath(
                "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[3]/div[1]").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("已读（1人）", hasReader, msg="已读富文本卡人数不正确！")
        self.assertEqual("第一单元-测试富文本卡", cardname, msg="完成富文本卡失败！")
        self.assertEqual("已完成", textCompleteStatus, msg="完成富文本卡失败！")
        print("-------------------> 【4 End】 学生成功完成富文本卡<----------------------\n")

    #@unittest.skip("暂不执行")
    @BeautifulReport.add_test_img('test_e_assignReadingCard')
    def test_e_assignReadingCard(self):
        '''老师和学生都进入课堂学生完成阅读卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(windows[0])
            print("-------------------> 【5 Start】 老师开始发送阅读卡<----------------------\n")
            # 滚动任务卡排
            # js2 = "document.getElementById('cardWarp').scroll(200,0);"
            # browser.execute_script(js2)
            # 点击 Text_Lesson 1模块
            browser.find_element_by_xpath("//div[@class='cardsSelectors']/p[9]").click()
            js = "$('.classroomCardSubContainer').scrollTop(800)"
            browser.execute_script(js)
            time.sleep(0.5)
            # 滚动到阅读卡
            # js = "document.getElementById('cardWarp').scroll(500,0);"
            # browser.execute_script(js)
            buttonflag = Common.isElementExist2(self, browser, "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[3]/div[1]")
            if buttonflag == True:
                # 获取阅读理解卡的最后一个任务状态
                # 点击更多按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]")
                #browser.find_element_by_xpath("//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]").click()
                # 点击删除按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                # browser.find_element_by_xpath(
                #     "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]/div/div/div[1]").click()
                time.sleep(0.5)
                # 点击确定按钮
                Common.findElementActionClick(self, browser, "//*[@class='ant-confirm-btns']/button[2]")
                time.sleep(0.5)
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[1]/div[1]/div[3]")
            elif buttonflag == False:
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[1]/div[1]/div[3]")

            # 弹窗出来有延时
            time.sleep(1)
            print("-------------------> 老师成功分配阅读卡 <----------------------\n")
            # 转到学生端窗口
            browser.switch_to.window(windows[1])
            # 发卡后学生端倒计时5s
            time.sleep(5.5)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
            # locator2 = (By.XPATH, "//*[@class='btnWrapper']/a[2]")
            # WebDriverWait(browser, 10).until(EC.presence_of_element_located(locator2))
            # 滚动到选题部分
            jquery = "$('.contentWrapper').scrollLeft(250)"
            browser.execute_script(jquery)
            time.sleep(0.5)
            Cname = " "
            cardname = " "
            Cname = browser.find_element_by_xpath("//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
            if Cname != "第一单元-阅读_综合能力阅读卡":
                browser.refresh()
                time.sleep(2)
                # 先判断有没有录屏安装弹窗   。。。
                butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                if (butbool):
                    # 点击录屏安装弹窗
                    Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                    #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
                print("-------------------> 学生未收到阅读卡，重新刷新页面收到卡！刷新页面前cardname=" + Cname + " <----------------------\n")
                # 获取学生端最终收到的任务卡名字
                cardname = browser.find_element_by_xpath(
                    "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
                print("-------------------> 学生收到阅读卡，cardname=" + cardname + "<----------------------\n")
            else:
                cardname = Cname
                print("-------------------> 学生收到阅读卡，cardname=" + cardname + "<----------------------\n")
            questionList = browser.find_elements_by_xpath("//div[@class='task-read__question']")
            for i in range(len(questionList)):
                # 输入第i题答案
                browser.find_element_by_xpath("//div[@class='task-read__questions']/div["+str(i+1)+"]/div/div/div/div[2]").click()
                if int(i+1) != len(questionList):
                    # 点击下一题按钮
                    Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div")
                    time.sleep(0.5)
                else:
                    time.sleep(0.5)
                    # 点击提交按钮
                    Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div")
                    time.sleep(1)
            student_count = 0
            student_Rightquestions = browser.find_elements_by_xpath("//span[@class='task-question__cell']")
            student_count = len(student_Rightquestions)
            print("-------------------> 学生成功提交阅读卡<----------------------\n")

            print("-------------------> 开始返回教师端查看报告 <----------------------\n")
            # 切换到教师端
            browser.switch_to.window(windows[0])
            time.sleep(0.6)
            # 点击查看报告按钮
            Common.findElementClick(self, browser, "//tbody[@class='ant-table-tbody']/tr/td[last()]/div")
            time.sleep(0.7)
            # 获取对的列表、总数
            teacher_Rightquestions = browser.find_elements_by_xpath("//a[@class='qBtn small success']")
            teacher_count = 0
            teacher_count = len(teacher_Rightquestions)
            rightCountFlag = False
            if student_count == teacher_count:
                rightCountFlag = True
            # 关闭详情弹窗
            browser.find_elements_by_xpath("//button[@class='ant-modal-close']")[1].click()
            time.sleep(0.5)
            completeStatus = " "
            completeStatus = browser.find_element_by_xpath(
                "//tbody[@class='ant-table-tbody']/tr/td[2]").text
            # 点击查看详情按钮弹窗关闭按钮
            browser.find_element_by_xpath("//button[@aria-label='Close']").click()
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("第一单元-阅读_综合能力阅读卡", cardname, msg="获取学生端阅读卡任务名称失败！")
        self.assertEqual(True, rightCountFlag, msg="教师端和学生端报告页答对题目总数不等！")
        self.assertEqual("已完成", completeStatus, msg="教师端查看学生阅读卡不是已完成！")
        print("-------------------> 【5 End】 学生成功完成阅读卡<----------------------\n")

    #@unittest.skip("暂不执行")
    @BeautifulReport.add_test_img('test_f_assignClozeProcedureCard')
    def test_f_assignClozeProcedureCard(self):
        '''老师和学生都进入课堂学生完成完形填空卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(windows[0])
            print("-------------------> 【5 Start】老师开始发送完形填空卡<----------------------\n")
            # 滚动任务卡排
            # js2 = "document.getElementById('cardWarp').scroll(200,0);"
            # browser.execute_script(js2)

            # 点击 Ability_Lesson 1模块
            browser.find_element_by_xpath("//div[@class='cardsSelectors']/p[9]").click()
            js = "$('.classroomCardSubContainer').scrollTop(800)"
            browser.execute_script(js)
            time.sleep(0.5)
            # 获取完形填空卡的最后一个任务状态
            buttonflag = Common.isElementExist(self, browser, "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[3]/div[1]")
            if buttonflag == True:
                # 点击更多按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[1]")
                # 点击删除按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                time.sleep(0.5)
                # 点击确定按钮
                Common.findElementActionClick(self, browser, "//*[@class='ant-confirm-btns']/button[2]")
                time.sleep(0.7)
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[2]/div[1]/div[3]")
            elif buttonflag == False:
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[2]/div[1]/div[3]")
            time.sleep(1)
            print("-------------------> 老师成功分配完形卡<----------------------\n")
            # 转到学生端窗口
            browser.switch_to.window(windows[1])
            # 发卡后学生端倒计时5s
            time.sleep(5.5)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            # 滚动到选题部分
            jquery = "$('.contentWrapper').scrollLeft(300)"
            browser.execute_script(jquery)
            time.sleep(0.5)
            # 获取学生端的任务卡标题
            Cname = " "
            cardname = " "
            Cname = browser.find_element_by_xpath("//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
            if Cname != "第一单元-阅读_综合能力完形填空卡":
                browser.refresh()
                time.sleep(2)
                # 先判断有没有录屏安装弹窗   。。。
                butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                if (butbool):
                    # 点击录屏安装弹窗
                    Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                print("-------------------> 学生未收到完形卡，重新刷新页面收到卡！刷新页面前cardname=" + Cname + " <----------------------\n")
                # 获取学生端最终收到的任务卡名字
                cardname = browser.find_element_by_xpath(
                    "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
                print("-------------------> 学生收到完形卡，cardname=" + cardname + "<----------------------\n")
            else:
                cardname = Cname
                print("-------------------> 学生收到完形卡，cardname=" + cardname + "<----------------------\n")
            questionList = browser.find_elements_by_xpath("//div[@class='task-read__question']")
            for i in range(len(questionList)):
                # 输入第一题答案
                browser.find_element_by_xpath("//div[@class='task-read__questions']/div["+str(i+1)+"]/div/div/div/div[2]").click()
                if i+1 != len(questionList):
                    # 点击下一题按钮
                    Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div")
                    time.sleep(0.5)
                else:
                    time.sleep(0.5)
                    # 点击提交按钮
                    Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div")
                    time.sleep(1)
            student_count = 0
            student_Rightquestions = browser.find_elements_by_xpath("//span[@class='task-question__cell']")
            student_count = len(student_Rightquestions)
            print("-------------------> 学生成功提交完形填空卡<----------------------\n")

            print("-------------------> 开始返回教师端查看报告 <----------------------\n")
            # 切换到教师端
            browser.switch_to.window(windows[0])
            time.sleep(0.6)
            # 点击查看报告按钮
            Common.findElementClick(self, browser, "//tbody[@class='ant-table-tbody']/tr/td[last()]/div")
            time.sleep(0.7)
            # 获取对的列表、总数
            teacher_Rightquestions = browser.find_elements_by_xpath("//a[@class='qBtn small success']")
            teacher_count = 0
            teacher_count = len(teacher_Rightquestions)
            rightCountFlag = False
            if student_count == teacher_count:
                rightCountFlag = True
            # 关闭详情弹窗
            browser.find_elements_by_xpath("//button[@class='ant-modal-close']")[1].click()
            time.sleep(0.5)
            completeStatus = " "
            completeStatus = browser.find_element_by_xpath(
                "//tbody[@class='ant-table-tbody']/tr/td[2]").text
            # 点击查看详情按钮弹窗关闭按钮
            browser.find_element_by_xpath("//button[@aria-label='Close']").click()
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("第一单元-阅读_综合能力完形填空卡", cardname, msg="完成完形填空卡失败！")
        self.assertEqual(True, rightCountFlag, msg="教师端和学生端报告页答对题目总数不等！")
        self.assertEqual("已完成", completeStatus, msg="教师端查看学生完成状态不是已完成！")
        print("-------------------> 【5 End】 学生成功完成完形填空卡<----------------------\n")

    #@unittest.skip("暂不执行")
    @BeautifulReport.add_test_img('test_g_assignListeningCard')
    def test_g_assignListeningCard(self):
        '''老师和学生都进入课堂学生完成听力卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(windows[0])
            print("-------------------> 【6 Start】 老师开始发送听力卡<----------------------\n")
            # 滚动任务卡排
            # js2 = "document.getElementById('cardWarp').scroll(200,0);"
            # browser.execute_script(js2)

            # 点击 Ability_Lesson 1模块
            Common.findElementClick(self, browser, "//div[@class='cardsSelectors']/p[5]")
            js = "$('.classroomCardSubContainer').scrollTop(700)"
            browser.execute_script(js)
            time.sleep(0.5)
            # 获取听力卡的最后一个任务状态
            buttonflag = Common.isElementExist2(self, browser, "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[3]/div[1]")
            if buttonflag == True:
                # 点击更多按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]")
                # browser.find_element_by_xpath(
                #     "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]").click()
                # 点击删除按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                # browser.find_element_by_xpath(
                #     "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]/div/div/div[1]").click()
                time.sleep(0.5)
                # 点击确定按钮
                Common.findElementActionClick(self, browser, "//*[@class='ant-confirm-btns']/button[2]")
                time.sleep(0.5)
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[1]/div[1]/div[3]")
            elif buttonflag == False:
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[1]/div[1]/div[3]")
            time.sleep(0.5)
            print("-------------------> 老师成功分配听力卡<----------------------\n")
            # 转到学生端窗口
            browser.switch_to.window(windows[1])
            time.sleep(7)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
            # 往左滚动一点
            js = "$('.contentWrapper').scrollLeft(250)"
            browser.execute_script(js)
            time.sleep(0.5)
            # 获取学生端的任务卡标题
            Cname = " "
            cardname = " "
            Cname = browser.find_element_by_xpath("//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
            if Cname != "第一单元-听力_综合能力听力卡":
                browser.refresh()
                time.sleep(2)
                # 先判断有没有录屏安装弹窗   。。。
                butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                if (butbool):
                    # 点击录屏安装弹窗
                    Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                    #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
                    time.sleep(0.5)
                print("-------------------> 学生未收到听力卡，重新刷新页面收到卡！刷新页面前cardname=" + Cname + " <----------------------\n")
                # 获取学生端最终收到的任务卡名字
                cardname = browser.find_element_by_xpath(
                    "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
                print("-------------------> 学生收到听力卡，cardname=" + cardname + "<----------------------\n")
            else:
                cardname = Cname
                print("-------------------> 学生收到听力卡，cardname=" + cardname + "<----------------------\n")
            questionList = browser.find_elements_by_xpath("//div[@class='task-listen__question']")
            i = 0
            x = 300
            while i < len(questionList):
                i = i + 1
                # 滚动听力卡的题目列
                jquery = "$('.task-listen__wrapper').scrollTop(" + str(x) + ")"
                browser.execute_script(jquery)
                x = x + 330
                # 输入第一题答案
                browser.find_element_by_xpath("//div[@class='task-listen__wrapper']/div["+str(i+2)+"]/div/div/div/div[3]").click()
                time.sleep(0.5)
            # 点击提交按钮
            Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div")
            time.sleep(1.5)
            # 获取学生端的任务卡标题
            student_count = 0
            rightList = Common.getElementsTextExpectStr(self, browser, "//div[@class='task-question__content']/div[1]", "答对了")
            student_count = len(rightList)
            print("-------------------> 学生成功提交听力卡<----------------------\n")

            print("-------------------> 开始返回教师端查看报告 <----------------------\n")
            # 切换到教师端
            browser.switch_to.window(windows[0])
            time.sleep(0.6)
            # 点击查看报告按钮
            Common.findElementClick(self, browser, "//tbody[@class='ant-table-tbody']/tr/td[last()]/div")
            time.sleep(0.7)
            # 获取错误的列表、总数
            teacher_Rightquestions = browser.find_elements_by_xpath("//div[@class='wQuestion undefined success']")
            teacher_count = 0
            teacher_count = len(teacher_Rightquestions)
            wrongCountFlag = False
            if student_count == teacher_count:
                wrongCountFlag = True
            # 关闭详情弹窗
            # btnlist = browser.find_elements_by_xpath("//button[@class='ant-modal-close']")
            # btnlist[1].click()
            browser.find_elements_by_xpath("//button[@class='ant-modal-close']")[1].click()
            time.sleep(0.3)
            # 点击查看详情按钮弹窗关闭按钮
            browser.find_element_by_xpath("//button[@aria-label='Close']").click()
            completeStatus = " "
            completeStatus = browser.find_element_by_xpath(
                "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[3]/div[1]").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("第一单元-听力_综合能力听力卡", cardname, msg="完成听力卡失败！")
        self.assertEqual(True, wrongCountFlag, msg="教师端和学生端报告页答对题目总数不等！")
        self.assertEqual("已完成", completeStatus, msg="查看教师端学生完成状态不是已完成！")
        print("-------------------> 【6 End】 学生成功完成听力卡<----------------------\n")

    #@unittest.skip("暂不执行")
    @BeautifulReport.add_test_img('test_h_assignStudyCard')
    def test_h_assignStudyCard(self):
        '''老师和学生都进入课堂学生完成学习卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(windows[0])
            print("-------------------> 【7 Start】 老师开始发送学习卡<----------------------\n")
            # 滚动任务卡排
            # js2 = "document.getElementById('cardWarp').scroll(200,0);"
            # browser.execute_script(js2)

            # 点击 Text_Lesson 1～Lesson 2模块
            Common.findElementActionClick(self, browser, "//div[@class='cardsSelectors']/p[8]")
            js = "$('.classroomCardSubContainer').scrollTop(810)"
            browser.execute_script(js)
            time.sleep(0.5)
            # 获取学习卡的最后一个任务状态
            buttonflag = Common.isElementExist2(self, browser, "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[3]/div[1]")
            if buttonflag == True:
                # 点击更多按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]")
                # browser.find_element_by_xpath(
                #     "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]").click()
                # 点击删除按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                # browser.find_element_by_xpath(
                #     "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]/div/div/div[1]").click()
                time.sleep(0.5)
                # 点击确定按钮
                Common.findElementActionClick(self, browser, "//*[@class='ant-confirm-btns']/button[2]")
                time.sleep(0.5)
                locat = (By.XPATH, "//*[@id='cardsContainer']/div[1]/div[1]/div[3]")
                WebDriverWait(browser, 5).until(EC.presence_of_element_located(locat))
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[1]/div[1]/div[3]")
            elif buttonflag == False:
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[1]/div[1]/div[3]")

            print("-------------------> 老师成功分配学习卡<----------------------\n")
            time.sleep(1)
            # 转到学生端窗口
            browser.switch_to.window(windows[1])
            time.sleep(6.5)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()

            # 滚动学习卡的pdf讲义
            # scrolljs = "document.getElementByClassName('wTask').scroll(0,300);"
            jquery = "$('.mainSlide').scrollTop(2000)"
            browser.execute_script(jquery)
            # 获取学生端的任务卡标题
            Cname = " "
            cardname = " "
            Cname = browser.find_element_by_xpath("//div[@class='pClassroom isStudent started PstudyCard']/div[1]/h2").text
            if Cname != "第一单元-look up":
                browser.refresh()
                time.sleep(2)
                # 先判断有没有录屏安装弹窗   。。。
                butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                if (butbool):
                    # 点击录屏安装弹窗
                    Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                    #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
                    time.sleep(0.5)
                print("-------------------> 学生未收到学习卡，重新刷新页面收到卡！刷新页面前cardname=" + Cname + " <----------------------\n")
                # 获取学生端最终收到的任务卡名字
                cardname = browser.find_element_by_xpath(
                    "//div[@class='pClassroom isStudent started PstudyCard']/div[1]/h2").text
                print("-------------------> 学生收到学习卡，cardname=" + cardname + "<----------------------\n")
            else:
                cardname = Cname
                print("-------------------> 学生收到学习卡，cardname=" + cardname + "<----------------------\n")
            # 切到教师端
            browser.switch_to.window(windows[0])
            time.sleep(0.5)
            # 点击返回课堂按钮
            Common.findElementClick(self, browser, "//div[@class='pStudyCard-header']/div[1]")
            time.sleep(0.5)
            # 点击更多按钮
            Common.findElementClick(self, browser, "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]")
            time.sleep(0.5)
            # 点击结束放映按钮
            Common.findElementClick(self, browser, "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]/div/div/div[3]")
            time.sleep(0.5)
            # 点击确定按钮
            Common.findElementClick(self, browser, "//*[@class='ant-confirm-btns']/button[2]")
            time.sleep(1)
            completeStatus = " "
            completeStatus = browser.find_element_by_xpath(
                "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[3]/div[1]").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("第一单元-look up", cardname, msg="获取学习卡卡名称！")
        self.assertEqual("已完成", completeStatus, msg="完成学习卡失败！")
        print("-------------------> 【7 End】 学生成功完成学习卡<----------------------\n")
    #@unittest.skip("暂不执行")
    @BeautifulReport.add_test_img('test_i_assignSubjectCard')
    def test_i_assignSubjectCard(self):
        '''老师和学生都进入课堂学生完成主观题卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(windows[0])
            print("-------------------> 【8 Start】 老师开始发送主观题卡<----------------------\n")
            # 点击 Text_Lesson 1～Lesson 2模块
            Common.findElementActionClick(self, browser, "//div[@class='cardsSelectors']/p[14]")
            # 向下滚动找到更多按钮
            jquery="$('.classroomCardSubContainer').scrollTop(700)"
            browser.execute_script(jquery)
            time.sleep(0.7)
            # 滚动任务卡排
            js2 = "document.getElementById('cardWarp').scroll(250,0);"
            browser.execute_script(js2)
            time.sleep(0.7)
            # 获取主观题卡的最后一个任务状态
            buttonflag = Common.isElementExist2(self, browser,
                "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[3]/div[1]")
            if buttonflag == True:
                # 点击更多按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[1]")
                # browser.find_element_by_xpath(
                #     "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[1]").click()
                # 点击删除按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                # browser.find_element_by_xpath(
                #     "//*[@id='cardsContainer']/div[2]/div[2]/div/div[last()]/div[1]/div/div/div[1]").click()
                time.sleep(0.5)
                # 点击确定按钮
                Common.findElementActionClick(self, browser, "//*[@class='ant-confirm-btns']/button[2]")
                time.sleep(0.5)
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[2]/div[1]/div[3]")
            elif buttonflag == False:
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[2]/div[1]/div[3]")
            time.sleep(1)
            # 获取输入框列表
            inputlist = browser.find_elements_by_xpath("//input[@type='checkbox']")
            inputlist[0].click()
            # 点击立即分配按钮
            Common.findElementClick(self, browser, "//button[@type='button']")
            print("-------------------> 老师成功分配主观题卡 <----------------------\n")
            # 转到学生端窗口
            browser.switch_to.window(windows[1])
            time.sleep(5.5)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
            time.sleep(0.5)
            # 向左滚动，显示提交按钮
            js="$('.mainLayout').scrollLeft(300)"
            browser.execute_script(js)
            time.sleep(0.5)
            # 获取学生端的任务卡标题
            Cname = " "
            cardname = " "
            Cname = browser.find_element_by_xpath("//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
            if Cname != "第一单元-主观题卡":
                browser.refresh()
                time.sleep(2)
                # 先判断有没有录屏安装弹窗   。。。
                butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                if (butbool):
                    # 点击录屏安装弹窗
                    Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                    #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
                    time.sleep(0.5)
                print("-------------------> 学生未收到主观题卡，重新刷新页面收到卡！刷新页面前cardname=" + Cname + " <----------------------\n")
                # 获取学生端最终收到的任务卡名字
                cardname = browser.find_element_by_xpath(
                    "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
                print("-------------------> 学生收到主观题卡，cardname=" + cardname + "<----------------------\n")
            else:
                cardname = Cname
                print("-------------------> 学生收到主观题卡，cardname=" + cardname + "<----------------------\n")
            # 点击提交按钮
            Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            time.sleep(0.6)
            # 点击确定弹窗按钮
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
            print("-------------------> 学生成功提交主观题卡 <----------------------\n")
            browser.switch_to.window(windows[0])
            time.sleep(1)
            completeStatus = " "
            completeStatus = browser.find_element_by_xpath(
                "//tbody[@class='ant-table-tbody']/tr/td[2]").text
            # 点击查看报告按钮
            Common.findElementClick(self, browser, "//tbody[@class='ant-table-tbody']/tr/td[last()]/div")
            time.sleep(0.6)
            completeMsg = browser.find_element_by_xpath("//div[@class='task-subjective__title']").text
            print("====================> 打开查看报告后显示学生完成时间信息为：" + completeMsg + "<====================\n")
            # 关闭详情弹窗
            browser.find_elements_by_xpath("//button[@class='ant-modal-close']")[1].click()
            time.sleep(0.3)
            # 点击查看详情按钮弹窗关闭按钮
            browser.find_element_by_xpath("//button[@aria-label='Close']").click()
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("第一单元-主观题卡", cardname, msg="主观题卡名称显示不正确！")
        self.assertEqual("已完成", completeStatus, msg="主观题卡完成状态不正确！")
        print("-------------------> 【8 End】 学生成功完成主观题卡<----------------------\n")

directList = Common.getDirectPath(Common)
report_dir = directList[0]
img_path = directList[1]

testsuit = unittest.TestSuite()
#testsuit.addTest(ClassroomDistributeCard_Pro("test_i_assignSubjectCard"))
testsuit.addTests(unittest.makeSuite(ClassroomDistributeCard_Pro))
run = BeautifulReport(testsuit)
run.report(filename='TAD1.0正服_课堂内给学生发卡（非智能卡）', description='TAD1.0_正服上课发各种非测评任务卡测试用例', report_dir=report_dir)
#run.report(filename='正服上课发非测评卡测试报告', description='正服上课发各种非测评任务卡测试用例', report_dir=os.path.abspath(r'./report'))