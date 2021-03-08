# -*- coding:utf-8 -*-

# 招生测评
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import traceback


# mobileEmulation = {'deviceName': 'iPhone 6'}
# options = webdriver.ChromeOptions()
# options.add_experimental_option('mobileEmulation', mobileEmulation)
#options.add_argument("start-maximized")

# 显示等待 & 点击
def obvious_wait_click(driver, xpath, prompt):
    locat = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
    driver.execute_script("arguments[0].click();", locat)


# 创建驱动实例
driver = webdriver.Chrome()
# 设定浏览器坐标
# driver.set_window_position(x=600, y=0)
# 打开招生测评链接
driver.get("https://t3.learnta.cn/__api/wechat/public/qRcode/activity/798")
# 输入用户名
driver.find_element_by_xpath("//*[@id='root']/div/div[2]/form/div[1]/input").send_keys("test")
print("----->输入用户名")
# 输入电话号码
driver.find_element_by_xpath("//*[@id='root']/div/div[2]/form/div[2]/input").send_keys("18301010101")
print("----->输入电话号码")
# 输入验证码
driver.find_element_by_xpath("//*[@id='root']/div/div[2]/form/div[3]/input").send_keys("1111")
print("----->输入验证码")
# 点击登录
driver.find_element_by_xpath("//*[@id='root']/div/div[2]/form/a/span").click()
print("----->点击登录")
# 点击开始测评
obvious_wait_click(driver, "//*[@id='root']/div/div[3]/div/ul/li[1]", "无法点击开始测评")
print("----->点击开始测评")
# 选择科目
obvious_wait_click(driver, "//*[@id='root']/div/div[2]/div/div/ul/li[1]", "无法选择科目")
print("----->选择科目")
# 选择年级
# obvious_wait_click(driver, "/html[@class='windows desktop landscape g-verdor-learnta g-Product-task g-for-self']/body/div[@id='root']/div[@class='mRecruitHome']/div[@class='mRecruit-content']/div/div[@class='step step-2']/ul/li[1]", "无法选择年级")
obvious_wait_click(driver, "//*[@id='root']/div/div[2]/div/div/ul/li[4]", "无法选择年级")
print("----->选择年级")


# 定义查询下一题按钮方法，1表示出现，0表示不出现
def find_next(driver):
    fnext = 1
    try:
        print("----->查找第下一题按钮")
        locator = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        print("----->找到下一题按钮")
    except:
        print("----->找不到下一题按钮")
        print("----->报告页")
        fnext = 0
    finally:
        return fnext

# 处理操作确认弹窗
# def operationConfirmation(driver):
#     driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[1]/div")
#     try:
#         locator = (By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div")
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
#         print("========出现弹窗=========")
#         # 点击“确定”按钮
#         print("========点击弹窗确定框=========")
#         driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[1]/div/div/div[2]/button[2]/span").click()
#     except :
#         print("========无弹窗出现=========")

# 记录题目数量
num = 0
# 循环做题
while find_next(driver):
    # 点击下一题按钮
    try:
        obvious_wait_click(driver, "//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]", "无法点击下一题按钮")
        obvious_wait_click(driver, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/div[2]/button[2]/span", "无法点击确定弹窗")
        num = num +1
        print("----->第 %d 道题完成" % (num))
    except:
        # 判断是否出现审题弹框提示
        traceback.print_exc()
        break

# 等待2s
time.sleep(2)
# 关闭浏览器
# driver.quit()
driver.close()