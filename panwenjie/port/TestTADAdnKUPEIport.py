#coding:utf-8
import re
import time
import json
import logging
import platform
import unittest
import requests
import configparser
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


#123123
    def test1customization(self):
        '''测试1.0go测评卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'branch': 1, 'username': 13975353140, 'code': 1111, 'systemId': 11, 'orgId': 1}
        loginOrgResponse = requests.post("https://t2.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        self.token = loginOrgResponse.json()['data']['access_token']
        # print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片

        datatest = requests.get('https://t2.learnta.cn/__api/wechat/public/qRcode/chargeExam/SYb84ATi1U1sUVsX88804')

        print(datatest.status_code)



        #获取题目id
        huoqkcid = requests.get('https://t2.learnta.cn/__api/beatV3/topic/goExam/SYb84ATi1U1sUVsX88804',headers=headers)
        kcid = huoqkcid.json()['cste']
        print(kcid)

        huoqtimid = requests.get('https://t2.learnta.cn/__api/beatV3/public/classroom/task/taskDetail/'+str(kcid),headers=headers)
        tmid = huoqtimid.json()['task']['topicId']
        print(tmid)

        huoqutimuid = requests.get('https://t2.learnta.cn/__api/wechat/go/next/'+str(tmid)+'/go',headers = headers)
        questionId = huoqutimuid.json()['data']['questionId']
        print(questionId)


        while questionId is not None:
            # 判题
            verifyPostdata = {'questionId': questionId, 'userAnswer': [""]}
            qweasd =  requests.post('https://t2.learnta.cn/__api/wechat/go/subject/study/item/quest/answer/verify',
                          data=json.dumps(verifyPostdata), headers=headers)
            # print(qweasd.url)
            # print(qweasd.status_code)
            # 推题拿questionId
            huoqutimuid = requests.get('https://t2.learnta.cn/__api/wechat/go/next/'+str(tmid)+'/go',headers = headers)
            logging.info(huoqutimuid.json())
            questionId = huoqutimuid.json()['data']['questionId']
            studyItemId = huoqutimuid.json()['data']['studyItemId']
            #print(questionId)

        # # 结算
        dxwa = {'shareType': "chargeExam"}
        requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/exam/addStudent/' + str(kcid), data=dxwa)

        dafa = {'answer': [str(studyItemId)]}
        asdzxc = requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/saveAnswer/'+str(kcid),data=json.dumps(dafa),headers=headers)

        jsjxj = requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/homework/finish/0/'+str(kcid),headers=headers)


        qfys = {'itemId': studyItemId, 'source': "teach_side"}
        yuming=requests.post('https://t2.learnta.cn/__api/wechat/public/subject/study/item',data=json.dumps(qfys),headers=headers)
        testResult = yuming.json()['message']
        self.assertEqual(testResult, 'success', msg="测试失败")



#123123
    def test3customization(self):
        '''测试3.0go测评卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'branch': 1, 'username': 13975353140, 'code': 1111, 'systemId': 11, 'orgId': 1}
        loginOrgResponse = requests.post("https://cj.t2.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片

        datatest = requests.get('https://t2.learnta.cn/__api/wechat/public/qRcode/chargeExam/5Kqo3mCRzZsQRrGs88957')

        print(datatest.status_code)



        #获取题目id
        huoqkcid = requests.get('https://t2.learnta.cn/__api/beatV3/topic/goExam/5Kqo3mCRzZsQRrGs88957',headers=headers)
        kcid = huoqkcid.json()['cste']
        print(kcid)

        huoqtimid = requests.get('https://t2.learnta.cn/__api/beatV3/public/classroom/task/taskDetail/'+str(kcid),headers=headers)
        tmid = huoqtimid.json()['task']['topicId']
        print(tmid)

        huoqutimuid = requests.get('https://t2.learnta.cn/__api/wechat/go/next/'+str(tmid)+'/go',headers = headers)
        questionId = huoqutimuid.json()['data']['questionId']
        print(questionId)


        while questionId is not None:
            # 判题
            verifyPostdata = {'questionId': questionId, 'userAnswer': [""]}
            qweasd =  requests.post('https://t2.learnta.cn/__api/wechat/go/subject/study/item/quest/answer/verify',
                          data=json.dumps(verifyPostdata), headers=headers)
            # print(qweasd.url)
            # print(qweasd.status_code)
            # 推题拿questionId
            huoqutimuid = requests.get('https://t2.learnta.cn/__api/wechat/go/next/'+str(tmid)+'/go',headers = headers)
            logging.info(huoqutimuid.json())
            questionId = huoqutimuid.json()['data']['questionId']
            studyItemId = huoqutimuid.json()['data']['studyItemId']
            #print(questionId)

        # # 结算
        dxwa = {'shareType': "chargeExam"}
        requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/exam/addStudent/' + str(kcid), data=dxwa)

        dafa = {'answer': [str(studyItemId)]}
        asdzxc = requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/saveAnswer/'+str(kcid),data=json.dumps(dafa),headers=headers)

        jsjxj = requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/homework/finish/0/'+str(kcid),headers=headers)


        qfys = {'itemId': studyItemId, 'source': "teach_side"}
        yuming=requests.post('https://t2.learnta.cn/__api/wechat/public/subject/study/item',data=json.dumps(qfys),headers=headers)
        testResult = yuming.json()['message']
        self.assertEqual(testResult, 'success', msg="测试失败")


#123123
    def test2customization(self):
        '''测试2.0go测评卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'branch': 1, 'username': 13975353140, 'code': 1111, 'systemId': 11, 'orgId': 1}
        loginOrgResponse = requests.post("https://panff.t2.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        self.token = loginOrgResponse.json()['data']['access_token']
        # print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片

        datatest = requests.get('https://t2.learnta.cn/__api/wechat/public/qRcode/chargeExam/snDeY4smKaNoPif488908')

        print(datatest.status_code)



        #获取题目id
        huoqkcid = requests.get('https://t2.learnta.cn/__api/beatV3/topic/goExam/snDeY4smKaNoPif488908',headers=headers)
        kcid = huoqkcid.json()['cste']
        print(kcid)

        huoqtimid = requests.get('https://t2.learnta.cn/__api/beatV3/public/classroom/task/taskDetail/'+str(kcid),headers=headers)
        tmid = huoqtimid.json()['task']['topicId']
        print(tmid)

        huoqutimuid = requests.get('https://t2.learnta.cn/__api/wechat/go/next/'+str(tmid)+'/go',headers = headers)
        questionId = huoqutimuid.json()['data']['questionId']
        print(questionId)


        while questionId is not None:
            # 判题
            verifyPostdata = {'questionId': questionId, 'userAnswer': [""]}
            qweasd =  requests.post('https://t2.learnta.cn/__api/wechat/go/subject/study/item/quest/answer/verify',
                          data=json.dumps(verifyPostdata), headers=headers)
            # print(qweasd.url)
            # print(qweasd.status_code)
            # 推题拿questionId
            huoqutimuid = requests.get('https://t2.learnta.cn/__api/wechat/go/next/'+str(tmid)+'/go',headers = headers)
            logging.info(huoqutimuid.json())
            questionId = huoqutimuid.json()['data']['questionId']
            studyItemId = huoqutimuid.json()['data']['studyItemId']
            #print(questionId)

        # # 结算
        dxwa = {'shareType': "chargeExam"}
        requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/exam/addStudent/' + str(kcid), data=dxwa)

        dafa = {'answer': [str(studyItemId)]}
        asdzxc = requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/saveAnswer/'+str(kcid),data=json.dumps(dafa),headers=headers)

        jsjxj = requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/homework/finish/0/'+str(kcid),headers=headers)


        qfys = {'itemId': studyItemId, 'source': "teach_side"}
        yuming=requests.post('https://t2.learnta.cn/__api/wechat/public/subject/study/item',data=json.dumps(qfys),headers=headers)
        testResult = yuming.json()['message']
        self.assertEqual(testResult, 'success', msg="测试失败")

#123123
    def test1Emigrated(self):
        '''测试1.0闯关卡'''
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
        fskp = {'orgId': 1, 'homeworkName': "字母和词法", 'tasks': [{'courseId': 17781, 'taskId': 1151746}]}
        data4 = requests.post('https://t2.learnta.cn/__api/beatV3/org/homework/assignTask', data=json.dumps(fskp),
                              headers=headers)
        self.kpid = data4.json()['id']

        # print(self.kpid)#卡片id
        # print(data4.status_code)#请求是否成功
        # 做题时登录

        loginOrgPostdata = {'openId': "", 'randomCode': self.kpid, 'shareType': "homework", 'username': "13975353140",
                            'mobile': "13975353140", 'code': 1111}
        loginOrgResponsedata = requests.post("https://t2.learnta.cn/__api/wechat/public/wechat/qRcode/login",
                                             data=json.dumps(loginOrgPostdata), headers=self.headers)
        # print(loginOrgResponsedata.status_code)
        # 获取homeworkId
        self.homeworkId = loginOrgResponsedata.json()['data']['homeworkId']
        # print(self.homeworkId)

        # 获取课程id
        params = {'content-type': 'application/json', 'authorization': 'Bearer ' + self.token}
        huoqkeid = requests.get(
            'https://t2.learnta.cn/__api/beatV3/org/homework/getHomework?homeworkId=' + self.homeworkId
            , headers=params)
        self.kecid = huoqkeid.json()['unDoneTaskExecutions'][0]['id']
        # print(self.kecid)
        # print(self.cs)
        # print(huoqkeid.url)
        # print(huoqkeid.status_code)

        # ===============================================

        num = 0
        while num < 10:
            # 获取   questionId
            # 获取题目id question
            qqbw = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': self.kecid}
            question = requests.post(
                'https://t2.learnta.cn/__api/beatV3/student/task/4/' + str(self.kecid) + '/question',
                data=json.dumps(qqbw), headers=headers)
            # print(question.status_code)
            # print(question.url)
            self.questionId = question.json()['data']['questions'][num]['id']
            # 做题

            data2 = {'startTime': time.time(), 'finishTime': time.time(), 'isSubmit': 0, 'questionId': self.questionId,
                     'answer': [], 'sourceOf': 1, 'parentQuestionId': self.questionId}
            data = requests.put('https://t2.learnta.cn/__api/beatV3/student/task/4/' + str(self.kecid) + '/answer',
                                data=json.dumps(data2), headers=headers)
            logging.info(data.json())
            # print(data.status_code)
            num += 1
        print("查看是否结算")
        huoqkeid = requests.put(
            'https://t2.learnta.cn/__api/beatV3/student/task/4/' + str(self.kecid) + '/end'
            , headers=params)
        print(huoqkeid.status_code)

        if huoqkeid.status_code == 200:
            print("进入结算页面")
        else:
            print('没有进入结算页面')

#123123
    def test1teaching(self):
        '''测试1.0go测评卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'branch': 1, 'username': 13975353140, 'code': 1111, 'systemId': 11, 'orgId': 1}
        loginOrgResponse = requests.post("https://t2.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        self.token = loginOrgResponse.json()['data']['access_token']
        # print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        fskp = {'orgId': 1, 'homeworkName': "字母和词法", 'tasks': [{'courseId': 17781, 'taskId': 1151753}]}
        datatest = requests.post('https://t2.learnta.cn/__api/beatV3/org/homework/assignTask', data=json.dumps(fskp),
                              headers=headers)
        self.kpid = datatest.json()['id']
        # 获取接口id
        self.qwe = datatest.json()['taskTOs'][0]['topicId']
        print(self.qwe)

        # print(self.kpid)#卡片id
        # print(data4.status_code)#请求是否成功
        # 做题时登录

        loginOrgPostdata = {'openId': "", 'randomCode': self.kpid, 'shareType': "homework", 'username': "13975353140", 'mobile': "13975353140",'code': 1111}
        loginOrgResponsedata = requests.post("https://t2.learnta.cn/__api/wechat/public/wechat/qRcode/login",
                                             data=json.dumps(loginOrgPostdata), headers=self.headers)
        # print(loginOrgResponsedata.status_code)
        # 获取homeworkId
        self.homeworkId = loginOrgResponsedata.json()['data']['homeworkId']
        # print(self.homeworkId)

        # 获取课程id
        params = {'content-type': 'application/json', 'authorization': 'Bearer ' + self.token}
        huoqkeid = requests.get(
            'https://t2.learnta.cn/__api/beatV3/org/homework/getHomework?homeworkId=' + str(self.homeworkId)
            , headers=params)
        self.kecid = huoqkeid.json()['unDoneTaskExecutions'][0]['id']
        print(self.kecid)

        #获取题目id
        huoqutimuid = requests.get('https://t2.learnta.cn/__api/wechat/go/next/'+str(self.qwe)+'/go',headers = params)
        questionId = huoqutimuid.json()['data']['questionId']
        print(questionId)

        while questionId is not None:
            # 判题
            verifyPostdata = {'questionId': questionId, 'userAnswer': [""]}
            qweasd =  requests.post('https://t2.learnta.cn/__api/wechat/go/subject/study/item/quest/answer/verify',
                          data=json.dumps(verifyPostdata), headers=headers)
            # print(qweasd.url)
            # print(qweasd.status_code)
            # 推题拿questionId
            huoqutimuid = requests.get('https://t2.learnta.cn/__api/wechat/go/next/'+str(self.qwe)+'/go',headers = params)
            logging.info(huoqutimuid.json())
            questionId = huoqutimuid.json()['data']['questionId']
            studyItemId = huoqutimuid.json()['data']['studyItemId']
            #print(questionId)

        # 结算
        dafa = {'answer': [str(studyItemId)]}
        asdzxc = requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/saveAnswer/'+str(self.kecid),data=json.dumps(dafa),headers=params)

        vsaa =  requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/homework/finish/0/'+str(self.kecid),headers=params)

        qfys = {'itemId': studyItemId, 'source': "weChat"}
        yuming=requests.post('https://t2.learnta.cn/__api/wechat/public/subject/study/item',data=json.dumps(qfys),headers=params)
        testResult = yuming.json()['message']
        self.assertEqual(testResult, 'success', msg="测试失败")


#123123
    def test2teaching(self):
        '''测试2.0教学测评卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'branch': 1, 'username': 13975353140, 'code': 1111, 'systemId': 11, 'orgId': 1}
        loginOrgResponse = requests.post("https://panff.t2.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        self.token = loginOrgResponse.json()['data']['access_token']
        # print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        fskp = {'orgId': 1001310, 'homeworkName': "二次函数", 'tasks': [{'courseId': "17801", 'taskId': 1152020}]}
        datatest = requests.post('https://panff.t2.learnta.cn/__api/beatV3/org/homework/assignTask', data=json.dumps(fskp),
                              headers=headers)
        self.kpid = datatest.json()['id']
        # 获取接口id
        self.qwe = datatest.json()['taskTOs'][0]['topicId']
        print(self.qwe)

        # print(self.kpid)#卡片id
        # print(data4.status_code)#请求是否成功
        # 做题时登录

        loginOrgPostdata = {'openId': "", 'randomCode': self.kpid, 'shareType': "homework", 'username': "13975353140", 'mobile': "13975353140",'code': 1111}
        loginOrgResponsedata = requests.post("https://t2.learnta.cn/__api/wechat/public/wechat/qRcode/login",
                                             data=json.dumps(loginOrgPostdata), headers=self.headers)
        # print(loginOrgResponsedata.status_code)
        # 获取homeworkId
        self.homeworkId = loginOrgResponsedata.json()['data']['homeworkId']
        # print(self.homeworkId)

        # 获取课程id
        huoqkeid = requests.get(
            'https://t2.learnta.cn/__api/beatV3/org/homework/getHomework?homeworkId=' + str(self.homeworkId)
            , headers=headers)
        self.kecid = huoqkeid.json()['unDoneTaskExecutions'][0]['id']
        print(self.kecid)

        #获取题目id
        huoqutimuid = requests.get('https://t2.learnta.cn/__api/wechat/go/next/'+str(self.qwe)+'/go',headers = headers)
        questionId = huoqutimuid.json()['data']['questionId']
        print(questionId)

        while questionId is not None:
            # 判题
            verifyPostdata = {'questionId': questionId, 'userAnswer': [""]}
            qweasd =  requests.post('https://t2.learnta.cn/__api/wechat/go/subject/study/item/quest/answer/verify',
                          data=json.dumps(verifyPostdata), headers=headers)
            # print(qweasd.url)
            # print(qweasd.status_code)
            # 推题拿questionId
            huoqutimuid = requests.get('https://t2.learnta.cn/__api/wechat/go/next/'+str(self.qwe)+'/go',headers = headers)
            logging.info(huoqutimuid.json())
            questionId = huoqutimuid.json()['data']['questionId']
            studyItemId = huoqutimuid.json()['data']['studyItemId']
            #print(questionId)

        # 结算
        dafa = {'answer': [str(studyItemId)]}
        asdzxc = requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/saveAnswer/'+str(self.kecid),data=json.dumps(dafa),headers=headers)

        vsaa =  requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/homework/finish/0/'+str(self.kecid),headers=headers)

        qfys = {'itemId': studyItemId, 'source': "weChat"}
        yuming=requests.post('https://t2.learnta.cn/__api/wechat/public/subject/study/item',data=json.dumps(qfys),headers=headers)
        testResult = yuming.json()['message']
        self.assertEqual(testResult, 'success', msg="测试失败")



#123123
    def test1work(self):
        '''测试1.0练习卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'branch': 1, 'username': 13975353140, 'code': 1111, 'systemId': 11, 'orgId': 1}
        loginOrgResponse = requests.post("https://t2.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        self.token = loginOrgResponse.json()['data']['access_token']
        # print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        adad = {'orgId': 1, 'homeworkName': "yiyiyiyi", 'tasks': [{'courseId': 17781, 'taskId': 1151638}]}
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
        #获取homeworkId
        self.homeworkId = loginOrgResponsedata.json()['data']['homeworkId']
        # print(homeworkId)

        #获取课程id
        params = {'content-type': 'application/json', 'authorization': 'Bearer '+ self.token}
        huoqkeid = requests.get('https://t2.learnta.cn/__api/beatV3/org/homework/getHomework?homeworkId='+self.homeworkId
                          ,headers=params)
        self.kecid = huoqkeid.json()['unDoneTaskExecutions'][0]['id']
        # print(self.cs)
        # print(huoqkeid.url)
        # print(huoqkeid.status_code)

        #===============================================
        num = 0
        while num < 5:
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
            , headers=params)
        print(huoqkeid.status_code)




#123123
    def test2work(self):
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
        while num < 5:
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