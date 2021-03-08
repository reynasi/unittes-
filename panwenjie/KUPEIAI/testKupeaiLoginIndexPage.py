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
        self.driver.get('https://www.kupeiai.cn/student/login')

    def tearDown(self):
        self.driver.quit()

    #     截图方法
    # 定义save_img()
    # 方法
    # imgname: 手动截图的时候才会用到的参数
    # 是输出截图的名字

        # 定义save_img()方法
        # imgname :手动截图的时候才会用到的参数 是输出截图的名字
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

    @BeautifulReport.add_test_img('testStuDentLogin')
    def testStuDentLogin(self):
        '''演示酷培学生端登陆的测试用例'''
        driver=self.driver
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/a').click()
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys("13975353140")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qweasd")
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        sleep(5)
        self.assertEqual(driver.current_url, "https://www.kupeiai.cn/student/home?category=1", msg="登录失败")

    @BeautifulReport.add_test_img('testStuDentLogout')
    def testStuDentLogout(self):
        '''演示酷培学生端退出的测试用例'''
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/a').click()
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys("13975353140")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qweasd")
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        sleep(5)
        driver.find_element_by_xpath('//*[@id="root"]/section/header/div/div/div[2]').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/ul/li[3]/span').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
        self.assertEqual(driver.current_url, "https://www.kupeiai.cn/student/login", msg="退出失败")
        sleep(5)


    @BeautifulReport.add_test_img('testStuDentReturn')
    def testStuDentReturn(self):
        '''测试酷培学生端学习轨迹功能是否正常'''
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/a').click()
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys("13975353140")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qweasd")
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        sleep(5)
        #点击学习轨迹
        driver.find_element_by_xpath('//*[@id="root"]/section/header/div/div/div[1]/button').click()

        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="root"]/section/div/p')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="切换学习轨迹出错")
            if result == 'false':
                is_fail()

        sleep(3)
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/section/header/div/div/div/button').click()
        sleep(2)
        self.assertEqual(driver.current_url, 'https://www.kupeiai.cn/student/home?category=1', msg='返回失败')
        sleep(2)

    @BeautifulReport.add_test_img('testStudentCut')
    def testStudentCut(self):
        '''测试酷培学生端切换科目功能是否正常'''
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/a').click()
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys("13975353140")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qweasd")
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        sleep(5)
        driver.find_element_by_xpath('//*[@id="root"]/section/header/span/div/div[2]').click()
        # 切换到英语
        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="root"]/section/main/div[2]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/img')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="切换数学出错")
            if result == 'false':
                is_fail()

        sleep(3)
        # 切换到物理
        driver.find_element_by_xpath('//*[@id="root"]/section/header/span/div/div[3]').click()
        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="root"]/section/main/div[2]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/img')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="切换物理出错")
            if result == 'false':
                is_fail()
        sleep(3)
        # 切换到化学
        driver.find_element_by_xpath('//*[@id="root"]/section/header/span/div/div[4]').click()
        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="root"]/section/main/div[2]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/img')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="切换化学出错")
            if result == 'false':
                is_fail()
        sleep(3)
        # 切换到数学
        driver.find_element_by_xpath('//*[@id="root"]/section/header/span/div/div[1]').click()
        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="root"]/section/main/div[2]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/img')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="切换数学出错")
            if result == 'false':
                is_fail()
        sleep(3)

    @BeautifulReport.add_test_img('testCapture')
    def testCapture(self):
        '''测试酷培学生端已攻克知识点列表功能是否正常'''
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/a').click()
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys("13975353140")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qweasd")
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        sleep(5)
        #点击已攻克
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div[1]/div[2]/div/div/div[2]/div/div/h4/span[1]').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver,
                                     '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/h4/span')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="查看已攻克出错")
            if result == 'false':
                is_fail()
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/button/span/div/img').click()
        sleep(3)

    @BeautifulReport.add_test_img('testNottoCapture')
    def testNottoCapture(self):
        '''测试酷培学生端未攻克知识点列表功能是否正常'''
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/a').click()
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys("13975353140")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qweasd")
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        sleep(5)
        # 点击未攻克
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div[1]/div[2]/div/div/div[2]/div/p[1]/span').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver,
                                     '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="查看未攻克出错")
            if result == 'false':
                is_fail()
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/button/span/div/img').click()
        sleep(3)

    @BeautifulReport.add_test_img('testWeakness')
    def testWeakness(self):
        '''测试酷培学生端薄弱知识点列表功能是否正常'''
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/a').click()
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys("13975353140")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qweasd")
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        sleep(5)
        #点击薄弱知识点
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div[1]/div[2]/div/div/div[2]/div/p[2]/span').click()
        sleep(4)
        try:
            result = is_element_exist(self.driver,
                                     '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="查看薄弱知识点出错")
            if result == 'false':
                is_fail()
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/button/span/div/img').click()
        sleep(3)

    @BeautifulReport.add_test_img('testContinue')
    def testContinue(self):
        '''测试酷培学生端继续知识点列表功能是否正常'''
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/a').click()
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys("13975353140")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qweasd")
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        sleep(5)
        #点击继续按扭
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div[1]/div[2]/div/div/div[2]/div/button').click()
        sleep(2)
        try:
            result = is_element_exist(self.driver,
                                     '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="查看继续知识点出错")
            if result == 'false':
                is_fail()
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/button/span/div/img').click()
        sleep(3)

    @BeautifulReport.add_test_img('testCapture')
    def testCapture(self):
        '''测试酷培学生端课程列表功能是否正常'''
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/a').click()
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys("13975353140")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qweasd")
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        sleep(5)
        #点击课程列表
        driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div[2]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[1]').click()
        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="root"]/div/div/div[2]/div/div[1]/div[1]/h3')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="切换课程列表失败")
            if result == 'false':
                is_fail()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/header/div[1]/div/div/button').click()
        sleep(3)




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