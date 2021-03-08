import platform
from selenium import webdriver
from time import sleep
from BeautifulReport import BeautifulReport
import socket
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import traceback
import unittest

# 引入自定义的模块
# 获取IP
# 获取计算机名称
hostname = socket.gethostname()
# 获取本机IP
ip = socket.gethostbyname(hostname)

# 根据系统环境判断需要读取的目录路径
if platform.system() == 'Windows':
    print(platform.system())
    report_dir = 'D:\\Report'
    filename = "D:\\Report\\day01"
    print(report_dir)
    print(filename)
elif platform.system() == 'Linux':
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
        self.driver.get_screenshot_as_file("{}/{}.png".format(filename, imgName))

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

    # 第一条测试用例
    def test_search(self):  # 默认开头，test_
        """我的自动化测试"""
        driver = self.driver
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('美女你好')
        self.driver.find_element_by_id('su').click()
        sleep(5)


testsuite = unittest.TestSuite()
testsuite.addTests(unittest.makeSuite(LogIn))

# 使用的report方法输出HTML格式的报告
runner = BeautifulReport((testsuite))

# 根据系统环境判断需要读取的目录路径
if (platform.system() == 'Windows'):
    report_dir = 'D:\\Report'
    filename = "D:\\Report\\day01"
    print(platform.system())
    runner.report(filename='../Reyna测试报告.html', description='Reyna测试报告', log_path=report_dir)
    print(report_dir)
    print(filename)
elif (platform.system() == 'Linux'):
    report_dir = "/opt/uitest/report"
    filename = '/opt/uitest/img'
    runner.report(filename='../Reyna测试报告.html', description='Reyna测试报告', report_dir=report_dir)
    print(report_dir)
    print(filename)
    print(platform.system())
else:
    print(platform.system())
