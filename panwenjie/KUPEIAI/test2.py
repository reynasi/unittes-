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

def is_element_exist(driver, xpath, prompt="err_message"):
    result = 'true'
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
    except:
        result = 'false'
    finally:
        return result

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

    @BeautifulReport.add_test_img('testStuDentReturn')
    def testStuDentReturn(self):
        '''测试酷培学生端学习轨迹功能是否正常'''
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/a').click()
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys("13975353140")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qweasd")
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        sleep(5)
        # 点击学习轨迹
        driver.find_element_by_xpath('//*[@id="root"]/section/header/div/div/div[1]/button').click()
        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="root"]/section/div/p')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="切换学习轨迹出错")

        sleep(3)
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/section/header/div/div/div/button').click()
        sleep(2)
        self.assertEqual(driver.current_url, 'https://www.kupeiai.cn/student/home?category=1', msg='返回失败')
        sleep(2)
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