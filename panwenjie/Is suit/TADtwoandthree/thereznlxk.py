#coding:utf-8
import re
import time
import json
import logging
import platform
import unittest
import requests
from BeautifulReport import BeautifulReport
import configparser

# 指定日志输出级别
logging.basicConfig(level=logging.INFO)

# 根据系统环境走不同的目录路径来写测试报告
if (platform.system() == 'Windows'):
    print(platform.system())
    report_dir = "D:\\uitest\\report"
    print(report_dir)
    # TAD读配置文件信息
    configInfo = "C:\\shh\\uitest\\panwenjie\\config.ini"
    config = configparser.ConfigParser()
    config.read(configInfo, encoding='UTF-8')
    ocode = config.get("Info", "vcode")
    ousername = config.get("Info", "TADusername")

    storgId = config.get("Info", "TADthreeorgid")
    #  酷培配置文件信息
    password = config.get("Info", "password")
    orgId = config.get("Info", "kupeiorgid")
    username = config.get("Info", "kupeiusername")
    passwords = config.get("Info", "passwords")
    usernames = config.get("Info", "kupeiaiusername")
    # 智能学习读配置文件信息
    cpassword = config.get("Info", "znxxpassword")
    corgId = config.get("Info", "znxxorgid")
    cusername = config.get("Info", "username")


elif (platform.system() == 'Linux'):
    report_dir = '/opt/uitest/report'
    print(platform.system())
    #  TAD读配置文件信息
    configInfo = "/opt/uitest/panwenjie/config.ini"
    config = configparser.ConfigParser()
    config.read(configInfo, encoding='UTF-8')
    ocode = config.get("Info", "vcode")
    oorgId = config.get("Info", "TADoneorgid")
    ousername = config.get("Info", "TADusername")
    torgId = config.get("Info", "TADtwoorgid")
    storgId = config.get("Info", "TADthreeorgid")
    #  酷培配置文件信息
    password = config.get("Info", "password")
    orgId = config.get("Info", "kupeiorgid")
    username = config.get("Info", "kupeiusername")
    passwords = config.get("Info", "passwords")
    usernames = config.get("Info", "kupeiaiusername")
    # 智能学习读配置文件信息
    cpassword = config.get("Info", "znxxpassword")
    corgId = config.get("Info", "znxxorgid")
    cusername = config.get("Info", "username")


else:
    print(platform.system())

# 开始测试
class algoTestdemo(unittest.TestCase):
    #获取token
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testthereznlxk(self):
        '''测试3.0智能练习卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {"branch":storgId, "username": ousername, "code": ocode, "systemId": 11, "orgId": storgId}
        loginOrgResponse = requests.post("https://cj.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        print(loginOrgResponse.status_code)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)  # 登录码

        # 请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        qwes = {"orgId": storgId, "homeworkName": "智能练习卡", "tasks": [{"courseId": "113691", "taskId": 20366561}]}
        data4 = requests.post('https://cj.learnta.cn/__api/beatV3/org/homework/assignTask',
                              data=json.dumps(qwes),
                              headers=headers)
        print(data4.status_code)
        cardid = data4.json()['id']

        # print(self.kpid)#卡片id
        # print(data4.status_code)#请求是否成功
        # 做题时登录

        loginOrgPostdata = {'openId': "", 'randomCode': cardid, 'shareType': "homework", 'username': '算法测试',
                            'mobile': ousername, 'code': ocode}
        loginOrgResponsedata = requests.post("https://learnta.cn/__api/wechat/public/wechat/qRcode/login",
                                             data=json.dumps(loginOrgPostdata), headers=self.headers)

        # 获取homeworkId
        homeworkId = loginOrgResponsedata.json()['data']['homeworkId']
        print(homeworkId)
        #
        # 获取课程id\
        huoqkeid = requests.get('https://learnta.cn/__api/beatV3/org/homework/getHomework?homeworkId=' + homeworkId
                                , headers=headers)
        taskExecutionId = huoqkeid.json()['unDoneTaskExecutions'][0]['id']
        # print(self.cs)
        # print(huoqkeid.url)
        # print(huoqkeid.status_code)
        #
        # #===============================================
        # 获取题目id question
        qqbw = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': taskExecutionId}
        questions = requests.post(
            'https://learnta.cn/__api/beatV3/student/task/33/' + str(taskExecutionId) + '/question',
            data=json.dumps(qqbw), headers=headers)
        # print(question.status_code)
        # print(question.url)
        questionId = questions.json()['data']['questions'][0]['id']
        question = questions.json()['message']
        # 做题

        while question == 'success':
            # 做题
            data2 = {'questionId': questionId, 'answer': [], 'sourceOf': 1}
            data = requests.put(
                'https://learnta.cn/__api/beatV3/student/task/33/' + str(taskExecutionId) + '/answer',
                data=json.dumps(data2), headers=headers)
            logging.info(data.json())
            print(data.status_code)

            # 获取题目id question
            # 获取题目id question
            qqbw = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': taskExecutionId}
            questions = requests.post(
                'https://learnta.cn/__api/beatV3/student/task/33/' + str(taskExecutionId) + '/question',
                data=json.dumps(qqbw), headers=headers)
            # print(question.status_code)
            # print(question.url)
            question = questions.json()['message']
            if question == 'success':
                questionId = questions.json()['data']['questions'][0]['id']

            # 做题

        report = requests.get('https://learnta.cn/__api/beatV3/student/task/33/' + str(taskExecutionId) + '/report',
                              headers=headers)
        print(report.status_code)
        testResult = report.json()['message']

        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="3.0智能练习卡测试失败")



testsuite = unittest.TestSuite()
testsuite.addTests(unittest.makeSuite(algoTestdemo))

#使用的report方法输出HTML格式的报告
runner = BeautifulReport((testsuite))
#runner.report(filename='KuPiWEB端测试.html', description='酷培学生端测试用例',log_path=report_dir)
# filename = time.strftime("%Y-%m-%d-%H-%M-%S")+r".html"



# 根据系统环境判断需要读取的目录路径
if(platform.system()=='Windows'):
    report_dir = 'C:\\python1\\day06'
    filename = "C:\\python1\\day05"
    print(platform.system())
    runner.report(filename='正服算法接口测试.html', description='正服算法接口测试', log_path=report_dir)
    print(report_dir)
    print(filename)
elif(platform.system()=='Linux'):
    report_dir = "/opt/uitest/report"
    filename = '/opt/uitest/img'
    runner.report(filename='正服算法接口测试.html', description='正服算法接口测试', report_dir=report_dir)
    print(report_dir)
    print(filename)
    print(platform.system())
else:
    print(platform.system())