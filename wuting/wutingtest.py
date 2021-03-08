#coding:utf-8
import os, sys
import platform
import unittest
from BeautifulReport import BeautifulReport
#引入自定义的模块
from chenjun.libs.RequestTest import *


# print(__file__)#获取的是相对路径
# print(os.path.abspath(__file__))#获得的是绝对路径
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(os.path.dirname('D:/uitest/chenjun/libs/RequestTest.py'))    # 返回目录路径
# Base_DIR = os.path.dirname('D:/uitest/chenjun/libs')
# print(Base_DIR)
# sys.path.append(Base_DIR)#添加环境变量，因为append是从列表最后开始添加路径，可能前面路径有重复，最好用sys.path.insert(Base_DIR)从列表最前面开始添加

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
class demoApiTest(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def testDemo2(self):
        '''测试get请求'''
        url = 'https://bcq.learnta.cn/__api/auth/role/rolelist/100240/11/0'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': 'Bearer d9b12089-83aa-3bc2-92f1-cdc10cfd230e'}
        TestResult = list(getRequestTest(url, headers))
        print('备课测试结果:' + str(TestResult))

testsuite = unittest.TestSuite()
testsuite.addTests(unittest.makeSuite(demoApiTest))

runner = BeautifulReport((testsuite))
runner.report(filename='全量场景接口测试.html', description='verifycode接口测试用例', report_dir=report_dir)