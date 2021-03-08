# -*- coding:utf-8 -*-

#教学测评

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import traceback

driver = webdriver.Chrome()
driver.get("https://t3.learnta.cn/__api/wechat/public/qRcode/chargeExam/3cVza3jYf2rq6rMy73871")
driver.find_element_by_xpath("//*[@id='root']/div/form/div[1]/input").send_keys("test")
driver.find_element_by_xpath("//*[@id='root']/div/form/div[2]/input").send_keys("18301010101")
driver.find_element_by_xpath("//*[@id='root']/div/form/div[3]/input").send_keys("1111")
driver.find_element_by_xpath("//*[@id='root']/div/form/a/span").click()

# 开始测评
element = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[3]/div/ul/li[1]")))
# 防报错处理，点击开始测评按钮功能
driver.execute_script("arguments[0].click();", element)


# 定义查询下一题按钮方法，1表示出现，0表示不出现
def find_next(driver):
    fnext = 1
    try:
        print ("----->查找第下一题按钮")
        locator = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]")
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(locator),"找不到下一题按钮")
        print("----->找到下一题按钮")
    except:
        print("----->无下一题按钮,做题结束")
        print("----->报告页")
        fnext = 0
    finally:
        return fnext

# 记录题目数量
num = 0
# 循环做题
while find_next(driver):
    try:
        # 点击下一题按钮
        nextQuestion = WebDriverWait(driver, 5).until(EC.presence_of_element_located((\
            By.XPATH, "//*[@id='root']/div/div/div/div/div/div/div/div[2]/div/a[2]"))\
            ,"无法点击下一个按钮")
        # 防报错处理，点击下一题按钮功能
        driver.execute_script("arguments[0].click();", nextQuestion)

        # 点击确定弹窗
        confirm = WebDriverWait(driver, 5).until(EC.presence_of_element_located((\
            By.XPATH, "/html[@class='windows desktop landscape g-verdor-learnta g-Product-task g-for-self']/body/div[5]/div/div[@class='ant-modal-wrap ']/div[@class='ant-modal ant-confirm ant-confirm-confirm']/div[@class='ant-modal-content']/div[@class='ant-modal-body']/div[@class='ant-confirm-body-wrapper']/div[@class='ant-confirm-btns']/button[@class='ant-btn ant-btn-primary ant-btn-lg']/span"))\
            ,"无法定位确定弹窗")
        # 防报错处理，点击确定按钮功能
        driver.execute_script("arguments[0].click()", confirm)

        # 题目数增加1
        num = num +1
        print("----->第 %d 道题完成" % (num))
    except:
        traceback.print_exc()
        print("----->做题报错")
        break

# 报告页停留3秒
time.sleep(3)
# 关闭浏览器
driver.quit()

