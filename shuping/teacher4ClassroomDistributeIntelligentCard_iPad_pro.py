#coding=utf-8

# @Time    : 2019/12/27
# @Author  : shuping zhao
# @File    : teacher4ClassroomDistributeIntelligentCard_iPad_pro.py
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

# addon_dir = os.path.dirname(os.path.dirname((__file__)))
# print("teacher4 addon_dir: " + addon_dir)
# sys.path.append(addon_dir)
sys.path.append('/opt/')
sys.path.append('/opt/uitest/shuping/common/ApiTestCasePro/')
from uitest.shuping.common.ApiTestCasePro import ApiTestCasePro

class teacher4ClassroomDistributeIntelligentCardiPad_pro(unittest.TestCase):
    def setUp(self):
        global browser
        global window_teacher
        global window_student
        global authorization2
        global authorization1
        global urlstr
        global orgId
        urlstr = "autotest.learnta.cn"
        orgId = 100040  # 测服是1000369
        try:
            # linux1路径
            #path = "/usr/local/python3/chromedriver"

            #path = os.path.dirname(os.path.abspath('./config/chromedriver/chromedriver'))
            url = directurl + "/teacher4"
            #mobileEmulation = {"deviceName": "iPad"}
            # linux使用的静默执行方法
            options = webdriver.ChromeOptions()
            #options.add_experimental_option("mobileEmulation", mobileEmulation)
            # options.add_argument('--headless')
            # options.add_argument('--disable-gpu')
            # options.add_argument('--no-sandbox')

            # 设置打开浏览器不显示data; 加载本地浏览器数据，加载很慢放弃！
            #options.add_argument('--user-data-dir=/Users/shuping/Library/Application Support/Google/Chrome/Default')
            # mac、linux配置
            #browser = webdriver.Chrome(executable_path=path, options=options)
            # 服务器上写法
            browser = webdriver.Chrome(options=options)

            #driver = webdriver.Chrome(executable_path=path)
            browser.implicitly_wait(5)
            browser.get(url)
            #browser.set_window_size(750, 750)
            browser.maximize_window()
            print(u"\nLogin start !")
            # url重定向需要等待时间
            time.sleep(1.5)
            browser.find_element_by_id("username").send_keys("18817572035")
            browser.find_element_by_xpath("//input[@placeholder='请输入验证码']").send_keys("1111")
            #点击登录按钮
            self.findElementActionClick("//button[@type='submit']")
            time.sleep(1.5)
            #获取教师端token
            tokenstr = " "
            tokenspr = []
            tokenstr = browser.execute_script('return window.localStorage.getItem("__ta/teacher_token");')
            tokenstr.encode('utf-8')
            tokenspr = tokenstr.split('[\"', 2)
            #tokenspr.encode('utf-8')
            teachertoken = str(tokenspr[1]).split('\",', 2)
            #print("teachertoken =" + teachertoken[0])
            authorization1 = "Bearer" + " " + teachertoken[0]
            print("-------------------> 【0】 Setup Teacher4 登录成功! <----------------------\n")
            # 点击学习系统模块
            self.findElementActionClick("//div[@name='layout_container_name']/div[1]")
            time.sleep(0.5)
            # 搜索课程名称
            browser.find_element_by_id("keyword").send_keys("测试自动化卡")
            browser.find_element_by_xpath("//a[@class='searchBtn']").click()
            time.sleep(1)
            # 点击进入课堂
            self.findElementActionClick("//*[@class='wCardsLayout']/div[1]/div[1]/div/a")
            time.sleep(1.5)
            # 获取窗口句柄
            #windows = browser.window_handles
            window_teacher = browser.window_handles[0]
            studentUrl = directurl + "/student4/login"
            js = 'window.open("' + studentUrl + '");'
            browser.execute_script(js)
            time.sleep(0.5)
            window_student = browser.window_handles[1]
            browser.switch_to.window(window_student)
            # 输入用户名、密码 登录
            browser.find_element_by_id("username").send_keys("17317495785")
            browser.find_element_by_id("password").send_keys("495785")
            # 点击登录按钮
            self.findElementActionClick("//button[@type='submit']")
            time.sleep(1)
            # 点击进入课堂按钮
            browser.find_element_by_xpath("//button[@type='button']").click()
            # 输入课堂码，点击确定按钮  ，则进入课堂
            browser.find_element_by_xpath("//input[@type='text']").send_keys("154826")
            self.findElementActionClick("//div[@class='ant-modal-confirm-btns']/button[2]")
            print("------------------> 【0】Setup 学生登录成功并进入到课堂里 <-------------------\n")
            #browser.find_element_by_xpath("//div[@class='cardWrapper']/div[1]").click()

            # 获取学生端token
            stoken = " "
            stokenspr = []
            stoken = browser.execute_script('return window.localStorage.getItem("__ta/student_token");')
            stoken.encode('utf-8')
            #strstoken = str(stoken)
            stokenspr = stoken.split('[\"', 2)
            studenttoken = str(stokenspr[1]).split('\",', 2)
            authorization2 = "Bearer" + " " + str(studenttoken[0])
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

    # 判断元素是否存在的方法
    def isElementExist(self, element):
        flag = True
        try:
            if browser.find_element_by_xpath(element):
                return flag
        except:
            flag = False
            return flag
    def isElementExist2(self, xpath):
        flag = True
        try:
            locator = (By.XPATH, xpath)
            element = WebDriverWait(browser, 3).until(EC.presence_of_element_located(locator))
            return flag
        except:
            flag = False
            return flag
            traceback.print_exc()
    # 判断元素s
    def isElementsExist(self, xpath):
        flag = True
        try:
            locator = (By.XPATH, xpath)
            element = WebDriverWait(browser, 3).until(EC.presence_of_all_elements_located(locator))
            return flag
        except:
            flag = False
            return flag
            traceback.print_exc()

    # # 判断元素是否存在的方法
    # def isElementsExist(self, elements):
    #     flag = True
    #     try:
    #         if browser.find_elements_by_xpath(elements):
    #             return flag
    #     except:
    #         flag = False
    #         return flag
    # 获取元素后点击
    def findElementClick(self, locator):
        try:
            element = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.XPATH, locator)), message="获取等待元素失败")
            element.click()
        except:
            traceback.print_exc()
            print("点击" + locator + "元素失败！")
    # 点击元素失败后跳出
    # def findElementClick(self, locator):
    #     try:
    #         element = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.XPATH, locator)), message="获取等待元素失败")
    #         element.click()
    #     except:
    #         traceback.print_exc()
    #         print("点击" + locator + "元素失败！")
    def findElementActionClick(self, locator):
        try:
            action = ActionChains(browser)
            above = browser.find_element_by_xpath(locator)
            action.move_to_element(above).perform()
            action.click(above).perform()
        except:
            traceback.print_exc()
            print("点击Action元素"+locator+"失败！\n")

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
            self.findElementActionClick("//div[@class='cardsSelectors']/p[3]")
            # 向下滚动找到更多按钮
            jquery = "$('.classroomCardSubContainer').scrollTop(700)"
            browser.execute_script(jquery)
            time.sleep(0.7)
            # 获取定制测评的最后一个任务状态
            buttonflag = self.isElementExist2("//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[3]/div[1]")
            if buttonflag == True:
                # 点击更多按钮
                self.findElementActionClick(
                    "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]")
                #time.sleep(0.5)
                # 点击删除按钮
                self.findElementActionClick(
                    "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                time.sleep(0.5)
                # 点击确定按钮
                self.findElementActionClick("//*[@class='ant-confirm-btns']/button[2]")
                time.sleep(1)
                # 点击分配任务按钮
                self.findElementActionClick("//*[@id='cardsContainer']/div[1]/div[1]/div[3]")
            elif buttonflag == False:
                # 点击分配任务按钮
                self.findElementActionClick("//*[@id='cardsContainer']/div[1]/div[1]/div[3]")
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
            self.findElementActionClick("//*[@class='pointsSelectModal']/div[3]/button")
            # 转到学生端窗口
            browser.switch_to.window(window_student)
            # 发卡后学生端倒计时5s
            time.sleep(5.5)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = self.isElementExist("//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                # 点击录屏安装弹窗
                self.findElementActionClick("//div[@class='ant-modal-body']/div/div[2]/button")

            js = "$('.mainLayout').scrollLeft(500)"
            browser.execute_script(js)
            time.sleep(0.5)
            # 教师端 从接口获取classroomId 、ExecutionId
            classroomId = ApiTestCasePro.test_getClassroomId(self, authorization1, urlstr, orgId)
            executionId = ApiTestCasePro.test_getTaskExecutionId(self, authorization2, urlstr, str(classroomId))
            # text = browser.switch_to.alert.text
            # browser.switch_to.alert.accept()
            # browser.find_element_by_xpath("//[@class='ant-confirm-btns']/button")
            locator2 = (By.XPATH, "//*[@class='btnWrapper']/a[2]")
            WebDriverWait(browser, 5).until(EC.presence_of_element_located(locator2))
            elementflag = self.isElementExist("//*[@class='btnWrapper']/a[2]")
            count = 0
            while (elementflag):
                qulist = ApiTestCasePro.test_get_studentquestion(self, authorization2, urlstr, executionId)
                # time.sleep(1)
                if qulist[1] == 1:
                    # 学生端 从接口获取questionId、qtype
                    blankanswer = ApiTestCasePro.get_answer(self, authorization2, urlstr, str(qulist[0]))
                    gaplist = browser.find_elements_by_xpath("//input[@class='gapInput']")
                    answercount = len(blankanswer)
                    gapcount = len(gaplist)
                    if answercount == gapcount:
                        for i in range(len(gaplist)):
                            gaplist[i].send_keys(blankanswer[i][0])
                        # 点击下一题按钮
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                    else:
                        # 点击下一题按钮
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                        time.sleep(0.5)
                        # 点击确定按钮
                        self.findElementActionClick("//div[@class='ant-modal-body']/div/div[2]/button[2]")
                elif qulist[1] == 0:
                    # 学生端 从接口获取questionId、qtype
                    selectanswer = ApiTestCasePro.get_answer(self, authorization2, urlstr, str(qulist[0]))
                    if selectanswer[0][0] == 'A':
                        self.findElementActionClick("//li[@tabindex='1']")
                        time.sleep(0.5)
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                    elif selectanswer[0][0] == 'B':
                        self.findElementActionClick("//li[@tabindex='2']")
                        time.sleep(0.5)
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                    elif selectanswer[0][0] == 'C':
                        self.findElementActionClick("//li[@tabindex='3']")
                        time.sleep(0.5)
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                    elif selectanswer[0][0] == 'D':
                        self.findElementActionClick("//li[@tabindex='2']")
                        time.sleep(0.5)
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                    else:
                        # 点击下一题按钮
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                else:
                    # 点击下一题按钮
                    self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                count = count + 1
                print("-------------------> 第" + str(count) + "道题完成<---------------------")
                elementflag = self.isElementExist("//*[@class='btnWrapper']/a[2]")
            cardname = browser.find_element_by_xpath("//div[@class='pSummaryBody']/div[1]/h4").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("专题：测试自动化卡定制测评", cardname, msg="学生完成Diygo卡失败！")
        print("-------------------> [1 End]学生成功完成Diygo卡 <---------------------\n")

    @BeautifulReport.add_test_img('test_b_assignintelligencePraticeCard')
    def test_b_assignintelligencePraticeCard(self):
        '''老师和学生都进入课堂学生完成智能练习卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)
            print("-------------------> 【2 Start】老师开始发送智能练习卡 <---------------------\n")
            # 点击 重点词汇——基础知识 模块
            self.findElementActionClick("//div[@class='cardsSelectors']/p[6]")
            # 向下滚动找到更多按钮
            jquery = "$('.classroomCardSubContainer').scrollTop(700)"
            browser.execute_script(jquery)
            time.sleep(0.7)
            # 滚动到智能练习卡
            # js2 = "document.getElementById('cardWarp').scroll(500,0);"
            # browser.execute_script(js2)
            time.sleep(1)
            buttonflag = self.isElementExist("//div[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[3]/div[1]")
            if buttonflag == True:
                # 点击更多按钮
                self.findElementActionClick("//div[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]")
                # 点击删除按钮
                self.findElementActionClick(
                    "//div[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                time.sleep(0.5)
                # 点击确定按钮
                self.findElementActionClick("//*[@class='ant-confirm-btns']/button[2]")
                time.sleep(0.5)
                # 点击分配任务按钮
                self.findElementActionClick("//div[@id='cardsContainer']/div[1]/div[1]/div[3]")
            elif buttonflag == False:
                # 点击分配任务按钮
                self.findElementActionClick("//div[@id='cardsContainer']/div[1]/div[1]/div[3]")

            time.sleep(0.5)
            # 转到学生端窗口
            browser.switch_to.window(window_student)
            js = "$('.mainLayout').scrollLeft(500)"
            browser.execute_script(js)
            # 发卡后学生端倒计时5s
            time.sleep(5)

            review = self.isElementExist2("//div[@class='ant-modal-body']/div/div[2]/button[2]")
            if review == True:
                # 点击复习一下按钮
                # self.findElementClick("//div[@class='ant-modal-body']/div/div[2]/button[2]")
                self.findElementActionClick("//div[@class='ant-modal-body']/div/div[2]/button[2]")
            time.sleep(1)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = self.isElementExist2("//*[@class='ant-modal-body']/div/div[2]/button")
            if butbool == True:
                # 点击录屏安装弹窗
                self.findElementActionClick("//*[@class='ant-modal-body']/div/div[2]/button")
                time.sleep(1)

            # 发完智能练习卡后，查询taskExecutionId、taskgroupid
            classroomId = ApiTestCasePro.test_getClassroomId(self, authorization1, urlstr, orgId)
            taskExecutionId = ApiTestCasePro.test_getTaskExecutionId(self, authorization2, urlstr, str(classroomId))
            locator2 = (By.XPATH, "//*[@class='btnWrapper']/a[2]")
            WebDriverWait(browser, 5).until(EC.presence_of_element_located(locator2))
            elementflag = self.isElementExist2("//*[@class='btnWrapper']/a[2]")
            questioncount = 0
            while (elementflag):
                # 学生端 从接口获取questionId、qtype
                qulist = ApiTestCasePro.test_getIntelligentquestion(self, authorization2, urlstr, taskExecutionId)
                if qulist[0] == 200:
                    if qulist[3] == qulist[4] and qulist[2] == 1:
                        blankanswer = ApiTestCasePro.get_answer(self, authorization2, urlstr, str(qulist[1]))
                        gaplist = browser.find_elements_by_xpath("//input[@class='gapInput']")
                        answercount = len(blankanswer)
                        gapcount = len(gaplist)
                        count=0
                        if answercount == gapcount:
                            for i in range(len(gaplist)):
                                count = i+1
                                gaplist[i].send_keys(blankanswer[i][0])
                                if answercount == count:
                                    break;
                            # 输入完答案点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                            #time.sleep(0.5)
                            # 到判题页再点击下一题按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                        else:
                            # 输入完答案点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                            #time.sleep(0.5)
                            # 点击弹窗确认按钮
                            self.findElementActionClick("//div[@class='ant-modal-body']/div/div[2]/button[2]")
                            # 到判题页再点击下一题按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")

                    elif qulist[3] == qulist[4] and qulist[2] == 0:
                        # 学生端 从接口获取questionId、qtype
                        selectanswer = ApiTestCasePro.get_answer(self, authorization2, urlstr, str(qulist[1]))
                        if selectanswer[0][0] == 'A':
                            #time.sleep(0.5)
                            self.findElementClick("//li[@tabindex='1']")
                            # 点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                            #time.sleep(0.5)
                            # 输入完答案，再点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")

                        elif selectanswer[0][0] == 'B':
                            #time.sleep(0.5)
                            self.findElementClick("//li[@tabindex='2']")
                            #self.findElementClick("//li[@tabindex='2']")
                            # 输入完答案，点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                            #time.sleep(0.5)
                            # 输入完答案，再点击下一步按钮
                            self.findElementClick("//div[@class='btnWrapper']/a[2]")

                        elif selectanswer[0][0] == 'C':
                            #time.sleep(0.5)
                            self.findElementClick("//li[@tabindex='3']")
                            # 输入完答案，点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                            #time.sleep(0.5)
                            # 输入完答案，再点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")

                        elif selectanswer[0][0] == 'D':
                            #time.sleep(0.5)
                            self.findElementClick("//li[@tabindex='2']")
                            #self.findElementClick("//li[@tabindex='4']")
                            # 点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                            #time.sleep(0.5)
                            # 点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")

                    elif qulist[3] != qulist[4] and qulist[2] == 1:
                        #time.sleep(0.5)
                        # 点击下一步按钮
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                        time.sleep(1)
                        # 再点击弹窗的确定按钮
                        self.findElementClick("//*[@class='ant-modal-body']/div/div[2]/button[2]")
                        blankanswer = ApiTestCasePro.get_answer(self, authorization2, urlstr, str(qulist[1]))
                        gaplist = browser.find_elements_by_xpath("//input[@class='gapInput']")
                        answercount = len(blankanswer)
                        gapcount = len(gaplist)
                        count = 0
                        if answercount == gapcount:
                            for i in range(len(gaplist)):
                                count =i + 1
                                gaplist[i].send_keys(blankanswer[i][0])
                                if answercount == count:
                                    break;
                            # 输入完答案点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                            # time.sleep(0.5)
                            # 输入完答案， 再点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")

                        else:
                            # 输入完答案点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                            # 点击弹窗确认按钮
                            self.findElementActionClick("//div[@class='ant-modal-body']/div/div[2]/button[2]")
                            # 到判题页再点击下一题按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")

                    elif qulist[3] != qulist[4] and qulist[2] == 0:
                        #time.sleep(0.5)
                        # 点击下一步按钮
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                        time.sleep(1)
                        # 再点击弹窗的确定按钮
                        self.findElementActionClick("//*[@class='ant-modal-body']/div/div[2]/button[2]")
                        #time.sleep(0.5)
                        selectanswer = ApiTestCasePro.get_answer(self, authorization2, urlstr, str(qulist[1]))
                        if selectanswer[0][0] == 'A':
                            self.findElementClick("//li[@tabindex='1']")
                            # 点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                            #time.sleep(0.5)
                            # 输入完答案，再点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")

                        elif selectanswer[0][0] == 'B':
                            self.findElementClick("//li[@tabindex='2']")
                            # 输入完答案，点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                            #time.sleep(0.5)
                            # 输入完答案，再点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")

                        elif selectanswer[0][0] == 'C':
                            self.findElementClick("//li[@tabindex='2']")
                            # 输入完答案，点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                            #time.sleep(0.5)
                            # 输入完答案，再点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")

                        elif selectanswer[0][0] == 'D':
                            self.findElementClick("//li[@tabindex='2']")
                            # 点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                            #time.sleep(0.5)
                            # 点击下一步按钮
                            self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                    else:
                        # 点击下一步按钮
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                        time.sleep(0.5)
                        # 点击弹窗确定按钮
                        self.findElementActionClick(
                            "//div[@class='ant-modal-body']/div/div[2]/button[2]")
                        # 到判题页再点击下一题按钮
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                    questioncount = questioncount + 1
                    print("-------------------> 第" + str(questioncount) + "道题完成<---------------------")
                elif qulist[0] == 403:
                    # 如果是到结果页 ，点击弹窗确定按钮
                    confirmflag = self.isElementExist(
                        "//div[@class='ant-modal-body']/div/div[2]/button[@class='ant-btn ant-btn-primary']")
                    if confirmflag == True:
                        time.sleep(0.5)
                        self.findElementActionClick(
                            "//div[@class='ant-modal-body']/div/div[2]/button[@class='ant-btn ant-btn-primary']")
                    print("-------------------> 点击提交的确认弹窗按钮 <---------------------\n")
                    break
                elementflag = self.isElementExist2("//*[@class='btnWrapper']/a[2]")
            time.sleep(1)
            # 获取学生端的任务卡标题
            topicname = " "
            topicname = browser.find_element_by_xpath("//*[@id='analyzeReport']/h4").text
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)
            self.findElementActionClick("//button[@class='ant-modal-close']/span")
            intelligentCompleteStatus = " "
            intelligentCompleteStatus = browser.find_element_by_xpath(
                "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[3]/div[1]").text
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("专题：重点词汇", topicname, msg="完成智能练习卡失败！")
        self.assertEqual("已完成", intelligentCompleteStatus, msg="智能练习卡未完成！")
        print("-------------------> 【2 End】学生成功完成智能练习卡 <---------------------\n")

    @BeautifulReport.add_test_img('test_c_assignGoTestCard')
    def test_c_assignGoTestCard(self):
        '''老师和学生都进入课堂学生完成Go卡'''
        try:
            time.sleep(0.5)
            # 切换到教师端窗口
            browser.switch_to.window(window_teacher)
            # 滚动任务卡排
            # js2 = "document.getElementById('cardWarp').scroll(200,0);"
            # browser.execute_script(js2)
            print("-------------------> 【3 Start】老师开始发送Go卡 <---------------------\n")
            # 点击 Text_Lesson 1模块
            self.findElementActionClick("//div[@class='cardsSelectors']/p[7]")
            # 向下滚动找到更多按钮
            jquery = "$('.classroomCardSubContainer').scrollTop(700)"
            browser.execute_script(jquery)
            time.sleep(0.7)
            # 获取智能练习卡的最后一个任务状态
            buttonflag = self.isElementExist("//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[3]/div[1]")
            if buttonflag == True:
                # 点击更多按钮
                self.findElementActionClick(
                    "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]")
                # 点击删除按钮
                self.findElementActionClick(
                    "//*[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                time.sleep(0.5)
                # 点击确定按钮
                self.findElementActionClick("//*[@class='ant-confirm-btns']/button[2]")
                time.sleep(0.5)
                # 点击分配任务按钮
                self.findElementActionClick("//*[@id='cardsContainer']/div[1]/div[1]/div[3]")
            elif buttonflag == False:
                # 点击分配任务按钮
                self.findElementActionClick("//*[@id='cardsContainer']/div[1]/div[1]/div[3]")

            time.sleep(0.5)
            # 转到学生端窗口
            browser.switch_to.window(window_student)
            js = "$('.mainLayout').scrollLeft(500)"
            browser.execute_script(js)
            # 发卡后学生端倒计时5s
            time.sleep(6)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = self.isElementExist2("//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                # 点击录屏安装弹窗
                self.findElementActionClick("//div[@class='ant-modal-body']/div/div[2]/button")

            # 获取taskExecutionId
            classroomId = ApiTestCasePro.test_getClassroomId(self, authorization1, urlstr, orgId)
            taskExecutionId = ApiTestCasePro.test_getTaskExecutionId(self, authorization2, urlstr, str(classroomId))

            executionId = str(taskExecutionId)
            # 获取测评卡的topicId
            topicIdlist = ApiTestCasePro.test_getTopicId(self, authorization2, urlstr, executionId)
            elementflag = self.isElementExist2("//div[@class='btnWrapper']/a[2]")
            count = 0
            while (elementflag):
                # 学生端 从接口获取questionId、qtype
                topicId = str(topicIdlist[0])
                goQuestionId = ApiTestCasePro.test_getGoquestionId(self, authorization2, urlstr, topicId)
                qulist = ApiTestCasePro.test_getTestingquestionId(self, authorization2, urlstr, goQuestionId)
                if qulist[1] == 1:
                    blankanswer = ApiTestCasePro.get_answer(self, authorization2, urlstr, str(qulist[0]))
                    gaplist = browser.find_elements_by_xpath("//input[@class='gapInput']")
                    answercount = len(blankanswer)
                    gapcount = len(gaplist)
                    if answercount == gapcount:
                        for i in range(len(gaplist)):
                            gaplist[i].send_keys(blankanswer[i][0])
                        time.sleep(0.5)
                        # 点击下一题按钮
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                    else:
                        # 点击下一题按钮
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                        time.sleep(0.5)
                        # 点击确定按钮
                        self.findElementActionClick("//div[@class='ant-modal-body']/div/div[2]/button[2]")

                elif qulist[1] == 0:
                    # 查询选择题答案
                    optionanswer = ApiTestCasePro.get_answer(self, authorization2, urlstr, str(qulist[0]))
                    if optionanswer[0][0] == 'A':
                        self.findElementActionClick("//li[@tabindex='1']")
                        time.sleep(0.5)
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                    elif optionanswer[0][0] == 'B':
                        self.findElementActionClick("//li[@tabindex='2']")
                        time.sleep(0.5)
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                    elif optionanswer[0][0] == 'C':
                        self.findElementActionClick("//li[@tabindex='3']")
                        time.sleep(0.5)
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                    elif optionanswer[0][0] == 'D':
                        self.findElementActionClick("//li[@tabindex='2']")
                        time.sleep(0.5)
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                    else:
                        # 点击下一题按钮
                        self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                else:
                    # 点击下一题按钮
                    self.findElementActionClick("//div[@class='btnWrapper']/a[2]")
                    # 点击确定按钮
                    self.findElementActionClick("//div[@class='ant-modal-body']/div/div[2]/button[2]")
                count = count + 1
                print("-------------------> 第" + str(count) + "道题完成<---------------------")
                elementflag = self.isElementExist2("//*[@class='btnWrapper']/a[2]")

            title = browser.find_element_by_xpath("//*[@id='analyzeReport']/h4").text

        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("专题：重点词汇", title, msg="完成Go卡失败！")
        # self.assertEqual("已完成", testingCompleteStatus, msg="测评卡未完成！")
        print("------------------->【3 End】学生成功完成Go卡 <---------------------\n")

directurl="https://autotest.learnta.cn"
platf = sys.platform
print("platform:"+platf)
if platf != 'darwin':
    report_dir = "/opt/uitest/report"
    img_path = "/opt/uitest/img"
else:
    report_dir = "./report"
    img_path = "./img"

testsuit = unittest.TestSuite()
#testsuit.addTest(teacher4ClassroomDistributeIntelligentCardiPad_pro("test_b_assignintelligencePraticeCard"))
testsuit.addTests(unittest.makeSuite(teacher4ClassroomDistributeIntelligentCardiPad_pro))
run = BeautifulReport(testsuit)
# 服务器存储路径
run.report(filename='TAD1.0_正服教师端ipad给学生端发卡（智能卡）', description='TAD1.0_正服ipad上课发各种智能测评任务卡测试用例', report_dir=report_dir)
