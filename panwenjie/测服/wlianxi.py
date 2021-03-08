#coding:utf-8
import re
import time
import json
import logging
import platform
import unittest
import requests
from BeautifulReport import BeautifulReport

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

    def testwork(self):
        '''测试2.0练习卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'branch': 1, 'username': 13975353140, 'code': 1111, 'systemId': 11, 'orgId': 1}
        loginOrgResponse = requests.post("https://panff.t2.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        adad = {'orgId': 1001310, 'homeworkName': "词汇_词汇练习卡", 'tasks': [{'courseId': "9036", 'taskId': 811995}]}
        data4 = requests.post('https://panff.t2.learnta.cn/__api/beatV3/org/homework/assignTask', data=json.dumps(adad),
                              headers=headers)
        print(data4.status_code)
        self.kpid = data4.json()['id']

        print(self.kpid)#卡片id
        # print(data4.status_code)#请求是否成功
        # 做题时登录
        #
        loginOrgPostdata = {"openId": "", "randomCode": self.kpid, "shareType": "homework", "username": 1231,
                            "mobile": 13975353140, "code": 1111}
        loginOrgResponsedata = requests.post("https://t2.learnta.cn/__api/wechat/public/wechat/qRcode/login",
                                             data=json.dumps(loginOrgPostdata), headers=self.headers)
        # print(loginOrgResponse.status_code)
        #获取homeworkId
        self.homeworkId = loginOrgResponsedata.json()['data']['homeworkId']
        # print(homeworkId)

        #获取课程id
        huoqkeid = requests.get('https://t2.learnta.cn/__api/beatV3/org/homework/getHomework?homeworkId='+self.homeworkId
                          ,headers=headers )
        self.kecid = huoqkeid.json()['unDoneTaskExecutions'][0]['id']
        print(self.kecid)
        # print(huoqkeid.url)
        # print(huoqkeid.status_code)
        #
        # #===============================================
        num = 0
        while num < 3:
        # 获取   questionId
            # 获取题目id question
            qqbw = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': self.kecid}
            question = requests.post('https://t2.learnta.cn/__api/beatV3/student/task/3/' + str(self.kecid) + '/question',
                                     data=json.dumps(qqbw), headers=headers)
            # print(question.status_code)
            # print(question.url)
            self.questionId = question.json()['data']['questions'][num]['id']
            #做题


            data2 = {'startTime':time.time() , 'finishTime': time.time(), 'isSubmit': 0, 'questionId': self.questionId, 'answer': [],'sourceOf': 1,'parentQuestionId': self.questionId}
            data = requests.put('https://t2.learnta.cn/__api/beatV3/student/task/3/'+str(self.kecid)+'/answer',data = json.dumps(data2),headers = headers)
            logging.info(data.json())
            print(data.status_code)

            num += 1
        huoqkeid = requests.put(
            'https://t2.learnta.cn/__api/beatV3/student/task/3/'+str(self.kecid)+'/end'
            , headers=headers)
        print(huoqkeid.status_code)

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