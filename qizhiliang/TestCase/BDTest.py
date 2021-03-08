# -*- coding: utf-8 -*-
# @Time    : 2020/12/28 14:44
# @Author  : Dean
# @Software: PyCharm
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
phone=15021201249
code=1111

# 根据系统环境判断需要读取的目录路径
if platform.system()=='Windows':
    print(platform.system())
    report_dir = 'C:\\python1\\day06'
    filename = "C:\\python1\\day05"
    print(report_dir)
    print(filename)
elif platform.system()=='Linux':
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

    @BeautifulReport.add_test_img('test_Dealer_get_TryOut')
    def test_Dealer_get_TryOut(self):
        """获取试用账号"""
        driver = self.driver
        #进入Dealer登录页
        self.driver.get('https://www.kupeiai.cn/dealer/login')
        #输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        #输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        #点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button').click()
        #强制等待2秒
        sleep(2)
        #获取试用账号列表
        self.driver.get('https://www.kupeiai.cn/dealer/home/studentAccount/trialAccount')
        #强制等待3秒
        sleep(3)
        #判断是否有账号
        result = is_element_exist(self.driver,
                                 '//*[@id="root"]/section/section/main/div/div/div/div[4]/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]')
        self.assertEqual(result, 'true', msg="获取失败")
        if result == 'false':
            is_fail()

#############################################################################################################################################
                                            # https://bda.learnta.com/
#获取页面
    @BeautifulReport.add_test_img('test_bda_learnta_login')
    def test_bda_learnta_login(self):
        """酷培合作伙伴-登录"""
        driver = self.driver
        # 打开网页
        self.driver.get('https://bda.learnta.com')
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[2]/ul')
        self.assertEqual(result, 'true', msg="登陆失败")
        if result == 'false':
            is_fail()
        sleep(3)


# 获取页面
    @BeautifulReport.add_test_img('test_bda_learnta_Page')
    def test_bda_learnta_Page(self):
        """酷培合作伙伴-获取页面"""
        driver = self.driver
        self.driver.get('https://bda.learnta.com')
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[1]')
        self.assertEqual(result, 'true', msg="未获取到页面")
        if result == 'false':
            is_fail()
        sleep(3)

#刷新界面
    @BeautifulReport.add_test_img('test_bda_learnta_Refresh')
    def test_bda_learnta_Refresh(self):
        """酷培合作伙伴-刷新页面"""
        driver = self.driver
        self.driver.get('https://bda.learnta.com')
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            driver.refresh()  # 刷新方法 refresh
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[1]')
        self.assertEqual(result, 'true', msg="未获取到页面")
        if result == 'false':
            is_fail()



# 获取二维码
    @BeautifulReport.add_test_img('test_bda_learnta_GetQRCode')
    def test_bda_learnta_GetQRCode(self):
        """酷培合作伙伴-获取二维码"""
        driver = self.driver
        self.driver.get('https://bda.learnta.com')
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/span[1]').click()
        sleep(2)
        try:
            result = is_element_exist(self.driver, '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/canvas')
        except:
            print('获取二维码失败')
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg='未获取到二维码')
            if result == 'false':
                is_fail()


# 打开二维码链接
    @BeautifulReport.add_test_img('test_bda_learnta_OpenQRCode')
    def test_bda_learnta_OpenQRCode(self):
        """酷培合作伙伴-打开二维码链接"""
        driver = self.driver
        self.driver.get('https://www.learnta.cn/bda/article/7uQNWvnIXmklGHyj2991?type=shareType')
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[2]/div/div[3]/figure/img')#失效
        print('二维码打开成功')
        sleep(3)

#####################################################################################################################################
#https://bd.kupeiai.com
#登录
    @BeautifulReport.add_test_img('test_bd_learnta_Login')
    def test_bd_learnta_Login(self):
        """论答商务合作-登录"""
        driver = self.driver
        self.driver.get('https://bd.learnta.com')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)


# 获取页面
    @BeautifulReport.add_test_img('test_bd_learnta_Page')
    def test_bd_learnta_Page(self):
        """论答商务合作-页面获取"""
        driver = self.driver
        self.driver.get('https://bd.learnta.com')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[1]')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="未获取到页面")
            if result == 'false':
                is_fail()

#刷新
    @BeautifulReport.add_test_img('test_bd_learnta_Refresh')
    def test_bd_learnta_Refresh(self):
        """论答商务合作-刷新测试"""
        driver = self.driver
        self.driver.get('https://bd.learnta.com')
        sleep(3)
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        try:
            driver.refresh()  # 刷新方法 refresh
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]')
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))



# 获取二维码
    @BeautifulReport.add_test_img('test_bd_learnta_GetQRCode')
    def test_bd_learnta_GetQRCode(self):
        """论答商务合作-获取二维码测试"""
        driver = self.driver
        self.driver.get('https://bd.learnta.com')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/span[1]').click()
        try:
            result = is_element_exist(self.driver, '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/canvas')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg='未获取到二维码')
            if result == 'false':
                is_fail()
        sleep(3)


#打开二维码链接
    @BeautifulReport.add_test_img('test_bd_learnta_OpenQRCode')
    def test_bd_learnta_OpenQRCode(self):
        """论答商务合作-打开二维码链接测试"""
        driver = self.driver
        self.driver.get('https://learnta.cn/bd/article/0u0GfDPDQUouCJQb285922?type=shareType')#失效
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[2]/div/div[3]/figure/img')
        sleep(3)


############################################################################################################################
#https://member.learnta.com
#登录
    @BeautifulReport.add_test_img('test_member_learnta_login')
    def test_member_learnta_login(self):
        """论答会员中心-登录"""
        driver = self.driver
        self.driver.get('https://member.learnta.com')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[1]')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="未获取到页面")
            if result == 'false':
                is_fail()


#获取页面
    @BeautifulReport.add_test_img('test_member_learnta_Page')
    def test_member_learnta_Page(self):
        """论答会员中心-获取页面测试"""
        driver = self.driver
        self.driver.get('https://member.learnta.com')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[1]')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="未获取到页面")
            if result == 'false':
                is_fail()

#刷新
    @BeautifulReport.add_test_img('test_member_learnta_Refresh')
    def test_member_learnta_Refresh(self):
        """论答会员中心-刷新测试"""
        driver = self.driver
        self.driver.get('https://member.learnta.com')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            driver.refresh()  # 刷新方法 refresh
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[1]')
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))


#获取二维码
    @BeautifulReport.add_test_img('test_member_learnta_GetQRCode')
    def test_member_learnta_GetQRCode(self):
        """论答会员中心-获取二维码测试"""
        driver = self.driver
        self.driver.get('https://member.learnta.com')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/span').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver, '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/canvas')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg='未获取到二维码')
            if result == 'false':
                is_fail()
        sleep(3)

# 打开二维码链接
    @BeautifulReport.add_test_img('test_member_learnta_OpenQRCode')
    def test_member_learnta_OpenQRCode(self):
        """论答会员中心-打开二维码链接测试"""
        driver = self.driver
        self.driver.get('https://learnta.cn/member/article/m5rVgRPNduLgpHLZ124420?type=shareType')
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[2]/div/div[3]/p[1]/span[1]/strong/span')


#######################################################################################################################################
#https://bd.kupeiai.com
#登录
    @BeautifulReport.add_test_img('test_bd_kupeiai_login')
    def test_bd_kupeiai_login(self):
        """酷培商务合作-登录测试"""
        driver = self.driver
        self.driver.get('https://bd.kupeiai.com')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[1]')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="未获取到页面")
            if result == 'false':
                is_fail()

#获取页面
    @BeautifulReport.add_test_img('test_bd_kupeiai_Page')
    def test_bd_kupeiai_Page(self):
        """酷培商务合作-获取页面测试"""
        driver = self.driver
        self.driver.get('https://bd.kupeiai.com')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[1]')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="未获取到页面")
            if result == 'false':
                is_fail()

#刷新
    @BeautifulReport.add_test_img('test_bd_kupeiai_Refrsh')
    def test_bd_kupeiai_Refrsh(self):
        """酷培商务合作-刷新测试"""
        driver = self.driver
        self.driver.get('https://bd.kupeiai.com')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            driver.refresh()  # 刷新方法 refresh
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[1]')
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))


#获取二维码
    @BeautifulReport.add_test_img('test_bd_kupeiai_GetQRcode')
    def test_bd_kupeiai_GetQRcode(self):
        """酷培商务合作-获取二维码测试"""
        driver = self.driver
        self.driver.get('https://bd.kupeiai.com')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/span[1]').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver, '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/canvas')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg='未获取到二维码')
            if result == 'false':
                is_fail()
        sleep(3)

#打开二维码链接
    @BeautifulReport.add_test_img('test_bd_kupeiai_OpenQRcode')
    def test_bd_kupeiai_OpenQRcode(self):
        """酷培商务合作-打开二维码链接测试"""
        driver = self.driver
        self.driver.get('https://www.learnta.cn/bdk/article/wzUROxlTDRyw16MH83259?type=shareType')#不失效
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[2]/div/div[1]').click()
        sleep(3)

 ##########################################################################################################################
#登录
    @BeautifulReport.add_test_img('test_partners_kupeiai_Login')
    def test_partners_kupeiai_Login(self):
        """论答合作伙伴-登录"""
        driver = self.driver
        self.driver.get('https://partners.kupeiai.com')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)

#获取页面
    @BeautifulReport.add_test_img('test_partners_kupeiai_Page')
    def test_partners_kupeiai_Page(self):
        """论答合作伙伴-获取页面测试"""
        driver = self.driver
        self.driver.get('https://partners.kupeiai.com')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[1]')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="未获取到页面")
            if result == 'false':
                is_fail()

#刷新
    @BeautifulReport.add_test_img('test_partners_kupeiai_Refresh')
    def test_partners_kupeiai_Refresh(self):
        """论答合作伙伴-刷新页面测试"""
        driver = self.driver
        self.driver.get('https://partners.kupeiai.com')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            driver.refresh()  # 刷新方法 refresh
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[1]')
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))



#获取二维码
    @BeautifulReport.add_test_img('test_partners_kupeiai_GetQRCode')
    def test_partners_kupeiai_GetQRCode(self):
        """论答合作伙伴-获取二维码测试"""
        driver = self.driver
        self.driver.get('https://partners.kupeiai.com')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/span[1]').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver, '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/canvas')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg='未获取到二维码')
            if result == 'false':
                is_fail()
        sleep(3)

#打开二维码链接
    @BeautifulReport.add_test_img('test_partners_kupeiai_OpenQRCode')
    def test_partners_kupeiai_OpenQRCode(self):
        """论答合作伙伴-打开二维码链接测试"""
        driver = self.driver
        self.driver.get('https://www.learnta.cn/partners/article/MbAgxB168Hh8J3aa25477?type=shareType')#不失效
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[2]/div/div[1]').click()
        sleep(3)


#######################################################################################################################################
#登录
    @BeautifulReport.add_test_img('test_bdw_learnta_Login')
    def test_bdw_learnta_Login(self):
        """微课·商务合作-登录"""
        driver = self.driver
        self.driver.get('https://bdw.learnta.com/signin')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)

# 获取页面
    @BeautifulReport.add_test_img('test_bdw_learnta_Page')
    def test_bdw_learnta_Page(self):
        """微课·商务合作-获取页面测试"""
        driver = self.driver
        self.driver.get('https://bdw.learnta.com/signin')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[1]')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="未获取到页面")
            if result == 'false':
                is_fail()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/span[1]').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[1]')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="未获取到页面")
            if result == 'false':
                is_fail()

#刷新
    @BeautifulReport.add_test_img('test_bdw_learnta_Refresh')
    def test_bdw_learnta_Refresh(self):
        """微课·商务合作-刷新页面测试"""
        driver = self.driver
        try:
            driver.refresh()  # 刷新方法 refresh
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[1]')
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))

#点击分享
    @BeautifulReport.add_test_img('test_bdw_learnta_Click')
    def test_bdw_learnta_Click(self):
        """微课·商务合作-点击分享测试"""
        driver = self.driver
        self.driver.get('https://bdw.learnta.com/signin')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[1]')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="未获取到页面")
            if result == 'false':
                is_fail()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/span[1]').click()

#获取二维码
    @BeautifulReport.add_test_img('test_bdw_learnta_GetQRCode')
    def test_bdw_learnta_GetQRCode(self):
        """微课·商务合作-获取二维码测试"""
        driver = self.driver
        self.driver.get('https://bdw.learnta.com/signin')
        sleep(3)
        # 输入手机号
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        # 输入验证码
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        # 点击登录
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/span[1]').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver, '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/canvas')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg='未获取到二维码')
            if result == 'false':
                is_fail()
        sleep(3)

#打开二维码链接
    @BeautifulReport.add_test_img('test_bdw_learnta_OpenQRCode')
    def test_bdw_learnta_OpenQRCode(self):
        """微课·商务合作-打开二维码链接测试"""
        driver = self.driver
        self.driver.get('https://www.learnta.cn/bdw/article/pxvFhwFRYvDy3xs8643?type=shareType')#失效
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[2]/div/div[3]/figure/img')



###########################################################################################################################################
#获取页面
    @BeautifulReport.add_test_img('test_CCNU_Login')
    def test_CCNU_Login(self):
        """CCNU获取页面"""
        driver = self.driver
        self.driver.get('https://learnta.cn/ccnu/home')
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/a/img')



######################################################################################################################################
    @BeautifulReport.add_test_img('test_qd_login')
    def test_qd_login(self):
        """渠道经理登录测试用例"""
        driver = self.driver
        self.driver.get('https://qd.kupeiai.com')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)


    @BeautifulReport.add_test_img('test_qd_Page')
    def test_qd_Page(self):
        """渠道经理获取页面"""
        driver = self.driver
        self.driver.get('https://qd.kupeiai.com')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver,'//*[@id="root"]/div/div/div/div[2]/div[2]/ul')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg="未获取到页面")
            if result == 'false':
                is_fail()


    @BeautifulReport.add_test_img('test_qd_refresh')
    def test_qd_refresh(self):
        """渠道经理刷新页面"""
        driver = self.driver
        self.driver.get('https://qd.kupeiai.com')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            driver.refresh()  # 刷新方法 refresh
            driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[2]/ul')
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))


    @BeautifulReport.add_test_img('test_qd_getcode')
    def test_qd_getcode(self):
        """渠道经理获取二维码测试"""
        driver = self.driver
        self.driver.get('https://qd.kupeiai.com')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/span[1]').click()
        sleep(3)
        try:
            result = is_element_exist(self.driver, '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/canvas')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg='未获取到二维码')
            if result == 'false':
                is_fail()
        sleep(3)
    @BeautifulReport.add_test_img('test_qd_opencode')
    def test_qd_opencode(self):
        """渠道经理打开二维码测试"""
        driver =self.driver
        self.driver.get('https://www.learnta.cn/qd/article/oheHch0OLtA1JqVw92?type=shareType')#不失效二维码
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[2]/div/div[3]/p[3]')



#########################################################################################################################33
    """LearntaPlus 商务合作登录"""
    def test_ilearnta_bd_login(self):
        "LearntaPlus商务合作登录"
        driver = self.driver
        self.driver.get('https://bd.ilearnta.com/signin')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()


        # 获取页面
    @BeautifulReport.add_test_img('test_ilearnta_bd_Page')
    def test_ilearnta_bd_Page(self):
        """LearntaPlus 商务合作-获取页面"""
        driver = self.driver
        self.driver.get('https://bd.ilearnta.com/signin')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[2]/ul')
        self.assertEqual(result, 'true', msg="未获取到页面")
        if result == 'false':
            is_fail()
        sleep(3)

    # 刷新界面
    @BeautifulReport.add_test_img('test_ilearnta_bd_Refresh')
    def test_ilearnta_bd_Refresh(self):
        """LearntaPlus 商务合作-刷新页面"""
        driver = self.driver
        self.driver.get('https://bd.ilearnta.com/signin')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            driver.refresh()  # 刷新方法 refresh
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[2]/ul')
        self.assertEqual(result, 'true', msg="未获取到页面")
        if result == 'false':
            is_fail()

    # 获取二维码
    @BeautifulReport.add_test_img('test_ilearnta_bd_GetQRCode')
    def test_ilearnta_bd_GetQRCode(self):
        """LearntaPlus 商务合作-获取二维码"""
        driver = self.driver
        self.driver.get('https://bd.ilearnta.com/signin')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/span[1]').click()
        sleep(2)
        try:
            result = is_element_exist(self.driver, '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/canvas')
        except:
            print('获取二维码失败')
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg='未获取到二维码')
            if result == 'false':
                is_fail()

        # 打开二维码链接
    @BeautifulReport.add_test_img('test_ilearnta_bd_OpenQRCode')
    def test_ilearnta_bd_OpenQRCode(self):
        """LearntaPlus 商务合作-打开二维码链接"""
        driver = self.driver
        self.driver.get('https://www.learnta.cn/ilearnta_bd/article/QYG6FQ7JYQC9qftG286?type=shareType')
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[2]/div/div[3]/figure/img')
        print('二维码打开成功')
        sleep(3)




###################################################################################################################################
    def test_ilearnta_partners_login(self):
        """LearntaPlus 合作伙伴登录"""
        driver = self.driver
        self.driver.get('https://partners.ilearnta.com/signin')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()


        # 获取页面

    @BeautifulReport.add_test_img('test_ilearnta_partners_Page')
    def test_ilearnta_partners_Page(self):
        """LearntaPlus 合作伙伴-获取页面"""
        driver = self.driver
        self.driver.get('https://partners.ilearnta.com/signin')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[2]/ul')
        self.assertEqual(result, 'true', msg="未获取到页面")
        if result == 'false':
            is_fail()
        sleep(3)

    # 刷新界面
    @BeautifulReport.add_test_img('test_ilearnta_partners_Refresh')
    def test_ilearnta_partners_Refresh(self):
        """LearntaPlus 合作伙伴-刷新页面"""
        driver = self.driver
        self.driver.get('https://partners.ilearnta.com/signin')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        try:
            driver.refresh()  # 刷新方法 refresh
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div/div/div[2]/div[2]/ul')
        self.assertEqual(result, 'true', msg="未获取到页面")
        if result == 'false':
            is_fail()

    # 获取二维码
    @BeautifulReport.add_test_img('test_ilearnta_partners_GetQRCode')
    def test_ilearnta_partners_GetQRCode(self):
        """LearntaPlus 合作伙伴-获取二维码"""
        driver = self.driver
        self.driver.get('https://partners.ilearnta.com/signin')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/button').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/span[1]').click()
        sleep(2)
        try:
            result = is_element_exist(self.driver, '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/canvas')
        except:
            print('获取二维码失败')
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true', msg='未获取到二维码')
            if result == 'false':
                is_fail()

        # 打开二维码链接

    @BeautifulReport.add_test_img('test_ilearnta_partners_OpenQRCode')
    def test_ilearnta_partners_OpenQRCode(self):
        """LearntaPlus 合作伙伴-打开二维码链接"""
        driver = self.driver
        self.driver.get('https://www.learnta.cn/ilearnta_partners/article/yBApRfqGqXCQFPmC141?type=shareType')
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[2]/div/div[3]/figure/img')
        print('二维码打开成功')
        sleep(3)



    @BeautifulReport.add_test_img('test_official_login')
    def test_official_login(self):
        """官网网站后台登录"""
        driver =self.driver
        self.driver.get('https://www.learnta.cn/official_admin#/signin=')
        driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="code"]/input').send_keys(code)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button').click()
        sleep(3)
        result = is_element_exist(self.driver, '//*[@id="root"]/div/div[1]/div/ul')
        self.assertEqual(result, 'true', msg="登陆失败")
        if result == 'false':
            is_fail()

    @BeautifulReport.add_test_img('test_official_refresh')
    def test_official_refresh(self):
        """官网后台刷新跳转"""
        driver =self.driver
        self.driver.get('https://www.learnta.cn/official_admin')
        sleep(2)
        try:
            driver.refresh()  # 刷新方法 refresh
            print('刷新成功')
        except Exception as e:
            print("Exception found", format(e))
        result = is_element_exist(self.driver, '//*[@id="mobile"]')
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
    runner.report(filename='../所有商务网站测试报告.html', description='所有商务网站测试报告', log_path=report_dir)
    print(report_dir)
    print(filename)
elif (platform.system() == 'Linux'):
    report_dir = "/opt/uitest/report"
    filename = '/opt/uitest/img'
    runner.report(filename='../所有商务网站测试报告.html', description='所有商务网站测试报告', report_dir=report_dir)
    print(report_dir)
    print(filename)
    print(platform.system())
else:
    print(platform.system())
