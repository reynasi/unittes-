# -*- coding:utf-8 -*-
import os
import traceback
import platform

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

env = 't2.'
org4 = 'zjt2.'
orgx = 'zjt2.'
orgai = 'bcq.'
mobil = '18301010101'
code = '1111'


def getreport():
    if 'Windows' in platform.platform():
        return os.path.abspath('./report')
    else:
        return '/opt/uitest/report'


def getimg():
    if 'Windows' in platform.platform():
        return os.path.abspath('D:\\Material\\python\\uitest\\zhangjinjin\\test\\img')
    else:
        return '/opt/uitest/img'


def getcase():
    if 'Windows' in platform.platform():
        return os.path.abspath('.')
    else:
        return '/opt/uitest/zhangjinjin/test/case'


def obvious_wait_click(driver, xpath, prompt='err_message'):
    """
显示等待并点击
    :param driver:
    :param xpath: 等待的元素xpath路径
    :param prompt: 报错信息，默认：err_message
    """
    locat = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
    # driver.execute_script("arguments[0].scrollIntoView();", locat)
    driver.execute_script("arguments[0].click();", locat)


def actionclickelement(driver, xpath, prompt='err_message'):
    locat = driver.find_element_by_xpath(xpath)
    actions = ActionChains(driver)
    actions.move_to_element(locat).perform()
    actions.click(locat).perform()


def obvious_wait_sendkeys(driver, xpath, keys, prompt='err_message'):
    """
显示等待并输入
    :param driver:
    :param xpath: 等待的元素xpath路径
    :param keys: 输入的信息
    :param prompt: 报错信息，默认：err_message
    """

    locat = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
    locat.send_keys(keys)


def new_tab_cn(driver, project):
    """
在新的标签页打开链接,访问方式：learna.cn/*
    :param project: 项目名
    """
    org = ''
    type = 'learnta'
    if (project == 'teacher4') | (project == 'student4'):
        org = org4
    elif project == 'teacherx':
        org = orgx
    elif (project == 'teacher') | (project == 'student'):
        org = orgai
        type = 'kupeiai'
    # url = 'window.open("http://' + org + env + type + '.cn/' + project + '");'
    # driver.execute_script(url)
    # handls = driver.window_handles
    # driver.switch_to.window(handls[-1])
    driver.get('http://' + org + env + type + '.cn/' + project)


def new_tab_com(driver, project):
    """
在新的标签页打开链接,访问方式：*.learna.com
    :param driver: 驱动
    :param project: 项目名
    """
    type = 'learnta'
    if (project == 'partners') | (project == 'bdk'):
        type = 'kupeiai'
    # url = 'window.open("http://' + project + '.' + env + type + '.com");'
    # driver.execute_script(url)
    # handls = driver.window_handles
    # driver.switch_to.window(handls[-1])
    driver.get('http://' + project + '.' + env + type + '.com')
    # return url


def login(driver, mobil_xpath, code_xpath, btn_xpath, prompt="err_message", m=None, c=None):
    """
各项目的登录界面输入信息并点击登录
    :param driver: 浏览器驱动
    :param mobil_xpath: 账号xpath路径
    :param code_xpath: 验证码xpath路径
    :param btn_xpath: 登录按钮xpath路径
    :param prompt: 报错信息
    :param m: 账号，默认同设置的mobil
    :param c: 验证码，默认同设置的code
    """
    if m is None:
        m = mobil
    if c is None:
        c = code
    obvious_wait_sendkeys(driver, mobil_xpath, m, prompt + ': 输入账号')
    obvious_wait_sendkeys(driver, code_xpath, c, prompt + ': 输入验证码')
    obvious_wait_click(driver, btn_xpath, prompt + ': 点击登录')


def is_element_exist(driver, xpath, prompt="err_message"):
    """
根据xpath判断元素是否存在，显示等待5秒
    :param driver:
    :param xpath: 元素xpath路径
    :param prompt: 报错信息,默认:err_message
    """
    result = 'true'
    try:
        WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
    except:
        result = 'false'
        traceback.print_exc()
    finally:
        return result


def is_element_exist2(driver, xpath, prompt="err_message"):
    """
根据xpath判断元素是否存在，显示等待5秒
    :param driver:
    :param xpath: 元素xpath路径
    :param prompt: 报错信息,默认:err_message
    """
    result = 'true'
    try:
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
    except:
        result = 'false'
        traceback.print_exc()
    finally:
        return result


def is_branch_exist(driver, xpath, project):
    """
判断分校是否存在，若存在返回true
    :param driver:
    :param xpath:
    :param project:
    :return: true:存在分校；false：没有分校
    """
    result = 'false'
    names = driver.find_elements_by_xpath(xpath)
    lists = []
    for i in names:
        a = i.text
        lists.append(a)
    length = len(lists[0].split('\n'))
    if 'teacher' in project:
        if length == 3:
            result = 'true'
    elif project == 'student4':
        if length == 4:
            result = 'true'
    elif project == 'student':
        if length == 2:
            result = 'true'
    return result


def get_elements(driver, xpath, prompt='err_message'):
    """
通过任务卡顶层div判断有几个任务卡，并返回相应数量
    :param driver:
    :param xpath:
    :param prompt:
    :return: 任务卡数量
    """
    top_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
    lis = top_div.find_elements_by_xpath('div')
    return len(lis)


def is_have_verify(driver):
    """
判断是否存在“正在审核”提示弹窗，若存在则审核通过
    :param driver:
    """
    is_exist = is_element_exist(driver, '//*[@class="ant-modal ant-confirm ant-confirm-error"]', '判断是否是正在审核的提示弹窗')
    if is_exist == 'true':
        obvious_wait_click(driver, '//*[@class="ant-modal ant-confirm ant-confirm-error"]/div/div/div/div[2]/button',
                           '点击正在审核提示弹窗确认按钮')
        obvious_wait_click(driver, '//*[@id="2$Menu"]/li[4]', '点击课程审核')
        obvious_wait_click(driver, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div['
                                   '1]/div/div/a/div[1]/div[1]', '进入审核课程')
        obvious_wait_click(driver, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[1]/div/div/div/button[1]',
                           '触发审核通过弹窗')
        obvious_wait_click(driver, '//*[@class="ant-confirm-body-wrapper"]/div[2]/button[2]',
                           '审核通过')
        obvious_wait_click(driver, '//*[@id="2$Menu"]/li[1]', '点击我的课程')
        obvious_wait_click(driver, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div['
                                   '1]/div/div/a', '进入课程')
        obvious_wait_click(driver, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[1]/div/div/a', '点击更多')
        obvious_wait_click(driver, '//*[@class="ant-dropdown ant-dropdown-placement-bottomCenter"]/ul/li[1]',
                           '触发提交审核弹窗')
