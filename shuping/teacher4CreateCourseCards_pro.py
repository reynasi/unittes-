#coding=utf-8

# @Time    : 2020/3/24
# @Author  : shuping zhao
# @File    : teacher4CreateCourseCards_pro.py

import os
import sys
import traceback
import unittest
import time

from BeautifulReport import BeautifulReport
from selenium import webdriver
from selenium.webdriver import ActionChains

sys.path.append('/opt/')
sys.path.append('/opt/uitest/shuping/common/Common/')
sys.path.append('/opt/uitest/shuping/page/LoginPage/')
from uitest.shuping.page.LoginPage import LoginPage
from uitest.shuping.common.Common import Common

class teacher4CreateCourseCards_pro(unittest.TestCase):
    urlstr = "autotest.learnta.cn"
    orgId = 100040  # 测服是1000369
    def setUp(self):
        global browser
        global windows
        global authorization2
        global authorization1
        try:
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
            # 点击选择备课系统
            Common.findElementActionClick(self, browser, "//div[@name='layout_container_name']/div[2]/div[1]/div")
            time.sleep(1.5)
            # 点击创建课程按钮
            Common.findElementClick(self, browser, "//div[@class='pPageHeaderTitle']/button")
            time.sleep(0.5)
            # 时间
            nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            if self._testMethodName =='test_a_createEnglishCourseCards':
                # 点击选择英语
                Common.findElementClick(self, browser,
                            "//form[@class='ant-form ant-form-horizontal createcourse']/div[1]/div[2]/div/div/label[1]")
                browser.find_element_by_xpath("//input[@placeholder='请输入要创建的课程名称']").send_keys(
                    "每天创建English课程" + nowtime)
            else:
                # 点击选择数学
                Common.findElementClick(self, browser,
                            "//form[@class='ant-form ant-form-horizontal createcourse']/div[1]/div[2]/div/div/label[2]")
                browser.find_element_by_xpath("//input[@placeholder='请输入要创建的课程名称']").send_keys(
                    "每天创建Math课程" + nowtime)
            time.sleep(0.6)
            js = "$('.ant-modal-wrap ').scrollTop(300)"
            browser.execute_script(js)
            time.sleep(0.7)
            Common.findElementAction(self, browser,
                                          "//form[@class='ant-form ant-form-horizontal createcourse']/div[2]/div[2]/div/div/label[3]")
            # 点击选择人教版
            Common.findElementActionClick(self, browser,
                "//form[@class='ant-form ant-form-horizontal createcourse']/div[2]/div[2]/div/div/label[1]")
            # 点击确定按钮
            Common.findElementClick(self, browser, "//div[@class='ant-modal-footer']/button[2]")
        except Exception as e:
            traceback.print_exc()
            print(e)
        # self.assertEqual("173测试学生", stuname, msg="学生不在线")
        # self.assertEqual("主讲人(1)", hostname, msg="教师不在线")

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
    @BeautifulReport.add_test_img('test_a_createEnglishCourseCards')
    def test_a_createEnglishCourseCards(self):
        '''创建英语课程及任务卡'''
        try:
            # 点击请选择年级下拉框
            Common.findElementClick(self, browser, "//span[@class='ant-cascader-picker']/i")
            time.sleep(0.5)
            # 点击选择5年级
            Common.findElementClick(self, browser, "//ul[@class='ant-cascader-menu']/li[5]")
            time.sleep(0.5)
            # 点击选择5年级上
            Common.findElementClick(self, browser, "//li[@title='五年级上']")
            # 点击添加单元按钮
            Common.findElementAction(self, browser, "//div[@class='lDropdownButton ant-dropdown-trigger']/button")
            time.sleep(0.5)
            # 点击新的单元
            browser.find_element_by_link_text("新的单元").click()
            # 点击添加教学点模块按钮
            Common.findElementAction(self, browser, "//div[@class='ant-card-body']/div[2]/button")
            # 点击添加教学点模块下拉框
            #browser.find_element_by_xpath("//div[@class='Course']/div[3]/div/div[3]/div[2]/button").click()
            time.sleep(0.5)
            # 点击选择教学点模块
            browser.find_element_by_link_text("教学点模块").click()
            time.sleep(0.5)
            print("=========================  成功添加教学点模块 =========================\n")
            # 点击选择教学点下拉框
            Common.findElementClick(self, browser, "//div[@class='ant-modal-body']/span")
            time.sleep(3)
            # 点击（更新版）七年级
            Common.findElementClickLongTime(self, browser, "//ul[@class='ant-select-tree']/li[4]/span")
            #browser.find_element_by_xpath("//ul[@class='ant-select-tree']/li[4]/span").click()
            # 点击7A下拉按钮
            Common.findElementClick(self, browser, "//ul[@class='ant-select-tree']/li[4]/ul/li[1]/span")
            # 点击 Starter Units 下拉按钮
            Common.findElementClick(self, browser, "//ul[@class='ant-select-tree']/li[4]/ul/li[1]/ul/li[1]/span")
            # 点选择 选择基础知识下拉按钮
            Common.findElementClick(self, browser,
                                    "//ul[@class='ant-select-tree']/li[4]/ul/li[1]/ul/li[1]/ul/li[1]/span")
            time.sleep(0.5)
            # 点击选择语法结构（可选）
            Common.findElementClick(self, browser,
                                    "//ul[@class='ant-select-tree']/li[4]/ul/li[1]/ul/li[1]/ul/li[1]/ul/li/a/span")
            time.sleep(0.5)
            # 点击 期中测试A 下拉按钮
            Common.findElementClick(self, browser, "//ul[@class='ant-select-tree']/li[4]/ul/li[1]/ul/li[11]/span")
            # 点击选择听力（可选）知识点
            Common.findElementClick(self, browser,
                                    "//ul[@class='ant-select-tree']/li[4]/ul/li[1]/ul/li[11]/ul/li[1]/a/span")
            # 点击选择阅读（可选）知识点
            Common.findElementClick(self, browser,
                                    "//ul[@class='ant-select-tree']/li[4]/ul/li[1]/ul/li[11]/ul/li[3]/a/span")
            # 点击确定按钮
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-footer']/button[2]")
            time.sleep(0.7)
            # 点击添加任务卡按钮
            Common.findElementActionClick(self, browser, "//div[@class='lCourseUnitStep']/div/div[last()]/div/div")
            time.sleep(0.5)
            # 点击选择解析卡
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]")
            time.sleep(0.5)
            browser.find_element_by_id("taskName").send_keys("测试解析卡1")
            # 获取第一个视频选择按钮列表
            classWrepperList = browser.find_elements_by_xpath("//div[@class='classWrepper']/div[1]/div/button[2]")
            classWrepperList[0].click()
            time.sleep(0.7)
            js0 = 'document.getElementsByTagName("main")[0].scroll(0,1200)'
            browser.execute_script(js0)
            time.sleep(0.5)
            # 点击创建解析卡按钮
            Common.findElementActionClick(self, browser, "//button[@type='submit']")
            time.sleep(1.5)
            # 点击添加任务卡按钮
            Common.findElementActionClick(self, browser, "//div[@class='lCourseUnitStep']/div/div[last()]/div/div")
            time.sleep(0.6)
            # 点击选择智能练习卡
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[5]")
            time.sleep(0.7)
            browser.find_element_by_id("taskName").clear()
            browser.find_element_by_id("taskName").send_keys("测试智能练习卡")
            time.sleep(0.5)
            # 点击选择创建智能练习卡按钮
            Common.findElementActionClick(self, browser, "//button[@type='submit']")
            time.sleep(1)
            js0 = 'document.getElementsByTagName("main")[0].scroll(0,400)'
            browser.execute_script(js0)
            time.sleep(0.6)
            # 继续点击添加任务卡按钮
            Common.findElementActionClick(self, browser, "//div[@class='lCourseUnitStep']/div/div[last()]/div/div")
            time.sleep(0.5)
            # 点击选择主观题卡
            Common.findElementClick(self, browser, "//div[@class='ant-modal-body']/div/div[last()]")
            time.sleep(0.5)
            #  搜索题目ID：789833
            browser.find_element_by_xpath("//input[@placeholder='搜索知识点关键词、题目ID或题目关键词']").send_keys("789833")
            # 点击搜索按钮
            Common.findElementActionClick(self, browser, "//span[@class='ant-input-suffix']")
            time.sleep(3)
            # 点击选择第一个输入框按钮
            Common.findElementActionClick(self, browser, "//thead[@class='ant-table-thead']/tr/th[1]")
            # 点击确定按钮
            Common.findElementActionClick(self, browser, "//div[@class='stepWrap']/div[2]/div[2]/button")
            time.sleep(0.6)
            js = 'document.getElementsByTagName("main")[0].scroll(0,700)'
            browser.execute_script(js)
            # 继续点击教学点模块， 添加富文本卡
            Common.findElementActionClick(self, browser, "//div[@class='ant-card lCourseUnit']/div[3]/div[2]/button")
            time.sleep(0.5)
            browser.find_element_by_link_text("教学活动").click()
            # 点击教学活动的添加任务卡按钮
            Common.findElementActionClick(self, browser, "//div[@class='courseUnitSteps']/div[4]/div/div/div/div/div")
            # 点击选择富文本卡
            Common.findElementActionClick(self, browser, "//div[@class='lTaskCardTypes clearfix']/div/a")
            time.sleep(0.5)
            # 输入富文本卡名字，及内容
            browser.find_element_by_id("taskName").send_keys("富文本卡1")
            time.sleep(0.5)
            inputList = browser.find_elements_by_xpath("//div[@role='presentation']")
            inputList[0].send_keys("富文本卡备注。")
            time.sleep(0.5)
            inputList[1].send_keys("富文本卡任务描述。。")
            #browser.find_element_by_id("contentintroduction").send_keys("富文本卡备注。")
            #browser.find_element_by_id("contenttaskData").send_keys("富文本卡任务描述。。")
            time.sleep(0.5)
            js2 = 'document.getElementsByTagName("main")[0].scroll(0,700)'
            browser.execute_script(js2)
            time.sleep(0.5)
            # 点击提交按钮,创建富文本卡按钮
            Common.findElementActionClick(self, browser, "//button[@type='submit']")
            time.sleep(2)
            elements = browser.find_elements_by_xpath("//div[@class='mlt-show']")
            elementlists = []
            for i in range(len(elements)):
                if elements[i].text != "" and elements[i].text != "添加任务卡":
                    elementlists.append(elements[i].text)
            print(elementlists)

            cardsList = browser.find_elements_by_xpath("//div[@class='lDropWrap taskDropWrap visiableOnHover']/div/div/div")
            #cardsList = browser.find_elements_by_link_text("预览")
            for i in range(len(cardsList)):
                cardFlag = False
                if i<7:
                    time.sleep(1)
                    js = 'document.getElementsByTagName("main")[0].scroll(0, 110)'
                    browser.execute_script(js)
                    #Common.findElementAction(self, browser, "//span[@class='headerTitle']")
                    Common.findElementActionClick(self, browser, "//div[@class='courseUnitSteps']/div[1]/div/div/div["+str(i+1)+"]")
                elif i==7:
                    time.sleep(1.8)
                    js1 = 'document.getElementsByTagName("main")[0].scroll(0, 110)'
                    browser.execute_script(js1)
                    Common.findElementActionClick(self, browser, "//div[@class='courseUnitSteps']/div[1]/div/div/div["+str(i+1)+"]")
                elif i==8:
                    time.sleep(1)
                    js2= 'document.getElementsByTagName("main")[0].scroll(0, 300)'
                    browser.execute_script(js2)
                    Common.findElementActionClick(self, browser,
                        "//div[@class='courseUnitSteps']/div[2]/div/div/div[1]")
                elif i>8 and i<=10:
                    time.sleep(1)
                    js3 = 'document.getElementsByTagName("main")[0].scroll(0, 300)'
                    browser.execute_script(js3)
                    Common.findElementActionClick(self, browser,
                        "//div[@class='courseUnitSteps']/div[3]/div/div/div["+str(i-8)+"]")
                elif i>10:
                    time.sleep(1.5)
                    js4 = 'document.getElementsByTagName("main")[0].scroll(0, 600)'
                    browser.execute_script(js4)
                    Common.findElementActionClick(self, browser,
                        "//div[@class='courseUnitSteps']/div[4]/div/div/div[1]")
                time.sleep(0.6)
                temp = browser.find_element_by_id("taskName").get_attribute("value")
                if temp == elementlists[i]:
                    cardFlag = True
                    print("第" + str(i + 1) + "张任务卡名字和编辑页面任务卡名字相同！")
                else:
                    print("第"+str(i+1)+"张任务卡名字和编辑页面任务卡名字不一致！")
                    break
                browser.find_element_by_xpath("//div[@class='pPageHeader']/a").click()
                time.sleep(0.7)
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual(True, cardFlag, msg="课程中任务卡名称显示不对！")
        # self.assertEqual(student_count, teacher_rightCount, msg="完成练习卡失败！")
        print("-------------------> 【1 End】 成功创建英语课程及任务卡<----------------------\n")

    #@unittest.skip("暂不执行")
    @BeautifulReport.add_test_img('test_b_createMathCourseCards')
    def test_b_createMathCourseCards(self):
        '''创建数学课程及任务卡'''
        try:
            # 点击请选择年级下拉框
            Common.findElementClick(self, browser, "//span[@class='ant-cascader-picker']/i")
            time.sleep(0.5)
            # 点击选择4年级
            Common.findElementClick(self, browser, "//li[@title='四年级']")
            time.sleep(0.5)
            # 点击选4年级上
            Common.findElementClick(self, browser, "//li[@title='四年级上']")
            # 点击添加单元按钮
            Common.findElementAction(self, browser, "//div[@class='lDropdownButton ant-dropdown-trigger']/button")
            time.sleep(0.5)
            # 点击新的单元
            browser.find_element_by_link_text("新的单元").click()
            # 点击添加教学点模块按钮
            Common.findElementAction(self, browser, "//div[@class='ant-card-body']/div[2]/button")
            # 点击添加教学点模块下拉框
            # browser.find_element_by_xpath("//div[@class='Course']/div[3]/div/div[3]/div[2]/button").click()
            time.sleep(0.5)
            # 点击选择教学点模块
            browser.find_element_by_link_text("教学点模块").click()
            time.sleep(0.5)
            print("=========================  成功添加教学点模块 =========================\n")
            # 点击选择教学点下拉框
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/span")
            time.sleep(3)
            # 点击八年级下册（更新版）
            Common.findElementClickLongTime(self, browser, "//ul[@class='ant-select-tree']/li[4]/span")
            time.sleep(0.4)
            # 点击7A下拉按钮
            Common.findElementClick(self, browser, "//ul[@class='ant-select-tree']/li[4]/ul/li[1]/span")
            time.sleep(0.4)
            # 点击 第十六章 二次根式 下拉按钮
            Common.findElementClick(self, browser, "//ul[@class='ant-select-tree']/li[4]/ul/li[1]/ul/li[1]/span")
            time.sleep(0.4)
            # 点击二次根式（可选）
            Common.findElementClick(self, browser,
                "//ul[@class='ant-select-tree']/li[4]/ul/li[1]/ul/li[1]/ul/li/a/span")
            time.sleep(0.4)
            # 点击确定按钮
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-footer']/button[2]")
            time.sleep(0.6)
            # 点击添加任务卡按钮
            Common.findElementActionClick(self, browser, "//div[@class='lCourseUnitStep']/div/div[last()]/div/div")
            time.sleep(0.5)
            # 点击选择解析卡
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[2]")
            time.sleep(0.5)
            browser.find_element_by_id("taskName").send_keys("测试解析卡1")
            # 获取第一个视频选择按钮列表
            classWrepperList = browser.find_elements_by_xpath("//div[@class='classWrepper']/div[1]/div/button[2]")
            classWrepperList[0].click()
            time.sleep(0.7)
            js0 = 'document.getElementsByTagName("main")[0].scroll(0,1300)'
            browser.execute_script(js0)
            time.sleep(0.5)
            # 点击创建解析卡按钮
            Common.findElementActionClick(self, browser, "//button[@type='submit']")
            time.sleep(1.2)
            # 点击添加任务卡按钮
            Common.findElementActionClick(self, browser, "//div[@class='lCourseUnitStep']/div/div[last()]/div/div")
            time.sleep(0.7)
            # 点击选择智能练习卡
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[5]")
            time.sleep(0.7)
            browser.find_element_by_id("taskName").clear()
            browser.find_element_by_id("taskName").send_keys("测试智能练习卡")
            time.sleep(0.6)
            # 点击选择创建智能练习卡按钮
            Common.findElementActionClick(self, browser, "//button[@type='submit']")
            time.sleep(1.2)
            # 继续点击添加任务卡按钮
            Common.findElementActionClick(self, browser, "//div[@class='lCourseUnitStep']/div/div[last()]/div/div")
            time.sleep(0.5)
            # 点击选择主观题卡
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-body']/div/div[last()]")
            time.sleep(0.5)
            #  搜索题目ID：789833
            browser.find_element_by_xpath("//input[@placeholder='搜索知识点关键词、题目ID或题目关键词']").send_keys("856980")
            # 点击搜索按钮
            Common.findElementActionClick(self, browser, "//span[@class='ant-input-suffix']")
            time.sleep(3.5)
            # 点击选择第一个输入框按钮
            Common.findElementActionClick(self, browser, "//thead[@class='ant-table-thead']/tr/th[1]")
            # 点击确定按钮
            Common.findElementActionClick(self, browser, "//div[@class='stepWrap']/div[2]/div[2]/button")
            time.sleep(0.6)
            js = 'document.getElementsByTagName("main")[0].scroll(0,800)'
            browser.execute_script(js)
            time.sleep(0.6)
            # 继续点击教学点模块， 添加富文本卡
            Common.findElementActionClick(self, browser, "//div[@class='ant-card lCourseUnit']/div[3]/div[2]/button")
            time.sleep(0.5)
            browser.find_element_by_link_text("教学活动").click()
            time.sleep(0.7)
            # 点击教学活动的添加任务卡按钮
            Common.findElementActionClick(self, browser, "//div[@class='courseUnitSteps']/div[2]/div/div/div/div/div")
            # 点击选择富文本卡
            Common.findElementActionClick(self, browser, "//div[@class='lTaskCardTypes clearfix']/div/a")
            time.sleep(0.5)
            # 输入富文本卡名字，及内容
            browser.find_element_by_id("taskName").send_keys("富文本卡1")
            time.sleep(0.5)
            inputList = browser.find_elements_by_xpath("//div[@role='presentation']")
            inputList[0].send_keys("富文本卡备注。")
            time.sleep(0.5)
            inputList[1].send_keys("富文本卡任务描述。。")
            # browser.find_element_by_id("contentintroduction").send_keys("富文本卡备注。")
            # browser.find_element_by_id("contenttaskData").send_keys("富文本卡任务描述。。")
            time.sleep(0.5)
            js2 = 'document.getElementsByTagName("main")[0].scroll(0,700)'
            browser.execute_script(js2)
            time.sleep(0.5)
            # 点击提交按钮,创建富文本卡按钮
            Common.findElementActionClick(self, browser, "//button[@type='submit']")
            time.sleep(2)

            elements = browser.find_elements_by_xpath("//div[@class='mlt-show']")
            elementlists = []
            for i in range(len(elements)):
                if elements[i].text != "" and elements[i].text != "添加任务卡":
                    elementlists.append(elements[i].text)
            print(elementlists)
            cardsList = browser.find_elements_by_xpath("//div[@class='lDropWrap taskDropWrap visiableOnHover']")
            for i in range(len(cardsList)):
                cardFlag = False
                if i < 7:
                    time.sleep(1)
                    # js3 = 'document.getElementsByTagName("main")[0].scroll(0, 300)'
                    # browser.execute_script(js3)
                    Common.findElementActionClick(self, browser,
                                        "//div[@class='courseUnitSteps']/div[1]/div/div/div[" + str(i+1) + "]")
                elif i ==7:
                    time.sleep(1.8)
                    js3 = 'document.getElementsByTagName("main")[0].scroll(0, 200)'
                    browser.execute_script(js3)
                    time.sleep(0.3)
                    Common.findElementActionClick(self, browser,
                                        "//div[@class='courseUnitSteps']/div[1]/div/div/div[" + str(i + 1) + "]")
                elif i == 8:
                    time.sleep(1.8)
                    js3 = 'document.getElementsByTagName("main")[0].scroll(0, 400)'
                    browser.execute_script(js3)
                    time.sleep(0.3)
                    Common.findElementActionClick(self, browser,
                                                "//div[@class='courseUnitSteps']/div[2]/div/div/div[1]")
                time.sleep(0.7)
                temp = browser.find_element_by_id("taskName").get_attribute("value")
                if temp == elementlists[i]:
                    cardFlag = True
                    print("第" + str(i + 1) + "张任务卡名字和编辑页面任务卡名字相同！")
                else:
                    print("第" + str(i + 1) + "张任务卡名字和编辑页面任务卡名字不一致！")
                    break
                browser.find_element_by_xpath("//div[@class='pPageHeader']/a").click()
                time.sleep(0.7)
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual(True, cardFlag, msg="课程中任务卡名称显示不对！")
        print("-------------------> 【2 End】 成功创建数学课程及任务卡<----------------------\n")

directList = Common.getDirectPath(Common)
report_dir = directList[0]
img_path = directList[1]

testsuit = unittest.TestSuite()
#testsuit.addTest(teacher4CreateCourseCards_pro("test_a_createEnglishCourseCards"))
testsuit.addTests(unittest.makeSuite(teacher4CreateCourseCards_pro))
run = BeautifulReport(testsuit)
run.report(filename='TAD1.0正服_创建课程及任务卡', description='TAD1.0正服_创建课程及任务卡', report_dir=report_dir)
#run.report(filename='正服上课发非测评卡测试报告', description='正服上课发各种非测评任务卡测试用例', report_dir=os.path.abspath(r'./report'))