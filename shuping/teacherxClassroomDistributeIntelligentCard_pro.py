#coding=utf-8

# @Time    : 2019/11/15
# @Author  : shuping zhao
# @File    : teacherxClassroomDistributeIntelligentCard_pro.py
import os
import sys
import traceback
import unittest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from BeautifulReport import BeautifulReport
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

sys.path.append('/opt/')
sys.path.append('/opt/uitest/shuping/common/Common/')
sys.path.append('/opt/uitest/shuping/page/LoginPage/')
from uitest.shuping.common.Common import Common
from uitest.shuping.page.LoginPage import LoginPage

class teacherxIntelligentCardTest_pro(unittest.TestCase):
    def setUp(self):
        global browser
        global window_teacher
        global window_student
        # global orgId
        # orgId = 100067  # 测服是1000369
        try:
            # mac本地
            #path = os.path.dirname(os.path.abspath('./config/chromedriver/chromedriver'))
            teacherUrl = Common.getUrl(self, "TypeUrl", "teacherxUrl")
            studentUrl = Common.getUrl(self, "TypeUrl", "studentxUrl")
            teacherUsername = "18817572035"
            teacherPassword = "1111"
            studentUsername = "17317495785"
            studentPassword = "495785"
            courseCode = "156609"
            searchName = "自动化测试课程英语人教版七年级同步课"

            #mobileEmulation = {"deviceName": "iPad"}
            # linux使用的静默执行方法
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument("--no-sandbox")
            options.add_argument('--disable-gpu')
            options.add_argument('window-size=850x750')
            #options.add_experimental_option("mobileEmulation", mobileEmulation)
            #options.add_argument("start-maximized")

            # options.add_argument('--headless')
            # options.add_argument('--disable-gpu')
            # options.add_argument('--no-sandbox')
            # 设置打开浏览器不显示data; 加载本地浏览器数据，加载很慢放弃！
            #options.add_argument('--user-data-dir=/Users/shuping/Library/Application Support/Google/Chrome/Default')
            # mac、linux配置
            #browser = webdriver.Chrome(executable_path=path, options=options)
            # 服务器上写法
            browser = webdriver.Chrome(options=options)
            windows = LoginPage.xLoginStudySystem(self, browser,teacherUrl, studentUrl, teacherUsername, teacherPassword, studentUsername, studentPassword,  searchName, courseCode)
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
        # 服务器存放图片路径
        browser.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))

    @BeautifulReport.add_test_img('test_a_xassignIntelligentAssessmentCard')
    def test_a_xassignIntelligentAssessmentCard(self):
        '''老师和学生进入课堂学生完成智能测评卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)
            print("---------------------> 【1 Start】老师开始发送智能测评卡 <------------------------\n")
            # 点击智能测评按钮
            browser.find_element_by_xpath("//div[@class='nvnIconBtnsRight']/div/div[2]").click()
            # 测评列表数据出来3秒
            time.sleep(2.5)
            # 点击第一个测评专题的开始测评
            browser.find_element_by_xpath("//div[@class='evaluateListWarpper']/div/div/div/div[1]/div[2]/div/div[2]/ul/li[1]/span[4]").click()
            # 获取输入框list
            # inputs = browser.find_elements_by_xpath("//input[@type='checkbox']")
            # browser.find_element_by_xpath("//div[@class='ant-table-header']/table/thread/tr/th[1]/span/div/label/span").click()
            js1="$('.ant-modal-wrap ')[1].scroll(600,600)"
            browser.execute_script(js1)
            time.sleep(1.5)
            print("--------------------->向上、向左滚动弹窗成功<------------------------")
            # 点击发送按钮
            Common.findElementClick(self, browser, "//div[@class='ant-modal-footer']/div/div/button")
            #browser.find_element_by_xpath("//div[@class='footerWarpper']/div/button").click()
            time.sleep(1)
            # 转到学生端窗口
            browser.switch_to.window(window_student)
            time.sleep(4)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser,"//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                # 点击录屏安装弹窗
                browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
                print("--------------------->成功关闭录屏弹窗<------------------------")
            time.sleep(0.5)
            js = "$('.mainLayout').scrollLeft(500)"
            browser.execute_script(js)
            elementflag = Common.isElementExist2(self, browser,"//div[@class='task-abstask__footer']/div")
            count = 0
            while (elementflag):
                # 点击下一题按钮
                browser.find_element_by_xpath("//div[@class='task-abstask__footer']/div").click()
                time.sleep(0.7)
                count = count + 1
                print("-------------------> 第" + str(count) + "道题完成<---------------------")
                elementflag = Common.isElementExist2(self, browser,"//div[@class='task-abstask__footer']/div")
            time.sleep(1.5)
            textname=""
            textname = browser.find_element_by_xpath(
                "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
            browser.switch_to.window(window_teacher)
            time.sleep(0.5)
            completestatus = " "
            completestatus=browser.find_element_by_xpath("//tbody[@class='ant-table-tbody']/tr/td[2]").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("第一单元-自动化测试课程英语人教版七年级同步课定制测评", textname, msg="学生完成智能测评卡失败！")
        self.assertEqual("已完成", completestatus, msg="未完成智能测评卡")
        print("-------------------> 【1 End】学生成功完成智能测评卡 <---------------------\n")

directList = Common.getDirectPath(Common)
report_dir = directList[0]
img_path = directList[1]

testsuit = unittest.TestSuite()
#testsuit.addTest(teacherxIntelligentCardTest_pro("test_a_assignIntelligentAssessmentCard"))
testsuit.addTests(unittest.makeSuite(teacherxIntelligentCardTest_pro))
run = BeautifulReport(testsuit)
# 服务器存储路径
run.report(filename='TAD2.0_正服给学生发送智能测评卡', description='TAD2.0_正服上课发智能测评任务卡测试用例', report_dir=report_dir)
