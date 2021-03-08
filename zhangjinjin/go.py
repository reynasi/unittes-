# -*- coding:utf-8 -*-
# 公众号智能测评

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import traceback


# 设定浏览器启动模式
# mobileEmulation = {'deviceName': 'iPhone 6'}
options = webdriver.ChromeOptions()
# options.add_experimental_option('mobileEmulation', mobileEmulation)
options.add_argument("start-maximized")
# 创建驱动实例
driver = webdriver.Chrome(options=options)
# 设定浏览器坐标
#driver.set_window_position(x=600, y=0)
# 打开公众号测评登录页面
driver.get("https://t1.learnta.cn/go/#/kupei/signin")
time.sleep(1)
# 输入用户名
driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[1]/input").send_keys("test")
# 输入电话
driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[2]/input").send_keys("18302020202")
# 输入验证码
driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[3]/input").send_keys("1111")
# 点击登录
driver.find_element_by_xpath("//*[@id='root']/div/div/form/a/span").click()
print("----->登录")
time.sleep(3)
#选择年级
driver.find_element_by_xpath("//*[@id='root']/div/div[2]/ul/li[1]").click()
print("----->选择年级")
time.sleep(1)
# 选择科目
driver.find_element_by_xpath("//*[@id='root']/div/div[2]/ul/li[2]/span[2]").click()
time.sleep(1)
print("----->选择科目")

# 定义查询下一题按钮方法，1表示出现，0表示不出现
def findNext(driver):
    fnext = 1
    try:
        print ("----->查找第下一题按钮")
        locator = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div/div[2]/a[2]")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        print("----->找到下一题按钮")
    except:
        print("----->找不到下一题按钮")
        print("----->报告页")
        fnext = 0
    finally:
        return fnext

# 定义审题弹框处理
def findReview(driver):
    try:
        locator = (By.XPATH, "/html/body/div[3]/div[2]/div")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        print("----->出现弹窗")
        # 点击“知道了”按钮
        print("----->点击弹窗确定框")
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[2]/a").click()
    except :
        print("----->无弹窗出现，出现报错")
        traceback.print_exc()

# 记录题目数量
num = 0
# 循环做题
while findNext(driver):
    # 点击下一题按钮
    try:
        driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[2]/div/div[2]/a[2]").click()
        num = num +1
        print("----->第 %d 道题完成" % (num))
    except:
        # 判断是否出现审题弹框提示
        findReview(driver)

# 关闭浏览器
driver.close()

# 手机型号
mobile_emulation = {
            "deviceName": "Apple iPhone 3GS",
            "deviceName": "Apple iPhone 4",
            "deviceName": "Apple iPhone 5",
            "deviceName": "Apple iPhone 6",
            "deviceName": "Apple iPhone 6 Plus",
            "deviceName": "BlackBerry Z10",
            "deviceName": "BlackBerry Z30",
            "deviceName": "Google Nexus 4",
            "deviceName": "Google Nexus 5",
            "deviceName": "Google Nexus S",
            "deviceName": "HTC Evo, Touch HD, Desire HD, Desire",
            "deviceName": "HTC One X, EVO LTE",
            "deviceName": "HTC Sensation, Evo 3D",
            "deviceName": "LG Optimus 2X, Optimus 3D, Optimus Black",
            "deviceName": "LG Optimus G",
            "deviceName": "LG Optimus LTE, Optimus 4X HD" ,
            "deviceName": "LG Optimus One",
            "deviceName": "Motorola Defy, Droid, Droid X, Milestone",
            "deviceName": "Motorola Droid 3, Droid 4, Droid Razr, Atrix 4G, Atrix 2",
            "deviceName": "Motorola Droid Razr HD",
            "deviceName": "Nokia C5, C6, C7, N97, N8, X7",
            "deviceName": "Nokia Lumia 7X0, Lumia 8XX, Lumia 900, N800, N810, N900",
            "deviceName": "Samsung Galaxy Note 3",
            "deviceName": "Samsung Galaxy Note II",
            "deviceName": "Samsung Galaxy Note",
            "deviceName": "Samsung Galaxy S III, Galaxy Nexus",
            "deviceName": "Samsung Galaxy S, S II, W",
            "deviceName": "Samsung Galaxy S4",
            "deviceName": "Sony Xperia S, Ion",
            "deviceName": "Sony Xperia Sola, U",
            "deviceName": "Sony Xperia Z, Z1",
            "deviceName": "Amazon Kindle Fire HDX 7″",
            "deviceName": "Amazon Kindle Fire HDX 8.9″",
            "deviceName": "Amazon Kindle Fire (First Generation)",
            "deviceName": "Apple iPad 1 / 2 / iPad Mini",
            "deviceName": "Apple iPad 3 / 4",
            "deviceName": "BlackBerry PlayBook",
            "deviceName": "Google Nexus 10",
            "deviceName": "Google Nexus 7 2",
            "deviceName": "Google Nexus 7",
            "deviceName": "Motorola Xoom, Xyboard",
            "deviceName": "Samsung Galaxy Tab 7.7, 8.9, 10.1",
            "deviceName": "Samsung Galaxy Tab",
            "deviceName": "Notebook with touch",
            "deviceName": "iPhone 6"
}
