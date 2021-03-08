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

authorizations = 'Bearer ed9cd164-0a74-36f9-bbbc-5f2de53fbf3c'

# 开始测试
class demoApiTest(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass


    def testcoursedata(self):
        '''测试移动课堂课程详情接口get（https://jumping1.t1.learnta.cn/__api/beatV3/org/homework/byId/19104?orgId=1000142&source=1）'''
        url = 'https://jumping1.t1.learnta.cn/__api/beatV3/org/homework/byId/19104?orgId=1000142&source=1'
        testurl = 'https://jumping1.t1.learnta.cn/__api/beatV3/org/homework/byId/{}?orgId={}&source={}'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        TestResult = list(getErrorRequestTest(url, testurl, headers))
        print('测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")


    def testprepdata(self):
        '''测试备课系统详情接口get（https://jumping1.t1.learnta.cn/__api/library/newCourse/byId/20053?orgId=1000142）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/newCourse/byId/20053?orgId=1000142'
        testurl = 'https://jumping1.t1.learnta.cn/__api/library/newCourse/byId/{}?orgId={}'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        TestResult = list(getErrorRequestTest(url, testurl, headers))
        print('备课系统详情测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")


    def testmycurr(self):
        '''测试我的课程接口get（https://jumping1.t1.learnta.cn/__api/library/newCourse/myCourse?orgId=1000142&pageNo=1&pageSize=10）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/newCourse/myCourse?orgId=1000142&pageNo=1&pageSize=10'
        testurl = 'https://jumping1.t1.learnta.cn/__api/library/newCourse/myCourse?orgId={}&pageNo={}&pageSize={}'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        TestResult = list(getErrorRequestTest(url, testurl, headers))
        print('我的课程测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testmycurr2(self):
        '''测试分页我的课程接口get（https://jumping1.t1.learnta.cn/__api/library/newCourse/myCourse?orgId=1000142&pageNo=0&pageSize=20）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/newCourse/myCourse?orgId=1000142&pageNo=0&pageSize=20'
        testurl = 'https://jumping1.t1.learnta.cn/__api/library/newCourse/myCourse?orgId={}&pageNo={}&pageSize={}'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        TestResult = list(getErrorRequestTest(url, testurl, headers))
        print('分页我的课程测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testlearncurr(self):
        '''测试备课系统-学习课程列表接口get（https://jumping1.t1.learnta.cn/__api/library/orgCourse/getOrgCourse?orgId=1000018&pageNo=1&pageSize=10）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/orgCourse/getOrgCourse?orgId=1000018&pageNo=1&pageSize=10'
        testurl = 'https://jumping1.t1.learnta.cn/__api/library/orgCourse/getOrgCourse?orgId={}&pageNo={}&pageSize={}'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        TestResult = list(getErrorRequestTest(url, testurl, headers))
        print('备课系统-学习课程列表测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testlearncurr2(self):
        '''测试分页备课系统-学习课程列表接口get（https://jumping1.t1.learnta.cn/__api/library/orgCourse/getOrgCourse?orgId=1000018&pageNo=0&pageSize=40）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/orgCourse/getOrgCourse?orgId=1000018&pageNo=0&pageSize=40'
        testurl = 'https://jumping1.t1.learnta.cn/__api/library/orgCourse/getOrgCourse?orgId={}&pageNo={}&pageSize={}'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        TestResult = list(getErrorRequestTest(url, testurl, headers))
        print('分页备课系统-学习课程列表测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testshpplist(self):
        '''测试课程市场列表接口get（https://jumping1.t1.learnta.cn/__api/library/newCourse/getAllOrgCourse?orgId=1000142&pageNo=1&pageSize=10）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/newCourse/getAllOrgCourse?orgId=1000142&pageNo=1&pageSize=10'
        testurl = 'https://jumping1.t1.learnta.cn/__api/library/newCourse/getAllOrgCourse?orgId={}&pageNo={}&pageSize={}'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        TestResult = list(getErrorRequestTest(url, testurl, headers))
        print('课程市场列表测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testshhlist(self):
        '''测试课程审核列表接口get（https://jumping1.t1.learnta.cn/__api/library/newCourse/getExamineCours?orgId=1000142&pageNo=1&pageSize=10&state=1）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/newCourse/getExamineCours?orgId=1000142&pageNo=1&pageSize=10&state=1'
        testurl = 'https://jumping1.t1.learnta.cn/__api/library/newCourse/getExamineCours?orgId={}&pageNo={}&pageSize={}&state={}'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        TestResult = list(getErrorRequestTest(url, testurl, headers))
        print('课程审核列表测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testshhlist2(self):
        '''测试分页课程审核列表接口get（https://jumping1.t1.learnta.cn/__api/library/newCourse/getExamineCours?orgId=1000142&pageNo=0&pageSize=20&state=0）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/newCourse/getExamineCours?orgId=1000142&pageNo=0&pageSize=20&state=0'
        testurl = 'https://jumping1.t1.learnta.cn/__api/library/newCourse/getExamineCours?orgId={}&pageNo={}&pageSize={}&state={}'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        TestResult = list(getErrorRequestTest(url, testurl, headers))
        print('分页课程审核列表测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testpptTask(self):
        '''测试搜索题目接口get（https://jumping1.t1.learnta.cn/__api/library/newCourse/getExamineCours?orgId=1000142&pageNo=0&pageSize=20&state=0）'''
        url = 'https://jumping1.t1.learnta.cn/__api/beatV3/pptTask/getAllTypeQuestion?orgId=1000142&category=0&pageSize=10&page=1&keywords=%E4%B8%80%E8%88%AC&pressId=6000000001&questionType=21'
        testurl = 'https://jumping1.t1.learnta.cn/__api/beatV3/pptTask/getAllTypeQuestion?orgId={}&category={}&pageSize={}&page={}&keywords={}&pressId={}&questionType={}'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        TestResult = list(getErrorRequestTest(url, testurl, headers))
        print('搜索题目测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")


    def testupcurr(self):
        '''测试修改课程接口put（https://jumping1.t1.learnta.cn/__api/library/newCourse/byId/20115）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/newCourse/byId/20115'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        putdata = {"grades": [1, 3]}
        TestResult = list(putRequestTest(url, headers, putdata))
        print('修改课程测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testsubshh(self):
        '''测试提交审核列表接口put（https://jumping1.t1.learnta.cn/__api/library/orgCourse/examine/20086）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/orgCourse/examine/20086'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        putdata = {"state":1,"reason":"null","mark":"hhhh"}
        TestResult = list(putRequestTest(url, headers, putdata))
        print('提交审核列表测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testshhyes(self):
        '''测试审核通过列表接口put（https://jumping1.t1.learnta.cn/__api/library/orgCourse/examine/20086）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/orgCourse/examine/20086'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        putdata = {"state":2,"audit":2,"reason":"sss"}
        TestResult = list(putRequestTest(url, headers, putdata))
        print('审核通过测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testshhnot(self):
        '''测试审核不通过列表接口put（https://jumping1.t1.learnta.cn/__api/library/orgCourse/examine/20086）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/orgCourse/examine/20086'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        putdata = {"state":3,"audit":3,"reason":"nnn"}
        TestResult = list(putRequestTest(url, headers, putdata))
        print('审核不通过测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")


    def teststutlist(self):
        '''测试开始上课-课堂列表接口post（https://jumping1.t1.learnta.cn/__api/beatV3/classroom/org/byTeacherId）'''
        url = 'https://jumping1.t1.learnta.cn/__api/beatV3/classroom/org/byTeacherId'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        postdata = {"state":0,"orgId":1000142}
        TestResult = list(postRequestTest(url, headers, postdata))
        print('开始上课-课堂列表测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def teststartlist(self):
        '''测试学生系统-课堂列表接口post（https://jumping1.t1.learnta.cn/__api/beatV3/classroom/org/byTeacherId）'''
        url = 'https://jumping1.t1.learnta.cn/__api/beatV3/classroom/byStudentId'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer 83040996-acc5-3e54-9f1b-7cb56f9796c1'}
        postdata = {"state": 0, "orgId": 1000142}
        TestResult = list(postRequestTest(url, headers, postdata))
        print('学生系统-课堂列表测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testinstcurr(self):
        '''测试创建课程接口post（https://jumping1.t1.learnta.cn/__api/library/newCourse/insert）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/newCourse/insert'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        postdata = 	{"orgId":1000142,"category":0,"press":6000000001,"courseName":"testdelete", "grades": [1,2]}
        TestResult = list(postRequestTest(url, headers, postdata))
        print('创建课程测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testpurcurr(self):
        '''测试购买课程接口post（https://jumping1.t1.learnta.cn/__api/library/orgCourse/buyOrgCourses/1000142）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/orgCourse/buyOrgCourses/1000142'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        postdata = {"orgCourseIds": [5486]}
        TestResult = list(postRequestTest(url, headers, postdata))
        print('购买课程测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")


testsuite = unittest.TestSuite()
testsuite.addTests(unittest.makeSuite(demoApiTest))

runner = BeautifulReport((testsuite))
runner.report(filename='备课系统项目旧接口测试.html', description='备课系统项目旧接口测试用例', report_dir=report_dir)