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
#继续做题循环
def find_next(driver):
    fnext = 1
    print("----->查找下一题按钮")
    try:
        sleep(3)
        locator = (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[3]')
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
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
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
        print("----->进入")
        fnext = 0
    except:
        print("----->未进入")

    finally:
        return fnext

#未攻克知识点循环
def find_two(driver):
    fnext = 1
    print("---->查找第下一题按钮")
    try:
        locator = (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[3]')
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
        print("----->找不到下一题按钮")
        fnext = 0
    except:
        print("----->找到下一题按钮")
        return
    finally:
        return fnext


#薄弱知识点立即攻克循环
def find_xix(driver):
    fnext = 1
    print("---->查找第下一题按钮")
    try:
        locator = (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[3]')
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
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
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
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

    @BeautifulReport.add_test_img('testContinue')
    def testContinue(self):
        '''测试酷培学生端继续学习功能是否正常'''
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/a').click()
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys("18707952558")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qwe")
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/section/main/div[2]/div/div[3]/div/div[2]/div[2]/div[1]/div')))
        driver.find_element_by_xpath('//*[@id="root"]/section/main/div[2]/div/div[3]/div/div[2]/div[2]/div[1]/div').click()
        sleep(3)
        #需要加一个循环判断
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/div/div[3]/div/button').click()

        while find_one(driver):
            try:
                result = is_element_exist(self.driver,
                                         '//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/div/div[3]/p')
                driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/div/div[3]/div/button').click()
            except:
                traceback.print_exc()
            finally:
                    return

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div')))
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div').click()
        #视频点击
        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="videoId"]')
        except:
            traceback.print_exc()
        finally:
            if result == 'true':
                driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div').click()
            else:
                return


        #做题
        #改循环\
        while find_next(driver):
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]').click()
            sleep(1)
            driver.find_element_by_xpath('/html/body/div[last()]/div/div[2]/div/div[2]/div/div/div[1]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[2]')))
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[2]')))
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]').click()

        #========

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[3]')))
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[3]').click()
        sleep(1)
        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="root"]/section/div/p')
        except:
            traceback.print_exc()
        finally:

            self.assertEqual(result, 'true', msg="课堂继续做题出错")

        sleep(3)

    @BeautifulReport.add_test_img('testCapture')
    def testCapture(self):
        '''测试酷培学生端未学习立即攻克功能是否正常'''
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/a').click()
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys("18707952558")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qwe")
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        # 点击未学习知识点
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/section/main/div[1]/div[2]/div/div/div[2]/div/p[1]/span')))
        driver.find_element_by_xpath('//*[@id="root"]/section/main/div[1]/div[2]/div/div/div[2]/div/p[1]/span').click()
        # 选择第一个知识点立即攻克
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[3]/button')))

        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[3]/button').click()
        # 点击继续按钮
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div').click()
        #判断是否有视频是否需要在次点击继续
        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="videoId"]')
        except:
            traceback.print_exc()
        finally:
            if result == 'false':
                return
            else:
                driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div').click()


#循环做题
        while find_two(driver):
            driver.implicitly_wait(5)
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]').click()
            sleep(1)
            driver.find_element_by_xpath('/html/body/div[last()]/div/div[2]/div/div[2]/div/div/div[1]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[2]')))
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[2]')))
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]').click()

        # 点击继续跳转到轨迹页
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[3]').click()
        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="root"]/section/div/p')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="查看继续知识点出错")
        driver.find_element_by_xpath('//*[@id="root"]/section/header/div/div/div/button')
        sleep(3)

    @BeautifulReport.add_test_img('testWeakness')
    def testWeakness(self):
        '''测试酷培学生端薄弱立即攻克功能是否正常'''
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/a').click()
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys("18707952558")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qwe")
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        # 点击薄弱知识点
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/section/main/div[1]/div[2]/div/div/div[2]/div/p[2]/span')))
        driver.find_element_by_xpath('//*[@id="root"]/section/main/div[1]/div[2]/div/div/div[2]/div/p[2]/span').click()

        # 选择第一个知识点立即攻克

        num = 1
        while find_yxy(driver):

            sleep(1)
            print(num)
            driver.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[%d]/div/div[3]/button' % (
                num,)).click()
            num += 1
            sleep(1)
            try:
                result = is_element_exist(self.driver,
                                         '/html/body/div[4]/div/div/button')
            except:
                traceback.print_exc()
            finally:
                if result == 'true':
                    driver.find_element_by_xpath('/html/body/div[4]/div/div/button').click()

        # 点击继续按钮
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div').click()
        # 判断是否有视频是否需要在次点击继续
        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="videoId"]')
        except:
            traceback.print_exc()
        finally:
            if result == 'false':
                return
            else:
                driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div').click()

        # 循环做题
        while find_xix(driver):
            driver.implicitly_wait(5)
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]').click()
            sleep(1)
            driver.find_element_by_xpath('/html/body/div[last()]/div/div[2]/div/div[2]/div/div/div[1]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[2]')))
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[2]')))
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]').click()

        # 点击继续跳转到轨迹页
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[3]').click()
        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="root"]/section/div/p')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="查看继续知识点出错")
        driver.find_element_by_xpath('//*[@id="root"]/section/header/div/div/div/button')
        sleep(3)

    @BeautifulReport.add_test_img('testBegin')
    def testegin(self):
        '''测试酷培学生端开始学习立即攻克功能是否正常'''
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/a').click()
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys("18707952558")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123qwe")
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/form/div[3]/div/div/span/button').click()
        # 点击薄弱知识点
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/section/main/div[1]/div[2]/div/div/div[2]/div/p[2]/span')))
        driver.find_element_by_xpath('//*[@id="root"]/section/main/div[1]/div[2]/div/div/div[2]/div/p[2]/span').click()

        # 选择第一个知识点立即攻克

        num = 1
        while find_yxy(driver):

            sleep(1)
            print(num)
            driver.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[%d]/div/div[3]/button' % (
                    num,)).click()
            num += 1
            sleep(1)
            try:
                result = is_element_exist(self.driver,
                                         '/html/body/div[4]/div/div/button')
            except:
                traceback.print_exc()
            finally:
                if result == 'true':
                    driver.find_element_by_xpath('/html/body/div[4]/div/div/button').click()

        # 点击继续按钮
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div').click()
        # 判断是否有视频是否需要在次点击继续
        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="videoId"]')
        except:
            traceback.print_exc()
        finally:
            if result == 'false':
                return
            else:
                driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]/div').click()

        # 循环做题
        while find_xix(driver):
            driver.implicitly_wait(5)
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]').click()
            sleep(1)
            driver.find_element_by_xpath('/html/body/div[last()]/div/div[2]/div/div[2]/div/div/div[1]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[2]')))
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]').click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div[2]')))
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[2]').click()

        # 点击继续跳转到轨迹页
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/div[3]').click()
        try:
            result = is_element_exist(self.driver,
                                     '//*[@id="root"]/section/div/p')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="查看继续知识点出错")
        driver.find_element_by_xpath('//*[@id="root"]/section/header/div/div/div/button')
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