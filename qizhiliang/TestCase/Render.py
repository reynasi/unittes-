"""本代码只支持t3测服render项目/只可本地跑"""
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

    def test_dealer_login(self):
        """Dealer登录"""
        driver = self.driver
        self.driver.get('https://t3.kupeiai.cn/dealer/login')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys('15298987878')
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button').click()
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/section/aside/div/div[1]/a/img')
        self.assertEqual(result, 'true', msg="登陆失败")
        if result == 'false':
            is_fail()

    def test_dealer_refresh(self):
        """Dealer刷新跳转"""
        driver = self.driver
        self.driver.get('https://t3.kupeiai.cn/dealer/login')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys('15298987878')
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button').click()
        sleep(3)
        try:
            driver.refresh()
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver, '//*[@id="root"]/section/aside/div/div[1]/a/img')
        self.assertEqual(result, 'true', msg="刷新失败")
        if result == 'false':
            is_fail()


    def test_dms_login(self):
        """Dms登录"""
        driver = self.driver
        self.driver.get('https://admin.t3.learnta.work/dms/login')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button').click()
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/section/aside/div/div[2]/ul')
        self.assertEqual(result, 'true', msg="登陆失败")
        if result == 'false':
            is_fail()

    def test_dms_refresh(self):
        """Dms刷新跳转"""
        driver = self.driver
        self.driver.get('https://admin.t3.learnta.work/dms/login')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button').click()
        sleep(3)
        try:
            driver.refresh()
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver, '//*[@id="root"]/section/aside/div/div[2]/ul')
        self.assertEqual(result, 'true', msg="登陆失败")
        if result == 'false':
            is_fail()

    def test_partners_login(self):
        """partners登录"""
        driver = self.driver
        self.driver.get('https://partners.t3.kupeiai.com/outer/detail#/')
        driver.find_element_by_xpath('//*[@id="details-button"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="proceed-link"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[2]/ul')
        self.assertEqual(result, 'true', msg="登陆失败")
        if result == 'false':
            is_fail()

    def test_partners_refresh(self):
        """partners刷新跳转"""
        driver = self.driver
        self.driver.get('https://partners.t3.kupeiai.com/outer/detail#/')
        driver.find_element_by_xpath('//*[@id="details-button"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="proceed-link"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            driver.refresh()
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[2]/ul')
        self.assertEqual(result, 'true', msg="刷新失败")
        if result == 'false':
            is_fail()

    def test_bd_login(self):
        """bd登录"""
        driver = self.driver
        self.driver.get('https://bd.t3.kupeiai.com/signin#/')
        driver.find_element_by_xpath('//*[@id="details-button"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="proceed-link"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[2]/ul')
        self.assertEqual(result, 'true', msg="登陆失败")
        if result == 'false':
            is_fail()

    def test_bd_refresh(self):
        """bd刷新跳转"""
        driver = self.driver
        self.driver.get('https://bd.t3.kupeiai.com/signin#/')
        driver.find_element_by_xpath('//*[@id="details-button"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="proceed-link"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            driver.refresh()
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[2]/ul')
        self.assertEqual(result, 'true', msg="刷新失败")
        if result == 'false':
            is_fail()

    def test_kupeiai_homepage(self):
        """官网首页"""
        driver = self.driver
        self.driver.get('https://www.t3.kupeiai.com/')
        driver.find_element_by_xpath('//*[@id="details-button"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="proceed-link"]').click()  # 跳证书
        result = is_element_exist(self.driver, '/html/body/div/div[2]')
        self.assertEqual(result, 'true', msg="获取失败")
        if result == 'false':
            is_fail()

    def test_kupeiai_content(self):
        """官网内容体系"""
        driver = self.driver
        self.driver.get('https://www.t3.kupeiai.com/content.html')
        driver.find_element_by_xpath('//*[@id="details-button"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="proceed-link"]').click()  # 跳证书
        result = is_element_exist(self.driver, '/html/body/div/div[2]')
        self.assertEqual(result, 'true', msg="获取失败")
        if result == 'false':
            is_fail()

    def test_kupeiai_sys(self):
        """官网学习系统"""
        driver = self.driver
        self.driver.get('https://www.t3.kupeiai.com/system.html')
        driver.find_element_by_xpath('//*[@id="details-button"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="proceed-link"]').click()  # 跳证书
        result = is_element_exist(self.driver, '/html/body/div/div[3]/img')
        self.assertEqual(result, 'true', msg="获取失败")
        if result == 'false':
            is_fail()

    def test_kupeiai_story(self):
        """官网学员故事"""
        driver = self.driver
        self.driver.get('https://www.t3.kupeiai.com/story.html')
        driver.find_element_by_xpath('//*[@id="details-button"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="proceed-link"]').click()  # 跳证书
        result = is_element_exist(self.driver, '/html/body/div/div[2]')
        self.assertEqual(result, 'true', msg="获取失败")
        if result == 'false':
            is_fail()

    def test_kupeiai_about(self):
        """官网关于我们"""
        driver = self.driver
        self.driver.get('https://www.t3.kupeiai.com/about.html')
        driver.find_element_by_xpath('//*[@id="details-button"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="proceed-link"]').click()  # 跳证书
        result = is_element_exist(self.driver, '/html/body/div/div[1]/div[2]')
        self.assertEqual(result, 'true', msg="获取失败")
        if result == 'false':
            is_fail()

    def test_kupeiai_partner(self):
        """官网招商合作"""
        driver = self.driver
        self.driver.get('https://www.t3.kupeiai.com')
        driver.find_element_by_xpath('//*[@id="details-button"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="proceed-link"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="nav"]/div/div[1]/span[6]/a').click()
        result = is_element_exist(self.driver, '/html/body/div/div[1]/div')
        self.assertEqual(result, 'true', msg="获取失败")
        if result == 'false':
            is_fail()

    def test_qd_login(self):
        # 渠道t3 无内容
        """渠道登录"""
        driver = self.driver
        self.driver.get('https://qd.t3.kupeiai.com/signin#/')
        driver.find_element_by_xpath('//*[@id="details-button"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="proceed-link"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[2]/ul')
        self.assertEqual(result, 'true', msg="登陆失败")
        if result == 'false':
            is_fail()

    def test_qd_refresh(self):
        """qd刷新跳转"""
        driver = self.driver
        self.driver.get('https://qd.t3.kupeiai.com/signin#/')
        driver.find_element_by_xpath('//*[@id="details-button"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="proceed-link"]').click()  # 跳证书
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            driver.refresh()
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[2]/ul')
        self.assertEqual(result, 'true', msg="刷新失败")
        if result == 'false':
            is_fail()

    def test_kp_student(self):
        """酷培_学生"""
        driver = self.driver
        self.driver.get('https://t3.kupeiai.cn/student/login')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[4]/div/div/span/button').click()
        sleep(3)
        result = is_element_exist(self.driver,'//*[@id="root"]/section/main/div[2]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/img')
        self.assertEqual(result, 'true', msg="登陆失败")
        if result == 'false':
            is_fail()

    def test_kp_refresh(self):
        """酷培_学生刷新"""
        driver = self.driver
        self.driver.get('https://t3.kupeiai.cn/student/login')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[4]/div/div/span/button').click()
        sleep(3)
        try:
            driver.refresh()
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver,'//*[@id="root"]/section/main/div[2]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/img')
        self.assertEqual(result, 'true', msg="刷新失败")
        if result == 'false':
            is_fail()

    def test_kupei_teacher(self):
        """酷培_教师"""
        driver = self.driver
        self.driver.get('https://t3.kupeiai.cn/teacher/login')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone1)
        driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div[2]/form/div[4]/div/div/span/button').click()
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div[2]/div/div')
        self.assertEqual(result, 'true', msg="登陆失败")
        if result == 'false':
            is_fail()

    def test_kupei_teacher_refresh(self):
        """酷培_教师刷新"""
        driver = self.driver
        self.driver.get('https://t3.kupeiai.cn/teacher/login')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone1)
        driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(code)
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div[1]/div[2]/form/div[4]/div/div/span/button').click()
        sleep(3)
        try:
            driver.refresh()
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div[2]/div/div')
        self.assertEqual(result, 'true', msg="刷新失败")
        if result == 'false':
            is_fail()

    def test_student_login(self):
        """酷培学生-登录"""
        driver = self.driver
        self.driver.get('https://kupeitrial.t3.kupeiai.cn/student/login')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        result = is_element_exist(self.driver,
                                 '//*[@id="root"]/section/main/div[2]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/img')
        self.assertEqual(result, 'true', msg="登陆失败")
        if result == 'false':
            is_fail()

    def test_student_refresh(self):
        "酷培学生-刷新正常跳转"
        driver = self.driver
        self.driver.get('https://kupeitrial.t3.kupeiai.cn/student/login')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        sleep(3)
        try:
            driver.refresh()
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver,
                                 '//*[@id="root"]/section/main/div[2]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/img')
        self.assertEqual(result, 'true', msg="刷新失败")
        if result == 'false':
            is_fail()

    def test_teacher_login(self):
        """酷培教师端-登录"""
        driver = self.driver
        self.driver.get('https://kupeitrial.t3.kupeiai.cn/teacher/login')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone1)
        driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(code)
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div[1]/div[2]/form/div[3]/div/div/span/button').click()
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div[2]/div/div')
        self.assertEqual(result, 'true', msg="登陆失败")
        if result == 'false':
            is_fail()

    def test_teacher_refresh(self):
        "酷培教师-刷新正常跳转"
        driver = self.driver
        self.driver.get('https://kupeitrial.t3.kupeiai.cn/teacher/login')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone1)
        driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(code)
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div[1]/div[2]/form/div[3]/div/div/span/button').click()
        sleep(3)
        try:
            driver.refresh()
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div[2]/div/div')
        self.assertEqual(result, 'true', msg="刷新失败")
        if result == 'false':
            is_fail()


testsuite = unittest.TestSuite()
testsuite.addTests(unittest.makeSuite(LogIn))

# 使用的report方法输出HTML格式的报告
runner = BeautifulReport((testsuite))

# 根据系统环境判断需要读取的目录路径
if (platform.system() == 'Windows'):
    report_dir = 'C:\\python1\\day06'
    filename = "C:\\python1\\day05"
    print(platform.system())
    runner.report(filename='../Report/Render酷培网站测试报告.html', description='Render酷培网站测试报告', log_path=report_dir)
    print(report_dir)
    print(filename)
elif (platform.system() == 'Linux'):
    report_dir = "/opt/uitest/report"
    filename = '/opt/uitest/img'
    runner.report(filename='../Report/Render酷培网站测试报告.html', description='Render酷培网站测试报告', report_dir=report_dir)
    print(report_dir)
    print(filename)
    print(platform.system())
else:
    print(platform.system())
