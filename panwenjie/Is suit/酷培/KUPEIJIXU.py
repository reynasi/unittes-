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
    # 读配置文件信息
    configInfo = "C:\\shh\\uitest\\panwenjie\\Is suit\\configkupei.ini"
    config = configparser.ConfigParser()
    config.read(configInfo, encoding='UTF-8')
    password = config.get("Info", "passwords")
    orgId = config.get("Info", "orgid")
    usernames = config.get("Info", "usernames")


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
        '''测试酷培继续'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录
        loginOrgPost = {'username': usernames, 'password': password, 'systemId': 4, 'orgId': orgId}
        loginOrgResponse = requests.post("https://www.kupeiai.cn/__api/auth/user/loginKupeiStudent",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        access_token = loginOrgResponse.json()['data']['access_token']
        orgid = loginOrgResponse.json()['data']['orgId']
        print(orgid)
        studentId = loginOrgResponse.json()['data']['user']['id']
        print(access_token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + access_token}
        #获取课程id
        data = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/category?isMember=false&isFromTAD=false&orgId=' + str(
                orgid) + '&studentId=' + str(studentId) + '&isKupeiStudent=true',
            headers=headers)
        category = data.json()['data'][0]['category']
        print(category)


        #获取课程房间id
        data2 = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/student/getIntelligentRoom?orgId=' + str(
                orgid) + '&category=' + str(category), headers=headers)
        print(data2.status_code)
        intelligentRoomId = data2.json()['data'][30]['intelligentRoomId']

        #获取卡片
        data4 = requests.get('https://www.kupeiai.cn/__api/beatV3/intelligentstudy/student/getChapter?intelligentRoomId='+str(intelligentRoomId)+'&source=pc',
                              headers=headers)
        werwr = data4.json()
        print(werwr)   
        chapterId = data4.json()['data']['chapterResults'][0]['chapterId']
        source = data4.json()['data']['source']

        # 获取taskExecutionId
        loginOrgResponsedata = requests.get('https://www.kupeiai.cn/__api/beatV3/intelligentstudy/'+str(chapterId)+'/chapter?source='+str(source)+'&roomId='+str(intelligentRoomId),
                                             headers=headers)
        #获取taskExecutionId
        taskExecutionId = loginOrgResponsedata.json()['data']['taskExecutionId']
        print(taskExecutionId)
        #
        # #获取课程id
        ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false','taskExecutionId': taskExecutionId}
        huoqkeid = requests.post('https://www.kupeiai.cn/__api/beatV3/student/task/22/'+str(taskExecutionId)+'/question'
                          ,data=json.dumps(ijsji),headers=headers)
        questionid = huoqkeid.json()['data']['questions'][0]['id']
        kpointId = huoqkeid.json()['data']['questions'][0]['kpointId']
        print(huoqkeid.status_code)
        print(questionid)
        #===============================================
        #做题
        num = 0
        while num <3 :
            adsad = {'questionId': questionid, 'answer': []}
            huoqutimuid = requests.put('https://www.kupeiai.cn/__api/beatV3/student/task/22/'+str(taskExecutionId)+'/answer', data=json.dumps(adsad),headers=headers)
            logging.info(huoqutimuid.json())
            print(huoqutimuid.status_code)

            ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                     'taskExecutionId': taskExecutionId}
            huoqkeid = requests.post(
                'https://www.kupeiai.cn/__api/beatV3/student/task/22/' + str(taskExecutionId) + '/question'
                , data=json.dumps(ijsji), headers=headers)
            questionid = huoqkeid.json()['data']['questions'][0]['id']
            kpointId = huoqkeid.json()['data']['questions'][0]['kpointId']
            print(questionid)
            num +=1
            #
        nihao1 = requests.get('https://www.kupeiai.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId=='+str(kpointId),headers=headers)
        print(nihao1.status_code)
        dasd = requests.get('https://www.kupeiai.cn/__api/beatV3/student/task/22/'+str(taskExecutionId)+'/report?isSummary=true',headers=headers)
        print(dasd.status_code)
        nihao2 = requests.get('https://www.kupeiai.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId=='+str(kpointId),headers=headers)
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