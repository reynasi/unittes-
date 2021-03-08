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
import requests
import json
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

def is_element_exist(driver, xpath, prompt="err_message"):
    result = 'true'
    try:
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
    except:
        result = 'false'
    finally:
        return result
#继续做题循环
def find_next(driver):
    sleep(10)
    fnext = 1
    print("----->查找下一题按钮")
    try:
        sleep(5)
        locator = (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[3]')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        print("----->找不到下一题按钮")
        fnext = 0
    except:
        print("----->找到下一题按钮")

    finally:
        return fnext

def find_cyc(driver):
    sleep(20)
    fnext = 1
    print("----->查找下一题按钮")
    try:
        sleep(5)
        locator = (By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/h5')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        print("----->找不到下一题按钮")
        fnext = 0
    except:
        print("----->找到下一题按钮")

    finally:
        return fnext

#进入课程循环
def find_one(driver):
    fnext = 1
    print("----->是否进入做题")
    try:

        locator = (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[1]/img')
        WebDriverWait(driver,20).until(EC.presence_of_element_located(locator))
        print("----->进入")
        fnext = 0
    except:
        print("----->未进入")

    finally:
        return fnext

#未攻克知识点循环
def find_two(driver):
    sleep(10)
    fnext = 1
    print("---->查找第下一题按钮")
    try:
        locator = (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[3]')
        WebDriverWait(driver,20).until(EC.presence_of_element_located(locator))
        print("----->找不到下一题按钮")
        fnext = 0
    except:
        print("----->找到下一题按钮")
        return
    finally:
        return fnext


#薄弱知识点立即攻克循环
def find_xix(driver):
    sleep(1)
    fnext = 1
    print("---->查找第下一题按钮")
    try:
        locator = (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[3]')
        WebDriverWait(driver,20).until(EC.presence_of_element_located(locator))
        print("----->找不到下一题按钮")
        fnext = 0
    except:
        print("----->找到下一题按钮")
        return
    finally:
        return fnext


#薄弱知识点置灰循环
def find_yxy(driver):
    fnext = 1
    print("---->点击立即攻克")
    try:
        locator = (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[1]/img')
        WebDriverWait(driver,20).until(EC.presence_of_element_located(locator))
        print("----->进入立即攻克")
        fnext = 0

    except:
        print("----->未进入立即攻克")
        return
    finally:
        return fnext

class Clasdw(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://www.kupeiai.cn/student/login')

    def tearDown(self):
        sleep(3)
        self.driver.quit()

    def save_img(self, imgName):
        self.driver.get_screenshot_as_file("{}/{}.png".format(filename, imgName))

    @BeautifulReport.add_test_img('testtest')
    def testtest(self):
        '''测试酷培学生端测一测功能是否正常'''
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        loginOrgPostdata = {"username": 15021201246, "code": 1111, "systemCode": "dms"}
        loginOrgResponsedata = requests.post("https://api.learnta.cn/v1/auth/crm/user/login",
                                             data=json.dumps(loginOrgPostdata), headers=self.headers)
        print(loginOrgResponsedata.status_code)
        self.token = loginOrgResponsedata.json()['data']['access_token']
        print(self.token)
        # put请求
        url = "https://api.learnta.cn/v1/dms/demoAccount/0/6/220793/reset"
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}

        r = requests.put(url, headers=headers)
        # print("请求url:", r.url)  # 响应对象.r

        # 4.获取响应状态码
        print("状态码", r.status_code)

        # # 5.获取响应对象
        # print( r.json)
        sleep(20)
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/a').click()
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys("00105144253")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("111111")
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        sleep(5)
        # 选择 课程
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/section/main/div[2]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/img')))
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div[2]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/img').click()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/button')))
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[2]/div/button').click()

        sleep(5)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div')))

        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div').click()
        # 做题循环
        while find_cyc(driver):
            sleep(5)
            WebDriverWait(driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]')))
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div[2]').click()
            sleep(5)
            driver.find_element_by_xpath('/html/body/div[last()]/div/div[2]/div/div[2]/div/div/div[1]').click()
        # ========
        sleep(5)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/div/div/div/div[3]')))
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[3]').click()
        sleep(1)
        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="root"]/section/div/p')
        except:
            traceback.print_exc()
        finally:

            self.assertEqual(result, 'true', msg="测一测做题出错")

        sleep(3)


testsuite = unittest.TestSuite()
testsuite.addTests(unittest.makeSuite(Clasdw))

#使用的report方法输出HTML格式的报告
runner = BeautifulReport((testsuite))
#runner.report(filename='KuPiWEB端测试.html', description='酷培学生端测试用例',log_path=report_dir)
# filename = time.strftime("%Y-%m-%d-%H-%M-%S")+r".html"



# 根据系统环境判断需要读取的目录路径
if(platform.system()=='Windows'):
    report_dir = 'C:\\python1\\day06'
    filename = "C:\\python1\\day05"
    print(platform.system())
    runner.report(filename='酷培学生端(刷题).html', description='酷培学生端(刷题)', log_path=report_dir)
    print(report_dir)
    print(filename)
elif(platform.system()=='Linux'):
    report_dir = "/opt/uitest/report"
    filename = '/opt/uitest/img'
    runner.report(filename='酷培学生端(刷题).html', description='酷培学生端(刷题)', report_dir=report_dir)
    print(report_dir)
    print(filename)
    print(platform.system())
else:
    print(platform.system())