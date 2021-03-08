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

    def test1znlxk(self):
        '''测试1.0智能练习卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'branch': 1, 'username': 13975353140, 'code': 1111, 'systemId': 11, 'orgId': 1}
        loginOrgResponse = requests.post("https://t2.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        self.token = loginOrgResponse.json()['data']['access_token']
        # print(self.token)#登录码

        # 请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        adad = {'orgId': 1, 'homeworkName': "正数和负数", 'tasks': [{'courseId': "17817", 'taskId': 1152352}]}
        data4 = requests.post('https://t2.learnta.cn/__api/beatV3/org/homework/assignTask', data=json.dumps(adad),
                              headers=headers)
        self.kpid = data4.json()['id']

        # print(self.kpid)#卡片id
        # print(data4.status_code)#请求是否成功
        # 做题时登录

        loginOrgPostdata = {"openId": "", "randomCode": self.kpid, "shareType": "homework", "username": 1231,
                            "mobile": 13975353140, "code": 1111}
        loginOrgResponsedata = requests.post("https://t2.learnta.cn/__api/wechat/public/wechat/qRcode/login",
                                             data=json.dumps(loginOrgPostdata), headers=self.headers)
        # 获取homeworkId
        self.homeworkId = loginOrgResponsedata.json()['data']['homeworkId']
        # print(homeworkId)

        # 获取课程id
        params = {'content-type': 'application/json', 'authorization': 'Bearer ' + self.token}
        huoqkeid = requests.get(
            'https://t2.learnta.cn/__api/beatV3/org/homework/getHomework?homeworkId=' + self.homeworkId
            , headers=params)
        self.kecid = huoqkeid.json()['unDoneTaskExecutions'][0]['id']
        # print(self.cs)
        # print(huoqkeid.url)
        # print(huoqkeid.status_code)

        # ===============================================
        adsad = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': self.kecid}
        huoqutimuid = requests.post(
            'https://t2.learnta.cn/__api/beatV3/student/task/11/' + str(self.kecid) + '/question',
            data=json.dumps(adsad), headers=headers)
        questionId = huoqutimuid.json()['data']['questions'][0]['id']
        print(questionId)
        question = huoqutimuid.json()['message']
        print(question)
        while question == 'success':
            verifyPostdata = {'questionId': questionId, 'answer': [], 'sourceOf': 'null'}
            qweasd = requests.put('https://t2.learnta.cn/__api/beatV3/student/task/11/' + str(self.kecid) + '/answer',
                                  data=json.dumps(verifyPostdata), headers=headers)
            print(qweasd.status_code)
            # print(qweasd.url)
            # print(qweasd.status_code)
            # 推题拿questionId
            adsad = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': self.kecid}
            huoqutimuid = requests.post(
                'https://t2.learnta.cn/__api/beatV3/student/task/11/' + str(self.kecid) + '/question',
                data=json.dumps(adsad), headers=headers)
            question = huoqutimuid.json()['message']
            if question == 'success':
                questionId = huoqutimuid.json()['data']['questions'][0]['id']
            logging.info(qweasd.json())

        asda = requests.get('https://t2.learnta.cn/__api/beatV3/student/task/11/' + '/report', headers=headers)

        testResult = asda.json()['message']

        # 断言测试结果
        self.assertEqual(testResult, 'Not Found', msg="测试失败")

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