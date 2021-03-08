# -*- coding:utf-8 -*-
# 备课系统练习卡

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import traceback


# 显示等待 & 点击
def obvious_wait_click(driver, xpath, prompt):
    locat = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
    driver.execute_script("arguments[0].click();", locat)


driver = webdriver.Chrome()
# driver.set_window_position(x=600, y=0)
driver.get("https://t3.learnta.cn/__api/wechat/public/qRcode/library/dUYjMa6o3n3UiM1L73901")
print("----->打开登录界面")
driver.find_element_by_xpath("//*[@id='root']/div/form/div[1]/input").send_keys("test")
print("----->输入用户名")
driver.find_element_by_xpath("//*[@id='root']/div/form/div[2]/input").send_keys("18301010101")
print("----->输入账号")
driver.find_element_by_xpath("//*[@id='root']/div/form/div[3]/input").send_keys("1111")
print("----->输入验证码")
obvious_wait_click(driver, "//*[@id='root']/div/form/a/span", "无法点击登录")
print("----->点击登录")


# 定义查询下一题按钮方法，1表示出现，0表示不出现
def find_next(driver):
    fnext = 1
    print("----->查找第下一题按钮")
    try:
        locator = (By.XPATH, "//*[@id='root']/div/div/div/div/div[2]/div/div[1]/div/a[2]")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
        print("----->找到下一题按钮")
    except:
        print("----->找不到下一题按钮")
        fnext = 0
    finally:
        return fnext


# 提交答案弹框处理，1：出现，0：不出现
def submit_answer(driver):
    sub = 0
    try:
        locator = (By.XPATH, "/html/body/div[4]/div/div[2]/div/div[1]/div/div")
        WebDriverWait(driver, 2).until(EC.presence_of_element_located(locator))
        print("----->出现提交答案弹框")
        sub = 1
    finally:
        return sub


# 记录题目数量
num = 0
# 循环做题
while find_next(driver):
    try:
        obvious_wait_click(driver, "//*[@id='root']/div/div/div/div/div[2]/div/div[1]/div/a[2]", "无法点击下一题按钮")
        print("----->点击下一题按钮")
        num = num +1
        print("----->第 %d 道题完成" % (num))
        if submit_answer(driver):
            obvious_wait_click(driver, "/html/body/div[4]/div/div[2]/div/div[1]/div/div/div[2]/button/span", "无法点击确认提交答案按钮")
            print("----->确认提交答案")
            print("----->报告页")
            break
    except:
        # 判断是否出现确认提交弹框提示
        traceback.print_exc()
        break


time.sleep(2)
driver.quit()


