"""本代码只针对域名中含有kupei的正服system"""
import platform
from selenium import webdriver
from time import sleep
from BeautifulReport import BeautifulReport
import socket
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import traceback
# import json
# import requests
import unittest

# 引入自定义的模块
# 获取IP
# 获取计算机名称
hostname = socket.gethostname()
# 获取本机IP
ip = socket.gethostbyname(hostname)
phone = 15021201246
phone1 = 18616215375
code = 1111

# 根据系统环境判断需要读取的目录路径
if (platform.system() == 'Windows'):
    print(platform.system())
    report_dir = 'C:\\python1\\day06'
    filename = "C:\\python1\\day05"
    print(report_dir)
    print(filename)
elif (platform.system() == 'Linux'):
    report_dir = "/opt/uitest/report"
    filename = '/opt/uitest/img'
    print(report_dir)
    print(filename)
    print(platform.system())
else:
    print(platform.system())


def is_fail():
    result = "false"
    return result


def is_element_exist(driver, xpath, prompt="err_message"):
    """
根据xpath判断元素是否存在，显示等待5秒
    :param driver:
    :param xpath: 元素xpath路径
    :param prompt: 报错信息,默认:err_message
    """
    result = 'true'
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
    except:
        result = 'false'
        traceback.print_exc()
    finally:
        return result


class LogIn(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.quit()

    def save_img(self, imgName):
        # figname 是一个全路径
        # 截图文件需要保持在当前的img的文件夹下
        # filename = os.path.dirname(__file__) + "/img/"
        # 截图并保保存在指定的路径下，文件名imgname+.png
        self.driver.get_screenshot_as_file(".png".format(filename, imgName))



    def is_element_exist(driver, xpath, prompt="err_message"):
        """
    根据xpath判断元素是否存在，显示等待5秒
        :param driver:
        :param xpath: 元素xpath路径
        :param prompt: 报错信息,默认:err_message
        """

        result = 'true'
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
        except:
            result = 'false'
            traceback.print_exc()
        finally:
            return result




    @BeautifulReport.add_test_img('test_dms_login')
    def test_dms_login(self):
        """DMS登录"""
        driver =self.driver
        self.driver.get('https://www.kupeiai.cn/dms')
        self.driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        self.driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button').click()
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/section/aside/div/div[2]/ul')
        self.assertEqual(result, 'true', msg="DMS登陆失败")
        if result == 'false':
            is_fail()

    @BeautifulReport.add_test_img('test_dms_refresh')
    def test_dms_refresh(self):
        """DMS刷新"""
        driver=self.driver
        self.driver.get('https://www.kupeiai.cn/dms')
        self.driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        self.driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button').click()
        sleep(3)
        try:
            driver.refresh()
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver, '//*[@id="root"]/section/aside/div/div[2]/ul')
        self.assertEqual(result, 'true', msg="刷新失败")
        if result == 'false':
            is_fail()


    @BeautifulReport.add_test_img('test_dealer_login')
    def test_dealer_login(self):
        """Dealer登录"""
        driver = self.driver
        self.driver.get('https://www.kupeiai.cn/dealer')
        self.driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        self.driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button').click()
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/section/aside/div/div[2]/ul')
        self.assertEqual(result, 'true', msg="DMS登陆失败")
        if result == 'false':
            is_fail()


    @BeautifulReport.add_test_img('test_dealer_refresh')
    def test_dealer_refresh(self):
        """Dealer刷新"""
        driver = self.driver
        self.driver.get('https://www.kupeiai.cn/dealer')
        self.driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        self.driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button').click()
        sleep(3)
        try:
            driver.refresh()
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver, '//*[@id="root"]/section/aside/div/div[2]/ul')
        self.assertEqual(result, 'true', msg="刷新失败")
        if result == 'false':
            is_fail()

    @BeautifulReport.add_test_img('test_partners_login')
    def test_partners_login(self):
        """Partners登录"""
        driver = self.driver
        self.driver.get('https://partners.kupeiai.com/signin')
        self.driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        self.driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div')
        self.assertEqual(result, 'true', msg="DMS登陆失败")
        if result == 'false':
            is_fail()


    @BeautifulReport.add_test_img('test_partners_refresh')
    def test_partners_refresh(self):
        """Partners刷新"""
        driver = self.driver
        self.driver.get('https://partners.kupeiai.com/signin')
        self.driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        self.driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            driver.refresh()
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div')
        self.assertEqual(result, 'true', msg="刷新失败")
        if result == 'false':
            is_fail()


    @BeautifulReport.add_test_img('test_bd_login')
    def test_bd_login(self):
        """BD登录"""
        driver = self.driver
        self.driver.get('https://bd.kupeiai.com/signin')
        self.driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        self.driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[3]/p[1]/div/div/div/video')
        self.assertEqual(result, 'true', msg="登陆失败")
        if result == 'false':
            is_fail()



    @BeautifulReport.add_test_img('test_bd_refresh')
    def test_bd_refresh(self):
        """BD刷新"""
        driver = self.driver
        self.driver.get('https://bd.kupeiai.com/signin')
        self.driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        self.driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            driver.refresh()
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[3]/p[1]/div/div/div/video')
        self.assertEqual(result, 'true', msg="刷新失败")
        if result == 'false':
            is_fail()


    @BeautifulReport.add_test_img('test_qd_login')
    def test_qd_login(self):
        """渠道登录"""
        driver = self.driver
        self.driver.get('https://qd.kupeiai.com/signin#/')
        self.driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        self.driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        result = is_element_exist(self.driver,'//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[3]/h2')
        self.assertEqual(result, 'true', msg="登陆失败")
        if result == 'false':
            is_fail()


    @BeautifulReport.add_test_img('test_qd_refresh')
    def test_qd_refresh(self):
        """渠道刷新"""
        driver = self.driver
        self.driver.get('https://qd.kupeiai.com/signin#/')
        self.driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        self.driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            driver.refresh()
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[3]/h2')
        self.assertEqual(result, 'true', msg="刷新失败")
        if result == 'false':
            is_fail()


    @BeautifulReport.add_test_img('test_kupeiai_homepage')
    def test_kupeiai_homepage(self):
        """官网首页"""
        driver = self.driver
        self.driver.get('https://www.kupeiai.com/')
        result = is_element_exist(self.driver, '/html/body/div/div[2]')
        self.assertEqual(result, 'true', msg="获取失败")
        if result == 'false':
            is_fail()



    @BeautifulReport.add_test_img('test_kupeiai_content')
    def test_kupeiai_content(self):
        """官网内容体系"""
        driver = self.driver
        self.driver.get('https://www.kupeiai.com/content.html')
        result = is_element_exist(self.driver, '/html/body/div/div[2]')
        self.assertEqual(result, 'true', msg="获取失败")
        if result == 'false':
            is_fail()

    @BeautifulReport.add_test_img('test_kupeiai_sys')
    def test_kupeiai_sys(self):
        """官网学习系统"""
        driver = self.driver
        self.driver.get('https://www.kupeiai.com/system.html')
        result = is_element_exist(self.driver, '/html/body/div/div[3]/img')
        self.assertEqual(result, 'true', msg="获取失败")
        if result == 'false':
            is_fail()





    @BeautifulReport.add_test_img('test_kupeiai_story')
    def test_kupeiai_story(self):
        """官网学员故事"""
        driver = self.driver
        self.driver.get('https://www.kupeiai.com/story.html')
        result = is_element_exist(self.driver, '/html/body/div/div[2]')
        self.assertEqual(result, 'true', msg="获取失败")
        if result == 'false':
            is_fail()


    @BeautifulReport.add_test_img('test_kupeiai_about')
    def test_kupeiai_about(self):
        """官网关于我们"""
        driver = self.driver
        self.driver.get('https://www.kupeiai.com/about.html')
        result = is_element_exist(self.driver, '/html/body/div/div[1]/div[2]')
        self.assertEqual(result, 'true', msg="获取失败")
        if result == 'false':
            is_fail()


    @BeautifulReport.add_test_img('test_kupeiai_partner')
    def test_kupeiai_partner(self):
        """官网招商合作"""
        driver = self.driver
        self.driver.get('https://www.kupeiai.com')
        driver.find_element_by_xpath('//*[@id="nav"]/div/div[1]/span[6]/a').click()
        result = is_element_exist(self.driver, '/html/body/div/div[1]/div')
        self.assertEqual(result, 'true', msg="获取失败")
        if result == 'false':
            is_fail()



    @BeautifulReport.add_test_img('test_KP_student_login')
    def test_KP_student_login(self):
        """酷培学习端学生登录"""
        driver =self.driver
        self.driver.get('https://www.kupeiai.cn/student/login')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        result = is_element_exist(self.driver,'//*[@id="root"]/section/main/div[2]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/img')
        self.assertEqual(result,'true',msg="获取失败")
        if result == 'flase':
            is_fail()


    @BeautifulReport.add_test_img('test_kp_student_refresh')
    def test_kp_student_refresh(self):
        """酷培学习端刷新"""
        driver = self.driver
        self.driver.get('https://www.kupeiai.cn/student/login')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        sleep(3)
        try:
            driver.refresh()
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver, '//*[@id="root"]/section/main/div[2]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/img')
        self.assertEqual(result, 'true', msg="刷新失败")
        if result == 'false':
            is_fail()

    # def test_kp_teacher_login(self):
    #     """酷培教师端登录"""
    #     driver = self.driver
    #     self.driver.get('https://www.kupeiai.cn/teacher/login')
    #     driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone1)
    #     driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(code)
    #     driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div[2]/form/div[3]/div/div/span/button').click()
    #     result = is_element_exist(self.driver,'//*[@id="root"]/div/div[2]/div/div')
    #     self.assertEqual(result, 'true', msg="获取失败")
    #     if result == 'flase':
    #         is_fail()
    #
    # def test_kp_teacher_refresh(self):
    #     """酷培教师端刷新"""
    #     driver = self.driver
    #     self.driver.get('https://www.kupeiai.cn/teacher/login')
    #     driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone1)
    #     driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(code)
    #     driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div[2]/form/div[3]/div/div/span/button').click()
    #     sleep(3)
    #     try:
    #         driver.refresh()
    #         print('刷新成功')
    #     except Exception as e:
    #         print("Exception found", format(e))
    #     result = is_element_exist(self.driver, '//*[@id="root"]/div/div[2]/div/div')
    #     self.assertEqual(result, 'true', msg="刷新失败")
    #     if result == 'false':
    #         is_fail()


    @BeautifulReport.add_test_img('test_kpdx_teacher_login')
    def test_kpdx_teacher_login(self):
        """单校老师登录"""
        driver = self.driver
        self.driver.get('https://testkefu.kupeiai.cn/teacher/home ')
        self.driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        self.driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(code)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div[2]/form/div[3]/div/div/span/button').click()
        result = is_element_exist(self.driver,'//*[@id="root"]/div/div[2]/div/div')
        self.assertEqual(result,'true',msg="刷新失败")
        if result == 'false':
            is_fail()


    @BeautifulReport.add_test_img('test_kpdx_teacher_refresh_login')
    def test_kpdx_teacher_refresh_login(self):
        """单校老师刷新"""
        driver = self.driver
        self.driver.get('https://testkefu.kupeiai.cn/teacher/home ')
        self.driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        self.driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(code)
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div[1]/div[2]/form/div[3]/div/div/span/button').click()
        sleep(3)
        try:
            driver.refresh()
            print('刷新成功')
        except Exception as e:
            print('Exception found',format(e))


    @BeautifulReport.add_test_img('testkupei_kupeiai')
    def testkupei_kupeiai(self):
        """kupei.cn是否跳转至www.kupeiai.cn/student/login"""
        driver =self.driver
        self.driver.get('https://kupei.cn')
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div')
        self.assertEqual(result, 'true', msg="刷新失败")
        if result == 'false':
            is_fail()




    @BeautifulReport.add_test_img('testkupei_kupeiai1')
    def testkupei_kupeiai1(self):
        """www.kupei.cn是否跳转至www.kupeiai.cn/student/login"""
        driver = self.driver
        self.driver.get('https://www.kupei.cn')
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div')
        self.assertEqual(result, 'true', msg="刷新失败")
        if result == 'false':
            is_fail()
    #
    # def test_no_www(self):
    #     driver = self.driver
    #     self.driver.get()








testsuite = unittest.TestSuite()
testsuite.addTests(unittest.makeSuite(LogIn))

# 使用的report方法输出HTML格式的报告
runner = BeautifulReport((testsuite))

# 根据系统环境判断需要读取的目录路径
if (platform.system() == 'Windows'):
    report_dir = 'C:\\python1\\day06'
    filename = "C:\\python1\\day05"
    print(platform.system())
    runner.report(filename='../正服Render酷培网站测试报告.html', description='正服Render酷培网站测试报告', log_path=report_dir)
    print(report_dir)
    print(filename)
elif (platform.system() == 'Linux'):
    report_dir = "/opt/uitest/report"
    filename = '/opt/uitest/img'
    runner.report(filename='../正服Render酷培网站测试报告.html', description='正服Render酷培网站测试报告', report_dir=report_dir)
    print(report_dir)
    print(filename)
    print(platform.system())
else:
    print(platform.system())
