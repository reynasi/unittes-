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

    def testck(self):
        '''测试1.0闯关卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'username': ousername, 'code': ocode, 'systemId': 11, 'orgId': oorgId}
        loginOrgResponse = requests.post("https://autotest.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        print(loginOrgResponse.status_code)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        qwes = {'orgId': oorgId, 'homeworkName': "练习闯关闯关卡测试1", 'tasks':  [{'courseId': "63533", 'taskId': 6753621}]}
        data4 = requests.post('https://autotest.learnta.cn/__api/beatV3/org/homework/assignTask', data=json.dumps(qwes),
                              headers=headers)
        print(data4.status_code)
        cardid = data4.json()['id']

        # print(self.kpid)#卡片id
        # print(data4.status_code)#请求是否成功
        # 做题时登录

        loginOrgPostdata = {'openId': "", 'randomCode': cardid, 'shareType': "homework", 'username': '算法测试','mobile': ousername,'code': ocode}
        loginOrgResponsedata = requests.post("https://learnta.cn/__api/wechat/public/wechat/qRcode/login",
                                             data=json.dumps(loginOrgPostdata), headers=self.headers)


        #获取homeworkId
        homeworkId = loginOrgResponsedata.json()['data']['homeworkId']
        print(homeworkId)
        #
        #获取课程id\
        huoqkeid = requests.get('https://learnta.cn/__api/beatV3/org/homework/getHomework?homeworkId='+homeworkId
                          ,headers=headers)
        taskExecutionId = huoqkeid.json()['unDoneTaskExecutions'][0]['id']
        # print(self.cs)
        # print(huoqkeid.url)
        # print(huoqkeid.status_code)
        #
        # #===============================================
        num = 0
        while num < 4:
        # 获取   questionId
            # 获取题目id question
            qqbw = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': taskExecutionId}
            question = requests.post('https://learnta.cn/__api/beatV3/student/task/4/' + str(taskExecutionId) + '/question',
                                     data=json.dumps(qqbw), headers=headers)
            # print(question.status_code)
            # print(question.url)
            questionId = question.json()['data']['questions'][num]['id']
            #做题

            data2 = {'startTime':time.time() , 'finishTime': time.time(), 'isSubmit': 0, 'questionId': questionId, 'answer': [],'sourceOf': 1,'parentQuestionId': questionId}
            data = requests.put('https://learnta.cn/__api/beatV3/student/task/4/'+str(taskExecutionId)+'/answer',data = json.dumps(data2),headers = headers)
            logging.info(data.json())
            print(data.status_code)

            num += 1
        huoqkeid = requests.put(
            'https://learnta.cn/__api/beatV3/student/task/4/'+str(taskExecutionId)+'/end'
            , headers=headers)
        print(huoqkeid.status_code)
        testResult = huoqkeid.json()['message']
        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="闯关卡做题失败")


    def testdzcp(self):
        '''测试1.0定制测评卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'username': ousername, 'code': ocode, 'systemId': 11, 'orgId': oorgId}
        loginOrgResponse = requests.post("https://autotest.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        print(loginOrgResponse.status_code)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        qwes = {'topicInfoId': "3496", 'kpointIds': [6000050826, 6000050827, 6000050828], 'orgId': oorgId,'examType':"newExam",'topicName':"Unit 1 情景交际"}
        data4 = requests.post('https://autotest.learnta.cn/__api/beatV3/topic/diygo/create', data=json.dumps(qwes),
                              headers=headers)
        print(data4.status_code)

        cardid = data4.json()['shareUrl']
        # 正则匹配后端返回的goUrl中的csteid
        pattern = re.findall('m/(.+?)$', cardid)  # 匹配规则cste=开头到&之间的字符串\
        result = pattern[0]
        print(result)

        # print(self.kpid)#卡片id
        # print(data4.status_code)#请求是否成功
        # 做题时登录

        loginOrgPostdata = {'openId': "", 'randomCode': result, 'shareType': "chargeExam", 'username': '算法测试','mobile': ousername,'code': ocode}
        loginOrgResponsedata = requests.post("https://learnta.cn/__api/wechat/public/wechat/qRcode/login",
                                             data=json.dumps(loginOrgPostdata), headers=self.headers)

        print(loginOrgResponsedata.status_code)

        #
        #获取cste
        huoqkeid = requests.get('https://learnta.cn/__api/beatV3/topic/goExam/'+str(result)
                          ,headers=headers)
        cste = huoqkeid.json()['cste']

        #获取question
        qqbw = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false','taskExecutionId': cste}
        questionasda = requests.post('https://learnta.cn/__api/beatV3/student/task/12/' + str(cste) + '/question',
                                 data=json.dumps(qqbw), headers=headers)
        question = questionasda.json()['data']['questions']
        questionId = questionasda.json()['data']['questions'][0]['id']

        # 做题
        while question is not None:
            #做题
            data2 = {'startTime':time.time(),'finishTime': time.time(), 'isSubmit': 0,'questionId': questionId, 'answer': [],'sourceOf': '','parentQuestionId': questionId}
            data = requests.put('https://learnta.cn/__api/beatV3/student/task/12/'+str(cste)+'/answer',data = json.dumps(data2),headers = headers)
            logging.info(data.json())
            print(data.status_code)
            #获取questionid

            qqbw = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                    'taskExecutionId': cste}
            questionasda = requests.post('https://learnta.cn/__api/beatV3/student/task/12/' + str(cste) + '/question',
                                         data=json.dumps(qqbw), headers=headers)
            question = questionasda.json()['data']['questions']
            if question is not None:
                questionId = questionasda.json()['data']['questions'][0]['id']


        ads = {'shareType': "chargeExam"}
        huoqkeid = requests.put(
            'https://learnta.cn/__api/beatV3/classroom/task/exam/addStudent/'+str(cste)
            ,data = json.dumps(ads), headers=headers)
        print(huoqkeid.status_code)

        adnis = requests.get(
            'https://learnta.cn/__api/beatV3/public/student/task/12/'+str(cste)+'/report'
            ,headers=headers)
        print(adnis.status_code)

        testResult = adnis.json()['message']
        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="定制测评卡做题失败")


    def testgo(self):
        '''测试go卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'username': ousername, 'code': ocode, 'systemId': 11, 'orgId': oorgId}
        loginOrgResponse = requests.post("https://autotest.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        print(loginOrgResponse.status_code)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        datatest = requests.get('https://www.learnta.cn/__api/wechat/public/qRcode/chargeExam/8fcRJSeSzuagADQ72923935')

        print(datatest.status_code)



        #获取题目id
        huoqkcid = requests.get('https://learnta.cn/__api/beatV3/topic/goExam/8fcRJSeSzuagADQ72923935',headers=headers)
        cste = huoqkcid.json()['cste']
        print(cste)

        huoqtimid = requests.get('https://learnta.cn/__api/beatV3/public/classroom/task/taskDetail/'+str(cste),headers=headers)
        topicId = huoqtimid.json()['task']['topicId']
        print(topicId)

        huoqutimuid = requests.get('https://learnta.cn/__api/wechat/go/next/'+str(topicId)+'/go',headers = headers)
        questionId = huoqutimuid.json()['data']['questionId']
        print(questionId)


        while questionId is not None:
            # 判题
            verifyPostdata = {'questionId': questionId, 'userAnswer': [""]}
            qweasd =  requests.post('https://learnta.cn/__api/wechat/go/subject/study/item/quest/answer/verify',
                          data=json.dumps(verifyPostdata), headers=headers)
            # print(qweasd.url)
            # print(qweasd.status_code)
            # 推题拿questionId
            huoqutimuid = requests.get('https://learnta.cn/__api/wechat/go/next/' + str(topicId) + '/go',
                                       headers=headers)
            questionId = huoqutimuid.json()['data']['questionId']
            print(questionId)
            studyItemId = huoqutimuid.json()['data']['studyItemId']
            #print(questionId)

        # # 结算
        dxwa = {'shareType': "chargeExam"}
        AS = requests.put('https://learnta.cn/__api/beatV3/classroom/task/exam/addStudent/'+str(cste), data=json.dumps(dxwa),headers=headers)
        print(AS.status_code)

        dafa = {'answer': [str(studyItemId)]}
        asdzxc = requests.put('https://learnta.cn/__api/beatV3/classroom/task/saveAnswer/'+str(cste),data=json.dumps(dafa),headers=headers)
        print(asdzxc.status_code)
        jsjxj = requests.put('https://learnta.cn/__api/beatV3/classroom/task/homework/finish/0/'+str(cste),headers=headers)
        print(jsjxj.status_code)

        qfys = {'itemId': studyItemId, 'source': "teach_side"}
        adnis=requests.post('https://learnta.cn/__api/wechat/public/subject/study/item',data=json.dumps(qfys),headers=headers)
        print(adnis.status_code)
        testResult = adnis.json()['message']
        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="go卡做题失败")

    def testlxk(self):
        '''测试1.0练习卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'username': ousername, 'code': ocode, 'systemId': 11, 'orgId': oorgId}
        loginOrgResponse = requests.post("https://autotest.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        print(loginOrgResponse.status_code)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        qwes = {'orgId': oorgId, 'homeworkName': "自选练习卡", 'tasks': [{'courseId': "39871", 'taskId': 7439120}]}
        data4 = requests.post('https://autotest.learnta.cn/__api/beatV3/org/homework/assignTask', data=json.dumps(qwes),
                              headers=headers)
        print(data4.status_code)
        cardid = data4.json()['id']

        # print(self.kpid)#卡片id
        # print(data4.status_code)#请求是否成功
        # 做题时登录

        loginOrgPostdata = {'openId': "", 'randomCode': cardid, 'shareType': "homework", 'username': '算法测试','mobile': ousername,'code': ocode}
        loginOrgResponsedata = requests.post("https://learnta.cn/__api/wechat/public/wechat/qRcode/login",
                                             data=json.dumps(loginOrgPostdata), headers=self.headers)


        #获取homeworkId
        homeworkId = loginOrgResponsedata.json()['data']['homeworkId']
        print(homeworkId)
        #
        #获取课程id\
        huoqkeid = requests.get('https://learnta.cn/__api/beatV3/org/homework/getHomework?homeworkId='+homeworkId
                          ,headers=headers)
        taskExecutionId = huoqkeid.json()['unDoneTaskExecutions'][0]['id']
        # print(self.cs)
        # print(huoqkeid.url)
        # print(huoqkeid.status_code)
        #
        # #===============================================
        num = 0
        while num < 11:
        # 获取   questionId
            # 获取题目id question
            qqbw = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': taskExecutionId}
            question = requests.post('https://learnta.cn/__api/beatV3/student/task/3/' + str(taskExecutionId) + '/question',
                                     data=json.dumps(qqbw), headers=headers)
            # print(question.status_code)
            # print(question.url)
            questionId = question.json()['data']['questions'][num]['id']
            #做题

            data2 = {'startTime':time.time() , 'finishTime': time.time(), 'isSubmit': 0, 'questionId': questionId, 'answer': [],'sourceOf': 1,'parentQuestionId': questionId}
            data = requests.put('https://learnta.cn/__api/beatV3/student/task/3/'+str(taskExecutionId)+'/answer',data = json.dumps(data2),headers = headers)
            logging.info(data.json())
            print(data.status_code)

            num += 1
        huoqkeid = requests.put(
            'https://learnta.cn/__api/beatV3/student/task/3/'+str(taskExecutionId)+'/end'
            , headers=headers)
        print(huoqkeid.status_code)
        testResult = huoqkeid.json()['message']
        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="练习卡做题失败")

    def testhxdxt(self):
        '''测试1.0化学多选题卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'username': ousername, 'code': ocode, 'systemId': 11, 'orgId': oorgId}
        loginOrgResponse = requests.post("https://autotest.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        print(loginOrgResponse.status_code)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)  # 登录码

        # 请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        qwes = {'orgId': oorgId, 'homeworkName': "多选题卡", 'tasks': [{'courseId': "113782", 'taskId': 20402645}]}
        data4 = requests.post('https://autotest.learnta.cn/__api/beatV3/org/homework/assignTask', data=json.dumps(qwes),
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
        num = 0
        while num < 4:
            # 获取   questionId
            # 获取题目id question
            qqbw = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': taskExecutionId}
            question = requests.post(
                'https://learnta.cn/__api/beatV3/student/task/27/' + str(taskExecutionId) + '/question',
                data=json.dumps(qqbw), headers=headers)
            # print(question.status_code)
            # print(question.url)

            questionId = question.json()['data']['questions'][num]['id']

            # 做题

            data2 = {'startTime': time.time(), 'finishTime': time.time(), 'isSubmit': 0, 'questionId': questionId,
                     'answer': [], 'sourceOf': 1, 'parentQuestionId': questionId}
            data = requests.put('https://learnta.cn/__api/beatV3/student/task/27/' + str(taskExecutionId) + '/answer',
                                data=json.dumps(data2), headers=headers)
            logging.info(data.json())
            print(data.status_code)

            num += 1
        end = requests.put(
            'https://learnta.cn/__api/beatV3/student/task/27/' + str(taskExecutionId) + '/end'
            , headers=headers)
        print(huoqkeid.status_code)
        report = requests.get(
            'https://learnta.cn/__api/beatV3/public/student/task/27/' + str(taskExecutionId) + '/report',
            headers=headers)
        testResult = end.json()['message']
        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="化学多选题卡做题失败")


    def testznlxk(self):
        '''测试1.0智能练习卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'username': ousername, 'code': ocode, 'systemId': 11, 'orgId': oorgId}
        loginOrgResponse = requests.post("https://autotest.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        print(loginOrgResponse.status_code)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        qwes = {'orgId': oorgId, 'homeworkName': "圆的有关概念", 'tasks': [{'courseId': "63509", 'taskId': 6752276}]}
        data4 = requests.post('https://autotest.learnta.cn/__api/beatV3/org/homework/assignTask', data=json.dumps(qwes),
                              headers=headers)
        print(data4.status_code)
        cardid = data4.json()['id']

        # print(self.kpid)#卡片id
        # print(data4.status_code)#请求是否成功
        # 做题时登录

        loginOrgPostdata = {'openId': "", 'randomCode': cardid, 'shareType': "homework", 'username': '算法测试','mobile': ousername,'code': ocode}
        loginOrgResponsedata = requests.post("https://learnta.cn/__api/wechat/public/wechat/qRcode/login",
                                             data=json.dumps(loginOrgPostdata), headers=self.headers)


        #获取homeworkId
        homeworkId = loginOrgResponsedata.json()['data']['homeworkId']
        print(homeworkId)
        #
        #获取课程id\
        huoqkeid = requests.get('https://learnta.cn/__api/beatV3/org/homework/getHomework?homeworkId='+homeworkId
                          ,headers=headers)
        taskExecutionId = huoqkeid.json()['unDoneTaskExecutions'][0]['id']
        # print(self.cs)
        # print(huoqkeid.url)
        # print(huoqkeid.status_code)
        #
        # #===============================================
        # 获取题目id question
        qqbw = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': taskExecutionId}
        questions = requests.post('https://learnta.cn/__api/beatV3/student/task/11/' + str(taskExecutionId) + '/question',
                                 data=json.dumps(qqbw), headers=headers)
        # print(question.status_code)
        # print(question.url)
        questionId = questions.json()['data']['questions'][0]['id']
        question = questions.json()['message']
        # 做题

        while question == 'success':
            #做题
            data2 = {'questionId': questionId, 'answer': [], 'sourceOf': 'null'}
            data = requests.put('https://learnta.cn/__api/beatV3/student/task/11/'+str(taskExecutionId)+'/answer',data = json.dumps(data2),headers = headers)
            logging.info(data.json())
            print(data.status_code)

            # 获取题目id question
            # 获取题目id question
            qqbw = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': taskExecutionId}
            questions = requests.post(
                'https://learnta.cn/__api/beatV3/student/task/11/' + str(taskExecutionId) + '/question',
                data=json.dumps(qqbw), headers=headers)
            # print(question.status_code)
            # print(question.url)
            question = questions.json()['message']
            if question == 'success':
                questionId = questions.json()['data']['questions'][0]['id']

            # 做题

        report = requests.get('https://learnta.cn/__api/beatV3/student/task/11/'+str(taskExecutionId)+ '/report', headers=headers)
        print(report.status_code)
        testResult = report.json()['message']

        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="智能练习卡测试失败")

    def testwldxt(self):
        '''测试1.0物理多选题卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'username': ousername, 'code': ocode, 'systemId': 11, 'orgId': oorgId}
        loginOrgResponse = requests.post("https://autotest.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        print(loginOrgResponse.status_code)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)  # 登录码

        # 请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        qwes = {'orgId': oorgId, 'homeworkName': "多选题卡", 'tasks': [{'courseId': "113779", 'taskId': 20402409}]}
        data4 = requests.post('https://autotest.learnta.cn/__api/beatV3/org/homework/assignTask', data=json.dumps(qwes),
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
        num = 0
        while num < 8:
            # 获取   questionId
            # 获取题目id question
            qqbw = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': taskExecutionId}
            question = requests.post(
                'https://learnta.cn/__api/beatV3/student/task/27/' + str(taskExecutionId) + '/question',
                data=json.dumps(qqbw), headers=headers)
            # print(question.status_code)
            # print(question.url)

            questionId = question.json()['data']['questions'][num]['id']

            # 做题

            data2 = {'startTime': time.time(), 'finishTime': time.time(), 'isSubmit': 0, 'questionId': questionId,
                     'answer': [], 'sourceOf': 1, 'parentQuestionId': questionId}
            data = requests.put('https://learnta.cn/__api/beatV3/student/task/27/' + str(taskExecutionId) + '/answer',
                                data=json.dumps(data2), headers=headers)
            logging.info(data.json())
            print(data.status_code)

            num += 1
        end = requests.put(
            'https://learnta.cn/__api/beatV3/student/task/27/' + str(taskExecutionId) + '/end'
            , headers=headers)
        print(huoqkeid.status_code)
        report = requests.get(
            'https://learnta.cn/__api/beatV3/public/student/task/27/' + str(taskExecutionId) + '/report',
            headers=headers)
        testResult = end.json()['message']
        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="物理多选题卡做题失败")

    #=============================================================



    def testkupcyc(self):
        '''测试酷培测一测'''
        print('测试酷培测一测')
        # 请求头I
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录
        loginOrgPost = {'username': username, 'password': password, 'systemId': 4, 'orgId': orgId}
        loginOrgResponse = requests.post("https://www.kupeiai.cn/__api/auth/user/loginKupeiStudent",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        self.token = loginOrgResponse.json()['data']['access_token']
        orgid = loginOrgResponse.json()['data']['orgId']
        print(orgid)
        studentId = loginOrgResponse.json()['data']['user']['id']
        print(self.token)  # 登录码

        # 请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}

        #进入课程
        data = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/category?isMember=false&isFromTAD=false&orgId='+str(orgid)+'&studentId='+str(studentId)+'&isKupeiStudent=true',
            headers=headers)
        category = data.json()['data'][0]['category']
        print(category)

        data2 = requests.get('https://www.kupeiai.cn/__api/beatV3/intelligentstudy/student/getIntelligentRoom?orgId='+str(orgid)+'&category='+str(category),headers=headers)
        print(data2.status_code)
        print(data2.url)
        intelligentRoomId = data2.json()['data'][0]['intelligentRoomId']

        data4 = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/student/getChapter?intelligentRoomId='+str(intelligentRoomId)+'&source=pc',
            headers=headers)
        # self.kpid = data4.json()['data']['roomId']
        chapterId = data4.json()['data']['chapterResults'][0]['chapterId']
        print(chapterId)  # 卡片id
        # 获取课程
        asdasdf = {'intelligentStudyRoomTopicId': chapterId, 'orgId': orgid}
        saad = requests.post('https://www.kupeiai.cn/__api/beatV3/student/task/24', json=asdasdf,
                             headers=headers)
        print(saad.status_code)
        taskExecutionId = saad.json()['data']['taskExecution']['id']
        print(taskExecutionId)
        # 获取题目id
        ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                 'taskExecutionId': taskExecutionId}
        huoqkeid = requests.post(
            'https://www.kupeiai.cn/__api/beatV3/student/task/24/' + str(taskExecutionId) + '/question'
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
                'https://www.kupeiai.cn/__api/beatV3/student/task/24/' + str(taskExecutionId) + '/answer',
                data=json.dumps(adsad), headers=headers)

            print(huoqutimuid.status_code)
            # 再次获取题目id
            ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                     'taskExecutionId': taskExecutionId}
            huoqkeid = requests.post(
                'https://www.kupeiai.cn/__api/beatV3/student/task/24/' + str(taskExecutionId) + '/question'
                , data=json.dumps(ijsji), headers=headers)
            print(huoqkeid.status_code)
            question = huoqkeid.json()['data']['questions']
            # print(question)
            if question is not None:
                questionId = huoqkeid.json()['data']['questions'][0]['id']
                print(questionId)
            num += 1
        #
        #进入报告页
        nihao1 = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/student/task/24/' + str(taskExecutionId) + '/report',
            headers=headers)
        print(nihao1.status_code)
        dasd = requests.get('https://www.kupeiai.cn/__api/beatV3/public/getOrg/'+str(orgid), headers=headers)

        testResult = nihao1.json()['message']
        print(testResult)
        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="酷培测一测测试失败")

    def testjixu(self):
        '''测试酷培继续'''
        # 请求头
        print('测试酷培继续')
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录
        loginOrgPost = {'username': usernames, 'password': passwords, 'systemId': 4, 'orgId': orgId}
        loginOrgResponse = requests.post("https://www.kupeiai.cn/__api/auth/user/loginKupeiStudent",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        access_token = loginOrgResponse.json()['data']['access_token']
        orgid = loginOrgResponse.json()['data']['orgId']
        print(orgid)
        studentId = loginOrgResponse.json()['data']['user']['id']
        print(access_token)  # 登录码

        # 请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + access_token}
        # 获取课程id
        data = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/category?isMember=false&isFromTAD=false&orgId=' + str(
                orgid) + '&studentId=' + str(studentId) + '&isKupeiStudent=true',
            headers=headers)
        category = data.json()['data'][0]['category']
        print(category)

        # 获取课程房间id
        data2 = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/student/getIntelligentRoom?orgId=' + str(
                orgid) + '&category=' + str(category), headers=headers)
        print(data2.status_code)
        intelligentRoomId = data2.json()['data'][30]['intelligentRoomId']

        # 获取卡片
        data4 = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/student/getChapter?intelligentRoomId=' + str(
                intelligentRoomId) + '&source=pc',
            headers=headers)
        # werwr = data4.json()
        # print(werwr)
        chapterId = data4.json()['data']['chapterResults'][1]['chapterId']
        source = data4.json()['data']['source']

        loginOrgResponsedata = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/' + str(chapterId) + '/chapter?source=' + str(
                source) + '&roomId=' + str(intelligentRoomId),
            headers=headers)
        # 获取taskExecutionId
        taskExecutionId = loginOrgResponsedata.json()['data']['taskExecutionId']
        print(taskExecutionId)
        #
        # #获取课程id
        ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                 'taskExecutionId': taskExecutionId}
        huoqkeid = requests.post(
            'https://www.kupeiai.cn/__api/beatV3/student/task/22/' + str(taskExecutionId) + '/question'
            , data=json.dumps(ijsji), headers=headers)
        questionid = huoqkeid.json()['data']['questions'][0]['id']
        kpointId = huoqkeid.json()['data']['questions'][0]['kpointId']
        print(huoqkeid.status_code)
        print(questionid)
        # ===============================================
        # 做题
        num = 0
        while num < 3:
            adsad = {'questionId': questionid, 'answer': []}
            huoqutimuid = requests.put(
                'https://www.kupeiai.cn/__api/beatV3/student/task/22/' + str(taskExecutionId) + '/answer',
                data=json.dumps(adsad), headers=headers)
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
            num += 1
            #
        dasd = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/student/task/22/' + str(taskExecutionId) + '/report?isSummary=true',
            headers=headers)
        print(dasd.status_code)
        testResult = dasd.json()['message']

        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="酷培继续测试失败")



    def testlijigk(self):
        '''测试酷培立即攻克'''
        print('测试酷培立即攻克')
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录
        loginOrgPost = {'username': usernames, 'password': passwords, 'systemId': 4, 'orgId': orgId}
        loginOrgResponse = requests.post("https://www.kupeiai.cn/__api/auth/user/loginKupeiStudent",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        access_token = loginOrgResponse.json()['data']['access_token']
        orgid = loginOrgResponse.json()['data']['orgId']
        print(orgid)
        studentId = loginOrgResponse.json()['data']['user']['id']
        print(access_token)  # 登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + access_token}
        # 获取课程id
        data = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/category?isMember=false&isFromTAD=false&orgId=' + str(
                orgid) + '&studentId=' + str(studentId) + '&isKupeiStudent=true',
            headers=headers)
        category = data.json()['data'][0]['category']
        print(category)
        # 获取课程房间id
        data2 = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/student/getIntelligentRoom?orgId=' + str(
                orgid) + '&category=' + str(category), headers=headers)
        print(data2.status_code)
        intelligentRoomId = data2.json()['data'][0]['intelligentRoomId']

        # 获取卡片
        data4 = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/student/getChapter?intelligentRoomId=' + str(
                intelligentRoomId) + '&source=pc',
            headers=headers)
        chapterId = data4.json()['data']['chapterResults'][0]['chapterId']

        #获取kpointId
        SDASD = requests.get(
            'https://www.kupeiai.cn/__api/beatV3/intelligentstudy/getKpointListByChapterId?chapterId=' + str(
                chapterId) + '&orgId='+str(orgid), headers=headers)
        print(SDASD.status_code)
        #换知识点
        kpointId = SDASD.json()['data'][3]['kpointId']
        print(kpointId)


        #获取taskExecutionId
        asdasdf = {'intelligentStudyRoomTopicId': chapterId, 'orgId': orgid, 'kpointId': kpointId}
        saad = requests.post('https://www.kupeiai.cn/__api/beatV3/student/task/23', json=asdasdf,
                             headers=headers)
        print(saad.status_code)
        taskExecutionId = saad.json()['data']['taskExecution']['id']
        print(taskExecutionId)


        # #获取题目questionId
        ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false','taskExecutionId': taskExecutionId}
        huoqkeid = requests.post('https://www.kupeiai.cn/__api/beatV3/student/task/23/'+str(taskExecutionId)+'/question'
                          ,data=json.dumps(ijsji),headers=headers)
        question = huoqkeid.json()['data']['questions']
        questionId = huoqkeid.json()['data']['questions'][0]['id']
        print(questionId)
        #===============================================
        #做题
        while question is not None:
            adsad = {'questionId': questionId, 'answer': []}
            huoqutimuid = requests.put('https://www.kupeiai.cn/__api/beatV3/student/task/23/'+str(taskExecutionId)+'/answer', data=json.dumps(adsad),headers=headers)
            logging.info(huoqutimuid.json())
            print(huoqutimuid.status_code)

            ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                     'taskExecutionId': taskExecutionId}
            huoqkeid = requests.post(
                'https://www.kupeiai.cn/__api/beatV3/student/task/23/' + str(taskExecutionId) + '/question'
                , data=json.dumps(ijsji), headers=headers)
            print(huoqkeid.status_code)
            question = huoqkeid.json()['data']['questions']
            if question is not None:
                questionId = huoqkeid.json()['data']['questions'][0]['id']
                print(questionId)
            print(questionId)


            #
        nihao1 = requests.get('https://www.kupeiai.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId='+str(kpointId),headers=headers)
        print(nihao1.status_code)
        dasd = requests.get('https://www.kupeiai.cn/__api/beatV3/student/task/23/'+str(taskExecutionId)+'/report?isSummary=false',headers=headers)
        print(dasd.status_code)
        testResult = dasd.json()['message']

        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="酷培立即攻克测试失败")


#====================================================================



    def testtadjix(self):
        '''测试智能学习继续'''
        # 请求头
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        loginOrgPost = {'username': cusername, 'branch': str(corgId), 'password': cpassword,
                        'systemId': 4, 'orgId': corgId}
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
                corgId), headers=headers)
        print(data.status_code)
        category = data.json()['data'][0]['category']
        print(category)

        # # 获取课程房间id
        data2 = requests.get(
            'https://cj.learnta.cn/__api/beatV3/studentClassroom/list?orgId=' + str(
                corgId) + '&category=' + str(category), headers=headers)
        print(data2.status_code)
        intelligentRoomId = data2.json()['data'][0]['intelligentRoomId']
        #
        print(intelligentRoomId)
        # # 获取卡片
        data4 = requests.get(
            'https://cj.learnta.cn/__api/beatV3/studentClassroom/' + str(
                intelligentRoomId) + '?orgId='+str(corgId),
            headers=headers)
        chapterId = data4.json()['data']['chapterResults'][0]['chapterId']
        print(chapterId)
        source = data4.json()['data']['source']
        print(source)
        #
        loginOrgResponsedata = requests.get(
            'https://cj.learnta.cn/__api/beatV3/intelligentstudy/' + str(chapterId) + '/chapter?source=' + str(
                source) + '&roomId=' + str(intelligentRoomId),
            headers=headers)
        # 获取taskExecutionId
        taskExecutionId = loginOrgResponsedata.json()['data']['taskExecutionId']
        print(taskExecutionId)
        #
        # #获取题目questionId
        ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                 'taskExecutionId': taskExecutionId}
        huoqkeid = requests.post(
            'https://cj.learnta.cn/__api/beatV3/student/task/30/' + str(taskExecutionId) + '/question'
            , data=json.dumps(ijsji), headers=headers)
        questionid = huoqkeid.json()['data']['questions'][0]['id']
        kpointId = huoqkeid.json()['data']['questions'][0]['kpointId']
        # ===============================================
        # 做题
        num = 0
        while num < 3:
            adsad = {'questionId': questionid, 'answer': []}
            huoqutimuid = requests.put(
                'https://cj.learnta.cn/__api/beatV3/student/task/30/' + str(taskExecutionId) + '/answer',
                data=json.dumps(adsad), headers=headers)
            logging.info(huoqutimuid.json())
            print(huoqutimuid.status_code)

            ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                     'taskExecutionId': taskExecutionId}
            huoqkeid = requests.post(
                'https://cj.learnta.cn/__api/beatV3/student/task/30/' + str(taskExecutionId) + '/question'
                , data=json.dumps(ijsji), headers=headers)
            questionid = huoqkeid.json()['data']['questions'][0]['id']
            kpointId = huoqkeid.json()['data']['questions'][0]['kpointId']
            num += 1
            #
        nihao1 = requests.get(
            'https://cj.learnta.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId=' + str(kpointId),
            headers=headers)
        print(nihao1.status_code)
        dasd = requests.get(
            'https://cj.learnta.cn/__api/beatV3/student/task/30/' + str(taskExecutionId) + '/report?isSummary=true',
            headers=headers)
        print(dasd.status_code)
        testResult = nihao1.json()['message']
        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="智能学习继续测试失败")

    def testtadljgk(self):
        '''测试智能学习立即攻克'''
        # 请求头
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        loginOrgPost = {'username': cusername, 'branch': str(corgId), 'password': cpassword,
                        'systemId': 4, 'orgId': corgId}
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
                corgId), headers=headers)
        print(data.status_code)
        category = data.json()['data'][1]['category']
        print(category)

        # # 获取课程房间id
        data2 = requests.get(
            'https://cj.learnta.cn/__api/beatV3/studentClassroom/list?orgId=' + str(
                corgId) + '&category=' + str(category), headers=headers)
        print(data2.status_code)
        intelligentRoomId = data2.json()['data'][0]['intelligentRoomId']
        #
        print(intelligentRoomId)
        # # 获取卡片
        data4 = requests.get(
            'https://cj.learnta.cn/__api/beatV3/studentClassroom/' + str(
                intelligentRoomId) + '?orgId='+str(corgId),
            headers=headers)
        chapterId = data4.json()['data']['chapterResults'][1]['chapterId']
        print(chapterId)
        source = data4.json()['data']['source']
        print(source)
        # 获取kpointId
        SDASD = requests.get(
            'https://cj.learnta.cn/__api/beatV3/studentClassroom/chapter?chapterId=' + str(
                chapterId) + '&studyRoomId=' + str(intelligentRoomId)+'&orgId='+str(corgId), headers=headers)
        print(SDASD.status_code)
        #换知识点
        kpointId = SDASD.json()['data']['kpoints'][3]['kpointId']
        print(kpointId)

        # 获取taskExecutionId
        asdasdf = {'intelligentStudyRoomTopicId': chapterId, 'orgId': corgId, 'kpointId': kpointId ,'studyRoomId':intelligentRoomId}
        saad = requests.post('https://cj.learnta.cn/__api/beatV3/student/task/31', json=asdasdf,
                             headers=headers)
        print(saad.status_code)
        taskExecutionId = saad.json()['data']['taskExecution']['id']
        print(taskExecutionId)

        # #获取题目questionId
        ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                 'taskExecutionId': taskExecutionId}
        huoqkeid = requests.post(
            'https://cj.learnta.cn/__api/beatV3/student/task/31/' + str(taskExecutionId) + '/question'
            , data=json.dumps(ijsji), headers=headers)
        question = huoqkeid.json()['data']['questions']
        questionId = huoqkeid.json()['data']['questions'][0]['id']
        print(questionId)
        # ===============================================
        # 做题
        num = 0
        while question is not None:
            adsad = {'questionId': questionId, 'answer': []}
            huoqutimuid = requests.put('https://cj.learnta.cn/__api/beatV3/student/task/31/'+str(taskExecutionId)+'/answer', data=json.dumps(adsad),headers=headers)
            logging.info(huoqutimuid.json())
            ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                     'taskExecutionId': taskExecutionId}
            huoqkeid = requests.post(
                'https://cj.learnta.cn/__api/beatV3/student/task/31/' + str(taskExecutionId) + '/question'
                , data=json.dumps(ijsji), headers=headers)
            question = huoqkeid.json()['data']['questions']
            if question is not None:
                questionId = huoqkeid.json()['data']['questions'][0]['id']
                print(questionId)


        nihao1 = requests.get(
            'https://cj.learnta.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId=' + str(kpointId),
            headers=headers)
        print(nihao1.status_code)
        dasd = requests.get(
            'https://cj.learnta.cn/__api/beatV3/student/task/31/' + str(taskExecutionId) + '/report?isSummary=false',
            headers=headers)
        print(dasd.status_code)
        testResult = nihao1.json()['message']
        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="智能学习立即攻克测试失败")

    def testtadcyc(self):
        '''测试智能学习测一测'''
        # 请求头
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        loginOrgPost = {'username': cusername, 'branch': str(corgId), 'password': cpassword,
                        'systemId': 4, 'orgId': corgId}
        loginOrgResponse = requests.post("https://cj.learnta.cn/__api/auth/user/loginOrgStudent",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        print(loginOrgResponse.status_code)
        access_token = loginOrgResponse.json()['data']['access_token']
        print(access_token)  # 登录码

        # 请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + access_token}
        # 获取课程id
        data = requests.get(
            'https://cj.learnta.cn/__api/beatV3/intelligentstudy/category?isFromTAD=true&orgId=' + str(
                corgId), headers=headers)
        print(data.status_code)
        category = data.json()['data'][1]['category']
        print(category)

        # # 获取课程房间id
        data2 = requests.get(
            'https://cj.learnta.cn/__api/beatV3/studentClassroom/list?orgId=' + str(
                corgId) + '&category=' + str(category), headers=headers)
        print(data2.status_code)
        intelligentRoomId = data2.json()['data'][1]['intelligentRoomId']
        #
        print(intelligentRoomId)
        # # 获取章节
        data4 = requests.get(
            'https://cj.learnta.cn/__api/beatV3/studentClassroom/' + str(
                intelligentRoomId) + '?orgId=' + str(corgId),
            headers=headers)
        chapterId = data4.json()['data']['chapterResults'][0]['chapterId']
        print(chapterId)

        # 获取taskExecutionId
        asdasdf = {'intelligentStudyRoomTopicId': chapterId, 'orgId': corgId, 'studyRoomId': intelligentRoomId}
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
            huoqutimuid = requests.put(
                'https://cj.learnta.cn/__api/beatV3/student/task/32/' + str(taskExecutionId) + '/answer',
                data=json.dumps(adsad), headers=headers)
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
        dasd = requests.get('https://cj.learnta.cn/__api/beatV3/public/getOrg/' + str(corgId), headers=headers)

        testResult = nihao1.json()['message']
        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="智能学习测一测测试失败")


    def testtwodzcp(self):
        '''2.0TAD智能测评卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'username': ousername, 'code': ocode, 'systemId': 11, 'orgId': torgId}
        loginOrgResponse = requests.post("https://testkefu.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        print(loginOrgResponse.status_code)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        qwes = {"topicInfoId":"3072","kpointIds":[6000033265,6000033266,6000033267],"orgId":torgId,"topicName":"第一单元 大数的认识","examType":"newExam"}
        data4 = requests.post('https://testkefu.learnta.cn/__api/beatV3/ppt/topic/diygo/create', data=json.dumps(qwes),
                              headers=headers)
        print(data4.status_code)

        cardid = data4.json()['shareUrl']
        # 正则匹配后端返回的goUrl中的csteid
        pattern = re.findall('m/(.+?)$', cardid)  # 匹配规则cste=开头到&之间的字符串\
        result = pattern[0]
        print(result)

        # print(self.kpid)#卡片id
        # print(data4.status_code)#请求是否成功
        # 做题时登录

        loginOrgPostdata = {'openId': "", 'randomCode': result, 'shareType': "chargeExam", 'username': '算法测试','mobile': ousername,'code': ocode}
        loginOrgResponsedata = requests.post("https://learnta.cn/__api/wechat/public/wechat/qRcode/login",
                                             data=json.dumps(loginOrgPostdata), headers=self.headers)

        print(loginOrgResponsedata.status_code)

        #
        #获取cste
        huoqkeid = requests.get('https://learnta.cn/__api/beatV3/topic/goExam/'+str(result)
                          ,headers=headers)
        cste = huoqkeid.json()['cste']

        #获取question
        qqbw = {"userAnswers": [],'isRecommIfNoWeakPoints':'false',"isEvaluated": 'true', "taskExecutionId": cste}
        questionasda = requests.post('https://learnta.cn/__api/beatV3/student/task/18/'+ str(cste) + '/question',
                                 data=json.dumps(qqbw), headers=headers)
        # print(questionasda.status_code)
        question = questionasda.json()['data']['questions']
        questionId = questionasda.json()['data']['questions'][0]['id']

        # 做题
        while question is not None:
            #做题
            data2 = {'startTime':time.time(),'finishTime': time.time(), 'isSubmit': 0,'questionId': questionId, 'answer': [],'sourceOf': 1,'parentQuestionId': questionId}
            data = requests.put('https://learnta.cn/__api/beatV3/student/task/18/'+str(cste)+'/answer',data = json.dumps(data2),headers = headers)
            logging.info(data.json())
            print(data.status_code)
            #获取questionid

            qqbw = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                    'taskExecutionId': cste}
            questionasda = requests.post('https://learnta.cn/__api/beatV3/student/task/18/' + str(cste) + '/question',
                                         data=json.dumps(qqbw), headers=headers)
            question = questionasda.json()['data']['questions']
            if question is not None:
                questionId = questionasda.json()['data']['questions'][0]['id']


        ads = {'shareType': "chargeExam"}
        huoqkeid = requests.put(
            'https://learnta.cn/__api/beatV3/classroom/task/exam/addStudent/'+str(cste)
            ,data = json.dumps(ads), headers=headers)
        print(huoqkeid.status_code)

        adnis = requests.get(
            'https://learnta.cn/__api/beatV3/public/student/task/18/'+str(cste)+'/report'
            ,headers=headers)
        print(adnis.status_code)

        testResult = adnis.json()['message']
        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="2.0TAD定制测评做题失败")


    def testtwogo(self):
        '''测试go卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'username': ousername, 'code': ocode, 'systemId': 11, 'orgId': torgId}
        loginOrgResponse = requests.post("https://testkefu.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        print(loginOrgResponse.status_code)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)  # 登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        datatest = requests.get('https://www.learnta.cn/__api/wechat/public/qRcode/chargeExam/0344pF56liR4ZJCX2931064')

        print(datatest.status_code)


        #获取题目id
        huoqkcid = requests.get('https://learnta.cn/__api/beatV3/topic/goExam/0344pF56liR4ZJCX2931064',headers=headers)
        cste = huoqkcid.json()['cste']
        print(cste)

        #那topicid
        huoqtimid = requests.get('https://learnta.cn/__api/beatV3/public/classroom/task/taskDetail/'+str(cste),headers=headers)
        topicId = huoqtimid.json()['task']['topicId']
        print(topicId)
        #拿questionId
        huoqutimuid = requests.get('https://learnta.cn/__api/wechat/go/next/'+str(topicId)+'/go',headers = headers)
        questionId = huoqutimuid.json()['data']['questionId']
        print(questionId)


        while questionId is not None:
            # 判题
            verifyPostdata = {'questionId': questionId, 'userAnswer': []}
            qweasd =  requests.post('https://learnta.cn/__api/wechat/go/subject/study/item/quest/answer/verify',
                          data=json.dumps(verifyPostdata), headers=headers)
            # print(qweasd.url)
            # print(qweasd.status_code)
            # 推题拿questionId
            huoqutimuid = requests.get('https://learnta.cn/__api/wechat/go/next/' + str(topicId) + '/go',
                                       headers=headers)
            logging.info(huoqutimuid.json())
            questionId = huoqutimuid.json()['data']['questionId']
            print(questionId)
            studyItemId = huoqutimuid.json()['data']['studyItemId']
            #print(questionId)

        # # 结算
        dxwa = {'shareType': "chargeExam"}
        AS = requests.put('https://learnta.cn/__api/beatV3/classroom/task/exam/addStudent/'+str(cste), data=json.dumps(dxwa),headers=headers)
        print(AS.status_code)

        dafa = {'answer': [str(studyItemId)]}
        asdzxc = requests.put('https://learnta.cn/__api/beatV3/classroom/task/saveAnswer/'+str(cste),data=json.dumps(dafa),headers=headers)
        print(asdzxc.status_code)
        jsjxj = requests.put('https://learnta.cn/__api/beatV3/classroom/task/homework/finish/0/'+str(cste),headers=headers)
        print(jsjxj.status_code)

        qfys = {'itemId': studyItemId, 'source': "teach_side"}
        adnis=requests.post('https://learnta.cn/__api/wechat/public/subject/study/item',data=json.dumps(qfys),headers=headers)
        print(adnis.status_code)
        testResult = adnis.json()['message']
        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="2.0go卡做题失败")

    def testtwolxk(self):
        '''测试2.0练习卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'username': ousername, 'code': ocode, 'systemId': 11, 'orgId': torgId}
        loginOrgResponse = requests.post("https://autotest.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        print(loginOrgResponse.status_code)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)  # 登录码

        # 请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        qwes = {'orgId': torgId, 'homeworkName': "一元二次方程", 'tasks': [{'courseId': "113820", 'taskId': 20411673}]}
        data4 = requests.post('https://autotest.learnta.cn/__api/beatV3/org/homework/assignTask', data=json.dumps(qwes),
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
        num = 0
        while num < 10:
            # 获取   questionId
            # 获取题目id question
            qqbw = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': taskExecutionId}
            question = requests.post(
                'https://learnta.cn/__api/beatV3/student/task/17/' + str(taskExecutionId) + '/question',
                data=json.dumps(qqbw), headers=headers)
            # print(question.status_code)
            # print(question.url)
            questionId = question.json()['data']['questions'][num]['id']
            # 做题

            data2 = {'startTime': time.time(), 'finishTime': time.time(), 'isSubmit': 0, 'questionId': questionId,
                     'answer': [], 'sourceOf': 1, 'parentQuestionId': questionId}
            data = requests.put('https://learnta.cn/__api/beatV3/student/task/17/' + str(taskExecutionId) + '/answer',
                                data=json.dumps(data2), headers=headers)
            logging.info(data.json())
            print(data.status_code)

            num += 1
        end = requests.put(
            'https://learnta.cn/__api/beatV3/student/task/17/' + str(taskExecutionId) + '/end'
            , headers=headers)
        report = requests.put(
            'https://learnta.cn/__api/beatV3/public/student/task/17/' + str(taskExecutionId) + '/report'
            , headers=headers)
        print(report.status_code)
        print(end.status_code)
        testResult = end.json()['message']
        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="2.0练习卡做题失败")


#=========================================================================

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

    def testtherego(self):
        '''测试3.0go卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {"branch": storgId, "username": ousername, "code": ocode, "systemId": 11, "orgId": storgId}
        loginOrgResponse = requests.post("https://cj.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        print(loginOrgResponse.status_code)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)  # 登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        datatest = requests.get('https://www.learnta.cn/__api/wechat/public/qRcode/chargeExam/p5w6GsLm8mklnTm72935341')

        print(datatest.status_code)



        #获取题目id
        huoqkcid = requests.get('https://learnta.cn/__api/beatV3/topic/goExam/p5w6GsLm8mklnTm72935341',headers=headers)
        cste = huoqkcid.json()['cste']
        print(cste)

        huoqtimid = requests.get('https://learnta.cn/__api/beatV3/public/classroom/task/taskDetail/'+str(cste),headers=headers)
        topicId = huoqtimid.json()['task']['topicId']
        print(topicId)

        huoqutimuid = requests.get('https://learnta.cn/__api/wechat/go/next/'+str(topicId)+'/go',headers = headers)
        questionId = huoqutimuid.json()['data']['questionId']
        print(questionId)


        while questionId is not None:
            # 判题
            verifyPostdata = {'questionId': questionId, 'userAnswer': [""]}
            qweasd =  requests.post('https://learnta.cn/__api/wechat/go/subject/study/item/quest/answer/verify',
                          data=json.dumps(verifyPostdata), headers=headers)
            # print(qweasd.url)
            # print(qweasd.status_code)
            # 推题拿questionId
            huoqutimuid = requests.get('https://learnta.cn/__api/wechat/go/next/' + str(topicId) + '/go',
                                       headers=headers)
            logging.info(huoqutimuid.json())
            questionId = huoqutimuid.json()['data']['questionId']
            print(questionId)
            studyItemId = huoqutimuid.json()['data']['studyItemId']
            #print(questionId)

        # # 结算
        dxwa = {'shareType': "chargeExam"}
        AS = requests.put('https://learnta.cn/__api/beatV3/classroom/task/exam/addStudent/'+str(cste), data=json.dumps(dxwa),headers=headers)
        print(AS.status_code)

        dafa = {'answer': [str(studyItemId)]}
        asdzxc = requests.put('https://learnta.cn/__api/beatV3/classroom/task/saveAnswer/'+str(cste),data=json.dumps(dafa),headers=headers)
        print(asdzxc.status_code)
        jsjxj = requests.put('https://learnta.cn/__api/beatV3/classroom/task/homework/finish/0/'+str(cste),headers=headers)
        print(jsjxj.status_code)

        qfys = {'itemId': studyItemId, 'source': "teach_side"}
        adnis=requests.post('https://learnta.cn/__api/wechat/public/subject/study/item',data=json.dumps(qfys),headers=headers)
        print(adnis.status_code)
        testResult = adnis.json()['message']
        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="3.0go卡做题失败")




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