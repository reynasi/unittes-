import os
import platform
import time
import traceback
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def getreport():

    if 'Windows' in platform.platform():
        return os.path.abspath('./report')
    else:
        return '/opt/uitest/report'


def getimg():
    if 'Windows' in platform.platform():
        return os.path.abspath('D:\\Material\\python\\uitest\\zhangjinjin\\go\\img')
    else:
        return '/opt/uitest/img'


def getcase():
    if 'Windows' in platform.platform():
        return os.path.abspath('.')
    else:
        return '/opt/uitest/zhangjinjin/go/case'


# 定义查询下一题按钮方法，1表示出现，0表示不出现
def findNext(driver):
    fnext = 1
    try:
        time.sleep(1)
        print ("----->查找第下一题按钮")
        driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[2]/div/div[2]/a[2]")
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div/div[2]/a[2]")), "查找下一题")
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
        print("----->找到下一题按钮")
    except:
        print("----->找不到下一题按钮")
        print("----->报告页")
        time.sleep(2)
        fnext = 0
    finally:
        return fnext

# 定义审题弹框处理
def findReview(driver):
    # try:
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div")
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
    print("----->出现弹窗")
    # 点击“知道了”按钮
    print("----->点击弹窗确定框")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[2]/a").click()
    # except :
    #     print("----->无弹窗出现，出现报错")
    #     traceback.print_exc()
