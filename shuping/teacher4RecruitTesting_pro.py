#coding=utf-8

# @Time    : 2020/02/19
# @Author  : shuping zhao
# @File    : teacher4RecruitTesting_Pro.py

import random
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
sys.path.append('/opt/uitest/shuping/common/ApiCasePro/')
sys.path.append('/opt/uitest/shuping/common/Common/')
sys.path.append('/opt/uitest/shuping/page/LoginPage/')
from uitest.shuping.common.Common import Common
from uitest.shuping.page.LoginPage import LoginPage
from uitest.shuping.common.ApiCasePro import *

class RecruitTesting_Pro(unittest.TestCase):
    def setUp(self):
        global browser
        global windows
        global authorization2
        global authorization1
        try:
            # mac 路径
            #path = "/Users/shuping/chromedriver"

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

            # mac配置
            #browser = webdriver.Chrome(executable_path=path, options=options)
            # 服务器上写法
            browser = webdriver.Chrome(options=options)
            windows = LoginPage.teacher4Login(self, browser, teacher4url, teacherUsername, teacherPassword)
            time.sleep(2)
            # 获取教师端token
            authorization1 = Common.getToken(self, browser, 'return window.localStorage.getItem("__ta/teacher_token")')
            print("-------------------> 【0】 Setup Teacher4 登录成功! <----------------------\n")
            # 点击招生测评系统模块
            Common.findElementActionClick(self, browser, "//div[@name='layout_container_name']/div[3]/div[1]/div")
            time.sleep(2)
            # 输入自动化测评，点击搜索按钮
            browser.find_element_by_id("name").send_keys("自动化测评培优20200218")
            browser.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(0.6)
            # 点击立即分享按钮
            browser.find_element_by_xpath("//tbody[@class='ant-table-tbody']/tr[1]/td[last()]/div/span[1]").click()
            # 获取招生测评连接地址
            imgurl = browser.find_element_by_xpath("//div[@class='img-url']/a").get_attribute("href")
            time.sleep(0.6)
            js = 'window.open("'+imgurl+'");'
            browser.execute_script(js)
            time.sleep(3)
            windows = browser.window_handles
            browser.switch_to.window(windows[1])
            print("-------------------> Setup 复制招生测评链接打开新窗口完成 <----------------------\n")
            # 输入姓名
            browser.find_element_by_id("username").send_keys("173测试")
            # 输入手机号
            browser.find_element_by_id("mobile").send_keys("17317495785")
            # 输入验证码
            browser.find_element_by_id("code").send_keys("1111")
            # 点击选择地区下拉框
            #browser.find_element_by_id("address").click()
            # # 点击选择天津（省）
            # browser.find_element_by_xpath("//body/div[4]/div/div/div/ul[1]/li[2]").click()
            # # 选择天津市
            # browser.find_element_by_xpath("//body/div[4]/div/div/div/ul[2]/li[1]").click()
            # # 选择和平区
            # browser.find_element_by_xpath("//body/div[4]/div/div/div/ul[3]/li[1]").click()
            # 点击开始测评登录按钮
            Common.findElementActionClick(self, browser, "//button[@type='submit']")
            print("-------------------> Setup 输入学生信息登录到招生测评完成 <----------------------\n")
            time.sleep(2)
            # 获取学生端token
            authorization2 = Common.getToken(self, browser, 'return window.localStorage.getItem("__ta/task_token");')
            # 点击开始测评
            browser.find_element_by_xpath("//*[@id='root']/div/div[3]/div[1]").click()
            print("-------------------> 选择招生测评科目 <----------------------\n")

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

    #@unittest.skip("跳过")
    @BeautifulReport.add_test_img('test_a_englishRecruit')
    def test_a_englishRecruit(self):
        ''' 完成2020春季英语招生测评，随机完成一个年级'''
        try:
            print("-------------------> [1]英语招生测评开始 <---------------------\n")
            time.sleep(1)
            # 选择英语
            browser.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[2]").click()
            time.sleep(0.5)
            # 随机获取年级数字
            grade = random.randint(4, 9)
            divNum = grade-2
            print("-------------------> 选择英语" + str(grade) + "年级的招生测评<---------------------")
            # 点击年级，进入测评
            Common.findElementClick(self, browser, "//*[@id='root']/div/div[2]/div/div["+str(divNum)+"]")
            count=0
            elementflag = False
            elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div[1]")
            # 获取招生测评的topisId, executionId, topicId
            activityId = ApiCasePro.getActivityId(browser, authorization1, directurl)
            pretopicId = ApiCasePro.getRecruitPreTopicIdNew(self, authorization2, str(activityId), 0, grade-4) # 0代表英语，grade代表年级
            executionId = ApiCasePro.getRecruitExecutionId(browser, authorization2, activityId, pretopicId)
            topicId = ApiCasePro.getRecruitTopicId(self, authorization2, str(executionId))
            while(elementflag):
                time.sleep(0.5)
                # 获取去题目序号
                questionText = ""
                questionText = browser.find_element_by_xpath("//div[@class='task-question__container']/div/span").text
                questionTupl = questionText.split('.', 2)
                questionNum = int(questionTupl[0])
                # 获取题目类型
                questionType = ApiCasePro.getQuestionType(self, authorization2, str(topicId))
                # 如果是选择题
                if questionType==0:
                    #selectBtnlist = browser.find_elements_by_xpath("//div[@class='task-option']")
                    #selectBtnlist[0].click()
                    Common.findElementClick(self, browser, "//div[@class='task-option'][1]")
                    time.sleep(0.3)
                    # 点击下一题按钮
                    Common.findElementClick(self, browser,
                                            "//div[@class='task-abstask__footer']/div[1]")
                    time.sleep(0.5)
                elif questionType ==1:  # 如果是填空题
                    # answerblank = ConnMysql.test_blank(browser, qlist[0])
                    inputlist = browser.find_elements_by_xpath("//input[@autocomplete='off']")
                    # time.sleep(1)
                    for i in range(len(inputlist)):
                        inputlist[i].send_keys("are")
                        time.sleep(0.3)
                    # 点击下一题按钮
                    Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div[1]")
                    time.sleep(0.5)
                count = count + 1
                print("-------------------> 第" + str(count) + "道题完成<---------------------")
                elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div[1]")
            time.sleep(2)
            name = ""
            name = browser.find_element_by_xpath("//div[@class='task-summary__head']/div[1]").text
            # questionlist =browser.find_elements_by_xpath("//div[@class='task-summary__content']/div[4]/div[2]/span")
            # questionCount_result = len(questionlist)
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("173测试", name, msg="测评报告学生名字显示不对")
        #self.assertEqual(questionNum, questionCount_result, msg="完成英语招生测评卡题目数量和报告页题目数量不一致！")
        print("-------------------> [1]英语招生测评结束 <---------------------\n")

    @BeautifulReport.add_test_img('test_b_mathRecruit')
    def test_b_mathRecruit(self):
        ''' 完成2020春季数学招生测评，随机完成一个年级，填空题全部输入根号5'''
        try:
            print("-------------------> [2]数学招生测评开始 <---------------------\n")
            time.sleep(1.5)
            # 选择数学
            browser.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[3]").click()
            time.sleep(0.6)
            # 随机获取年级数字
            grade = random.randint(1, 9)
            divNum = grade+1
            print("-------------------> 选择数学" + str(grade) + "年级的招生测评<---------------------")
            # 点击年级，进入测评
            Common.findElementClick(self, browser, "//*[@id='root']/div/div[2]/div/div["+str(divNum)+"]")
            count=0
            elementflag = False
            elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div[1]")
            # 获取招生测评的topisId, executionId, topicId
            activityId = ApiCasePro.getActivityId(browser, authorization1, directurl)
            pretopicId = ApiCasePro.getRecruitPreTopicIdNew(self, authorization2, str(activityId), 1, grade-1)
            executionId = ApiCasePro.getRecruitExecutionId(browser, authorization2, activityId, pretopicId)
            topicId = ApiCasePro.getRecruitTopicId(self, authorization2, str(executionId))
            while(elementflag):
                time.sleep(0.5)
                # 获取题目序号
                questionText = ""
                questionText = browser.find_element_by_xpath("//div[@class='task-question__container']/div/span").text
                questionTupl = questionText.split('.', 2)
                questionNum = 0
                questionNum = int(questionTupl[0])
                # 获取题目类型
                questionType = ApiCasePro.getQuestionType(self, authorization2, str(topicId))
                # 如果是选择题
                if questionType == 0:
                    # 获取选择项列表
                    #selectBtnlist = browser.find_elements_by_xpath("//div[@class='task-option']")
                    #selectBtnlist[1].click()
                    Common.findElementClick(self, browser, "//div[@class='task-option'][1]")
                    time.sleep(0.3)
                    # 点击下一题按钮
                    Common.findElementClick(self, browser,
                                            "//div[@class='task-abstask__footer']/div[1]")
                    time.sleep(0.4)
                elif questionType == 1:  # 如果是填空题
                    # answerblank = ConnMysql.test_blank(browser, qlist[0])
                    inputlist = browser.find_elements_by_xpath("//span[@class='mq-root-block mq-empty']")
                    for i in range(len(inputlist)):
                        # 点击填空题，准备输入内容
                        Common.findElementClick(self, browser, "//span[@class='mq-root-block mq-empty'][1]")
                        #inputlist[i].click()
                        time.sleep(0.5)
                        # 输入根号
                        Common.findElementClick(self, browser,
                                                "//div[@class='gapInput-keypad__keys_wrapper']/div[1]/div/div[1]/div/span[9]")
                        time.sleep(0.3)
                        # 输入数字5
                        Common.findElementClick(self, browser,
                                                "//div[@class='gapInput-keypad__keys_wrapper']/div[1]/div/div[2]/span[10]")
                        # 点击空白处 ，关闭数学公式
                        Common.findElementActionClick(self, browser, "//div[@class='task-question__container']")
                        time.sleep(0.4)
                    # 点击空白处 ，关闭数学公式
                        Common.findElementActionClick(self, browser, "//div[@class='task-question__container']")
                    time.sleep(0.4)
                    # 点击下一题按钮
                    Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div[1]")
                    time.sleep(0.5)
                count = count + 1
                print("-------------------> 第" + str(count) + "道题完成<---------------------")
                elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div[1]")
            time.sleep(2)
            name = ""
            name = browser.find_element_by_xpath("//div[@class='task-summary__head']/div[1]").text
            questionlist = browser.find_elements_by_xpath("//div[@class='task-summary__content']/div[4]/div[2]/span")
            # questionCount_result = 0
            # questionCount_result = len(questionlist)
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("173测试", name, msg="测试报告学生名字不对")
        #self.assertEqual(questionNum, questionCount_result, msg="完成数学招生测评卡题目数量和报告页题目数量不一致！")
        print("-------------------> [2]招生测评数学结束 <---------------------\n")

directurl="https://autotest.learnta.cn"
directList = Common.getDirectPath(Common)
report_dir = directList[0]
img_path = directList[1]
testsuit = unittest.TestSuite()
#testsuit.addTest(RecruitTesting_Pro("test_a_englishRecruit"))
testsuit.addTests(unittest.makeSuite(RecruitTesting_Pro))
run = BeautifulReport(testsuit)
run.report(filename='TAD1.0正服_招生测评复制链接完成测评', description='TAD1.0正服_招生测评复制链接完成测评测试用例', report_dir=report_dir)