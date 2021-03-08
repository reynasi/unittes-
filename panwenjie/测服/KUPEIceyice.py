#coding:utf-8
import re
import time
import json
import logging
import platform
import unittest
import requests
from BeautifulReport import BeautifulReport
from time import sleep
# 指定日志输出级别
logging.basicConfig(level=logging.INFO)

# 根据系统环境走不同的目录路径来写测试报告
if (platform.system() == 'Windows'):
    print(platform.system())
    report_dir = "D:\\uitest\\report"
    print(report_dir)

elif (platform.system() == 'Linux'):
    report_dir = '/opt/uitest/report'
    print(platform.system())
else:
    print(platform.system())

# 开始测试
class algoTestdemo(unittest.TestCase):
    #获取token
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testkupcyc(self):
        '''测试酷培测一测'''
        # 请求头
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录
        loginOrgPost = {'username': "00108333654", 'password': "111111", 'systemId': 4, 'orgId': 1000650}
        loginOrgResponse = requests.post("https://kupeitrial.t2.kupeiai.cn/__api/auth/user/loginKupeiStudent",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)  # 登录码

        # 请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}

        # dms登录请求
        # login = {'username': "13975353140", 'code': "1111", 'systemCode': "dms"}
        # loginsd = requests.post("https://api.t2.learnta.cn/v1/auth/crm/user/login",
        #                         data=json.dumps(login), headers=self.headers)
        # erer = loginsd.json()['data']['access_token']
        # print(erer)
        #
        #
        #
        # heads = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + erer}
        # data4 = requests.put('https://api.t2.learnta.cn/v1/dms/demoAccount/0/6/8588/reset',
        #                       headers=heads)
        # print(data4.status_code)
        # sleep(30)

        data4 = requests.get(
            'https://kupeitrial.t2.kupeiai.cn/__api/beatV3/intelligentstudy/student/getChapter?intelligentRoomId=8813&source=pc',
            headers=headers)
        # self.kpid = data4.json()['data']['roomId']
        chapterId = data4.json()['data']['chapterResults'][0]['chapterId']
        print(chapterId)  # 卡片id
        # 获取课程
        asdasdf = {'intelligentStudyRoomTopicId': chapterId, 'orgId': 1000787}
        saad = requests.post('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/24', json=asdasdf,
                             headers=headers)
        print(saad.status_code)
        taskExecutionId = saad.json()['data']['taskExecution']['id']
        print(taskExecutionId)
        # 获取题目id
        ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                 'taskExecutionId': taskExecutionId}
        huoqkeid = requests.post(
            'https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/24/' + str(taskExecutionId) + '/question'
            , data=json.dumps(ijsji), headers=headers)
        print(huoqkeid.status_code)
        questionId = huoqkeid.json()['data']['questions'][0]['id']
        question = huoqkeid.json()['data']['questions']
        print(questionId)

        num = 0
        # #===============================================
        # 做题
        while question is not None:
            #
            adsad = {'questionId': questionId, 'answer': []}
            huoqutimuid = requests.put(
                'https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/24/' + str(taskExecutionId) + '/answer',
                data=json.dumps(adsad), headers=headers)

            print(huoqutimuid.status_code)

            ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                     'taskExecutionId': taskExecutionId}
            huoqkeid = requests.post(
                'https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/24/' + str(taskExecutionId) + '/question'
                , data=json.dumps(ijsji), headers=headers)
            print(huoqkeid.status_code)
            question = huoqkeid.json()['data']['questions']
            print(question)
            if question is not None:
                questionId = huoqkeid.json()['data']['questions'][0]['id']
                print(questionId)
            num += 1
        #
        #
        nihao1 = requests.get(
            'https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/24/' + str(taskExecutionId) + '/report',
            headers=headers)
        print(nihao1.status_code)
        dasd = requests.get('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/public/getOrg/1000787', headers=headers)
        print(dasd.status_code)

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
    runner.report(filename='算法接口测试.html', description='算法接口测试', log_path=report_dir)
    print(report_dir)
    print(filename)
elif(platform.system()=='Linux'):
    report_dir = "/opt/uitest/report"
    filename = '/opt/uitest/img'
    runner.report(filename='算法接口测试.html', description='算法接口测试', report_dir=report_dir)
    print(report_dir)
    print(filename)
    print(platform.system())
else:
    print(platform.system())