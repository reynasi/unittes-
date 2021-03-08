#coding:utf-8
import os, sys
import platform
import unittest
from BeautifulReport import BeautifulReport
#引入自定义的模块
from chenjun.libs.RequestTest import *

# 根据系统环境判断需要读取的目录路径
if(platform.system()=='Windows'):
    print(platform.system())
    report_dir = "D:\\uitest\\report"
    print(report_dir)
elif(platform.system()=='Linux'):
    report_dir = '/opt/uitest/report'
    print(platform.system())
else:
    print(platform.system())

# 开始测试
class learntaplus(unittest.TestCase):

    def setUp(self):
        url = 'https://t1.learnta.cn/__api/auth/user/loginOrg'
        data = {"branch":"1","username":"13975353140","code":"1111","systemId":11,"orgId":1}
        headers = {'content-type': 'application/json;charset=UTF-8'}
        loginOrgResponse = requests.post(url,data=json.dumps(data), headers=headers)
        access_token = loginOrgResponse.json()['data']['access_token']
        print(access_token)
        self.headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' + access_token}

    def tearDown(self):
        pass

    def testhuoquzjie(self):
        '''继续接口--刘俊峰'''
        demo = requests.get(
            'https://api.t1.learnta.cn/v1/beatV3/intelligentstudy/51022/chapter?source=2&roomId=2826',
            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="获取章节列表测试失败")
        taskExecutionId = demo.json()['data']['taskExecutionId']
        print(taskExecutionId)
        data = {"userAnswers":[],"isEvaluated":'true',"taskExecutionId":taskExecutionId}
        demo1 = requests.post(
            'https://api.t1.learnta.cn/v1/beatV3/student/task/39/'+str(taskExecutionId)+'/question',data=json.dumps(data),
            headers=self.headers)
        self.assertEqual(demo1.status_code, 200, msg="获取章节列表测试失败")
        print(demo1.json())


testsuite = unittest.TestSuite()
testsuite.addTests(unittest.makeSuite(learntaplus))

#使用的report方法输出HTML格式的报告
runner = BeautifulReport((testsuite))
#runner.report(filename='KuPiWEB端测试.html', description='酷培学生端测试用例',log_path=report_dir)
# filename = time.strftime("%Y-%m-%d-%H-%M-%S")+r".html"



# 根据系统环境判断需要读取的目录路径
if(platform.system()=='Windows'):
    report_dir = 'C:\\python1\\day06'
    filename = "C:\\python1\\day05"
    print(platform.system())
    runner.report(filename='预发布服务接口测试.html', description='预发布服务接口测试', log_path=report_dir)
    print(report_dir)
    print(filename)
elif(platform.system()=='Linux'):
    report_dir = "/opt/uitest/report"
    filename = '/opt/uitest/img'
    runner.report(filename='预发布服务接口测试.html', description='预发布服务接口测试', report_dir=report_dir)
    print(report_dir)
    print(filename)
    print(platform.system())
else:
    print(platform.system())