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
    configInfo = "C:\\shh\\uitest\\panwenjie\\config.ini"
    config = configparser.ConfigParser()
    config.read(configInfo, encoding='UTF-8')
    code = config.get("Info", "vcode")
    orgId = config.get("Info", "TADoneorgid")
    username = config.get("Info", "TADusername")

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

    def testdzcp(self):
        '''测试1.0定制测评'''
        # 请求头
        self.headers = {'content-type': 'application/json;charset=UTF-8'};
        # 教师端登录

        loginOrgPost = {'username': username, 'code': code, 'systemId': 11, 'orgId': orgId}
        loginOrgResponse = requests.post("https://autotest.learnta.cn/__api/auth/user/loginOrg",
                                         data=json.dumps(loginOrgPost), headers=self.headers)
        print(loginOrgResponse.status_code)
        self.token = loginOrgResponse.json()['data']['access_token']
        print(self.token)#登录码

        #请求头
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + self.token}
        # 发送卡片
        qwes = {'topicInfoId': "3496", 'kpointIds': [6000050826, 6000050827, 6000050828], 'orgId': orgId,'examType':"newExam",'topicName':"Unit 1 情景交际"}
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

        loginOrgPostdata = {'openId': "", 'randomCode': result, 'shareType': "chargeExam", 'username': '算法测试','mobile': username,'code': code}
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
        self.assertEqual(testResult, 'success', msg="练习卡做题失败")


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