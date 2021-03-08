# -*- coding:utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import traceback

env = 't3.'
org4 = 'zjt3.'
orgx = 'learnta.'
orgai = 'onlyai.'
mobil = '18301010101'
code = '1111'
# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()


# def close_all_tab():
#     handles = driver.window_handles
#     for clo in handles:
#         driver.switch_to.window(clo)
#         driver.close

def obvious_wait_click(xpath, prompt='err_message'):
    """
显示等待并点击
    :param xpath: 等待的元素xpath路径
    :param prompt: 报错信息，默认：err_message
    """
    locat = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
    driver.execute_script("arguments[0].click();", locat)


def obvious_wait_sendkeys(xpath, keys, prompt='err_message'):
    """
显示等待并输入
    :param xpath: 等待的元素xpath路径
    :param keys: 输入的信息
    :param prompt: 报错信息，默认：err_message
    """
    locat = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)
    locat.send_keys(keys)


def new_tab_cn(project):
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
    url = 'window.open("http://' + org + env + type + '.cn/' + project + '");'
    driver.execute_script(url)
    handls = driver.window_handles
    driver.switch_to.window(handls[-1])
    return url


def new_tab_com(project):
    """
在新的标签页打开链接,访问方式：*.learna.com
    :param project: 项目名
    """
    type = 'learnta'
    if (project == 'partners') | (project == 'bdk'):
        type = 'kupeiai'
    url = 'window.open("http://' + project + '.' + env + type + '.com");'
    driver.execute_script(url)
    handls = driver.window_handles
    driver.switch_to.window(handls[-1])
    return url


def login(mobil_xpath, code_xpath, btn_xpath, prompt="err_message", m=None, c=None):
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
    obvious_wait_sendkeys(mobil_xpath, m, prompt + ': 输入账号')
    obvious_wait_sendkeys(code_xpath, c, prompt + ': 输入验证码')
    obvious_wait_click(btn_xpath, prompt + ': 点击登录')


def is_element_exist(xpath, prompt="err_message"):
    """
根据xpath判断元素是否存在，显示等待5秒
    :param xpath: 元素xpath路径
    :param prompt: 报错信息,默认:err_message
    """
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)), prompt)


def is_branch_exist(xpath, project):
    """
判断是否存在分校，存在返回true,不存在返回false
    :param xpath: 表单顶端元素xpath路径
    :param project: 项目名
    :return: 判断结果，存在返回true,不存在返回false
    """
    result = 'false'
    names = driver.find_elements_by_xpath(xpath)
    lists = []
    for i in names:
        a = i.text
        lists.append(a)
    length = len(lists[0].split('\n'))
    if (project == 'teacher4') | (project == 'teacherx'):
        if length == 3:
            result = 'true'
    elif project == 'student4':
        if length == 4:
            result = 'true'
    elif project == 'student':
        if length == 2:
            result = 'true'
    return result


pass_project = []  # list
fail_project = {}  # 字典


# teacher4自定义域名内容库
url = 'http://hc.zhihuichaoren.com/teacher4'
driver.get(url)
try:
    is_element_exist('//*[@id="root"]/div/div[1]/div/div[1]/p/b', 'teacher4自定义域名登录页')
    mobil_xpath = "//*[@id='username']"
    code_xpath = "//*[@id='code']"
    branch = is_branch_exist('//*[@id="root"]/div/div[1]/div/form', 'teacher4')
    if branch == 'true':
        obvious_wait_click('//*[@id="root"]/div/div[1]/div/form/div[1]/div/div/div/div/span', '选择校区')
        obvious_wait_click('/html/body/div[4]/div/div/div/ul/li[1]', '选择总校区')
        btn_xpath = '//*[@id="root"]/div/div[1]/div/form/div[4]/button'
    else:
        btn_xpath = "//*[@id='root']/div/div[1]/div/form/div[3]/button/span"
    login(mobil_xpath, code_xpath, btn_xpath, 'teacher4')
    obvious_wait_click("//*[@id='root']/div/header/div[1]/div[2]/div[3]", "内容库")
    is_element_exist("//*[@id='contentAdmin']", "内容库iframe")
    driver.switch_to.frame("contentAdmin")
    is_element_exist('//*[@id="题  库$Menu"]/li[2]/span/span[2]', '我的题库')
    obvious_wait_click('//*[@id="题  库$Menu"]/li[2]/span/span[2]', "我的题库点击")
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# teacher4内容库
project = 'teacher4'
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div[1]/div/div[1]/p/b', 'teacher4登录页')
    mobil_xpath = "//*[@id='username']"
    code_xpath = "//*[@id='code']"
    branch = is_branch_exist('//*[@id="root"]/div/div[1]/div/form', project)
    if branch == 'true':
        obvious_wait_click('//*[@id="root"]/div/div[1]/div/form/div[1]/div/div/div/div/span', '选择校区')
        obvious_wait_click('/html/body/div[4]/div/div/div/ul/li[1]', '选择总校区')
        btn_xpath = '//*[@id="root"]/div/div[1]/div/form/div[4]/button'
    else:
        btn_xpath = "//*[@id='root']/div/div[1]/div/form/div[3]/button/span"
    login(mobil_xpath, code_xpath, btn_xpath, 'teacher4')
    obvious_wait_click('//*[@id="root"]/div/header/div[1]/div[1]/div[2]/div[3]', "内容库")
    is_element_exist("//*[@id='contentAdmin']", "内容库iframe")
    driver.switch_to.frame("contentAdmin")
    is_element_exist('//*[@id="题  库$Menu"]/li[2]/span/span[2]', '我的题库')
    obvious_wait_click('//*[@id="题  库$Menu"]/li[2]/span/span[2]', "我的题库点击")
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# teacherx内容库
project = "teacherx"
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div[1]/div/div[1]/p/b', project + '登录页')
    mobil_xpath = "//*[@id='username']"
    code_xpath = "//*[@id='code']"
    branch = is_branch_exist('//*[@id="root"]/div/div[1]/div/form', project)
    if branch == 'true':
        obvious_wait_click('//*[@id="root"]/div/div[1]/div/form/div[1]/div/div/div/div/span', '选择校区')
        obvious_wait_click('/html/body/div[4]/div/div/div/ul/li[1]', '选择总校区')
        btn_xpath = '//*[@id="root"]/div/div[1]/div/form/div[4]/button'
    else:
        btn_xpath = "//*[@id='root']/div/div[1]/div/form/div[3]/button/span"
    login(mobil_xpath, code_xpath, btn_xpath, project)
    obvious_wait_click('//*[@id="root"]/div/header/div[1]/div[1]/div[2]/div[5]/div[2]', '题库点击')  # 进入题库
    is_element_exist("//*[@id='contentAdmin']", "题库iframe")
    driver.switch_to.frame("contentAdmin")
    obvious_wait_click('//*[@id="root"]/div/div/div/div/div/div/div[2]/div/div[1]/div[1]', "英语题库点击")
    driver.switch_to.default_content()
    obvious_wait_click('//*[@id="root"]/div/header/h1/img', '进入选择界面')
    obvious_wait_click('//*[@id="root"]/div/header/div[1]/div[1]/div[2]/div[7]', '多媒体库点击')  # 进入多媒体库
    is_element_exist("//*[@id='contentAdmin']", "多媒体库iframe")
    driver.switch_to.frame('contentAdmin')
    obvious_wait_click('//*[@id="多媒体库$Menu"]/li[2]/span/span[2]', '我的视频点击')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# TAD学生端(student4)
project = "student4"
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div[1]/div', project + '登录页')
    mobil_xpath = '//*[@id="username"]'
    code_xpath = '//*[@id="password"]'
    branch = is_branch_exist('//*[@id="root"]/div/div[1]/div/form', project)
    if branch == 'true':
        obvious_wait_click('//*[@id="branch"]/div/span', '选择校区')
        obvious_wait_click('/html/body/div[3]/div/div/div/ul/li[1]', '选择总校区')
        btn_xpath = '//*[@id="root"]/div/div[1]/div/form/div[4]/div/div/span/button'
    else:
        btn_xpath = '//*[@id="root"]/div/div[1]/div/form/div[3]/div/div/span/button'
    login(mobil_xpath, code_xpath, btn_xpath, project, "18300000001", "000001")
    is_element_exist("//*[@id='root']/div/aside/div[1]/img", "TAD学生端")
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# TAD自定义域名学生端(student4)
url = 'window.open("http://hc.zhihuichaoren.com/student4")'
driver.execute_script(url)
handls = driver.window_handles
driver.switch_to.window(handls[-1])
try:
    is_element_exist('//*[@id="root"]/div/div[1]/div', 'TAD自定义域名学生端登录页')
    mobil_xpath = '//*[@id="username"]'
    code_xpath = '//*[@id="password"]'
    branch = is_branch_exist('//*[@id="root"]/div/div[1]/div/form', project)
    if branch == 'true':
        obvious_wait_click('//*[@id="branch"]/div/span', '选择校区')
        obvious_wait_click('/html/body/div[3]/div/div/div/ul/li[1]', '选择总校区')
        btn_xpath = '//*[@id="root"]/div/div[1]/div/form/div[4]/div/div/span/button'
    else:
        btn_xpath = '//*[@id="root"]/div/div[1]/div/form/div[3]/div/div/span/button'
    login(mobil_xpath, code_xpath, btn_xpath, project, "18300000001", "000001")
    is_element_exist("//*[@id='root']/div/aside/div[1]/img", "TAD自定义域名学生端学生端")
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 酷培ai学生端(student)
project = "student"
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div/div/p', project + '登录页')
    obvious_wait_click('//*[@id="root"]/div/div/div/div[2]/div/a', project + '密码登录')
    mobil_xpath = '//*[@id="mobile"]'
    code_xpath = '//*[@id="password"]'
    branch = is_branch_exist('//*[@id="root"]/div/div/div/div[2]/form', project)
    if branch == 'true':
        obvious_wait_click('//*[@id="branch"]/div/span/i', '选择校区')
        obvious_wait_click('/html/body/div[3]/div/div/div/ul/li[1]', '选择总校区')
        btn_xpath = '//*[@id="root"]/div/div/div/div[2]/form/div[4]/div/div/span/button'
    else:
        btn_xpath = '//*[@id="root"]/div/div/div/div[2]/form/div[3]/div/div/span/button'
    login(mobil_xpath, code_xpath, btn_xpath, project, "18300000001", "1111")
    is_element_exist('//*[@id="root"]/section/header/img', "酷培ai学生端")
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 酷培ai教师端(teacher)
project = "teacher"
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div/div/p', project + '登录页')
    mobil_xpath = '//*[@id="mobile"]'
    code_xpath = '//*[@id="captcha"]'
    branch = is_branch_exist('//*[@id="root"]/div/div/div/div[2]/form', project)
    if branch == 'true':
        obvious_wait_click('//*[@id="branch"]/div/span', '选择校区')
        obvious_wait_click('/html/body/div[3]/div/div/div/ul/li[1]', '选择总校区')
        btn_xpath = '//*[@id="root"]/div/div/div/div[2]/form/div[4]/div/div/span/button'
    else:
        btn_xpath = '//*[@id="root"]/div/div/div/div[2]/form/div[3]/div/div/span/button'
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist('//*[@id="root"]/div/div[1]/div[1]/span', "酷培ai教师端")
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# learnta管理系统(admin)
project = "admin"
try:
    url = new_tab_cn(url)
    is_element_exist('//*[@id="root"]/div/div/h1', project + '登录页面')
    mobil_xpath = "//*[@id='username']"
    code_xpath = "//*[@id='root']/div/div/form/div[2]/div[2]/div/div/div/div[1]/input"
    btn_xpath = "//*[@id='root']/div/div/form/div[3]/div/div/button"
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist("//*[@id='root']/div/div[1]/h1/a/span[2]", project + '登陆后元素存在判定')
    obvious_wait_click('//*[@id="root"]/div/div[2]/ul/li[2]/div', '题目管理')  # 题目管理
    obvious_wait_click('//*[@id="题目管理$Menu"]/li[1]', '题目录入')  # 题目录入
    obvious_wait_click('//*[@id="category"]/label[1]/span[2]', '数学')  # 数学
    obvious_wait_click('//*[@id="state"]/label[2]/span[2]', '练习题')  # 练习题
    obvious_wait_click('//*[@id="type"]/label[2]/span[2]', '选择题')  # 选择题
    driver.execute_script('window.scrollBy(0, 200)')  # 页面下滑200像素
    obvious_wait_click('//*[@id="isImageOptions"]', '图片选项')  # 图片选项
    obvious_wait_sendkeys(
        '//*[@id="root"]/div/div[2]/div/div/form/div[5]/div[2]/div/div/div[1]/div[2]/div/span/div/span/input',
        'D:\Material\图片\8952.jpg', '图片上传')
    # obvious_wait_click('//*[@id="root"]/div/div[2]/ul/li[3]/div/span/span', '知识点管理')  # 知识点管理
    # obvious_wait_click('//*[@id="知识点管理$Menu"]/li[2]', '知识点列表')  # 知识点列表
    # obvious_wait_sendkeys('//*[@class="videoUpload"]/form/div[4]/div[2]/div/div/div/input', 'D:\Material\视频\hd.mp4',
    #                       '英语视频上传')  # 英语视频上传
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 公众号(go)
project = "go"
name_xpath = '//*[@id="root"]/div/div/form/div[1]/input'
mobile_xpath = '//*[@id="root"]/div/div/form/div[2]/input'
code_xpath = '//*[@id="root"]/div/div/form/div[3]/input'
btn_xpath = '//*[@id="root"]/div/div/form/a/span'
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div/div/div[2]', project + '登录页')
    obvious_wait_sendkeys(name_xpath, '梅婕')
    obvious_wait_sendkeys(mobile_xpath, '18616215375')
    obvious_wait_sendkeys(code_xpath, '1111')
    obvious_wait_click(btn_xpath)
    is_element_exist('//*[@id="root"]/div/div[2]/div', project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 机构管理后台(entry_admin)
project = "entry_admin"
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div[1]/div/div', project + '登录页')
    mobil_xpath = "//*[@id='mobile']"
    code_xpath = "//*[@id='code']/input"
    btn_xpath = "//*[@id='root']/div/div[1]/form/button"
    login(mobil_xpath, code_xpath, btn_xpath, project)
    isexist = "//*[@id='root']/div/div[1]/div"
    is_element_exist(isexist, project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 内容分布式开发平台(material)
project = "material"
mobil_xpath = "//*[@id='mobile']"
code_xpath = "//*[@id='code']/input"
btn_xpath = "//*[@id='root']/div/div[1]/form/button"
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div[1]/div/div', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist("//*[@id='root']/div/section/aside/div/div[1]/a/img", project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e
try:
    url = new_tab_com(project)
    is_element_exist('//*[@id="root"]/div/div[1]/div/div', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist("//*[@id='root']/div/section/aside/div/div[1]/a/img", project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 员工管理系统(user_management)
project = "user_management"
mobil_xpath = "//*[@id='mobile']"
code_xpath = "//*[@id='code']/input"
btn_xpath = "//*[@id='root']/div/div[1]/form/button"
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div[1]/div/img', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist("//*[@id='root']/section/aside/div/div[1]/a/img", project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 数据看板(dashboard)
project = "dashboard"
mobil_xpath = "//*[@id='mobile']"
code_xpath = "//*[@id='captcha']"
btn_xpath = "//*[@id='root']/div/div[1]/div/div[2]/div/form/div[3]/div/div/span/button"
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div[1]/div/div[1]/div/img', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist("//*[@id='root']/div/section/section/header/div/div[1]/span/span[1]/a/img", project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e
try:
    url = new_tab_com(project)
    is_element_exist('//*[@id="root"]/div/div[1]/div/div[1]/div/img', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist("//*[@id='root']/div/section/section/header/div/div[1]/span/span[1]/a/img", project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 论答会员中心(member)
project = "member"
mobil_xpath = "//*[@id='mobile']"
code_xpath = "//*[@id='code']/input"
btn_xpath = "//*[@id='root']/div/div/div/div[2]/div/form/button"
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div/div/div[2]/div/form/img', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist("//*[@id='root']/div/div/div/div[1]/div[2]/div/a/img", project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e
try:
    url = new_tab_com(project)
    is_element_exist('//*[@id="root"]/div/div/div/div[2]/div/form/img', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist("//*[@id='root']/div/div/div/div[1]/div[2]/div/a/img", project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 官网后台(official_admin )
project = "official_admin"
mobil_xpath = "//*[@id='mobile']"
code_xpath = "//*[@id='code']/input"
btn_xpath = "//*[@id='root']/div/div[1]/form/button"
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div[1]/div/div', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist("//*[@id='root']/div/div[1]/div/div/img", project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 论答官网(official)
project = "official"
try:
    url = new_tab_cn(project)
    is_element_exist("//*[@id='root']/div/div/div/div[1]/a[2]/img", project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 研究中心后台(ccnu_admin)
project = "ccnu_admin"
mobil_xpath = "//*[@id='mobile']"
code_xpath = "//*[@id='code']/input"
btn_xpath = "//*[@id='root']/div/div[1]/form/button"
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div[1]/div/div', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist("//*[@id='root']/div/div[1]/div/div/img", project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 研究中心(ccnu)
project = "ccnu"
try:
    url = new_tab_cn(project)
    is_element_exist("//*[@id='root']/div/div/div[2]/div[1]/a/img", project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 论答人工智能学习系统(https://www.learnta.com/business1?utmSource=wechat01)
project = "business1"
try:
    url = 'window.open("https://www.learnta.com/business1?utmSource=wechat01");'
    driver.execute_script(url)
    handls = driver.window_handles
    driver.switch_to.window(handls[-1])
    is_element_exist('//*[@id="root"]/div/div/div/div[1]/div[1]/div[1]/p', project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e


# 论答商务合作(bd)
project = "bd"
mobil_xpath = "//*[@id='mobile']"
code_xpath = "//*[@id='code']/input"
btn_xpath = "//*[@id='root']/div/div/div/div[2]/div/form/button"
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div/div/div[2]/div/form/img', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist("//*[@id='root']/div/div/div/div[2]/div[3]/div[1]/span[1]/span[1]", project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e
try:
    url = new_tab_com(project)
    is_element_exist('//*[@id="root"]/div/div/div/div[2]/div/form/img', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist("//*[@id='root']/div/div/div/div[2]/div[3]/div[1]/span[1]/span[1]", project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 酷培商务合作(bdk.kupeiai.com、partners.bdk.com、learnta.cn/bdk)
project = 'bdk'
mobil_xpath = '//*[@id="mobile"]'
code_xpath = "//*[@id='code']/input"
btn_xpath = "//*[@id='root']/div/div/div/div[2]/div/form/button"
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div/div/div[2]/div/form/img', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist('//*[@id="root"]/div/div/div/div[1]/div[4]/span/input', project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 论答合作伙伴（bda）
project = "bda"
mobil_xpath = "//*[@id='mobile']"
code_xpath = "//*[@id='code']/input"
btn_xpath = "//*[@id='root']/div/div/div/div[2]/div/form/button"
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div/div/div[2]/div/form/img', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist('//*[@id="root"]/div/div/div/div[1]/div[4]/span/input', project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e
try:
    url = new_tab_com(project)
    is_element_exist('//*[@id="root"]/div/div/div/div[2]/div/form/img', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist('//*[@id="root"]/div/div/div/div[1]/div[4]/span/input', project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 酷培合作伙伴(partners.kupeiai.com、partners.learnta.com、learnta.cn/partners)
project = 'partners'
mobil_xpath = '//*[@id="mobile"]'
code_xpath = "//*[@id='code']/input"
btn_xpath = "//*[@id='root']/div/div/div/div[2]/div/form/button"
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div/div/div[2]/div/form/img', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist('//*[@id="root"]/div/div/div/div[1]/div[4]/span/input', project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e
try:
    url = new_tab_com(project)
    is_element_exist('//*[@id="root"]/div/div/div/div[2]/div/form/img', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist('//*[@id="root"]/div/div/div/div[1]/div[4]/span/input', project + '登陆后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

# 短信通知网站(sms)
project = "sms"
mobil_xpath = "//*[@id='mobile']"
code_xpath = "//*[@id='code']/input"
btn_xpath = "//*[@id='root']/div/div[1]/form/button"
try:
    url = new_tab_cn(project)
    is_element_exist('//*[@id="root"]/div/div[1]/div/div', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist('//*[@id="root"]/div/div[1]/div/div/img', project + '登录后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e
try:
    url = new_tab_com(project)
    is_element_exist('//*[@id="root"]/div/div[1]/div/div', project + '登录页')
    login(mobil_xpath, code_xpath, btn_xpath, project)
    is_element_exist('//*[@id="root"]/div/div[1]/div/div/img', project + '登录后元素存在判定')
    pass_project.append(url)
except Exception as e:
    fail_project[url] = e

print('以下是通过的项目：')
for s in pass_project:
    print(s)

print('以下是未通过的项目：')
for ss in fail_project.keys():
    print(ss + ":" + str(fail_project[ss]).strip())
driver.quit()
