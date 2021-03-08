#coding=utf-8

# @Time    : 2020/1/12
# @Author  : shuping zhao
# @File    : TAD1IndexPageConfig_t1.py
import os
import platform
import sys
import time
import traceback
import unittest
from typing import List

from selenium import webdriver
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from BeautifulReport import BeautifulReport
from selenium.webdriver.support import expected_conditions as EC


class TAD1IndexPageConfig_t1(unittest.TestCase):
    def setUp(self):
        try:
            global driver
            # linux1路径
            #path = "/usr/local/python3/chromedriver"
            # linux2路径
            #path = os.path.dirname(os.path.abspath('./config/chromedriver/chromedriver'))
            url = "https://learnta.t1.learnta.cn/os/login"

            # linux使用的静默执行方法
            options = webdriver.ChromeOptions()
            # options.add_argument('--headless')
            # options.add_argument('--disable-gpu')
            # options.add_argument('--no-sandbox')

            # 设置打开浏览器不显示data; 加载本地浏览器数据，加载很慢放弃！
            #options.add_argument('--user-data-dir=/Users/shuping/Library/Application Support/Google/Chrome/Default')
            # linux配置
            #driver = webdriver.Chrome(executable_path=path, chrome_options=options)
            # 服务器上写法
            driver = webdriver.Chrome(options=options)

            driver.implicitly_wait(10)
            driver.get(url)
            driver.maximize_window()

            print(u"\nLogin start !")
            driver.find_element_by_xpath("//span[@class='ant-select-arrow']").click()
            driver.find_element_by_xpath("//ul[@role='listbox']/li[1]").click()
            driver.find_element_by_id("username").send_keys("18817572035")
            #driver.find_element_by_id("code").send_keys("1111")
            driver.find_element_by_xpath("//div[@id='code']/input").send_keys("1111")
            #点击登录按钮
            driver.find_element_by_xpath("//button[@type='submit']").click()
            print("Login Success!")
        except :
            traceback.print_exc()
            print("登录失败")

    def tearDown(self):
        try:
            driver.close()
            driver.quit()
        except:
            print("close fail")


    def click(self, loc):
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located(By.XPATH, loc))
            return True
        except:
            print(u'元素点击失败！')
            #self.saveScreenShot_error('元素点击失败')
            return False

    def save_img(self, img_name):  # 错误截图方法，这个必须先定义好
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        # mac存放图片路径
        driver.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))  # os.path.abspath(r"G:\Test_Project\img")截图存放路径
        # mac存放图片路径
        #driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"/Users/shuping/.jenkins/workspace/autotest/img"), img_name))  # os.path.abspath(r"G:\Test_Project\img")截图存放路径
        # linux存放图片路径        driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"/img"), img_name))  # os.path.abspath(r"G:\Test_Project\img")截图存放路径

    # 判断元素是否存在的方法
    def isElementExist(self, element):
        flag = True
        try:
            # locator2 = (By.XPATH, element)
            # WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator2))
            driver.implicitly_wait(5)
            if driver.find_element_by_xpath(element):
                return flag
        except:
            flag = False
            return flag

    def isElementExistclass(self, element):
        flag = True
        try:
            if driver.find_element_by_class_name(element):
                return flag
        except:
            flag = False
            return flag

        # 获取元素后点击
    def findElementClick(self, locator):
        try:
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, locator)),
                                                      message="获取等待元素失败")
            element.click()
        except:
            traceback.print_exc()
            print("点击元素"+locator+"失败！")

    def findElementGetText(self, locator):
        try:
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, locator)),
                                                      message="获取等待元素失败")
            divtext = element.text
        except:
            traceback.print_exc()
            print("获取元素"+locator+"text失败！")
        return divtext

    def findElementActionClick(self, locator):
        try:
            action = ActionChains(driver)
            above = driver.find_element_by_xpath(locator)
            action.move_to_element(above).perform()
            action.click(above).perform()
        except:
            traceback.print_exc()
            print("点击Action元素"+locator+"失败！\n")

    def getElementNum(self, xpath):
        elements = driver.find_elements_by_xpath(xpath)
        lists = []
        for num in elements:
            if num.text!= "":
                temp = num.text
                lists.append(temp)
        truelist = lists[0].splitlines()
        ElementNum = len(lists)
        return lists

    # 上传背景图片保存到本地
    @BeautifulReport.add_test_img('test_a_testSetBackground')
    def test_a_testSetBackground(self):
        '''进入教师端选择布局背景图片'''
        try:
            time.sleep(1)
            print("-------------------> 【1 Start】选择布局背景图片<----------------------\n")
            # 点击自定义按钮
            self.findElementActionClick("//*[@id='root']/div/div/div[1]/a/div")
            time.sleep(1)
            # 点击选择背景
            self.findElementActionClick("//div[@name='editor_header_container']/div[2]/div/div")
            time.sleep(1)
            imgbak = ""
            imgbak = driver.find_element_by_xpath("//div[@class='ant-modal-body']/div[2]/div[3]/div/div").get_attribute(
                "style")
            temp = imgbak.split("(\"")[1]
            imgsrc = ""
            imgsrc = temp.split("\")")[0]
            print("获取要选择的背景图片imgsrc:" + imgsrc)
            # 点击选择第二个背景图片
            self.findElementActionClick("//div[@class='ant-modal-body']/div[2]/div[3]/div/div")
            # 点击确定按钮，保存背景图片
            self.findElementActionClick("//div[@role='document']/div[2]/div[@class='ant-modal-footer']/div/button")
            time.sleep(1)
            # 点击保存按钮
            self.findElementActionClick("//div[@id='root']/div/div[3]/button[2]")

            # 获取页面的button列表
            #buttonlist = driver.find_elements_by_xpath("//button[@type='button']/span")
            # if len(buttonlist) != 1:
            #     for j in range(len(buttonlist)):
            #         if buttonlist[j].text == "保存":
            #             self.findElementActionClick("//div[@id='root']/div/div[3]/button[1]")
            # else:
            #     driver.find_element_by_xpath("//div[@id='root']/div/div[3]/button[1]").click()
            print("保存成功，进入到教师端产品包主页面")
            # 点击选择产品包
            self.findElementActionClick("//div[@id='root']/div/header/div[1]/div/div/p")

            time.sleep(1)
            # 获取设置背景后的背景图片链接
            imgbak = ""
            # 获取产品包列表的第一个产品包的背景图片
            imgbak = driver.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[1]/div[1]").get_attribute("style")
            temp = imgbak.split("(\"")[1]
            backimg = ""
            backimg = temp.split("\")")[0]
            print("成功获取添加背景图片后的图片backimg:" + backimg)
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual(imgsrc, backimg, msg="选择背景图片保存失败！")
        print("-------------------> 【1 End】选择背景图片并保存成功<----------------------\n")

    # 选择产品包后保存
    @BeautifulReport.add_test_img('test_b_testReplaceProductPackage')
    def test_b_testReplaceProductPackage(self):
        '''替换产品包使用'''
        try:
            print("-------------------> 【2 Start】替换产品包<----------------------\n")
            time.sleep(1)
            # 点击选择产品包
            self.findElementActionClick("//div[@id='root']/div/header/div[1]/div/div/p")
            classcard1 = "index-pkg_card"
            selectPackName = ""
            aftersysname = ""
            # 获取产品包列表

            packagelist = driver.find_elements_by_xpath("//div[@class='ant-modal-body']/div/div")
            for i in range(len(packagelist)):
                num = str(i+1)
                packclassname = driver.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[" + num + "]").get_attribute("class")
                if "_selected" not in packclassname:
                    # 获取自定义系统包名
                    selectPackName=driver.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[" + num + "]/div[2]/p").text
                    # 点击第一个没有被选中的系统
                    self.findElementActionClick("//div[@class='ant-modal-body']/div/div[" + num + "]")
                    #点击保存按钮
                    self.findElementActionClick("//div[@class='ant-modal-footer']/div/button")
                    break;
            knowbtn = self.isElementExist("//div[@class='ant-modal-body']/div/div[2]/button/span")
            if knowbtn==True:
                knowButton = driver.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button/span").text
                if knowButton == "知道了":
                    self.save_img("test_b_replaceProductPackage")
                    print("-------------------->替换产品包失败，报错\"未找到产品包!\"<----------------------")
            else:
                aftersysname = driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[@name='layout_container_name']/p").text
                time.sleep(1)
                #syslist = self.getElementNum("//p[@class='common_card_title']")
                layoutlist = self.getElementNum("//*[@id='root']/div/div/div/div/*[@name='layout_container_name']/div/div[*]/div[*]/div/div/p")
                # 获取系统模块可点击列表
                #clicklist = driver.find_elements_by_xpath("//*[@id='root']/div/div/div/*[@name='layout_container_name']/div[*]/div[*]/div")
                columnlist = driver.find_elements_by_xpath("//*[@id='root']/div/div/div/div/*[@name='layout_container_name']/div/div[*]")
                flag = False
                count = 0
                for i in range(len(columnlist)):
                    columnNum = str(i+1)
                    rowlist = driver.find_elements_by_xpath(
                        "//*[@id='root']/div/div/div/div/*[@name='layout_container_name']/div/div["+columnNum+"]/div[*]")
                    for j in range(len(rowlist)):
                        rowNum = str(j+1)
                        elementText = layoutlist[count]
                        count = count + 1
                        strcount = str(count)
                        self.findElementActionClick("//*[@id='root']/div/div/div/div/*[@name='layout_container_name']/div/div["+columnNum+"]/div["+rowNum+"]/div")
                        time.sleep(4.5)
                        # 获取左侧边栏的第一排文字
                        titlename = self.findElementGetText("//div[@class='subSystemDropDown']/div[2]/span")

                        if titlename == elementText:
                            print("-------------------->添加第"+strcount +"个系统模块和进入的系统名称一致！<----------------------")
                            # 点击logo返回主页面
                            self.findElementActionClick("//header/h1/img")
                            flag = True
                            time.sleep(1)
                        else:
                            flag = False
                            print("-------------------->添加第" + strcount + "个系统模块和进入的系统名称不一致！<----------------------")
                            # 点击logo返回主页面
                            self.findElementActionClick("//header/h1/img")
                            time.sleep(1)
        except Exception as e:
            traceback.print_exc()
            print(e)
        #self.assertEqual(selectPackName, aftersysname , msg="选择要保存的产品包名保存失败！")
        self.assertEqual(True, flag, msg="验证保存的产品包中系统不都能正常访问！")
        print("-------------------> 【2 End】成功替换产品包<----------------------\n")

    @BeautifulReport.add_test_img('test_c_testDeleteProductPackage')
    def test_c_testDeleteProductPackage(self):
        '''删除产品包'''
        try:
            time.sleep(1)
            print("-------------------> 【3 Start】开始删除产品包<----------------------\n")
            # 点击选择产品包
            self.findElementActionClick("//div[@id='root']/div/header/div[1]/div/div/p")
            classcard1 = "index-pkg_card"
            time.sleep(0.5)
            # 获取产品包列表
            beforepackagelist = driver.find_elements_by_xpath("//div[@class='ant-modal-body']/div/div")
            delbefore=0
            delbefore = len(beforepackagelist)
            for i in range(len(beforepackagelist)):
                num = str(i + 1)
                deleteclassname = driver.find_element_by_xpath(
                    "//div[@class='ant-modal-body']/div/div[" + num + "]/div[3]").get_attribute("class")
                if "index-has_delete" not in deleteclassname:
                    # 点击第一个有...删除按钮
                    self.findElementActionClick("//div[@class='ant-modal-body']/div/div[" + num + "]/div[3]/div")
                    # 点击第一个有删除按钮进行删除
                    self.findElementActionClick("//div[@class='ant-modal-body']/div/div[" + num + "]/div[3]/div/div")
                    # 点击弹窗的确认按钮
                    self.findElementActionClick("//div[@class='ant-modal-body']/div/div[2]/button[2]")
                    break
            time.sleep(1)
            afterpackagelist = driver.find_elements_by_xpath("//div[@class='ant-modal-body']/div/div")
            aftercount = 0
            temp = len(afterpackagelist)
            aftercount = temp+1
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual(delbefore, aftercount, msg="删除产品包失败！")
        print("-------------------> 【3 End】删除产品包成功<----------------------\n")

    @BeautifulReport.add_test_img('test_d_testAddLayout1')
    def test_d_testAddLayout1(self):
        '''进入TAD系统配置第1个自定义产品包'''
        try:
            print("-------------------> 【4 Start】开始配置第1个自定义产品包<----------------------\n")
            classstr = "index-icon"
            qstr = "index-icon-"
            classnamestr = qstr.__contains__(classstr)
            # 点击自定义按钮
            self.findElementActionClick("//*[@id='root']/div/div/div[1]/a/div")
            time.sleep(0.5)
            # 点击第1个布局
            self.findElementActionClick("//div[@name='editor_header_container']/div[1]/div[1]/div")
            # 点击编辑自定义包名
            self.findElementActionClick("//div[@name='layout_container_name']/div[1]/*[name()='svg'][1]")
            # 先清空文本框内容
            driver.find_element_by_xpath("//input[@type='text']").clear()
            # 输入自定义包名称
            driver.find_element_by_xpath("//input[@type='text']").send_keys("自动化测试自定义系统包1")
            # 点击确认图片b保存按钮
            self.findElementActionClick("//div[@name='layout_container_name']/span/span/div/*[name()='svg'][1]")

            # 获取添加的系统模块列表,如果有一句添加的系统模块先执行删除
            #beforedellist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div[2]/div[*]/div[*]/div/div/div/div/img")
            beforedellist = driver.find_elements_by_tag_name("img")
            #beforedellist = driver.find_elements_by_xpath("//p[@class='common_card_title']")
            if len(beforedellist)!=0:
                # 获取删除按钮列表
                # 获取总列数的删除按钮元素
                rowlist = driver.find_elements_by_xpath(
                    "//div[@name='layout_container_name']/div[2]/div")
                for i in range(len(rowlist)):
                    rowNum= str(i+1)
                    arrowlist = driver.find_elements_by_xpath(
                        "//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div")
                    #modulelist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div[*]/div[*]/div/*[name()='svg'][1]")
                    for j in range(len(arrowlist)):
                        arrowNum = str(j + 1)
                        imgFlag = self.isElementExist("//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div["+arrowNum+"]/div/div")
                        if imgFlag == True:
                            # 开始点击删除按钮
                            self.findElementActionClick(
                                "//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div["+arrowNum+"]/div/*[name()='svg'][1]")
                            print("-------------------> 已删除第 " + rowNum + " 列,第 " + arrowNum + " 行的系统模块 <----------------------\n")
                        #time.sleep(0.5)
            afterdellist = driver.find_elements_by_tag_name("img")
            #afterdellist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div[2]/div[*]/div[*]/div/div/div/div/img")
            if len(afterdellist)==0:
                print("-------------------> 成功删除已有的系统模块！ <----------------------\n")
            else:
                print("-------------------> 删除已有的系统模块失败! <----------------------\n")
            # 要添加系统模块列表
            layout_modulelist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div[2]/div[*]/div[*]")
            count_module = len(layout_modulelist)
            # 获取模块列数
            rowlist = driver.find_elements_by_xpath(
                "//div[@name='layout_container_name']/div[2]/div")
            for i in range(len(rowlist)):
                rowNum = str(i + 1)
                arrowlist = driver.find_elements_by_xpath(
                    "//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div")
                # modulelist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div[*]/div[*]/div/*[name()='svg'][1]")
                for j in range(len(arrowlist)):
                    arrowNum = str(j + 1)
                    # 点击弹窗中布局模块的第一个添加按钮
                    self.findElementClick("//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div["+arrowNum+"]/div/*[name()='svg'][1]")
                    time.sleep(0.5)
                    # 点击弹窗的第一个模块
                    cardname =""
                    cardname = driver.find_element_by_xpath("//div[@class='ant-modal-body']/div[1]/div/p").text
                    self.findElementActionClick("//div[@class='ant-modal-body']/div[1]/div")
                    time.sleep(0.5)
                    # 获取当前布局中的第i+1个名称
                    modename = ""
                    modename = driver.find_element_by_xpath(
                        "//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div["+arrowNum+"]/div/div/div/p").text
                    if cardname == modename:
                        print("-------------------> 已添加第 " + rowNum + " 列,第 " + arrowNum + " 行个系统模块 <----------------------\n")
                        continue;
                    else:
                        print("第1个布局中的第 " + rowNum + " 列,第 " + arrowNum + " 行模块中添加的模块名称不一致")
                        break;
            # 获取页面的button列表
            buttonlist = driver.find_elements_by_xpath("//button[@type='button']/span")
            if len(buttonlist)!=1:
                for k in range(len(buttonlist)):
                    if buttonlist[k].text == "保 存":
                        self.findElementActionClick("//div[@id='root']/div/div[3]/button[2]")
                        print("===================== 点击保存为产品包保存成功 ========================")
                        break;
            else:
                self.findElementActionClick("//div[@id='root']/div/div[3]/button[2]")
            time.sleep(1)
            # 获取主页面的系统包列表
            saved_modulelist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div/div[*]/div")
            saved_module_count = len(saved_modulelist)
            systemname = ""
            if count_module == saved_module_count:
                systemname = self.findElementGetText("//*[@id='root']/div/div[1]/div/div/div[@name='layout_container_name']/p")
            else:
                print("显示的模块数量和创建时不一致！\n")
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("自动化测试自定义系统包1", systemname, msg="第一个布局保存到本地失败！")
        print("-------------------> 【4 End】第1个产品包成功保存到本地<----------------------\n")

    @BeautifulReport.add_test_img('test_e_testAddLayout5')
    def test_e_testAddLayout5(self):
        '''进入TAD系统配置第5个自定义产品包'''
        try:
            print("-------------------> 【5 Start】开始配置第5个自定义产品包<----------------------\n")
            classstr = "index-icon"
            qstr = "index-icon-"
            classnamestr = qstr.__contains__(classstr)
            # 点击自定义按钮
            self.findElementActionClick("//*[@id='root']/div/div/div[1]/a/div")
            time.sleep(0.5)
            # 点击第5个布局
            self.findElementActionClick("//div[@name='editor_header_container']/div[1]/div[8]/div")
            # 点击编辑自定义包名
            self.findElementActionClick("//div[@name='layout_container_name']/div[1]/*[name()='svg'][1]")
            # 先清空文本框内容
            driver.find_element_by_xpath("//input[@type='text']").clear()
            # 输入自定义包名称
            driver.find_element_by_xpath("//input[@type='text']").send_keys("自动化测试自定义系统包5")
            # 点击确认图片b保存按钮
            self.findElementActionClick("//div[@name='layout_container_name']/span/span/div/*[name()='svg'][1]")

            # 获取添加的系统模块列表,如果有一句添加的系统模块先执行删除
            #beforedellist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div[2]/div[*]/div[*]/div/div/div/div/img")
            beforedellist = driver.find_elements_by_tag_name("img")
            #beforedellist = driver.find_elements_by_xpath("//p[@class='common_card_title']")
            if len(beforedellist)!=0:
                # 获取删除按钮列表
                # 获取总列数的删除按钮元素
                rowlist = driver.find_elements_by_xpath(
                    "//div[@name='layout_container_name']/div[2]/div")
                for i in range(len(rowlist)):
                    rowNum= str(i+1)
                    arrowlist = driver.find_elements_by_xpath(
                        "//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div")
                    #modulelist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div[*]/div[*]/div/*[name()='svg'][1]")
                    for j in range(len(arrowlist)):
                        arrowNum = str(j + 1)
                        imgFlag = self.isElementExist("//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div["+arrowNum+"]/div/div")
                        if imgFlag == True:
                            # 开始点击删除按钮
                            self.findElementActionClick(
                                "//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div["+arrowNum+"]/div/*[name()='svg'][1]")
                            print("-------------------> 已删除第 " + rowNum + " 列,第 " + arrowNum + " 行的系统模块 <----------------------\n")
                        #time.sleep(0.5)
            afterdellist = driver.find_elements_by_tag_name("img")
            #afterdellist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div[2]/div[*]/div[*]/div/div/div/div/img")
            if len(afterdellist)==0:
                print("-------------------> 成功删除已有的系统模块！ <----------------------\n")
            else:
                print("-------------------> 删除已有的系统模块失败! <----------------------\n")
            # 要添加系统模块列表
            layout_modulelist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div[2]/div[*]/div[*]")
            count_module = len(layout_modulelist)
            # 获取模块列数
            rowlist = driver.find_elements_by_xpath(
                "//div[@name='layout_container_name']/div[2]/div")
            for i in range(len(rowlist)):
                rowNum = str(i + 1)
                arrowlist = driver.find_elements_by_xpath(
                    "//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div")
                # modulelist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div[*]/div[*]/div/*[name()='svg'][1]")
                for j in range(len(arrowlist)):
                    arrowNum = str(j + 1)
                    # 点击弹窗中布局模块的第一个添加按钮
                    self.findElementClick("//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div["+arrowNum+"]/div/*[name()='svg'][1]")
                    time.sleep(0.5)
                    # 点击弹窗的第一个模块
                    cardname =""
                    cardname = driver.find_element_by_xpath("//div[@class='ant-modal-body']/div[1]/div/p").text
                    self.findElementActionClick("//div[@class='ant-modal-body']/div[1]/div")
                    time.sleep(0.5)
                    # 获取当前布局中的第i+1个名称
                    modename = ""
                    modename = driver.find_element_by_xpath(
                        "//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div["+arrowNum+"]/div/div/div/p").text
                    if cardname == modename:
                        print("-------------------> 已添加第 " + rowNum + " 列,第 " + arrowNum + " 行个系统模块 <----------------------\n")
                        continue;
                    else:
                        print("第1个布局中的第 " + rowNum + " 列,第 " + arrowNum + " 行模块中添加的模块名称不一致")
                        break;

            # 获取页面的button列表
            buttonlist = driver.find_elements_by_xpath("//button[@type='button']/span")
            if len(buttonlist)!=1:
                for k in range(len(buttonlist)):
                    if buttonlist[k].text == "保 存":
                        self.findElementActionClick("//div[@id='root']/div/div[3]/button[2]")
                        print("===================== 点击保存为产品包保存成功 ========================")
                        break;
            else:
                self.findElementActionClick("//div[@id='root']/div/div[3]/button[2]")
            time.sleep(1)
            # 获取主页面的系统包列表
            saved_modulelist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div/div[*]/div")
            saved_module_count = len(saved_modulelist)
            systemname = " "
            if count_module == saved_module_count:
                systemname = self.findElementGetText(
                    "//*[@id='root']/div/div[1]/div/div/div[@name='layout_container_name']/p")
                #systemname = driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div/p").text
            else:
                print("显示的模块数量和创建时不一致！\n")
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("自动化测试自定义系统包5", systemname, msg="第5个布局保存到本地失败！")
        # self.assertEqual("True", flag, msg="添加系统模块和进入系统左侧边栏不一致！")
        print("-------------------> 【5 End】第5个产品包成功保存到本地<----------------------\n")

    @BeautifulReport.add_test_img('test_f_testAddLayout8')
    def test_f_testAddLayout8(self):
        '''进入TAD系统配置第8个自定义产品包'''
        try:
            print("-------------------> 【6 Start】开始配置第8个自定义产品包<----------------------\n")
            classstr = "index-icon"
            qstr = "index-icon-"
            classnamestr = qstr.__contains__(classstr)
            # 点击自定义按钮
            self.findElementActionClick("//*[@id='root']/div/div/div[1]/a/div")
            time.sleep(0.5)
            # 点击第8个布局
            self.findElementActionClick("//div[@name='editor_header_container']/div[1]/div[8]/div")
            # 点击编辑自定义包名
            self.findElementActionClick("//div[@name='layout_container_name']/div[1]/*[name()='svg'][1]")
            # 先清空文本框内容
            driver.find_element_by_xpath("//input[@type='text']").clear()
            # 输入自定义包名称
            driver.find_element_by_xpath("//input[@type='text']").send_keys("自动化测试自定义系统包8")
            # 点击确认图片b保存按钮
            self.findElementActionClick("//div[@name='layout_container_name']/span/span/div/*[name()='svg'][1]")

            # 获取添加的系统模块列表,如果有一句添加的系统模块先执行删除
            #beforedellist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div[2]/div[*]/div[*]/div/div/div/div/img")
            beforedellist = driver.find_elements_by_tag_name("img")
            #beforedellist = driver.find_elements_by_xpath("//p[@class='common_card_title']")
            if len(beforedellist)!=0:
                # 获取删除按钮列表
                # 获取总列数的删除按钮元素
                rowlist = driver.find_elements_by_xpath(
                    "//div[@name='layout_container_name']/div[2]/div")
                for i in range(len(rowlist)):
                    rowNum= str(i+1)
                    arrowlist = driver.find_elements_by_xpath(
                        "//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div")
                    #modulelist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div[*]/div[*]/div/*[name()='svg'][1]")
                    for j in range(len(arrowlist)):
                        arrowNum = str(j + 1)
                        imgFlag = self.isElementExist("//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div["+arrowNum+"]/div/div")
                        if imgFlag == True:
                            # 开始点击删除按钮
                            self.findElementActionClick(
                                "//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div["+arrowNum+"]/div/*[name()='svg'][1]")
                            print("-------------------> 已删除第 " + rowNum + " 列,第 " + arrowNum + " 行的系统模块 <----------------------\n")
                        #time.sleep(0.5)
            afterdellist = driver.find_elements_by_tag_name("img")
            #afterdellist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div[2]/div[*]/div[*]/div/div/div/div/img")
            if len(afterdellist)==0:
                print("-------------------> 成功删除已有的系统模块！ <----------------------\n")
            else:
                print("-------------------> 删除已有的系统模块失败! <----------------------\n")
            # 要添加系统模块列表
            layout_modulelist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div[2]/div[*]/div[*]")
            count_module = len(layout_modulelist)
            # 获取模块列数
            rowlist = driver.find_elements_by_xpath(
                "//div[@name='layout_container_name']/div[2]/div")
            for i in range(len(rowlist)):
                rowNum = str(i + 1)
                arrowlist = driver.find_elements_by_xpath(
                    "//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div")
                for j in range(len(arrowlist)):
                    arrowNum = str(j + 1)
                    # 点击弹窗中布局模块的第一个添加按钮
                    self.findElementClick("//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div["+arrowNum+"]/div/*[name()='svg'][1]")
                    time.sleep(0.5)
                    # 点击弹窗的第一个模块
                    cardname =""
                    cardname = driver.find_element_by_xpath("//div[@class='ant-modal-body']/div[1]/div/p").text
                    self.findElementActionClick("//div[@class='ant-modal-body']/div[1]/div")
                    time.sleep(0.5)
                    # 获取当前布局中的第i+1个名称
                    modename = ""
                    modename = driver.find_element_by_xpath(
                        "//div[@name='layout_container_name']/div[2]/div[" + rowNum + "]/div["+arrowNum+"]/div/div/div/p").text
                    if cardname == modename:
                        print("-------------------> 已添加第 " + rowNum + " 列,第 " + arrowNum + " 行个系统模块 <----------------------\n")
                        continue;
                    else:
                        print("第1个布局中的第 " + rowNum + " 列,第 " + arrowNum + " 行模块中添加的模块名称不一致")
                        break;

            # 获取页面的button列表
            buttonlist = driver.find_elements_by_xpath("//button[@type='button']/span")
            if len(buttonlist)!=1:
                for k in range(len(buttonlist)):
                    if buttonlist[k].text == "保 存":
                        self.findElementActionClick("//div[@id='root']/div/div[3]/button[2]")
                        print("===================== 点击保存为产品包保存成功 ========================")
                        break;
            else:
                self.findElementActionClick("//div[@id='root']/div/div[3]/button[2]")
            time.sleep(1)
            # 获取主页面的系统包列表
            saved_modulelist = driver.find_elements_by_xpath("//div[@name='layout_container_name']/div/div[*]/div")
            saved_module_count = len(saved_modulelist)
            systemname = " "
            if count_module == saved_module_count:
                systemname = self.findElementGetText(
                    "//*[@id='root']/div/div[1]/div/div/div[@name='layout_container_name']/p")
                #systemname = driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div/p").text
            else:
                print("显示的模块数量和创建时不一致！\n")
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual("自动化测试自定义系统包8", systemname, msg="第8个布局保存到本地失败！")
        # self.assertEqual("True", flag, msg="添加系统模块和进入系统左侧边栏不一致！")
        print("-------------------> 【6 End】第8个产品包成功保存到本地<----------------------\n")


#if __name__ == '__main__':
#unittest.main()

platf = sys.platform
print("platform:"+platf)
if platf != 'darwin':
    report_dir = "/opt/uitest/report"
    img_path = "/opt/uitest/img"
else:
    report_dir = "./report"
    img_path = "./img"

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

testsuite = unittest.TestSuite()
#testsuite.addTest(TAD1IndexPageConfig_t1("test_b_testReplaceProductPackage"))
testsuite.addTests(unittest.makeSuite(TAD1IndexPageConfig_t1))

run = BeautifulReport(testsuite)
# Mac 存放路径
run.report(filename='TAD教学系统首页配置产品包自动化测试.html', description='TAD教学系统首页配置产品包测试用例', report_dir=report_dir)

