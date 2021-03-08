#coding=utf-8

# @Time    : 2019/11/27
# @Author  : shuping zhao
# @File    : teacher4ClassroomDistributeIntelligentCard_Pro.py
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
from selenium.webdriver.common.keys import Keys
# addon_dir=os.path.dirname(os.path.dirname(__file__))
# sys.path.append(addon_dir)


sys.path.append('/opt/')
sys.path.append('/opt/uitest/shuping/common/ApiCasePro/')
sys.path.append('/opt/uitest/shuping/common/Common/')
sys.path.append('/opt/uitest/shuping/page/LoginPage/')
from uitest.shuping.common.ApiCasePro import ApiCasePro
from uitest.shuping.page.LoginPage import LoginPage
from uitest.shuping.common.Common import Common


class teacher4ClassroomDistributeIntelligentCard_pro(unittest.TestCase):
    urlstr = "autotest.learnta.cn"
    orgId = 100040  # 测服是1000369
    searchName = "测试自动化卡"
    # def __init__(self):

    def setUp(self):
        try:
            global browser
            global window_teacher
            global window_student
            global authorization2
            global authorization1
            # browser = webdriver.Chrome(options=options)
            # browser.implicitly_wait(5)
            teacher4url = Common.getUrl(self, "TypeUrl", "teacher4Url")
            studentUrl = Common.getUrl(self, "TypeUrl", "student4Url")
            teacherUsername = "18817572035"
            teacherPassword ="1111"
            studentUsername ="17317495785"
            studentPassword ="495785"
            courseCode = "154826"

            # linux使用的静默执行方法
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument("--no-sandbox")
            options.add_argument('--disable-gpu')
            options.add_argument('window-size=1280x1024')
            # # options.add_argument('--headless')
            # # options.add_argument('--disable-gpu')
            # # options.add_argument('--no-sandbox')
            #
            # # 设置打开浏览器不显示data; 加载本地浏览器数据，加载很慢放弃！
            # #options.add_argument('--user-data-dir=/Users/shuping/Library/Application Support/Google/Chrome/Default')
            # # mac、linux配置
            # #browser = webdriver.Chrome(executable_path=path, options=options)
            # # 服务器上写法
            # browser = webdriver.Chrome(options=options)
            #
            # #driver = webdriver.Chrome(executable_path=path)

            # 服务器上写法
            browser = webdriver.Chrome(options=options)

            windows = LoginPage.login(self, browser, teacher4url, studentUrl, teacherUsername, teacherPassword, studentUsername, studentPassword, self.searchName, courseCode)
            window_teacher = windows[0]
            window_student = windows[1]
            authorization1 = Common.getToken(self, browser, 'return window.localStorage.getItem("__ta/teacher_token");')
            authorization2 = Common.getToken(self, browser, 'return window.localStorage.getItem("__ta/student_token");')

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

    #@unittest.skip("跳过")
    @BeautifulReport.add_test_img('test_a_assiginDiygoCard')
    def test_a_assiginDiygoCard(self):
        '''老师和学生进入课堂学生完成定制测评卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)
            # 滚动任务卡排
            # js2 = "document.getElementById('cardWarp').scroll(200,0);"
            # browser.execute_script(js2)
            print("-------------------> [1 Start]老师开始发送Diygo卡 <----------------------\n")
            # 点击定制测评模块
            Common.findElementActionClick(self, browser, "//div[@class='cardsSelectors']/p[3]")
            # 向下滚动找到更多按钮
            jquery = "$('.classroomCardSubContainer').scrollTop(700)"
            browser.execute_script(jquery)
            time.sleep(0.7)
            # 获取定制测评的最后一个任务状态
            buttonflag = Common.isElementExist2(self, browser, "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[3]/div[1]")
            if buttonflag == True:
                # 点击更多按钮
                Common.findElementActionClick(self, browser,
                    "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]")
                #time.sleep(0.5)
                # 点击删除按钮
                Common.findElementActionClick(self, browser,
                    "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                time.sleep(0.5)
                # 点击确定按钮
                Common.findElementActionClick(self, browser, "//*[@class='ant-confirm-btns']/button[2]")
                time.sleep(1)
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[1]/div[1]/div[3]")
            elif buttonflag == False:
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//*[@id='cardsContainer']/div[1]/div[1]/div[3]")
            # 弹窗出来有延时
            time.sleep(1)
            inputs = browser.find_elements_by_xpath("//input[@type='checkbox']")
            inputs[1].click()

            # 选择第一个教学点的所有知识点
            # if inputs[0].get_attribute('type') == 'checkbox':
            #     inputs[0].click()
            # browser.find_elements_by_css_selector('input[type=checkbox]').pop().click()

            time.sleep(0.5)
            # 点击确定按钮
            Common.findElementActionClick(self, browser, "//*[@class='pointsSelectModal']/div[3]/button")
            # 转到学生端窗口
            browser.switch_to.window(window_student)
            # 发卡后学生端倒计时5s
            time.sleep(5.5)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")

            js = "$('.mainLayout').scrollLeft(500)"
            browser.execute_script(js)
            time.sleep(0.5)

            elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div")
            count = 0
            while (elementflag):
                # 点击下一题按钮
                Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div")
                time.sleep(0.5)
                count = count + 1
                print("-------------------> 第" + str(count) + "道题完成<---------------------")
                elementflag = Common.isElementExist(self, browser, "//div[@class='task-abstask__footer']/div")
            cardname = browser.find_element_by_xpath("//div[@class='task-summary__content']/div[3]/div[1]").text
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)
            completeStatus = " "
            completeStatus = browser.find_element_by_xpath(
                "//tbody[@class='ant-table-tbody']/tr/td[2]").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("专题：测试自动化卡定制测评", cardname, msg="学生完成Diygo卡失败！")
        self.assertEqual("已完成", completeStatus, msg="智能练习卡未完成！")
        print("-------------------> [1 End]学生成功完成Diygo卡 <---------------------\n")

    #@unittest.skip("跳过")
    @BeautifulReport.add_test_img('test_b_assignintelligencePraticeCard')
    def test_b_assignintelligencePraticeCard(self):
        ''' 老师和学生都进入课堂学生完成智能练习卡 '''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)
            print("-------------------> 【2 Start】老师开始发送智能练习卡 <---------------------\n")
            # 点击 重点词汇——基础知识 模块
            Common.findElementActionClick(self, browser, "//div[@class='cardsSelectors']/p[6]")
            # 向下滚动找到更多按钮
            jquery = "$('.classroomCardSubContainer').scrollTop(700)"
            browser.execute_script(jquery)
            time.sleep(0.7)
            # 滚动到智能练习卡
            # js2 = "document.getElementById('cardWarp').scroll(500,0);"
            # browser.execute_script(js2)
            time.sleep(1)
            buttonflag = Common.isElementExist(self, browser, "//div[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[3]/div[1]")
            if buttonflag == True:
                # 点击更多按钮
                Common.findElementActionClick(self, browser, "//div[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]")
                # 点击删除按钮
                Common.findElementActionClick(self, browser,
                    "//div[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                time.sleep(0.5)
                # 点击确定按钮
                Common.findElementActionClick(self, browser, "//*[@class='ant-confirm-btns']/button[2]")
                time.sleep(0.5)
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//div[@id='cardsContainer']/div[1]/div[1]/div[3]")
            elif buttonflag == False:
                # 点击分配任务按钮
                Common.findElementActionClick(self, browser, "//div[@id='cardsContainer']/div[1]/div[1]/div[3]")

            time.sleep(0.5)
            # 转到学生端窗口
            browser.switch_to.window(window_student)
            js = "$('.mainLayout').scrollLeft(500)"
            browser.execute_script(js)
            # 发卡后学生端倒计时5s
            time.sleep(5)

            review = Common.isElementExist2(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
            if review == True:
                # 点击复习一下按钮
                # Common.findElementClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
            time.sleep(1)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist2(self, browser, "//*[@class='ant-modal-body']/div/div[2]/button")
            if butbool == True:
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//*[@class='ant-modal-body']/div/div[2]/button")
            time.sleep(1)
            # 发完智能练习卡后，查询taskExecutionId、taskgroupid
            classroomId = ApiCasePro.getClassroomId(self, authorization1, self.urlstr, self.orgId, self.searchName)
            taskList = ApiCasePro.getTaskExecutionId(self, authorization2, self.urlstr,
                                                                                  str(classroomId))
            taskExecutionId = taskList[0]
            taskType = taskList[1]
            locator2 = (By.XPATH, "//div[@class='task-abstask__footer']/div")
            WebDriverWait(browser, 5).until(EC.presence_of_element_located(locator2))
            elementflag = Common.isElementExist2(self, browser, "//div[@class='task-abstask__footer']/div")
            questioncount = 0
            count = 0
            qulist = ApiCasePro.getIntelligentQuestion(self, authorization2, self.urlstr,
                                                           str(taskExecutionId), str(taskType))
            while (elementflag):
                # 判断是否有下一题
                if qulist[0] == True:
                    # 点击下一步按钮
                    Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div")
                    time.sleep(0.5)
                    # 判题页，点击弹窗确定按钮
                    Common.findElementClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[2]")
                    time.sleep(0.5)
                    # 点击下一步按钮    #   task-learn__list /h3
                    Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div")
                    textFlag = Common.isElementExist3(self, browser, "//div[@class='task-learn__list']")
                    if textFlag == True:
                        # 点击下一步按钮
                        Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div")
                        # 点击弹窗确定按钮
                        Common.findElementClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button[@class='ant-btn ant-btn-primary']")
                        time.sleep(0.5)
                elif qulist[0] == False:
                    time.sleep(0.6)
                    # 如果是到结果页 ，点击弹窗确定按钮
                    confirmflag = Common.isElementExist(self, browser,
                        "//div[@class='ant-modal-body']/div/div[2]/button[@class='ant-btn ant-btn-primary']")
                    if confirmflag == True:
                        time.sleep(0.5)
                        Common.findElementClick(self, browser,
                            "//div[@class='ant-modal-body']/div/div[2]/button[@class='ant-btn ant-btn-primary']")
                qulist = ApiCasePro.getIntelligentQuestion(self, authorization2, self.urlstr,
                                                               str(taskExecutionId), str(taskType))
                count = count + 1
                print("-------------------> 第" + str(count) + "道题完成<---------------------")
                elementflag = Common.isElementExist2(self, browser, "//div[@class='task-abstask__footer']/div")
            time.sleep(1.5)
            # 获取学生端的任务卡标题
            topicname = ""
            topicname = browser.find_element_by_xpath("//div[@class='task-summary__content']/div[3]/div[1]").text
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)
            #Common.findElementActionClick(self, browser, "//button[@class='ant-modal-close']/span")
            intelligentCompleteStatus = " "
            intelligentCompleteStatus = browser.find_element_by_xpath(
                "//tbody[@class='ant-table-tbody']/tr/td[2]").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        #self.assertEqual("专题：词汇", topicname, msg="完成智能练习卡失败！")
        self.assertEqual("已完成", intelligentCompleteStatus, msg="智能练习卡未完成！")
        print("-------------------> 【2 End】学生成功完成智能练习卡 <---------------------\n")

    #@unittest.skip("跳过")
    @BeautifulReport.add_test_img('test_c_assignGoTestCard')
    def test_c_assignGoTestCard(self):
        '''老师和学生都进入课堂学生完成测评卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)
            time.sleep(0.5)
            print("-------------------> 【3 Start】老师开始发送Go卡 <---------------------\n")
            # 点击 Text_Lesson 1模块
            Common.findElementClick(self, browser, "//div[@class='cardsSelectors']/p[7]")
            time.sleep(0.4)
            # 向下滚动找到更多按钮
            jquery = "$('.classroomCardSubContainer').scrollTop(700)"
            browser.execute_script(jquery)
            time.sleep(0.7)
            # 获取测评卡的最后一个任务状态
            buttonflag = Common.isElementExist(self, browser, "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[3]/div[1]")
            if buttonflag == True:
                # 点击更多按钮
                Common.findElementActionClick(self, browser,
                    "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]")
                # 点击删除按钮
                Common.findElementActionClick(self, browser,
                    "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
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
            # 转到学生端窗口
            browser.switch_to.window(window_student)
            js = "$('.mainLayout').scrollLeft(500)"
            browser.execute_script(js)
            # 发卡后学生端倒计时5s
            time.sleep(6)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = Common.isElementExist2(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                # 点击录屏安装弹窗
                Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]/button")

            elementflag = Common.isElementExist2(self, browser, "//div[@class='task-abstask__footer']/div")
            count = 0
            while (elementflag):
                # 点击下一题按钮
                Common.findElementClick(self, browser, "//div[@class='task-abstask__footer']/div")
                time.sleep(0.5)
                count = count + 1
                print("-------------------> 第" + str(count) + "道题完成<---------------------")
                elementflag = Common.isElementExist2(self, browser, "//div[@class='task-abstask__footer']/div")
            time.sleep(0.5)
            title = browser.find_element_by_xpath("//div[@class='task-summary__content']/div[3]/div[1]").text
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)
            CompleteStatus = " "
            CompleteStatus = browser.find_element_by_xpath(
                "//tbody[@class='ant-table-tbody']/tr/td[2]").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        #self.assertEqual("专题：词汇", title, msg="完成Go卡失败！")
        self.assertEqual("已完成", CompleteStatus, msg="测评卡未完成！")
        print("------------------->【3 End】学生成功完成Go卡 <---------------------\n")

directList = Common.getDirectPath(Common)
report_dir = directList[0]
img_path = directList[1]

testsuit = unittest.TestSuite()
#testsuit.addTest(teacher4ClassroomDistributeIntelligentCard_pro("test_b_assignintelligencePraticeCard"))
testsuit.addTests(unittest.makeSuite(teacher4ClassroomDistributeIntelligentCard_pro))
run = BeautifulReport(testsuit)
# 服务器存储路径
run.report(filename='TAD1.0正服_教师端给学生端发卡（智能卡）', description='TAD1.0_正服上课发各种智能测评任务卡测试用例', report_dir=report_dir)
