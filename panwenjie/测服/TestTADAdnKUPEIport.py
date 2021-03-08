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

    def test3dzcp(self):
        '''测试3.0定制测评卡'''
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

        datatest = requests.get('https://t2.learnta.cn/__api/wechat/public/qRcode/chargeExam/6OhJXmMqh8dfMxPc88987')

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

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}

        data4 = requests.get(
            'https://kupeitrial.t2.kupeiai.cn/__api/beatV3/intelligentstudy/student/getChapter?intelligentRoomId=8813&source=pc',
            headers=headers)
        # self.kpid = data4.json()['data']['roomId']
        chapterId = data4.json()['data']['chapterResults'][0]['chapterId']
        print(chapterId)#卡片id
        #获取课程
        asdasdf = {'intelligentStudyRoomTopicId': chapterId, 'orgId': 1000787}
        saad = requests.post('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/24',json=asdasdf,headers=headers)
        print(saad.status_code)
        taskExecutionId = saad.json()['data']['taskExecution']['id']
        print(taskExecutionId)
        #获取题目id
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
        #做题
        while question is not None :
            #
            adsad = {'questionId': questionId, 'answer': []}
            huoqutimuid = requests.put('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/24/'+str(taskExecutionId)+'/answer', data=json.dumps(adsad),headers=headers)

            print(huoqutimuid.status_code)

            ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                     'taskExecutionId': taskExecutionId}
            huoqkeid = requests.post(
                'https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/24/' + str(taskExecutionId) + '/question'
                , data=json.dumps(ijsji), headers=headers)
            print(huoqkeid.status_code)
            question = huoqkeid.json()['data']['questions']
            if question is not None:
                questionId = huoqkeid.json()['data']['questions'][0]['id']
            num+=1
 #
        #
        nihao1 = requests.get('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/24/'+str(taskExecutionId)+'/report',headers=headers)
        print(nihao1.status_code)
        dasd = requests.get('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/public/getOrg/1000787',headers=headers)
        print(dasd.status_code)

        # asdasd = requests.get('https://t2.learnta.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId='+str(self.kccsd),headers=headers)
        # print(asdasd.status_code)
    def testkupeijix(self):
        '''测试酷培继续'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录
        loginOrgPost = {'username': "13975353140", 'password': "123qwe", 'systemId': 4, 'orgId': 1000650}
        loginOrgResponse = requests.post("https://kupeitrial.t2.kupeiai.cn/__api/auth/user/loginKupeiStudent",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        data4 = requests.get('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/intelligentstudy/student/getChapter?intelligentRoomId=6974&source=pc',
                              headers=headers)
        self.kpid = data4.json()['data']['chapterResults'][1]['chapterId']
        print(self.kpid)#卡片id

        loginOrgResponsedata = requests.get('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/intelligentstudy/'+str(self.kpid)+'/chapter?source=2&roomId=6974',
                                             headers=headers)
        #获取homeworkId
        self.homeworkId = loginOrgResponsedata.json()['data']['taskExecutionId']
        print(self.homeworkId)
        #
        # #获取课程id
        ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': self.homeworkId}
        huoqkeid = requests.post('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/22/'+str(self.homeworkId)+'/question'
                          ,data=json.dumps(ijsji),headers=headers)
        self.kecid = huoqkeid.json()['data']['questions'][0]['id']
        self.kccsd = huoqkeid.json()['data']['questions'][0]['kpointId']
        print(self.kecid)
        print(self.kccsd)
        num = 0
        #===============================================
        while num <3 :
            adsad = {'questionId': self.kecid, 'answer': [""]}
            huoqutimuid = requests.put('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/22/'+str(self.homeworkId)+'/answer', data=json.dumps(adsad),headers=headers)

            print(huoqutimuid.status_code)

            ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false', 'taskExecutionId': self.homeworkId}
            huoqkeid = requests.post('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/22/' + str(self.homeworkId) + '/question'
                , json=ijsji, headers=headers)
            print(huoqkeid.status_code)
            self.kecid = huoqkeid.json()['data']['questions'][0]['id']
            print(self.kecid)
            num += 1
        #
        nihao1 = requests.get('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId='+str(self.kccsd),headers=headers)
        print(nihao1.status_code)
        dasd = requests.get('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/22/309373/report?isSummary=true',headers=headers)
        print(dasd.status_code)
        testResult = dasd.json()['message']

        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="测试失败")

    def testqwe(self):
        '''测试酷培立即攻克'''
        # 请求头
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录
        loginOrgPost = {'username': "13975353140", 'password': "123qwe", 'systemId': 4, 'orgId': 1000650}
        loginOrgResponse = requests.post("https://kupeitrial.t2.kupeiai.cn/__api/auth/user/loginKupeiStudent",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)  # 登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        data4 = requests.get('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/intelligentstudy/student/getChapter?intelligentRoomId=8947&source=pc',
                              headers=headers)
        # self.kpid = data4.json()['data']['roomId']
        chapterId = data4.json()['data']['chapterResults'][0]['chapterId']
        print(chapterId)#卡片id

        #获取需要的知识点id
        SDASD = requests.get('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/intelligentstudy/getKpointListByChapterId?chapterId='+str(chapterId)+'&orgId=1000787',headers=headers)
        print(SDASD.status_code)
        kpointId = SDASD.json()['data'][9]['kpointId']
        print(kpointId)
        #
        asdasdf = {'intelligentStudyRoomTopicId': chapterId, 'orgId': 1000787, 'kpointId': kpointId}
        saad = requests.post('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/23',json=asdasdf,headers=headers)
        print(saad.status_code)
        taskExecutionId = saad.json()['data']['taskExecution']['id']
        print(taskExecutionId)
        #获取题目id
        ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                 'taskExecutionId': taskExecutionId}
        huoqkeid = requests.post(
            'https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/23/' + str(taskExecutionId) + '/question'
            , data=json.dumps(ijsji), headers=headers)

        print(huoqkeid.status_code)
        questionId = huoqkeid.json()['data']['questions'][0]['id']
        question = huoqkeid.json()['data']['questions']
        print(questionId)

        #
        num = 0
        # # # #===============================================
        while question is not None:


            adsad = {'questionId': questionId, 'answer': []}
            huoqutimuid = requests.put('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/23/'+str(taskExecutionId)+'/answer', data=json.dumps(adsad),headers=headers)
            logging.info(huoqutimuid.json())
            print(huoqutimuid.status_code)
        #
            num+=1
        #
            ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                     'taskExecutionId': taskExecutionId}
            huoqkeid = requests.post(
                'https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/23/' + str(taskExecutionId) + '/question'
                , data=json.dumps(ijsji), headers=headers)
            print(num)
            print(huoqkeid.status_code)
            question = huoqkeid.json()['data']['questions']
            if question is not None:
                questionId = huoqkeid.json()['data']['questions'][0]['id']
            print(questionId)
        # # #
        nihao1 = requests.get('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId='+str(kpointId),headers=headers)
        print(nihao1.status_code)
        dasd = requests.get('https://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/23/'+str(taskExecutionId)+'/report?isSummary=false',headers=headers)
        print(dasd.status_code)
        # # asdasd = requests.get('https://t2.learnta.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId='+str(self.kccsd),headers=headers)
        # # print(asdasd.status_code)
        testResult = nihao1.json()['message']

        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="测试失败")
        # dasd = requests.get('ttps://kupeitrial.t2.kupeiai.cn/__api/beatV3/student/task/23/'+str(taskExecutionId)+'/report?isSummary=false',headers=headers)
        # print(dasd.status_code)
        # # asdasd = requests.get('https://t2.learnta.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId='+str(self.kccsd),headers=headers)
        # # print(asdasd.status_code)

    def test1cgk(self):
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

    def test1dzcp(self):
        '''测试1.0定制测评卡'''
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

        datatest = requests.get('https://t2.learnta.cn/__api/wechat/public/qRcode/chargeExam/SYb84ATi1U1sUVsX88804')

        print(datatest.status_code)

        # 获取题目id
        huoqkcid = requests.get('https://t2.learnta.cn/__api/beatV3/topic/goExam/SYb84ATi1U1sUVsX88804',
                                headers=headers)
        kcid = huoqkcid.json()['cste']
        print(kcid)

        huoqtimid = requests.get('https://t2.learnta.cn/__api/beatV3/public/classroom/task/taskDetail/' + str(kcid),
                                 headers=headers)
        tmid = huoqtimid.json()['task']['topicId']
        print(tmid)

        huoqutimuid = requests.get('https://t2.learnta.cn/__api/wechat/go/next/' + str(tmid) + '/go', headers=headers)
        questionId = huoqutimuid.json()['data']['questionId']
        print(questionId)

        while questionId is not None:
            # 判题
            verifyPostdata = {'questionId': questionId, 'userAnswer': [""]}
            qweasd = requests.post('https://t2.learnta.cn/__api/wechat/go/subject/study/item/quest/answer/verify',
                                   data=json.dumps(verifyPostdata), headers=headers)
            # print(qweasd.url)
            # print(qweasd.status_code)
            # 推题拿questionId
            huoqutimuid = requests.get('https://t2.learnta.cn/__api/wechat/go/next/' + str(tmid) + '/go',
                                       headers=headers)
            logging.info(huoqutimuid.json())
            questionId = huoqutimuid.json()['data']['questionId']
            studyItemId = huoqutimuid.json()['data']['studyItemId']
            # print(questionId)

        # # 结算
        dxwa = {'shareType': "chargeExam"}
        requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/exam/addStudent/' + str(kcid), data=dxwa)

        dafa = {'answer': [str(studyItemId)]}
        asdzxc = requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/saveAnswer/' + str(kcid),
                              data=json.dumps(dafa), headers=headers)

        jsjxj = requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/homework/finish/0/' + str(kcid),
                             headers=headers)

        qfys = {'itemId': studyItemId, 'source': "teach_side"}
        yuming = requests.post('https://t2.learnta.cn/__api/wechat/public/subject/study/item', data=json.dumps(qfys),
                               headers=headers)
        testResult = yuming.json()['message']
        self.assertEqual(testResult, 'success', msg="测试失败")


    def test1go(self):
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

    def test1lxk(self):
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
        testResult = huoqkeid.json()['message']

        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="测试失败")

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

    def testhuoxdxt(self):
        '''测试化学多选练习卡'''
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
        adad = {'orgId': 1, 'homeworkName': "元素周期表_物质的量练习卡", 'tasks': [{'courseId': "17859", 'taskId': 1152923}]}
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
        taskExecutionId = huoqkeid.json()['unDoneTaskExecutions'][0]['id']
        # print(self.cs)
        # print(huoqkeid.url)
        # print(huoqkeid.status_code)

        #================
        # ===============================

        num = 0
        while num < 5:
            ## 获取   questionId
            # 获取题目id question
            shud = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': taskExecutionId}
            asdada = requests.post('https://t2.learnta.cn/__api/beatV3/student/task/3/' + str(taskExecutionId) + '/question',data = json.dumps(shud),headers = headers)
            questionid = asdada.json()['data']['questions'][num]['id']

            #做题
            data2 = {'startTime':time.time() , 'finishTime': time.time(), 'isSubmit': 0, 'questionId': questionid, 'answer': [],'sourceOf': 1,'parentQuestionId': questionid}
            data = requests.put('https://t2.learnta.cn/__api/beatV3/student/task/3/'+str(questionid)+'/answer',data = json.dumps(data2),headers = headers)
            logging.info(data.json())
            print(data.status_code)

            num += 1
        huoqkeid = requests.put(
            'https://t2.learnta.cn/__api/beatV3/student/task/3/'+str(taskExecutionId)+'/end'
            , headers=params)
        print(huoqkeid.status_code)

        testResult = huoqkeid.json()['message']

        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="测试失败")

    def testwork(self):
        '''测试TAD智能练习继续'''
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
        chapterId = data4.json()['data']['chapterResults'][1]['chapterId']
        print(chapterId)#卡片id

        loginOrgResponsedata = requests.get('https://t2.learnta.cn/__api/beatV3/intelligentstudy/'+str(chapterId)+'/chapter?source=1&roomId=7924',
                                             headers=headers)
        #获取homeworkId
        taskExecutionId = loginOrgResponsedata.json()['data']['taskExecutionId']
        print(taskExecutionId)
        #
        # #获取课程id
        ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false', 'taskExecutionId': taskExecutionId}
        huoqkeid = requests.post('https://t2.learnta.cn/__api/beatV3/student/task/30/'+str(taskExecutionId)+'/question'
                          ,data=json.dumps(ijsji),headers=headers)
        questionid = huoqkeid.json()['data']['questions'][0]['id']
        kpointId = huoqkeid.json()['data']['questions'][0]['kpointId']
        print(questionid)
        print(kpointId)
        # print(huoqkeid.status_code)
        num = 0
        #===============================================
        while num <3 :
            adsad = {'questionId': questionid, 'answer': [""]}
            huoqutimuid = requests.put('https://t2.learnta.cn/__api/beatV3/student/task/30/'+str(taskExecutionId)+'/answer', data=json.dumps(adsad),headers=headers)
            logging.info(huoqutimuid.json())
            print(huoqutimuid.status_code)

            ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                     'taskExecutionId': taskExecutionId}
            huoqkeid = requests.post(
                'https://t2.learnta.cn/__api/beatV3/student/task/30/' + str(taskExecutionId) + '/question'
                , data=json.dumps(ijsji), headers=headers)
            questionid = huoqkeid.json()['data']['questions'][0]['id']
            kpointId = huoqkeid.json()['data']['questions'][0]['kpointId']
            num += 1
        #
        nihao1 = requests.get('https://t2.learnta.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId='+str(kpointId),headers=headers)
        print(nihao1.status_code)
        dasd = requests.get('https://t2.learnta.cn/__api/beatV3/student/task/30/'+str(taskExecutionId)+'/report?isSummary=true',headers=headers)
        print(dasd.status_code)
        asdasd = requests.get('https://t2.learnta.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId='+str(kpointId),headers=headers)
        print(asdasd.status_code)
        testResult = asdasd.json()['message']

        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="测试失败")


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
        kpointId = SDASD.json()['data']['kpoints'][7]['kpointId']
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
        testResult = dasd.json()['message']

        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="测试失败")

        #
        nihao1 = requests.get('https://t2.learnta.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId='+str(kpointId),headers=headers)
        print(nihao1.status_code)
        dasd = requests.get('https://t2.learnta.cn/__api/beatV3/student/task/31/'+str(taskExecutionId)+'/report?isSummary=false',headers=headers)
        print(dasd.status_code)
        # asdasd = requests.get('https://t2.learnta.cn/__api/beatV3/intelligentstudy/ratelimitstatus?kpointId='+str(self.kccsd),headers=headers)
        # print(asdasd.status_code)

    def testqldx(self):
        '''测试物理多选练习卡'''
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
        adad = {'orgId': 1, 'homeworkName': "字母和词法", 'tasks': [{'courseId': "17881", 'taskId': 1153444}]}
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
        taskExecutionId = huoqkeid.json()['unDoneTaskExecutions'][0]['id']
        # print(self.cs)
        # print(huoqkeid.url)
        # print(huoqkeid.status_code)

        #================
        # ===============================

        num = 0
        while num < 3:
            ## 获取   questionId
            # 获取题目id question
            shud = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': taskExecutionId}
            asdada = requests.post('https://t2.learnta.cn/__api/beatV3/student/task/3/' + str(taskExecutionId) + '/question',data = json.dumps(shud),headers = headers)
            questionid = asdada.json()['data']['questions'][num]['id']

            #做题
            data2 = {'startTime':time.time() , 'finishTime': time.time(), 'isSubmit': 0, 'questionId': questionid, 'answer': [],'sourceOf': 1,'parentQuestionId': questionid}
            data = requests.put('https://t2.learnta.cn/__api/beatV3/student/task/3/'+str(questionid)+'/answer',data = json.dumps(data2),headers = headers)
            logging.info(data.json())
            print(data.status_code)

            num += 1
        huoqkeid = requests.put(
            'https://t2.learnta.cn/__api/beatV3/student/task/3/'+str(taskExecutionId)+'/end'
            , headers=params)
        print(huoqkeid.status_code)
        testResult = huoqkeid.json()['message']

        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="测试失败")

    def test2dzcp(self):
        '''测试2.0定制测评卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'branch': 1, 'username': 13975353140, 'code': 1111, 'systemId': 11, 'orgId': 1}
        loginOrgResponse = requests.post("https://panff.t2.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        self.token = loginOrgResponse.json()['data']['access_token']
        # print(self.token)#登录码

        # 请求头
        headers = {'content-type'
                   : 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片

        datatest = requests.get('https://t2.learnta.cn/__api/wechat/public/qRcode/chargeExam/snDeY4smKaNoPif488908')

        print(datatest.status_code)

        # 获取题目id
        huoqkcid = requests.get('https://t2.learnta.cn/__api/beatV3/topic/goExam/snDeY4smKaNoPif488908',
                                headers=headers)
        kcid = huoqkcid.json()['cste']
        print(kcid)

        huoqtimid = requests.get('https://t2.learnta.cn/__api/beatV3/public/classroom/task/taskDetail/' + str(kcid),
                                 headers=headers)
        tmid = huoqtimid.json()['task']['topicId']
        print(tmid)

        huoqutimuid = requests.get('https://t2.learnta.cn/__api/wechat/go/next/' + str(tmid) + '/go', headers=headers)
        questionId = huoqutimuid.json()['data']['questionId']
        print(questionId)

        while questionId is not None:
            # 判题
            verifyPostdata = {'questionId': questionId, 'userAnswer': [""]}
            qweasd = requests.post('https://t2.learnta.cn/__api/wechat/go/subject/study/item/quest/answer/verify',
                                   data=json.dumps(verifyPostdata), headers=headers)
            # print(qweasd.url)
            # print(qweasd.status_code)
            # 推题拿questionId
            huoqutimuid = requests.get('https://t2.learnta.cn/__api/wechat/go/next/' + str(tmid) + '/go',
                                       headers=headers)
            logging.info(huoqutimuid.json())
            questionId = huoqutimuid.json()['data']['questionId']
            studyItemId = huoqutimuid.json()['data']['studyItemId']
            # print(questionId)

        # # 结算
        dxwa = {'shareType': "chargeExam"}
        requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/exam/addStudent/' + str(kcid), data=dxwa)

        dafa = {'answer': [str(studyItemId)]}
        asdzxc = requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/saveAnswer/' + str(kcid),
                              data=json.dumps(dafa), headers=headers)

        jsjxj = requests.put('https://t2.learnta.cn/__api/beatV3/classroom/task/homework/finish/0/' + str(kcid),
                             headers=headers)

        qfys = {'itemId': studyItemId, 'source': "teach_side"}
        yuming = requests.post('https://t2.learnta.cn/__api/wechat/public/subject/study/item', data=json.dumps(qfys),
                               headers=headers)
        testResult = yuming.json()['message']
        self.assertEqual(testResult, 'success', msg="测试失败")


    def test2jxcp(self):
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
    def test2lxk(self):
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
        testResult = huoqkeid.json()['message']

        # 断言测试结果
        self.assertEqual(testResult, 'success', msg="测试失败")


    def test2znlxk(self):
        '''测试2.0智能练习卡'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'branch': "1000487", 'username': "13975353140", 'code': "1111", 'systemId': 11, 'orgId': 1000487}
        loginOrgResponse = requests.post("https://cj.t2.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        self.token = loginOrgResponse.json()['data']['access_token']
        # print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        adad = {'orgId': 1000487, 'homeworkName': "自定义练习", 'tasks': [{'courseId': "17739", 'taskId': 1153473}]}
        data4 = requests.post('https://cj.t2.learnta.cn/__api/beatV3/org/homework/assignTask', data=json.dumps(adad),
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
        adsad = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': self.kecid}
        huoqutimuid = requests.post('https://t2.learnta.cn/__api/beatV3/student/task/33/' + str(self.kecid) + '/question', data=json.dumps(adsad),headers=headers)
        questionId = huoqutimuid.json()['data']['questions'][0]['id']
        print(questionId)
        question = huoqutimuid.json()['message']
        print(question)
        while question == 'success':
            verifyPostdata={'questionId': questionId, 'answer': [], 'sourceOf': 1}
            qweasd = requests.put('https://t2.learnta.cn/__api/beatV3/student/task/33/' + str(self.kecid) +'/answer',
                                   data=json.dumps(verifyPostdata), headers=headers)
            print(qweasd.status_code)
            # print(qweasd.url)
            # print(qweasd.status_code)
            # 推题拿questionId
            adsad = {'userAnswers': [], 'isEvaluated': 'true', 'taskExecutionId': self.kecid}
            huoqutimuid = requests.post(
                'https://t2.learnta.cn/__api/beatV3/student/task/33/' + str(self.kecid) + '/question',
                data=json.dumps(adsad), headers=headers)
            question = huoqutimuid.json()['message']
            if question == 'success':
                questionId = huoqutimuid.json()['data']['questions'][0]['id']
            logging.info(qweasd.json())

        asda = requests.get('https://t2.learnta.cn/__api/beatV3/student/task/33/'+'/report',headers=headers)
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