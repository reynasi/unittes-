#coding:utf-8
import re
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
    # 读配置文件信息
    configInfo = "D:\\uitest\\chenjun\\algorithmTest\\config.ini"
    config = configparser.ConfigParser()
    config.read(configInfo, encoding='gbk')
    vcode = config.get("Info", "vcode")
    orgid = config.get("Info", "orgid")
    username = config.get("Info", "username")
elif (platform.system() == 'Linux'):
    report_dir = '/opt/uitest/report'
    print(platform.system())
else:
    print(platform.system())

# 开始测试
class algoTestdemo(unittest.TestCase):

    def setUp(self):
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        loginOrgPostdata={"branch":orgid,"username":username,"code":vcode,"systemId":11,"orgId":orgid}
        loginOrgResponsedata=requests.post("https://cj.learnta.cn/__api/auth/user/loginOrg",data=json.dumps(loginOrgPostdata),headers=self.headers)
        self.token=loginOrgResponsedata.json()['data']['access_token']
        #print(self.token)
    def tearDown(self):
        pass

    def testGO_01(self):
        '''测试go测评卡'''

        headers = {'content-type': 'application/json;charset=UTF-8','authorization': 'Bearer ' + self.token};

        # 拿goUrl
        goUrlResponsedata=requests.get('https://cj.learnta.cn/__api/beatV3/topic/go/100283/3410',headers=headers)
        goUrl = goUrlResponsedata.json()['goUrl']
        # 正则匹配后端返回的goUrl中的csteid
        pattern = re.compile(r'cste=(.*?)&')  # 匹配规则cste=开头到&之间的字符串
        result = pattern.findall(goUrl)

        # 拿Cste
        cste = result[0]
        #print(cste)

        # 拿topicId
        taskDetailResponsedata=requests.get('https://www.learnta.cn/__api/beatV3/public/classroom/task/taskDetail/' + cste,headers=headers)
        #print(taskDetailResponsedata.json()['task']['topicId'])
        topicId=taskDetailResponsedata.json()['task']['topicId']

        # 推题拿questionId
        goResponsedata=requests.get('https://www.learnta.cn/__api/wechat/go/next/'+str(topicId)+'/go',headers=headers)
        questionId=goResponsedata.json()['data']['id']

        while questionId is not None:
            # 判题
            verifyPostdata = {"questionId":questionId,"userAnswer":[""]}
            requests.post('https://www.learnta.cn/__api/wechat/go/subject/study/item/quest/answer/verify',data=json.dumps(verifyPostdata),headers=headers)
            # 推题拿questionId
            goResponsedata=requests.get('https://www.learnta.cn/__api/wechat/go/next/'+str(topicId)+'/go',headers=headers)
            logging.info(goResponsedata.json())
            questionId=goResponsedata.json()['data']['id']
            studyItemId=goResponsedata.json()['data']['studyItemId']

        # exam/addStudent
        addStudentPostdata={"shareType": "orgShare"}
        addStudentResponsedata=requests.put('https://www.learnta.cn/__api/beatV3/classroom/task/exam/addStudent/'+ cste,data=json.dumps(addStudentPostdata),headers=headers)
        #print(addStudentResponsedata.json())

        # saveAnswer
        saveAnswerPostdata={"answer": [str(studyItemId)]}
        saveAnswerResponsedata=requests.put('https://www.learnta.cn/__api/beatV3/classroom/task/saveAnswer/' + cste, data=json.dumps(saveAnswerPostdata),headers=headers)
        #print(saveAnswerResponsedata.json())

        # homework/finish
        finishResponsedata=requests.put('https://www.learnta.cn/__api/beatV3/classroom/task/homework/finish/0/' + cste,headers=headers)
        #print(finishResponsedata.json())

        # /study/item
        itemPostdata={"itemId":studyItemId,"source":"teach_side"}
        itemResponsedata=requests.post('https://www.learnta.cn/__api/wechat/public/subject/study/item',data=json.dumps(itemPostdata),headers=headers)
        #print(itemResponsedata.json())
        testResult=itemResponsedata.json()['message']

        #断言测试结果
        self.assertEqual(testResult, 'success', msg="测试失败")

testsuite = unittest.TestSuite()
testsuite.addTests(unittest.makeSuite(algoTestdemo))

runner = BeautifulReport((testsuite))
runner.report(filename='算法demo测试.html', description='算法demo测试测试用例', report_dir=report_dir)