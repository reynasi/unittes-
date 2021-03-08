#coding=utf-8

# @Time    : 2020/02/19
# @Author  : shuping zhao
# @File    : teacher4TestingCase_Pro.py

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
from uitest.shuping.common.ApiCasePro import *

class teacherxCustomizeTestingCase_Pro(unittest.TestCase):
    def setUp(self):
        global browser
        global windows
        global authorization2
        global authorization1
        global imgurl
        try:
            # mac 路径
            #path = "/Users/shuping/chromedriver"

            #path = os.path.dirname(os.path.abspath('./config/chromedriver/chromedriver'))
            url = directurl+"/teacherx"

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

            browser.implicitly_wait(5)
            browser.get(url)
            #browser.maximize_window()
            print(u"\nLogin start !")
            time.sleep(1.5)
            browser.find_element_by_id("username").send_keys("18817572035")
            browser.find_element_by_xpath("//input[@placeholder='请输入验证码']").send_keys("1111")
            #点击登录按钮
            browser.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(1.5)
            # 获取教师端token
            tokenstr = " "
            tokenspr = []
            time.sleep(1.5)
            tokenstr = browser.execute_script('return window.localStorage.getItem("__ta/teacher_token")')
            tokenstr.encode('utf-8')
            tokenspr = tokenstr.split('[\"', 2)
            teachertoken = tokenspr[1].split('\",', 2)
            # print("teachertoken =" + teachertoken[0])
            authorization1 = "Bearer" + " " + teachertoken[0]
            print("Teacher4 Login Success!")
            print("-------------------> 【0】 Setup Teacher4登录成功! <----------------------\n")
            # 点击移动课堂系统模块
            self.findElementActionClick("//div[@name='layout_container_name']/div[3]/div[3]/div")
            # 点击目录栏开始测评
            #self.findElementClick("//*[@id='4$Menu']/li[1]")
            time.sleep(2)
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

    def isElementExist(self, xpath):
        flag = False
        try:
            locator = (By.XPATH, xpath)
            element = WebDriverWait(browser, 2).until(EC.presence_of_element_located(locator))
            flag = True
        except:
            traceback.print_exc()
        return flag

    def findElementClick(self, locator):
        try:
            element = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, locator)),
                                                      message="获取等待元素失败")
            element.click()
        except:
            traceback.print_exc()
            print("点击" + locator + "元素失败！")

    def findElementActionClick(self, locator):
        try:
            action = ActionChains(browser)
            above = browser.find_element_by_xpath(locator)
            action.move_to_element(above).perform()
            action.click(above).perform()
        except:
            traceback.print_exc()
            print("点击Action元素"+locator+"失败！\n")
    def selectCatagory(self, topicId):
        try:
            # 输入英语词汇U2，点击搜索按钮
            browser.find_element_by_id("keyword").send_keys(topicId)
            browser.find_element_by_xpath("//div[@class='searchWrapper']/a").click()
            time.sleep(0.6)
            # 点击查看详情按钮
            browser.find_element_by_xpath("//span[@class='click-btn']").click()
            # 点击定制测评tab
            browser.find_element_by_xpath("//div[@class='ant-tabs-nav-scroll']/div/div[3]").click()
            time.sleep(1.3)
            # 获取测评专题名称
            topicName = browser.find_element_by_xpath("//span[@class='headerTitle']").text
            # 点击全部选择输入框 ,第一个输入框
            browser.find_element_by_xpath("//input[@type='checkbox'][1]").click()
            # 点击 生成定制测评按钮
            self.findElementActionClick("//div[@class='boxShadow']/button[@type='button']")
            # 清除定制测评默认标题名
            browser.find_element_by_id("evaluationTitle").clear()
            # 重命名标题名
            browser.find_element_by_id("evaluationTitle").send_keys("定制测评_"+topicName)
            # 点击弹窗确定按钮
            self.findElementClick("//div[@class='ant-modal-footer']/button[2]")
            # 获取招生测评连接地址
            imgurl = browser.find_element_by_xpath("//div[@role='tabpanel'][2]/div/div[1]/div[2]/div[3]/div[2]/a/span").text
            # imgurl = browser.find_element_by_xpath("//span[@class='address'][2]").text
            time.sleep(0.6)
            js = 'window.open("' + imgurl + '");'
            browser.execute_script(js)
            time.sleep(3)
            windows = browser.window_handles
            browser.switch_to.window(windows[1])
            print("-------------------> Setup 教学测评复制链接打开新窗口完成 <----------------------\n")
            # 输入姓名
            browser.find_element_by_id("username").send_keys("173测试")
            # 输入手机号
            browser.find_element_by_id("mobile").send_keys("17317495785")
            # 输入验证码
            browser.find_element_by_id("code").send_keys("1111")
            # 点击选择地区下拉框
            # browser.find_element_by_id("address").click()

            # # 点击选择天津（省）
            # browser.find_element_by_xpath("//body/div[4]/div/div/div/ul[1]/li[2]").click()
            # # 选择天津市
            # browser.find_element_by_xpath("//body/div[4]/div/div/div/ul[2]/li[1]").click()
            # # 选择和平区
            # browser.find_element_by_xpath("//body/div[4]/div/div/div/ul[3]/li[1]").click()
            # 点击开始测评登录按钮
            self.findElementActionClick("//button[@type='submit']")
            time.sleep(0.5)
            print("-------------------> Setup 输入学生信息登录到教学测评系统完成 <----------------------\n")
            time.sleep(1.5)
            # 获取学生端token
            stoken = " "
            stokenspr = []
            stoken = browser.execute_script('return window.localStorage.getItem("__ta/task_token");')
            stoken.encode('utf-8')
            # strstoken = str(stoken)
            stokenspr = stoken.split('[\"', 2)
            studenttoken = str(stokenspr[1]).split('\",', 2)
            authorization2 = "Bearer" + " " + str(studenttoken[0])
            # 点击开始测评
            browser.find_element_by_xpath("//*[@id='root']/div/div[3]/div[1]").click()
            print("-------------------> 进入开始测评做题页完成 <----------------------\n")
            list = []
            list.append(authorization2)
            list.append(imgurl)
        except:
            traceback.print_exc()
            print("搜索测评专题，登录测评系统！\n")
        return list


    @BeautifulReport.add_test_img('test_a_customizeEnglishTesting')
    def test_a_customizeEnglishTesting(self):
        ''' 完成英语定制测评 '''
        try:
            time.sleep(2)
            # topicNum = "hA0nZushljCiwjd21387398"
            tipicId = "CERJT006B020101"
            list2 = self.selectCatagory(tipicId)
            print("-------------------> [1]英语定制测评开始 <---------------------\n")
            time.sleep(1)
            # # 随机获取年级数字
            # grade = random.randint(4, 9)
            # divNum = grade-2
            # print("-------------------> 选择英语" + str(grade) + "年级的招生测评<---------------------")
            # # 点击年级，进入测评
            # self.findElementClick("//*[@id='root']/div/div[2]/div/div["+str(divNum)+"]")
            count=0
            elementflag = False
            elementflag = self.isElementExist("//div[@class='task-abstask__footer']/div[1]")
            shareUrl = ""
            #shareUrl = ApiCasePro.getCustomizeEngShareUrl(self, authorization1)
            shareUrl = list2[1]
            topicNum_ = shareUrl.split("chargeExam/", 2)
            # 获取教学测评的 executionId, topicId（使用招生测评的接口获取topicId，questionType）
            executionList = ApiCasePro.getTestingExecutionId(self, list2[0], topicNum_[1])
            #topicId = ApiCasePro.getRecruitTopicId(self, authorization2, str(executionId))
            while(elementflag):
                time.sleep(0.5)
                # 获取去题目序号
                questionText = ""
                questionText = browser.find_element_by_xpath("//div[@class='task-question__container']/div/span").text
                questionTupl = questionText.split('.', 2)
                questionNum = int(questionTupl[0])
                # 获取题目类型
                questionType = ApiCasePro.getCustomizeQuestionType(self, list2[0], str(executionList[1]), str(executionList[0]))
                # 如果是选择题
                if questionType==0:
                    #selectBtnlist = browser.find_elements_by_xpath("//div[@class='task-option']")
                    #selectBtnlist[0].click()
                    self.findElementClick("//div[@class='task-option'][1]")
                    time.sleep(0.3)
                    # 点击下一题按钮
                    self.findElementClick(
                        "//div[@class='task-abstask__footer']/div[1]")
                    time.sleep(0.5)
                elif questionType ==1:  # 如果是填空题
                    inputlist = browser.find_elements_by_xpath("//input[@autocomplete='off']")
                    # time.sleep(1)
                    for i in range(len(inputlist)):
                        inputlist[i].send_keys("are")
                        time.sleep(0.3)
                    # 点击下一题按钮
                    self.findElementClick("//div[@class='task-abstask__footer']/div[1]")
                    time.sleep(0.5)
                elif questionType == 2:
                    break;
                count = count + 1
                print("-------------------> 第" + str(count) + "道题完成<---------------------")
                elementflag = self.isElementExist("//div[@class='task-abstask__footer']/div[1]")
            time.sleep(2)
            name = ""
            name = browser.find_element_by_xpath("//div[@class='task-summary__head']/div[1]").text
            # questionlist =browser.find_elements_by_xpath("//div[@class='task-summary__content']/div[4]/div[2]/span")
            # questionCount_result = len(questionlist)
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("173测试", name, msg="英语定制测评报告学生名字显示不对")
        #self.assertEqual(questionNum, questionCount_result, msg="完成英语招生测评卡题目数量和报告页题目数量不一致！")
        print("-------------------> [1]英语定制测评结束 <---------------------\n")
    @BeautifulReport.add_test_img('test_b_customizeMathTesting')
    def test_b_customizeMathTesting(self):
        ''' 完成数学定制测评 '''
        try:
            time.sleep(2)
            #topicNum = "jsJ7s80scFMCajQS1362991"
            topicId = "CMBST009B512041"
            list3 = self.selectCatagory(topicId)
            print("-------------------> [2]数学定制测评开始 <---------------------\n")
            time.sleep(1)
            count=0
            elementflag = False
            elementflag = self.isElementExist("//div[@class='task-abstask__footer']/div[1]")
            shareUrl = ""
            shareUrl = list3[1]
            topicNum_ = shareUrl.split("chargeExam/", 2)
            # 获取教学测评的 executionId, topicId（使用招生测评的接口获取topicId，questionType）
            executionList = ApiCasePro.getTestingExecutionId(browser, list3[0], topicNum_[1])
            while(elementflag):
                time.sleep(0.5)
                # 获取题目序号
                questionText = ""
                questionText = browser.find_element_by_xpath("//div[@class='task-question__container']/div/span").text
                questionTupl = questionText.split('.', 2)
                questionNum = 0
                questionNum = int(questionTupl[0])
                # 获取题目类型
                questionType = ApiCasePro.getCustomizeQuestionType(self, list3[0], str(executionList[1]), str(executionList[0]))
                # 如果是选择题
                if questionType == 0:
                    # 获取选择项列表
                    #selectBtnlist = browser.find_elements_by_xpath("//div[@class='task-option']")
                    #selectBtnlist[0].click()
                    self.findElementClick("//div[@class='task-option'][1]")
                    time.sleep(0.3)
                    # 点击下一题按钮
                    self.findElementClick(
                        "//div[@class='task-abstask__footer']/div[1]")
                    time.sleep(0.4)
                elif questionType == 1:  # 如果是填空题
                    inputlist = browser.find_elements_by_xpath("//span[@class='mq-root-block mq-empty']")
                    i = 0
                    for i in range(len(inputlist)):
                        # 点击填空题，准备输入内容
                        self.findElementClick("//span[@class='mq-root-block mq-empty'][1]")
                        #inputlist[i].click()
                        time.sleep(0.5)
                        # 输入根号
                        self.findElementClick("//div[@class='gapInput-keypad__keys_wrapper']/div[1]/div/div[1]/div/span[9]")
                        time.sleep(0.3)
                        # 输入数字5
                        self.findElementClick(
                            "//div[@class='gapInput-keypad__keys_wrapper']/div[1]/div/div[2]/span[10]")
                        # 点击空白处 ，关闭数学公式
                        self.findElementActionClick("//div[@class='task-question__container']")
                        time.sleep(0.4)
                    # # 点击空白处 ，关闭数学公式
                    # self.findElementActionClick("//div[@class='task-question__container']")
                    time.sleep(0.4)
                    # 点击下一题按钮
                    self.findElementClick("//div[@class='task-abstask__footer']/div[1]")
                    time.sleep(0.5)
                elif questionType == 2:
                    break;
                count = count + 1
                print("-------------------> 第" + str(count) + "道题完成<---------------------")
                elementflag = self.isElementExist("//div[@class='task-abstask__footer']/div[1]")
            time.sleep(2)
            name = ""
            name = browser.find_element_by_xpath("//div[@class='task-summary__head']/div[1]").text
            questionlist = browser.find_elements_by_xpath("//div[@class='task-summary__content']/div[4]/div[2]/span")
            # questionCount_result = 0
            # questionCount_result = len(questionlist)
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("173测试", name, msg="数学定制测评报告学生名字不对")
        #self.assertEqual(questionNum, questionCount_result, msg="完成数学招生测评卡题目数量和报告页题目数量不一致！")
        print("-------------------> [2]数学定制测评结束 <---------------------\n")

directurl="https://autotestx.learnta.cn"
platf = sys.platform
print("platform:"+platf)
if platf != 'darwin':
    report_dir = "/opt/uitest/report"
    img_path = "/opt/uitest/img"
else:
    report_dir = "./report"
    img_path = "./img"
testsuit = unittest.TestSuite()
#testsuit.addTest(teacherxCustomizeTestingCase_Pro("test_a_customizeEnglishTesting"))
testsuit.addTests(unittest.makeSuite(teacherxCustomizeTestingCase_Pro))
run = BeautifulReport(testsuit)
run.report(filename='TAD2.0正服_定制测评复制链接完成测评', description='TAD2.0正服_定制测评复制链接完成测评测试用例', report_dir=report_dir)