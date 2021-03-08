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
import sys
# 指定日志输出级别
logging.basicConfig(level=logging.INFO)

# 根据系统环境走不同的目录路径来写测试报告
if (platform.system() == 'Windows'):
    print(platform.system())
    report_dir = "D:\\uitest\\report"
    print(report_dir)
    # 读配置文件信息
    configInfo = "C:\\shh\\uitest\\panwenjie\\configkupei.ini"
    config = configparser.ConfigParser()
    config.read(configInfo, encoding='UTF-8')
    password = config.get("Info", "passwords")
    orgId = config.get("Info", "orgid")
    username = config.get("Info", "usernames")
    calss = config.get("Info", "calss")
    gradeName = config.get("Info", "gradeName")
    pressName = config.get("Info", "pressName")

elif (platform.system() == 'Linux'):
    report_dir = '/opt/uitest/report'
    configInfo = '/opt/uitest/chenjun/ApiTest/config.ini'
    orgId = str(sys.argv[1]) #orgid输入
    username = str(sys.argv[2]) #账号输入userInames
    password = str(sys.argv[3]) #密码输入passwords
    calss = str(sys.argv[4]) #输入什么课calss
    gradeName = str(sys.argv[5])#输入什么年级gradeName
    pressName = str(sys.argv[6])#输入什么版本gradeName

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
        '''测试酷培一键继续自动化'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 学生登录
        loginOrgPost = {'username': username, 'password': password, 'systemId': 4, 'orgId': orgId}
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
        num = 0
        while num != 1000 :
            name = data.json()['data'][num]['name']
            #对应课程
            if name == calss :
                category = data.json()['data'][num]['category']
                num = 999
            num += 1
        # # #获取课程房间id
        data2 = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/student/getIntelligentRoom?orgId=' + str(
                orgid) + '&category=' + str(category), headers=headers)

        intelligentRoomId = data2.json()['data'][0]['intelligentRoomId']
        num=0
        while num != 100:
            presName = data2.json()['data'][num]['pressName']
            gradName = data2.json()['data'][num]['gradeName']

            #对应课程版本
            if presName == pressName and gradName == gradeName:
                print("测试"+presName,gradName)
                intelligentRoomId = data2.json()['data'][num]['intelligentRoomId']
                num = 99
            num += 1


        #查询里面有多少章节
        data4 = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/student/getChapter?intelligentRoomId=' + str(
                intelligentRoomId) + '&source=pc',
            headers=headers)

        #123
        tx = data4.json()['data']['chapterResults']
        num = 0
        for i in tx:
            num += 1
        arg = 0


        #开始进行测一测
        while arg != num:
            #获取章节的id
            print('进入第'+str(arg+1)+'章')
            data4 = requests.get('https://www.kupeiai.cn/__api/beatV3/intelligentstudy/student/getChapter?intelligentRoomId='+str(intelligentRoomId)+'&source=pc',
                                  headers=headers)
            chapterId = data4.json()['data']['chapterResults'][arg]['chapterId']
            # print(chapterId)
            #开始测一测
            asdasdf = {'intelligentStudyRoomTopicId': chapterId, 'orgId': orgid}
            saad = requests.post('https://www.kupeiai.cn/__api/beatV3/student/task/24', json=asdasdf,
                                 headers=headers)
            # print(saad.status_code)
            taskExecutionId = saad.json()['data']['taskExecution']['id']
            # print(taskExecutionId)
            #拿题目id
            ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                     'taskExecutionId': taskExecutionId}
            huoqkeid = requests.post(
                'https://www.kupeiai.cn/__api/beatV3/student/task/24/' + str(taskExecutionId) + '/question'
                , data=json.dumps(ijsji), headers=headers)
            sw = huoqkeid.status_code
            if sw == 200:
                questionId = huoqkeid.json()['data']['questions'][0]['id']
                question = huoqkeid.json()['data']['questions']
                # print(questionId)
                # #===============================================
                # 循环做题
                while question is not None:
                    #
                    adsad = {'questionId': questionId, 'answer': []}
                    huoqutimuid = requests.put(
                        'https://www.kupeiai.cn/__api/beatV3/student/task/24/' + str(taskExecutionId) + '/answer',
                        data=json.dumps(adsad), headers=headers)

                    # print(huoqutimuid.status_code)
                    # 再次获取题目id
                    ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                             'taskExecutionId': taskExecutionId}
                    huoqkeid = requests.post(
                        'https://www.kupeiai.cn/__api/beatV3/student/task/24/' + str(taskExecutionId) + '/question'
                        , data=json.dumps(ijsji), headers=headers)
                    # print(huoqkeid.status_code)
                    question = huoqkeid.json()['data']['questions']
                    # print(question)
                    if question is not None:
                        questionId = huoqkeid.json()['data']['questions'][0]['id']
                        # print(questionId)
                nihao1 = requests.get(
                    'https://www.kupeiai.cn/__api/beatV3/student/task/24/' + str(taskExecutionId) + '/report',
                    headers=headers)
                # print(nihao1.status_code)
                dasd = requests.get('https://www.kupeiai.cn/__api/beatV3/public/getOrg/' + str(orgid), headers=headers)
                print('第' + str(arg+1) + '章测一测完成')

                testResult = nihao1.json()['message']
                # print(testResult)
                # 断言测试结果
                self.assertEqual(testResult, 'success', msg="酷培测一测测试失败")
            else:
                print("该知识点不能进行测一测")
            arg += 1
            #
        #继续
        # 查询里面有多少章节
        print("开始进行继续")
        data4 = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/student/getChapter?intelligentRoomId=' + str(
                intelligentRoomId) + '&source=pc',
            headers=headers)
        tx = data4.json()['data']['chapterResults']
        num = 0
        for i in tx:
            num += 1

        zj = 0
        while zj != num:
            print('进入第' + str(zj + 1) + '章')
            # 拿章节Id
            data4 = requests.get(
                'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/student/getChapter?intelligentRoomId=' + str(
                    intelligentRoomId) + '&source=pc',
                headers=headers)
            chapterId = data4.json()['data']['chapterResults'][zj]['chapterId']
            source = data4.json()['data']['source']

            # 判断知识点id有多少个
            print('获取知识点数量')
            data4 = requests.get(
                'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/getKpointListByChapterId?chapterId=' + str(
                    chapterId) + '&orgId=' + str(orgid),
                headers=headers)
            CX = data4.json()['data']
            Class = 0
            for i in CX:
                Class += 1
            zuoti = 0
            while zuoti < Class:
                print("开始做第" + str(zuoti + 1) + "个知识点")
                yun = data4.json()['data'][zuoti]['kpointId']
                loginOrgResponsedata = requests.get(
                    'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/' + str(
                        chapterId) + '/chapter?source=' + str(
                        source) + '&roomId=' + str(intelligentRoomId),
                    headers=headers)
                # 获取taskExecutionId
                taskExecutionId = loginOrgResponsedata.json()['data']['taskExecutionId']
                if taskExecutionId is not None:
                    kpointIds = requests.get(
                        'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/' + str(yun) + '/kPoint',
                        headers=headers)
                    kpointId = kpointIds.json()['data']['kpointId']

                    ijsji = {"userAnswers": [], "isEvaluated": 'true', "isRecommIfNoWeakPoints": 'false',
                             "taskExecutionId": taskExecutionId}
                    huoqkeid = requests.post(
                        'https://www.kupeiai.cn/__api/beatV3/student/task/22/' + str(taskExecutionId) + '/question'
                        , data=json.dumps(ijsji), headers=headers)
                    question = huoqkeid.json()['data']
                    if question is not None:
                        questionid = huoqkeid.json()['data']['questions'][0]['id']

                        # ===============================================
                        # 做题
                        numm = 0
                        print("开始做题")
                        while numm < 3:

                            adsad = {'questionId': questionid, 'answer': []}
                            huoqutimuid = requests.put(
                                'https://www.kupeiai.cn/__api/beatV3/student/task/22/' + str(
                                    taskExecutionId) + '/answer',
                                data=json.dumps(adsad), headers=headers)
                            logging.info(huoqutimuid.json())

                            ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                                     'taskExecutionId': taskExecutionId}

                            huoqkeid = requests.post(
                                'https://www.kupeiai.cn/__api/beatV3/student/task/22/' + str(
                                    taskExecutionId) + '/question'
                                , data=json.dumps(ijsji), headers=headers)
                            question = huoqkeid.json()['data']['questions']
                            if question is not None:
                                questionid = huoqkeid.json()['data']['questions'][0]['id']

                            else:
                                numm = 4
                            numm += 1

                        # 结算页
                        nihao1 = requests.get(
                            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId=' + str(
                                kpointId),
                            headers=headers)
                        dasd = requests.get('https://www.kupeiai.cn/__api/beatV3/student/task/22/' + str(
                            taskExecutionId) + '/report?isSummary=true', headers=headers)
                        nihao2 = requests.get(
                            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId=' + str(
                                kpointId),
                            headers=headers)
                        testResult = nihao1.json()['message']
                        # print(testResult)
                        # 断言测试结果
                        self.assertEqual(testResult, 'success', msg="酷培测一测测试失败")

                else:
                    print('已做完退出')
                    zuoti = 1000

                zuoti += 1
            zj += 1
        #立即攻克
        print("开始进行立即攻克")
        # 查询里面有多少章节
        data4 = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/student/getChapter?intelligentRoomId=' + str(
                intelligentRoomId) + '&source=pc',
            headers=headers)
        tx = data4.json()['data']['chapterResults']
        num = 0
        for i in tx:
            num += 1

        zj = 0
        while zj != num:
            print('进入第' + str(zj + 1) + '章')
            # 拿章节Id
            data4 = requests.get(
                'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/student/getChapter?intelligentRoomId=' + str(
                    intelligentRoomId) + '&source=pc',
                headers=headers)
            chapterId = data4.json()['data']['chapterResults'][zj]['chapterId']
            source = data4.json()['data']['source']
            # 判断知识点id有多少个
            print('获取知识点数量')
            data4 = requests.get(
                'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/getKpointListByChapterId?chapterId=' + str(
                    chapterId) + '&orgId=' + str(orgid),
                headers=headers)
            CX = data4.json()['data']
            Class = 0
            for i in CX:
                Class += 1
            # 获取到知识点数量
            zuoti = 0
            while zuoti < Class:
                print("开始做第" + str(zuoti + 1) + "个知识点")
                kpointId = data4.json()['data'][zuoti]['kpointId']
                asdasdf = {'intelligentStudyRoomTopicId': chapterId, 'orgId': orgid, 'kpointId': kpointId}
                saad = requests.post('https://www.kupeiai.cn/__api/beatV3/student/task/23', json=asdasdf,
                                     headers=headers)
                taskExecutionId = saad.json()['data']['taskExecution']['id']
                # #获取题目questionId
                ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                         'taskExecutionId': taskExecutionId}
                huoqkeid = requests.post(
                    'https://www.kupeiai.cn/__api/beatV3/student/task/23/' + str(taskExecutionId) + '/question'
                    , data=json.dumps(ijsji), headers=headers)
                questio = huoqkeid.json()['data']
                if questio is not None:
                    question = huoqkeid.json()['data']['questions']
                    questionId = huoqkeid.json()['data']['questions'][0]['id']
                    # ===============================================
                    # 做题
                    while question is not None:
                        adsad = {'questionId': questionId, 'answer': []}
                        huoqutimuid = requests.put(
                            'https://www.kupeiai.cn/__api/beatV3/student/task/23/' + str(taskExecutionId) + '/answer',
                            data=json.dumps(adsad), headers=headers)
                        logging.info(huoqutimuid.json())

                        ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                                 'taskExecutionId': taskExecutionId}
                        huoqkeid = requests.post(
                            'https://www.kupeiai.cn/__api/beatV3/student/task/23/' + str(taskExecutionId) + '/question'
                            , data=json.dumps(ijsji), headers=headers)
                        question = huoqkeid.json()['data']['questions']
                        if question is not None:
                            questionId = huoqkeid.json()['data']['questions'][0]['id']
                    nihao1 = requests.get(
                        'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId=' + str(
                            kpointId), headers=headers)
                    dasd = requests.get('https://www.kupeiai.cn/__api/beatV3/student/task/23/' + str(
                        taskExecutionId) + '/report?isSummary=false', headers=headers)
                    testResult = dasd.json()['message']

                    # 断言测试结果
                    self.assertEqual(testResult, 'success', msg="酷培立即攻克测试失败")

                else:
                    print("立即攻克已经做完")
                zuoti += 1
            zj += 1


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
    runner.report(filename='酷培AI一键继续.html', description='酷培AI一键继续', log_path=report_dir)
    print(report_dir)
    print(filename)
elif(platform.system()=='Linux'):
    report_dir = "/opt/uitest/report"
    filename = '/opt/uitest/img'
    runner.report(filename='酷培AI一键继续.html', description='酷培AI一键继续', report_dir=report_dir)
    print(report_dir)
    print(filename)
    print(platform.system())
else:
    print(platform.system())