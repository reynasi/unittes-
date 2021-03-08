import platform
from selenium import webdriver
import unittest
from time import sleep
from BeautifulReport import BeautifulReport
import socket
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import traceback
# 引入自定义的模块
# 获取IP
#获取计算机名称
hostname=socket.gethostname()
#获取本机IP
ip=socket.gethostbyname(hostname)

# 根据系统环境判断需要读取的目录路径
if(platform.system()=='Windows'):
    print(platform.system())
    report_dir = 'C:\\python1\\day06'
    filename = "C:\\python1\\day05"
    print(report_dir)
    print(filename)
elif(platform.system()=='Linux'):
    report_dir = "/opt/uitest/report"
    filename = '/opt/uitest/img'
    print(report_dir)
    print(filename)
    print(platform.system())
else:
    print(platform.system())

def find_next(driver):
    fnext = 1
    print("----->查找第下一题按钮")
    try:
        locator = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[3]')
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
        print("----->找不到下一题按钮")
        fnext = 0
    except:
        print("----->找到下一题按钮")

    finally:
        return fnext



def is_fail():
    result = "false"
    return result


def is_element_exist(driver, xpath, prompt="err_message"):
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
        self.driver.get('https://www.kupeiai.cn/student/login')

    def tearDown(self):
        self.driver.quit()

    def save_img(self, imgName):
        self.driver.get_screenshot_as_file("{}/{}.png".format(filename, imgName))

    def is_element_exist(driver, xpath, prompt="err_message"):
        result = 'true'
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
        except:
            result = 'false'
            traceback.print_exc()
        finally:
            return result

    @BeautifulReport.add_test_img('testCapture')
    def testCapture(self):
        '''测试酷培学生端未学习立即攻克功能是否正常'''
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/a').click()
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys("13975353140")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qweasd")
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        # 点击未学习知识点
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,'//*[@id="root"]/section/main/div[1]/div[2]/div/div/div[2]/div/p[1]/span' )))
        driver.find_element_by_xpath('//*[@id="root"]/section/main/div[1]/div[2]/div/div/div[2]/div/p[1]/span').click()
        #选择另外一立即攻克
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[3]/button')))

        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[3]/button').click()
        # 点击继续按钮
        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="videoId"]')
        except:
            traceback.print_exc()
        finally:
            if result == 'false':
                is_fail()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]/div')))
                driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/div').click()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]/div')))
                driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/div').click()
            else:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]/div')))
                driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/div').click()


        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]')))

        while find_next(driver):
            # try:
            #     result = is_element_exist(self.driver,'//*[@id="root"]/div/div/div[2]/div/div[2]')
            # except:
            #     traceback.print_exc()
            # finally:
            #     if result == 'false':
            #         is_fail()
            #     else:
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]')))
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]')))
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]')))



testsuite = unittest.TestSuite()
testsuite.addTests(unittest.makeSuite(LogIn))

#使用的report方法输出HTML格式的报告
runner = BeautifulReport((testsuite))
#runner.report(filename='KuPiWEB端测试.html', description='酷培学生端测试用例',log_path=report_dir)
# filename = time.strftime("%Y-%m-%d-%H-%M-%S")+r".html"


# 根据系统环境判断需要读取的目录路径
if(platform.system()=='Windows'):
    report_dir = 'C:\\python1\\day06'
    filename = "C:\\python1\\day05"
    print(platform.system())
    runner.report(filename='酷培学生端(登录和首页部分).html', description='酷培学生端(登录和首页部分)', log_path=report_dir)
    print(report_dir)
    print(filename)
elif(platform.system()=='Linux'):
    report_dir = "/opt/uitest/report"
    filename = '/opt/uitest/img'
    runner.report(filename='酷培学生端(登录和首页部分).html', description='酷培学生端(登录和首页部分)', report_dir=report_dir)
    print(report_dir)
    print(filename)
    print(platform.system())
else:
    print(platform.system())