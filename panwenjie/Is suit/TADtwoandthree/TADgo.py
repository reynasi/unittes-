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
    ousername = config.get("Info", "TADusername")
    torgId = config.get("Info", "TADtwoorgid")


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
        self.assertEqual(testResult, 'success', msg="2.0go做题失败")

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