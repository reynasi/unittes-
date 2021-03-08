#coding=utf-8

# @Time    : 2020/4/2
# @Author  : shuping zhao
# @File    : teacher4ClassroomPhysicsCards_Pro.py

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

class teacher4ClassroomPhysicsCards_Pro(unittest.TestCase):
    urlstr = "autotest.learnta.cn"
    orgId = 100040  # 测服是1000369
    searchName = "自动化测试物理课程新卡"
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
            studentUsername = "18400000000"
            studentPassword = "000000"
            courseCode = "174733"

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
    @BeautifulReport.add_test_img('test_a_assignMultiSelectCard')
    def test_a_assignMultiSelectCard(self):
        '''老师和学生都进入课堂学生完成多选题卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(windows[0])
            print("-------------------> 【1 Start】 老师开始发送多选题卡<----------------------\n")
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
            # 点击选择题目框第一个勾选框按钮
            Common.findElementActionClick(self, browser, "//div[@class='assignHeader']/label/span/input")
            print("=========================老师选择完题目=======================")
            time.sleep(1)
            # 点击确定按钮
            Common.findElementActionClick(self, browser, "//div[@class='footerSubmit fixFooter']/button[@type='button']")
            print("-------------------> 老师成功分配多选题卡 <----------------------\n")
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
            if Cname != "单元1-测试多选题卡":
                browser.refresh()
                time.sleep(2)
                # 先判断有没有录屏安装弹窗   。。。
                butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                if (butbool):
                    # 点击录屏安装弹窗
                    Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                    #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
                print("-------------------> 学生未收到多选题卡，重新刷新页面收到卡！刷新页面前cardname=" + Cname + " <----------------------\n")
                # 获取学生端最终收到的任务卡名字
                cardname = browser.find_element_by_xpath(
                    "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
                print("-------------------> 学生收到多选题卡，cardname=" + cardname + "<----------------------\n")
            else:
                cardname = Cname
                print("-------------------> 学生收到多选题卡，cardname=" + cardname + "<----------------------\n")
            time.sleep(1)
            # 输入第一题答案       time.sleep(0.5)
            Common.findElementClick(self, browser, "//div[@class='task-question__content']/div[2]")
            Common.findElementClick(self, browser, "//div[@class='task-question__content']/div[4]")
            # 点击下一题按钮
            Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            time.sleep(0.5)
            js = "$('.task-abstask__content').scrollTop(800)"
            browser.execute_script(js)
            time.sleep(0.5)
            # 输入第二题答案
            Common.findElementClick(self, browser, "//div[@class='task-question__content']/div[2]")
            Common.findElementClick(self, browser, "//div[@class='task-question__content']/div[4]")
            # 点击提交按钮
            Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            # 点击提交的弹窗确定按钮
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
            time.sleep(1)
            # 获取学生对的题目列表
            student_rightList= browser.find_elements_by_xpath("//div[@class='task-question__tips task-question__tips_correct']")
            student_count = 0
            student_count = len(student_rightList)
            print("-------------------> 开始返回教师端查看报告 <----------------------\n")
            # 切换到教师端
            browser.switch_to.window(windows[0])
            time.sleep(1)
            textCompleteStatus = " "
            textCompleteStatus = browser.find_element_by_xpath(
                "//tbody[@class='ant-table-tbody']/tr/td[2]").text
            # 点击查看报告按钮
            Common.findElementClick(self, browser, "//tbody[@class='ant-table-tbody']/tr/td[last()]/div")
            # 获取教师端查看报告对的列表、总数
            rightList = browser.find_elements_by_xpath("//div[@class='wQuestion undefined success']")
            teacher_rightCount = 0
            teacher_rightCount = len(rightList)
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("单元1-测试多选题卡", cardname, msg="多选题卡名字不正确！")
        self.assertEqual("已完成", textCompleteStatus, msg="完成多选题卡状态不是已完成！")
        self.assertEqual(student_count, teacher_rightCount, msg="多选题卡正确题数和教师端查看报告正确题数不一致！")
        print("-------------------> 【1 End】 学生成功完成多选题卡<----------------------\n")

    @BeautifulReport.add_test_img('test_b_assignNewTypeCard')
    def test_b_assignNewTypeCard(self):
        '''老师和学生都进入课堂学生完成新题型卡'''
        try:
            time.sleep(0.5)
            # 切换到教师端窗口
            browser.switch_to.window(windows[0])
            print("-------------------> 【2 Start]】老师开始发送新题型卡<----------------------\n")
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
            print("-------------------> 老师成功分配新题型卡 <----------------------\n")
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
            if Cname != "单元1-测试物理新题型卡":
                browser.refresh()
                time.sleep(2)
                # 先判断有没有录屏安装弹窗   。。。
                butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                if (butbool):
                    # 点击录屏安装弹窗
                    Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
                    #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
                print("-------------------> 学生未收到新题型卡，重新刷新页面收到卡！刷新页面前cardname=" + Cname + " <----------------------\n")
                # 获取学生端最终收到的任务卡名字
                cardname = browser.find_element_by_xpath(
                    "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
                print("-------------------> 学生收到新题型卡，cardname=" + cardname + "<----------------------\n")
            else:
                cardname = Cname
                print("-------------------> 学生收到新题型卡，cardname=" + cardname + "<----------------------\n")

            # 输入第一题答案 大小
            browser.find_element_by_xpath("//input[@autocomplete='off']").send_keys("大小")

            inputList = browser.find_elements_by_xpath("//div[@class='gapInput-mathinput__field mq-editable-field mq-math-mode']")
            for i in range(len(inputList)):
                if i ==0:
                    inputList[i].click()
                    Common.findElementClick(self, browser, "//span[@data-value='letter']")
                    Common.findElementClick(self,browser, "//span[@data-value='shift']")
                    Common.findElementClick(self, browser, "//span[@data-value='b']")
                    Common.findElementClick(self, browser, "//span[@data-value='c']")
                if i ==1:
                    js = "$('.task-multi__questions').scrollTop(850)"
                    browser.execute_script(js)
                    time.sleep(0.5)
                    inputList[i].click()
                    Common.findElementClick(self, browser, "//span[@data-value='b']")
                    Common.findElementClick(self, browser, "//span[@data-value='d']")
            # 点击其他地方，关闭公式弹窗
            Common.findElementActionClick(self, browser, "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2")
            # 点击下一题按钮
            Common.findElementActionClick(self, browser, "//div[@class='task-abstask__footer']/div[3]")
            time.sleep(0.5)
            # 点击提交的弹窗确定按钮
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
            time.sleep(0.7)
            stu_rightlist = browser.find_elements_by_xpath("//div[@class='task-question__tips task-question__tips_correct']")
            student_count = 0
            student_count = len(stu_rightlist)
            print("-------------------> 开始返回教师端查看报告 <----------------------\n")
            # 切换到教师端
            browser.switch_to.window(windows[0])
            time.sleep(1)
            textCompleteStatus = " "
            textCompleteStatus = browser.find_element_by_xpath(
                "//tbody[@class='ant-table-tbody']/tr/td[2]").text
            # 点击查看报告按钮
            Common.findElementClick(self, browser, "//tbody[@class='ant-table-tbody']/tr/td[last()]/div")
            # 获取对的列表、总数
            tea_rightlist = browser.find_elements_by_xpath("//div[@class='wChildQuestion wQuestion undefined success']")
            teacher_count = 0
            teacher_count = len(tea_rightlist)
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("单元1-测试物理新题型卡", cardname, msg="学生端完成任务卡后学生端标题不正确！")
        self.assertEqual("已完成", textCompleteStatus, msg="完成新题型卡状态不正确！")
        self.assertEqual(student_count, teacher_count, msg="学生端正确的题数和教师端查看报告的题数不等！")
        print("-------------------> 【2 End】 学生成功完成新题型卡<----------------------\n")


directList = Common.getDirectPath(Common)
report_dir = directList[0]
img_path = directList[1]

testsuit = unittest.TestSuite()
#testsuit.addTest(teacher4ClassroomPhysicsCards_Pro("test_a_assignMultiSelectCard"))
testsuit.addTests(unittest.makeSuite(teacher4ClassroomPhysicsCards_Pro))
run = BeautifulReport(testsuit)
run.report(filename='TAD1.0正服_物理课堂内给学生发任务卡', description='TAD1.0_物理课堂内给学生发任务卡测试用例', report_dir=report_dir)
#run.report(filename='正服上课发非测评卡测试报告', description='正服上课发各种非测评任务卡测试用例', report_dir=os.path.abspath(r'./report'))