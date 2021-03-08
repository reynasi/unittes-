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

    def testtadznxxljgk(self):
        '''测试TAD智能学习立即攻克'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'username': "PKAxB6A/BqLSEOQbD64rNg==", 'branch': "1", 'password': "XOLj6SkDrZEI0ERiYWwYLw==", 'systemId': 4,'orgId': 1}
        loginOrgResponse = requests.post("https://t2.learnta.cn/__api/auth/user/loginOrgStudent",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        data4 = requests.get('https://t2.learnta.cn/__api/beatV3/studentClassroom/7924?orgId=1',
                              headers=headers)
        # self.kpid = data4.json()['data']['roomId']
        chapterId = data4.json()['data']['chapterResults'][0]['chapterId']
        print(chapterId)#卡片id


        SDASD = requests.get('https://t2.learnta.cn/__api/beatV3/studentClassroom/chapter?chapterId='+str(chapterId)+'&studyRoomId=7924&orgId=1',headers=headers)
        print(SDASD.status_code)
        kpointId = SDASD.json()['data']['kpoints'][2]['kpointId']
        print(kpointId)

        asdasdf = {'intelligentStudyRoomTopicId': chapterId, 'orgId': 1, 'kpointId': kpointId, 'studyRoomId': "7924"}
        saad = requests.post('https://t2.learnta.cn/__api/beatV3/student/task/31',json=asdasdf,headers=headers)
        print(saad.status_code)
        taskExecutionId = saad.json()['data']['taskExecutionId']
        print(taskExecutionId)
        #获取课程id
        ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                 'taskExecutionId': taskExecutionId}
        huoqkeid = requests.post(
            'https://t2.learnta.cn/__api/beatV3/student/task/31/' + str(taskExecutionId) + '/question'
            , data=json.dumps(ijsji), headers=headers)
        print(huoqkeid.status_code)
        question = huoqkeid.json()['data']['questions']
        questionId = huoqkeid.json()['data']['questions'][0]['id']
        num = 0
        # # # #===============================================
        while question is not None:

            adsad = {'questionId': questionId, 'answer': []}
            huoqutimuid = requests.put(
                'https://t2.learnta.cn/__api/beatV3/student/task/31/' + str(taskExecutionId) + '/answer',
                data=json.dumps(adsad), headers=headers)
            logging.info(huoqutimuid.json())
            print(huoqutimuid.status_code)
            #
            num += 1

            #
            ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                     'taskExecutionId': taskExecutionId}
            huoqkeid = requests.post(
                'https://t2.learnta.cn/__api/beatV3/student/task/31/' + str(taskExecutionId) + '/question'
                , data=json.dumps(ijsji), headers=headers)
            print(huoqkeid.status_code)
            question = huoqkeid.json()['data']['questions']
            if question is not None:
                questionId = huoqkeid.json()['data']['questions'][0]['id']
            print(questionId)

        #
        nihao1 = requests.get('https://t2.learnta.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId='+str(kpointId),headers=headers)
        print(nihao1.status_code)
        dasd = requests.get('https://t2.learnta.cn/__api/beatV3/student/task/31/'+str(taskExecutionId)+'/report?isSummary=false',headers=headers)
        print(dasd.status_code)
        nihao2 = requests.get(
            'https://t2.learnta.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId=' + str(kpointId),
            headers=headers)
        print(nihao2.status_code)
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