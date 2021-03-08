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
import configparser
# 指定日志输出级别
logging.basicConfig(level=logging.INFO)

# 根据系统环境走不同的目录路径来写测试报告
if (platform.system() == 'Windows'):
    print(platform.system())
    report_dir = "D:\\uitest\\report"
    print(report_dir)
    # 读配置文件信息
    configInfo = "C:\\shh\\uitest\\panwenjie\\Is suit\\configtad.ini"
    config = configparser.ConfigParser()
    config.read(configInfo, encoding='UTF-8')
    password = config.get("Info", "password")
    orgId = config.get("Info", "orgid")
    username = config.get("Info", "username")

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
        '''测试智能学习测一测'''
        # 请求头
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        loginOrgPost = {'username': username, 'branch': str(orgId), 'password': password,
                        'systemId': 4, 'orgId': orgId}
        loginOrgResponse = requests.post("https://cj.learnta.cn/__api/auth/user/loginOrgStudent",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        print(loginOrgResponse.status_code)
        access_token = loginOrgResponse.json()['data']['access_token']
        print(access_token)  # 登录码

        # 请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + access_token}
        # 获取课程id
        data = requests.get(
            'https://cj.learnta.cn/__api/beatV3/intelligentstudy/category?isFromTAD=true&orgId='+ str(
                orgId), headers=headers)
        print(data.status_code)
        category = data.json()['data'][1]['category']
        print(category)

        # # 获取课程房间id
        data2 = requests.get(
            'https://cj.learnta.cn/__api/beatV3/studentClassroom/list?orgId=' + str(
                orgId) + '&category=' + str(category), headers=headers)
        print(data2.status_code)
        intelligentRoomId = data2.json()['data'][1]['intelligentRoomId']
        #
        print(intelligentRoomId)
        # # 获取章节
        data4 = requests.get(
            'https://cj.learnta.cn/__api/beatV3/studentClassroom/' + str(
                intelligentRoomId) + '?orgId='+str(orgId),
            headers=headers)
        chapterId = data4.json()['data']['chapterResults'][0]['chapterId']
        print(chapterId)

        # 获取taskExecutionId
        asdasdf = {'intelligentStudyRoomTopicId': chapterId, 'orgId': orgId ,'studyRoomId':intelligentRoomId}
        saad = requests.post('https://cj.learnta.cn/__api/beatV3/student/task/32', json=asdasdf,
                             headers=headers)
        print(saad.status_code)
        taskExecutionId = saad.json()['data']['taskExecution']['id']
        print(taskExecutionId)

        # #获取题目questionId
        ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                 'taskExecutionId': taskExecutionId}
        huoqkeid = requests.post(
            'https://cj.learnta.cn/__api/beatV3/student/task/32/' + str(taskExecutionId) + '/question'
            , data=json.dumps(ijsji), headers=headers)
        question = huoqkeid.json()['data']['questions']
        questionId = huoqkeid.json()['data']['questions'][0]['id']
        print(questionId)
        # ===============================================
        # 做题
        num = 0
        while question is not None:
            adsad = {'questionId': questionId, 'answer': []}
            huoqutimuid = requests.put('https://cj.learnta.cn/__api/beatV3/student/task/32/'+str(taskExecutionId)+'/answer', data=json.dumps(adsad),headers=headers)
            logging.info(huoqutimuid.json())
            ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                     'taskExecutionId': taskExecutionId}
            huoqkeid = requests.post(
                'https://cj.learnta.cn/__api/beatV3/student/task/32/' + str(taskExecutionId) + '/question'
                , data=json.dumps(ijsji), headers=headers)
            question = huoqkeid.json()['data']['questions']
            if question is not None:
                questionId = huoqkeid.json()['data']['questions'][0]['id']
                print(questionId)

        # 进入报告页
        nihao1 = requests.get(
            'https://cj.learnta.cn/__api/beatV3/student/task/32/' + str(taskExecutionId) + '/report',
            headers=headers)
        print(nihao1.status_code)
        dasd = requests.get('https://cj.learnta.cn/__api/beatV3/public/getOrg/' + str(orgId), headers=headers)

        testResult = nihao1.json()['message']
        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="智能学习测一测测试失败")



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