# -*- coding:utf-8 -*-
import os
import platform
import traceback

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

env = ''
org4 = 'learnta.'
orgx = 'i.'
orgai = 'bcq.'
mobil = '18616215375'
code = '1111'


def getreport():
    """
    获取报告页存储路径，若在本机则返回report文件所在路径，若在服务器则返回服务器中写死的路径
    :return: 报告页存储路径
    """
    if 'Windows' in platform.platform():
        return os.path.abspath('./report')
    else:
        return '/opt/uitest/report'


def getimg():
    """
    获取截图存储路径，若在本机则返回img文件所在路径，若在服务器则返回服务器中写死的路径
    :return: 截图所在的路径
    """
    if 'Windows' in platform.platform():
        return os.path.abspath('D:\\Material\\python\\uitest\\zhangjinjin\\render\\img')
    else:
        return '/opt/uitest/img'


def getcase():
    """
    获取测试用例路径，若在本机则返回当前路径，若在服务器则返回服务器中写死的路径
    :return: 测试用例所在的路径
    """
    if 'Windows' in platform.platform():
        return os.path.abspath('.')
    else:
        return '/opt/uitest/zhangjinjin/render/case'


def obvious_wait_click(driver, xpath, prompt='err_message'):
    """
显示等待并点击
    :param driver:
    :param xpath: 等待的元素xpath路径
    :param prompt: 报错信息，默认：err_message
    """
    locat = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
    driver.execute_script("arguments[0].click();", locat)


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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
    except:
        result = 'false'
        traceback.print_exc()
    finally:
        return result


def is_branch_exist(driver, xpath, project):
    """
    判断机构是否存在分校
    :param driver:
    :param xpath: 顶级的from表单xpath路径
    :param project: 项目名
    :return:
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


def is_fail():
    result = "false"
    return result

