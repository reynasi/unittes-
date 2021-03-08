import time
import traceback
import  unittest

from uitest.shuping.common.Common import Common


class LoginPage:

    # def __init__(self, ):
    #     Page.__init__(self)

    def login(self, browser, teacherUrl, studentUrl, teacherUsername, teacherPassword, studentUsername, studentPassword, searchName, courseCode):
        try:
            browser.implicitly_wait(5)
            browser.get(teacherUrl)
            # browser.set_window_size(750, 750)
            # browser.maximize_window()
            print(u"\nLogin start !")
            # url重定向需要等待时间
            time.sleep(1.5)
            browser.find_element_by_id("username").send_keys(teacherUsername)
            browser.find_element_by_xpath("//input[@placeholder='请输入验证码']").send_keys(teacherPassword)
            # 点击登录按钮
            Common.findElementClick(self, browser, "//button[@type='submit']")
            print("-------------------> 【0】 Setup Teacher4 登录成功! <----------------------\n")
            # 点击学习系统模块
            Common.findElementActionClick(self, browser, "//div[@name='layout_container_name']/div[1]")
            time.sleep(0.5)
            # 搜索课程名称
            browser.find_element_by_id("keyword").send_keys(searchName)
            browser.find_element_by_xpath("//a[@class='searchBtn']").click()
            time.sleep(1)
            # 点击进入课堂
            Common.findElementActionClick(self, browser, "//*[@class='wCardsLayout']/div[1]/div[1]/div/a")
            time.sleep(2.5)
            # 获取窗口句柄
            # windows = browser.window_handles
            window_teacher = browser.window_handles[0]
            #studentUrl = Common.getUrl("TypeUrl", "student4Url")
            js = 'window.open("' + studentUrl + '");'
            browser.execute_script(js)
            time.sleep(0.5)
            window_student = browser.window_handles[1]
            browser.switch_to.window(window_student)
            # 输入用户名、密码 登录
            browser.find_element_by_id("username").send_keys(studentUsername)
            browser.find_element_by_id("password").send_keys(studentPassword)
            # 点击登录按钮
            Common.findElementActionClick(self, browser, "//button[@type='submit']")
            time.sleep(1)
            # 点击进入课堂按钮
            browser.find_element_by_xpath("//button[@type='button']").click()
            # 先点击课程码输入框， 输入课堂码，点击确定按钮，则进入课堂
            browser.find_element_by_xpath("//input[@type='text']").send_keys(courseCode)
            time.sleep(0.5)
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-confirm-btns']/button[2]")
            print("------------------> 【0】Setup 学生登录成功并进入到课堂里 <-------------------\n")
            windows = browser.window_handles

        except Exception as e:
            traceback.print_exc()
            print(e)
        return windows

    def xLoginStudySystem(self, browser, teacherxUrl, studentUrl, teacherUsername, teacherPassword, studentUsername, studentPassword, searchName, courseCode):
        try:
            browser.implicitly_wait(5)
            browser.get(teacherxUrl)
            # browser.set_window_size(850, 750)
            # browser.maximize_window()
            print(u"\nLogin start !")
            # url重定向需要等待时间
            time.sleep(1.5)
            browser.find_element_by_id("username").send_keys(teacherUsername)
            browser.find_element_by_xpath("//input[@placeholder='请输入验证码']").send_keys(teacherPassword)
            # 点击登录按钮
            browser.find_element_by_xpath("//button[@type='submit']").click()
            print("-------------------> 【0】Setup Teacher4 登录成功! <----------------------\n")
            time.sleep(1)
            # 点击教学系统模块
            Common.findElementActionClick(self, browser, "//div[@name='layout_container_name']/div[1]/div[1]/div")
            time.sleep(0.8)
            # 搜索课程名称
            browser.find_element_by_id("keyword").send_keys(searchName)
            Common.findElementClick(self, browser, "//a[@class='searchBtn']")
            time.sleep(0.5)
            # 点击进入课堂  自动化测试课程 英语人教版七年级同步课
            browser.find_element_by_xpath("//div[@class='lessonCardWrap']/a").click()
            time.sleep(4)
            js = 'window.open("' + studentUrl + '");'
            browser.execute_script(js)
            window_student = browser.window_handles[1]
            browser.switch_to.window(window_student)
            time.sleep(1.5)
            # 输入用户名、密码 登录
            browser.find_element_by_id("username").send_keys(studentUsername)
            browser.find_element_by_id("password").send_keys(studentPassword)
            # 点击登录按钮
            browser.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(2)
            # 点击进入课堂按钮 , 自动化测试课程 英语人教版七年级同步课
            Common.findElementActionClick(self, browser, "//button[@type='button']")
            # 先点击课程码输入框， 输入课堂码，点击确定按钮，则进入课堂
            browser.find_element_by_xpath("//input[@type='text']").send_keys(courseCode)
            time.sleep(0.7)
            Common.findElementActionClick(self, browser, "//div[@class='ant-modal-confirm-btns']/button[2]")
            # 点击进入课堂 自动化测试课程 英语人教版七年级同步课
            #self.findElementClick("//div[@class='cardWrapper']/div[1]/div/a")
            print("-------------------> 【0】Setup 学生登录成功并进入到课堂里 <-------------------\n")
            windows = browser.window_handles

        except Exception as e:
            traceback.print_exc()
            print(e)
        return windows

    def teacher4Login(self, browser, teacher4url, teacherUsername, teacherPassword):
        try:
            browser.implicitly_wait(5)
            browser.get(teacher4url)
            # browser.set_window_size(750, 750)
            # browser.maximize_window()
            print(u"\nLogin start !")
            # url重定向需要等待时间
            time.sleep(1.5)
            browser.find_element_by_id("username").send_keys(teacherUsername)
            browser.find_element_by_xpath("//input[@placeholder='请输入验证码']").send_keys(teacherPassword)
            # 点击登录按钮
            Common.findElementClick(self, browser, "//button[@type='submit']")
            time.sleep(1.5)
            print("-------------------> 【0】 Setup Teacher4 登录成功! <----------------------\n")
            # 获取窗口句柄
            # windows = browser.window_handles
            # studentUrl = Common.getUrl("TypeUrl", "student4Url")
            windows = browser.window_handles
        except Exception as e:
            traceback.print_exc()
            print(e)

    def teacherxLogin(self, browser, teacherxurl, teacherUsername, teacherPassword):
        try:
            browser.implicitly_wait(5)
            browser.get(teacherxurl)
            # browser.set_window_size(750, 750)
            # browser.maximize_window()
            print(u"\nLogin start !")
            # url重定向需要等待时间
            time.sleep(1.5)
            browser.find_element_by_id("username").send_keys(teacherUsername)
            browser.find_element_by_xpath("//input[@placeholder='请输入验证码']").send_keys(teacherPassword)
            # 点击登录按钮
            Common.findElementClick(self, browser, "//button[@type='submit']")
            time.sleep(1.5)
            print("-------------------> 【0】 Setup Teacherx 登录成功! <----------------------\n")
            # 获取窗口句柄
            windows = browser.window_handles
            return windows
        except Exception as e:
            traceback.print_exc()
            print(e)

    def taskLogin(self, browser, taskImgUrl, stuName, taskUsername, taskPassword):
        try:
            print("======================= task学生登陆开始 =========================\n")
            js2 = 'window.open("' + taskImgUrl + '");'
            browser.execute_script(js2)
            # 获取新打开页窗口
            window_task = browser.window_handles[1]
            browser.switch_to.window(window_task)
            time.sleep(3)
            # 输入账号、密码、点击登录
            browser.find_element_by_id("username").send_keys(stuName)
            browser.find_element_by_id("mobile").send_keys(taskUsername)
            browser.find_element_by_id("code").send_keys(taskPassword)
            browser.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(1)
            print("======================= task学生登陆结束 =========================\n")
        except Exception as e:
            traceback.print_exc()
            print(e)









