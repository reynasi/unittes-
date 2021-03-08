# -*- encoding=utf8 -*-
__author__ = "chenjun"

from airtest.core.api import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver=webdriver.Chrome()

#driver = WebChrome()
driver.implicitly_wait(20)

driver.get("https://autotestx.learnta.cn/teacherx")
#driver.find_element_by_xpath("//div[@style='display: block; user-select: none;']").click()
#driver.find_element_by_xpath("/html/body/div[4]/div/div/div/ul/li").click()
driver.find_element_by_xpath("//input[@placeholder='请输入手机号码']").send_keys('18817572035')
driver.find_element_by_xpath("//input[@placeholder='请输入验证码']").send_keys("1111")
driver.find_element_by_xpath("//button[@type='submit']").click()


def getElementNum():
    elements = driver.find_elements_by_class_name("subSystemMenuContainer")
    lists = []
    for num in elements:
        temp = num.text
        lists.append(temp)
    truelist = lists[0].splitlines() 
    ElementNum = len(truelist)
    return ElementNum


loopNum = getElementNum()
for i in range(loopNum):
    divNum = str(i+1)
    print(divNum)
    print (type(divNum))
    elementText = driver.find_element_by_xpath("//*[@id=\"root\"]/div/header/div/div/div[2]/div[" + divNum + "]/div[2]").text
    print (elementText)
    driver.find_element_by_xpath("//*[@id=\"root\"]/div/header/div/div/div[2]/div[" + divNum + "]/div[2]").click()
    sleep(2);
    driver.find_element_by_xpath("//img[@src='https://lcdns-pic.learnta.com/defaultLogo_02.png']").click()
driver.quit()

auto_setup(__file__)
