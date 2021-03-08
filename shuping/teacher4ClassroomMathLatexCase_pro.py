#coding=utf-8

# @Time    : 2020/2/16
# @Author  : shuping zhao
# @File    : teacher4ClassroomMathLatexCase_pro.py
import sys
import time
import traceback
import unittest

from BeautifulReport import BeautifulReport
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class teacher4ClassroomMathLatexCase_pro(unittest.TestCase):

    def setUp(self):
        global browser
        global windows
        global urlstr
        global orgId
        urlstr = "autotest.learnta.cn"
        orgId = 100040  # 测服是1000369
        try:
            # linux1路径
            #path = "/usr/local/python3/chromedriver"
            #path = os.path.dirname(os.path.abspath('./config/chromedriver/chromedriver'))
            url = directurl + "/teacher4"
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
            # mac、linux配置
            #browser = webdriver.Chrome(executable_path=path, options=options)
            # 服务器上写法
            browser = webdriver.Chrome(options=options)

            #driver = webdriver.Chrome(executable_path=path)
            browser.implicitly_wait(10)
            browser.get(url)
            #browser.set_window_size(750, 750)
            #browser.maximize_window()
            print(u"\nLogin start !")
            # url重定向需要等待时间
            time.sleep(1.5)
            browser.find_element_by_id("username").send_keys("18817572035")
            browser.find_element_by_xpath("//input[@placeholder='请输入验证码']").send_keys("1111")
            #点击登录按钮
            self.findElementClick("//button[@type='submit']")
            print("-------------------> 【0】 Setup Teacher4 登录成功! <----------------------\n")
            time.sleep(1)
            # 点击学习系统模块
            self.findElementClick("//div[@name='layout_container_name']/div[1]/div[1]/div")
            time.sleep(0.5)
            # 搜索课程名称
            browser.find_element_by_id("keyword").send_keys("自动化测试数学课程数学公式")
            browser.find_element_by_xpath("//a[@class='searchBtn']").click()
            time.sleep(1)
            # 点击课程进入课堂
            self.findElementActionClick("//div[@class='wCardsLayout']/div/div[1]/div[@class='lessonCardWrap']")
            time.sleep(3)
            studentUrl = directurl + "/student4/login"
            js = 'window.open("' + studentUrl + '");'
            browser.execute_script(js)
            windows = browser.window_handles
            browser.switch_to.window(windows[1])
            # 输入用户名、密码 登录
            browser.find_element_by_id("username").send_keys("17317495785")
            browser.find_element_by_id("password").send_keys("495785")
            # 点击登录按钮
            browser.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(2)
            # 输入课程码进入课堂
            browser.find_element_by_xpath("//button[@type='button']").click()
            # 输入课堂码，点击确定按钮 ，则进入课堂
            browser.find_element_by_xpath("//input[@type='text']").send_keys("172539")
            self.findElementActionClick("//div[@class='ant-modal-confirm-btns']/button[2]")
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

    def findElementActionClick(self, locator):
        try:
            action = ActionChains(browser)
            above = browser.find_element_by_xpath(locator)
            action.move_to_element(above).perform()
            action.click(above).perform()
        except:
            traceback.print_exc()
            print("点击Action元素"+locator+"失败！\n")

#   #获取元素后点击
    def findElementClick(self, locator):
        try:
            element = WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.XPATH, locator)), message="获取等待元素失败")
            element.click()
        except:
            traceback.print_exc()
            print("点击" + locator + "元素失败！")

    def isElementExist(self, xpath):
        flag = True
        try:
            locator = (By.XPATH, xpath)
            element = WebDriverWait(browser, 3).until(EC.presence_of_element_located(locator))
            return flag
        except:
            flag = False
            return flag
            traceback.print_exc()

    @BeautifulReport.add_test_img('test_a_assiginMathLatexCard_pro')
    def test_a_assiginMathLatexCard_pro(self):
        '''老师和学生都进入课堂学生完成所有数学公式练习卡'''
        try:
            time.sleep(1)
            # 切换到教师端窗口
            browser.switch_to.window(windows[0])
            print("-------------------> 【Start】 老师开始发送练习卡<----------------------\n")
            # 点击 Text_Lesson 1模块
            self.findElementActionClick("//div[@class='cardsSelectors']/p[4]")
            js = "$('.classroomCardSubContainer').scrollTop(700)"
            browser.execute_script(js)
            time.sleep(0.5)
            # 获取练习卡的最后一个任务状态
            buttonflag = self.isElementExist("//div[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[3]/div[1]")
            print("=========================buttonflag:"+str(buttonflag)+"=======================")
            if buttonflag == True:
                # 点击更多按钮
                print("=========================准备点击更多按钮=======================")
                self.findElementActionClick("//div[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]")
                print("=========================点击更多按钮完成，准备点击删除按钮=======================")
                # 点击删除按钮
                self.findElementActionClick("//div[@id='cardsContainer']/div[1]/div[2]/div/div[last()]/div[1]/div/div/div[1]")
                print("=========================点击删除按钮完成，准备点击确定按钮=======================")
                time.sleep(0.5)
                # 点击确定按钮
                self.findElementActionClick("//*[@class='ant-confirm-btns']/button[2]")
                print("=========================点击确定按钮完成，准备点击分配任务按钮=======================")
                time.sleep(1)
                # 点击分配任务按钮
                self.findElementActionClick("//div[@id='cardsContainer']/div[1]/div[1]/div[3]")
                print("=========================点击分配任务按钮完成=======================")
                # element = browser.find_element_by_css_selector('div[class*="loadingWhiteBox"]')
                # browser.execute_script("arguments[0].click();", element)
            elif buttonflag == False:
                time.sleep(0.5)
                # 点击分配任务按钮
                self.findElementActionClick("//div[@id='cardsContainer']/div[1]/div[1]/div[3]")
            # 弹窗出来有延时
            time.sleep(1)
            # 点击选择题目框第一个勾选框按钮
            self.findElementActionClick("//div[@class='assignHeader']/label/span/input")
            print("=========================老师选择完题目=======================")
            time.sleep(1)
            # 点击确定按钮
            self.findElementActionClick("//div[@class='footerSubmit fixFooter']/button[@type='button']")
            print("-------------------> 老师成功分配练习卡 <----------------------\n")
            # 转到学生端窗口
            browser.switch_to.window(windows[1])
            # 发卡后学生端倒计时5s
            time.sleep(6)
            # 先判断有没有录屏安装弹窗   。。。
            butbool = self.isElementExist("//div[@class='ant-modal-body']/div/div[2]/button")
            if (butbool):
                # 点击录屏安装弹窗
                self.findElementActionClick("//div[@class='ant-modal-body']/div/div[2]/button")
                #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
            time.sleep(0.5)
            Cname = " "
            cardname = " "
            Cname = browser.find_element_by_xpath("//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
            if Cname != "单元1-三角形的概念及表示方法_1.1 认识三角形__数学公式题目练习卡":
                browser.refresh()
                time.sleep(2)
                # 先判断有没有录屏安装弹窗   。。。
                butbool = self.isElementExist("//div[@class='ant-modal-body']/div/div[2]/button")
                if (butbool):
                    # 点击录屏安装弹窗
                    self.findElementActionClick("//div[@class='ant-modal-body']/div/div[2]/button")
                    #browser.find_element_by_xpath("//div[@class='ant-modal-body']/div/div[2]/button").click()
                print("-------------------> 学生未收到数学公式练习卡，重新刷新页面收到卡！刷新页面前cardname=" + Cname + " <----------------------\n")
                # 获取学生端最终收到的任务卡名字
                cardname = browser.find_element_by_xpath(
                    "//div[@class='pClassroom isStudent started Pcard']/div[1]/h2").text
                print("-------------------> 学生收到数学公式练习卡，cardname=" + cardname + "<----------------------\n")
            else:
                cardname = Cname
                print("-------------------> 学生收到数学公式练习卡，cardname=" + cardname + "<----------------------\n")

            inputlist = browser.find_elements_by_xpath("//div[@class='gapInput-mathinput gapInput-mathinput_empty']")
            for i in range(len(inputlist)):
                # 点击第一个未填写的填空题，准备输入内容
                self.findElementClick("//div[@class='gapInput-mathinput gapInput-mathinput_empty'][1]")
                time.sleep(0.5)
                if i == 0:   # 输入根号3
                    # 输入公式根号
                    self.findElementClick("//span[@data-value='\sqrt']")
                    time.sleep(0.3)
                    # 输入数字3
                    self.findElementClick("//span[@data-value='3']")
                    # 点击空白处 ，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 1:  # 输入x的平方
                    # 输入公式
                    self.findElementClick("//span[@data-value='x']")
                    time.sleep(0.3)
                    # 输入平方2
                    self.findElementClick("//span[@data-value='^2']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 2:  # 输入C2
                    # 点击abc键盘
                    self.findElementClick("//span[@data-value='letter']")
                    time.sleep(0.3)
                    # 点击shift键
                    self.findElementClick("//span[@data-value='shift']")
                    # 点击c键
                    self.findElementClick("//span[@data-value='c']")
                    # 点击num键
                    self.findElementClick("//span[@data-value='num']")
                    # 点击_键
                    self.findElementClick("//span[@data-value='_']")
                    # 点击2键
                    self.findElementClick("//span[@data-value='2']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 3:   # 输入x分之y
                    # 输入公式
                    self.findElementClick("//span[@data-value='\\frac']")  # /f需要转义
                    time.sleep(0.3)
                    # 点击输入y
                    self.findElementClick("//span[@data-value='y']")
                    time.sleep(0.3)
                    # 点击分母位置
                    self.findElementClick("//*[@class='task-html']/div[1]/span[last()]/div/div/span[2]/span/span[2]")
                    # 点击输入x
                    self.findElementClick("//span[@data-value='x']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 4:   # 输入根号9开3次方
                    # 输入公式
                    self.findElementClick("//span[@data-value='\\nthroot']")
                    time.sleep(0.3)
                    # 输入数字3
                    self.findElementClick("//span[@data-value='3']")
                    self.findElementClick("//span[@data-value='Right']")
                    self.findElementClick("//span[@data-value='9']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 5:   # 输入|y|
                    # 输入公式
                    self.findElementClick("//span[@data-value='|']")
                    time.sleep(0.3)
                    # 输入y
                    self.findElementClick("//span[@data-value='y']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 6:  # 输入a.x
                    # 输入公式
                    self.findElementClick("//span[@data-value='a']")
                    time.sleep(0.3)
                    # 输入数字5
                    self.findElementClick("//span[@data-value='\cdot']")
                    time.sleep(0.3)
                    self.findElementClick("//span[@data-value='x']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 7: # 输入 0<y<=6
                    # 输入0
                    self.findElementClick("//span[@data-value='0']")
                    time.sleep(0.3)
                    # 输入<
                    self.findElementClick("//span[@data-value='<']")
                    # 输入y
                    self.findElementClick("//span[@data-value='y']")
                    # 输入<=
                    self.findElementClick("//span[@data-value='\leq']")
                    # 输入数字6
                    self.findElementClick("//span[@data-value='6']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 8:  # 输入 x>y>=6
                    # 输入x
                    self.findElementClick("//span[@data-value='x']")
                    time.sleep(0.3)
                    # 输入>
                    self.findElementClick("//span[@data-value='>']")
                    # 输入y
                    self.findElementClick("//span[@data-value='y']")
                    # 输入>=
                    self.findElementClick("//span[@data-value='\geq']")
                    # 输入数字6
                    self.findElementClick("//span[@data-value='6']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 9:  # 输入 (a!=x)
                    # 输入(
                    self.findElementClick("//span[@data-value='(']")
                    time.sleep(0.3)
                    # 输入a
                    self.findElementClick("//span[@data-value='a']")
                    # 输入不=
                    self.findElementClick("//span[@data-value='\\neq']")
                    # 输入x
                    self.findElementClick("//span[@data-value='x']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 10:   # 输入 [a=pi]
                    # 滚动左边区域
                    js = "$('.gapInput-keypad__math__keys').scrollTop(400)"
                    browser.execute_script(js)
                    # 输入(
                    self.findElementClick("//span[@data-value='[']")
                    time.sleep(0.3)
                    # 输入a
                    self.findElementClick("//span[@data-value='a']")
                    # 输入=
                    self.findElementClick("//span[@data-value='=']")
                    # 输入pi
                    self.findElementClick("//span[@data-value='\pi']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 11:   # 输入 100%
                    # 输入1
                    self.findElementClick("//span[@data-value='1']")
                    time.sleep(0.3)
                    # 输入0
                    self.findElementClick("//span[@data-value='0']")
                    # 输入0
                    self.findElementClick("//span[@data-value='0']")
                    # 输入%
                    self.findElementClick("//span[@data-value='%']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 12:   # 输入 a:x
                    # 输入a
                    self.findElementClick("//span[@data-value='a']")
                    time.sleep(0.3)
                    # 输入x
                    self.findElementClick("//span[@data-value='x']")
                    # 左移一次光标
                    self.findElementClick("//span[@data-value='Left']")
                    # 滚动左边区域
                    js = "$('.gapInput-keypad__math__keys').scrollTop(100)"
                    browser.execute_script(js)
                    # 输入:
                    self.findElementClick("//span[@data-value=':']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 13:   # 输入 {且或非}
                    # 滚动左边区域
                    js = "$('.gapInput-keypad__math__keys').scrollTop(150)"
                    browser.execute_script(js)
                    # 输入a
                    self.findElementClick("//span[@data-value='{']")
                    time.sleep(0.3)
                    # 输入且
                    self.findElementClick("//span[@data-value='且']")
                    # 输入或
                    self.findElementClick("//span[@data-value='或']")
                    # 输入非
                    self.findElementClick("//span[@data-value='非']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 14:   # 输入 sin a
                    # 滚动左边公式区域
                    js = "$('.gapInput-keypad__math__keys').scrollTop(400)"
                    browser.execute_script(js)
                    # 输入
                    self.findElementClick("//span[@data-value='\sin']")
                    time.sleep(0.3)
                    # 滚动左边公式区域
                    js = "$('.gapInput-keypad__math__keys').scrollTop(0)"
                    browser.execute_script(js)
                    # 输入a
                    self.findElementClick("//span[@data-value='a']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 15:   # 输入 cos a
                    # 滚动左边公式区域
                    js = "$('.gapInput-keypad__math__keys').scrollTop(400)"
                    browser.execute_script(js)
                    # 输入cot
                    self.findElementClick("//span[@data-value='\cos']")
                    time.sleep(0.3)
                    # 滚动左边公式区域
                    js = "$('.gapInput-keypad__math__keys').scrollTop(0)"
                    browser.execute_script(js)
                    # 输入a
                    self.findElementClick("//span[@data-value='a']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 16:   # 输入 cot a
                    # 滚动左边公式区域
                    js = "$('.gapInput-keypad__math__keys').scrollTop(300)"
                    browser.execute_script(js)
                    # 输入tan
                    self.findElementClick("//span[@data-value='\cot']")
                    time.sleep(0.3)
                    # 滚动左边公式区域
                    js = "$('.gapInput-keypad__math__keys').scrollTop(0)"
                    browser.execute_script(js)
                    # 输入a
                    self.findElementClick("//span[@data-value='a']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 17:   # 输入 tan a
                    # 滚动左边公式区域
                    js = "$('.gapInput-keypad__math__keys').scrollTop(300)"
                    browser.execute_script(js)
                    # 输入tan
                    self.findElementClick("//span[@data-value='\\tan']")
                    time.sleep(0.3)
                    # 滚动左边公式区域
                    js = "$('.gapInput-keypad__math__keys').scrollTop(0)"
                    browser.execute_script(js)
                    # 输入a
                    self.findElementClick("//span[@data-value='a']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 18:   # 输入 lg2
                    # 滚动左边公式区域
                    js = "$('.gapInput-keypad__math__keys').scrollTop(400)"
                    browser.execute_script(js)
                    # 输入lg
                    self.findElementClick("//span[@data-value='\lg\left(\\right)']")
                    time.sleep(0.3)
                    # 输入Left
                    self.findElementClick("//span[@data-value='Left']")
                    # 输入2
                    self.findElementClick("//span[@data-value='2']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 19:   # 输入 lne
                    # 滚动左边公式区域
                    js = "$('.gapInput-keypad__math__keys').scrollTop(400)"
                    browser.execute_script(js)
                    # 输入ln
                    self.findElementClick("//span[@data-value='\ln\left(\\right)']")
                    time.sleep(0.3)
                    # 输入Left
                    self.findElementClick("//span[@data-value='Left']")
                    # 输入letter
                    self.findElementClick("//span[@data-value='letter']")
                    # 输入e
                    self.findElementClick("//span[@data-value='e']")
                    # 点击返回数字键盘
                    self.findElementClick("//span[@data-value='num']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 20:   # 输入 log2(8)
                    js = "$('.gapInput-keypad__math__keys').scrollTop(400)"
                    browser.execute_script(js)
                    # 输入log
                    self.findElementClick("//span[@data-value='\log_{}\left(\\right)']")
                    time.sleep(0.3)
                    # 输入Left
                    self.findElementClick("//span[@data-value='Left']")
                    # 输入 8
                    self.findElementClick("//span[@data-value='8']")
                    # 输入3次左移
                    self.findElementClick("//span[@data-value='Left']")
                    # 输入2次左移
                    self.findElementClick("//span[@data-value='Left']")
                    # 输入1次左移
                    self.findElementClick("//span[@data-value='Left']")
                    # 输入e
                    self.findElementClick("//span[@data-value='2']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 21:   # 输入 角A
                    # 滚动左边公式区域
                    js = "$('.gapInput-keypad__math__keys').scrollTop(400)"
                    browser.execute_script(js)
                    # 输入角
                    self.findElementClick("//span[@data-value='∠']")
                    time.sleep(0.3)
                    # 输入letter
                    self.findElementClick("//span[@data-value='letter']")
                    # 输入shift
                    self.findElementClick("//span[@data-value='shift']")
                    # 输入A
                    self.findElementClick("//span[@data-value='a']")
                    # 点击返回数字键盘
                    self.findElementClick("//span[@data-value='num']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)
                elif i == 22:   # 输入 60度
                    # 输入6
                    self.findElementClick("//span[@data-value='6']")
                    time.sleep(0.3)
                    # 输入0
                    self.findElementClick("//span[@data-value='0']")
                    # 滚动左边公式区域
                    js = "$('.gapInput-keypad__math__keys').scrollTop(400)"
                    browser.execute_script(js)
                    # 输入度
                    self.findElementClick("//span[@data-value='^{\circ}']")
                    # 点击空白处，关闭数学公式
                    self.findElementActionClick("//div[@class='xantd pheads flexContainer']")
                    time.sleep(0.4)

                print("-------------------> 第" + str(i + 1) + "道题完成<---------------------")

            # 点击提交按钮
            self.findElementActionClick("//div[@class='task-abstask__btn_next task-abstask__btn']")
            time.sleep(0.7)
            # 点击提交的弹窗确定按钮
            self.findElementActionClick("//div[@class='ant-modal-body']/div/div[2]/button[2]")
            time.sleep(1.5)
            #self.save_img("test_a_assiginMathLatexCard")
            browser.switch_to.window(windows[0])
            time.sleep(1)
            completeStatus = ""
            completeStatus = browser.find_element_by_xpath("//tbody[@class='ant-table-tbody']/tr[1]/td[2]").text
            time.sleep(1)
            browser.switch_to.window(windows[1])
            # 正确总数
            correctcount = 0
            correctlist = browser.find_elements_by_xpath("//div[@class='task-gap__answer task-gap__answer_correct']")
            correctcount = len(correctlist)
        except Exception as e:
            traceback.print_exc()
            print(e)
        self.assertEqual(23, correctcount, "输入的答案没有完全判对")
        self.assertEqual("已完成", completeStatus, msg="完成数学公式练习卡失败！")
        self.assertEqual("单元1-三角形的概念及表示方法_1.1 认识三角形__数学公式题目练习卡", cardname, msg="学生端收到任务卡名称不对！")
        print("-------------------> 【End】 学生成功完成数学公式练习卡<----------------------\n")


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
#testsuit.addTest(teacher4ClassroomMathLatexCase_pro("test_a_assiginMathLatexCard_pro"))
testsuit.addTests(unittest.makeSuite(teacher4ClassroomMathLatexCase_pro))
run = BeautifulReport(testsuit)
# 服务器存储路径
run.report(filename='TAD1.0正服_学生端上课完成所有数学公式练习卡', description='TAD1.0正服_学生端上课完成所有数学公式练习卡测试用例', report_dir=report_dir)
