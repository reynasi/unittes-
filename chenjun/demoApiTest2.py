#coding:utf-8
import sys
import platform
import unittest
from BeautifulReport import BeautifulReport
# 引入自定义的模块
sys.path.append('/opt/uitest/')
sys.path.append('/opt/uitest/chenjun/')
sys.path.append('/opt/uitest/chenjun/libs/RequestTest')
from chenjun.libs.RequestTest import *

# 根据系统环境走不同的目录路径来写测试报告
if (platform.system() == 'Windows'):
    print(platform.system())
    report_dir = "D:\\uitest\\report"
    print(report_dir)
elif (platform.system() == 'Linux'):
    report_dir = '/opt/uitest/report'
    print(platform.system())
    print(report_dir)
else:
    print(platform.system())

# 开始测试
class demoApiTest(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    # def testDemo(self):
    #     '''测试一下verifycode'''
    #     url = 'https://cj.t1.learnta.cn/__api/auth/user/verifycode'
    #     headers = {'content-type': 'application/json;charset=UTF-8'}
    #     postdata = {'mobile': 18616015760, 'orgId': 1000491}
    #     TestResult = list(postRequestTest(url, headers, postdata))
    #     print('测试结果:' + str(TestResult))
    #     print('\n')
    #     self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")
    #
    # def testDemo1(self):
    #     '''测试一下csm/alarm'''
    #     url = 'https://t1.learnta.cn/__api/csm/alarm'
    #     headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer 3dad9541-6db0-3a97-9d36-5c489957e794'}
    #     postdata = {"time":"2020-06-01 18:59:33","type":1,"content":"2345"}
    #     TestResult = list(postRequestTest(url, headers, postdata))
    #     print('测试结果:' + str(TestResult))
    #     print('\n')
    #     self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")
    #
    # def testDemo2(self):
    #     '''测试get请求'''
    #     url = 'https://bcq.learnta.cn/__api/auth/role/rolelist/100240/11/0'
    #     headers = {'content-type': 'application/json;charset=UTF-8','authorization': 'Bearer d9b12089-83aa-3bc2-92f1-cdc10cfd230e'}
    #     TestResult = list(getRequestTest(url, headers))
    #     print('测试结果:' + str(TestResult))
    #     print('\n')
    #     self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")
    #
    # def testDemo3(self):
    #     '''测试put请求'''
    #     url = 'https://t1.learnta.cn/__api/crm/leads/39/3133/update'
    #     headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ddee48d8-83cb-3473-94e6-d64804158947'}
    #     putdata = {"stars": 2}
    #     TestResult = list(putRequestTest(url, headers, putdata))
    #     print('测试结果:' + str(TestResult))
    #     print('\n')
    #     self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")
    #
    # def testDemo4(self):
    #     '''测试创建课程接口https: // ceshixia.t1.learnta.cn / __api / library / newCourse / insert'''
    #     url = 'https://ceshixia.t1.learnta.cn/__api/library/newCourse/insert'
    #     headers = {'content-type': 'application/json;charset=UTF-8',
    #                'authorization': 'Bearer ddee48d8-83cb-3473-94e6-d64804158947'}
    #     postdata = {'orgId': 1000142, 'category': 0, 'press': 6000000001, 'courseName': "英语仁爱版test"}
    #     TestResult = list(postRequestTest(url, headers, postdata))
    #     print('测试结果:' + str(TestResult))
    #     print('\n')
    #     self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")
    #
    # def testDemo5(self):
    #     '''测试get请求'''
    #     url = 'https://jumping1.t1.learnta.cn/__api/beatV3/org/homework/byId/19104?orgId=1000142&source=1'
    #     headers = {'content-type': 'application/json;charset=UTF-8',
    #                'authorization': 'Bearer 5362770a-c686-3664-a96f-6710ae961b8c'}
    #     TestResult = list(getRequestTest(url, headers))
    #     print('测试结果:' + str(TestResult))
    #     print('\n')
    #     self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    # def testDemo6(self):
    #     '''测试新get请求'''
    #     url = 'https://bcq.learnta.cn/__api/auth/role/rolelist/100240/11/0'
    #     testurl = 'https://bcq.learnta.cn/__api/auth/role/rolelist/{}/{}/{}'
    #     headers = {'content-type': 'application/json;charset=UTF-8','authorization': 'Bearer d9b12089-83aa-3bc2-92f1-cdc10cfd230e'}
    #     TestResult = list(getErrorRequestTest(url, testurl, headers))
    #     print('测试结果:' + str(TestResult))
    #     print('\n')
    #     self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")
    def testDemo7(self):
        '''测试put 请求为list类型'''
        url = 'https://learnta.cn/__api/crm/leads/39/3133/update'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ddee48d8-83cb-3473-94e6-d64804158947'}
        putdata = [123,123,123]
        TestResult = list(putRequestTest(url, headers, putdata))
        print('测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

testsuite = unittest.TestSuite()
testsuite.addTests(unittest.makeSuite(demoApiTest))

runner = BeautifulReport((testsuite))
runner.report(filename='全量场景接口测试.html', description='全量场景接口测试用例', report_dir=report_dir)