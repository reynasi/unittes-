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

authorizations = 'Bearer b5b47c95-6047-330d-a029-953604c46cd8'

# 开始测试
class demoApiTest(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass


    def testvideodata(self):
        '''测试获取视频列表接口get（https://jumping1.t1.learnta.cn/__api/library/video?page=1&size=10）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/video?page=1&size=10'
        testurl = 'https://jumping1.t1.learnta.cn/__api/library/video?page={}&size={}'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        TestResult = list(getErrorRequestTest(url, testurl, headers))
        print('获取视频列表测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testrelavideodata(self):
        '''测试获取相关视频列表接口get（https://jumping1.t1.learnta.cn/__api/library/video/relatedVideos?kPointName=三角形的三边关系&page=1&size=10）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/video/relatedVideos?kPointName=三角形的三边关系&page=1&size=10'
        testurl = 'https://jumping1.t1.learnta.cn/__api/library/video/relatedVideos?kPointName={}&page={}&size={}'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        TestResult = list(getErrorRequestTest(url, testurl, headers))
        print('获取相关视频列表测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testlinkedTreeNodeIds(self):
        '''测试根据知识点获取该知识点在树上的链路树节点ID列表接口get（https://jumping1.t1.learnta.cn/__api/library/tree/linkedTreeNodeIds/6000057607）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/tree/linkedTreeNodeIds/6000057607'
        testurl = 'https://jumping1.t1.learnta.cn/__api/library/tree/linkedTreeNodeIds/6000057607'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        TestResult = list(getErrorRequestTest(url, testurl, headers))
        print('根据知识点获取该知识点在树上的链路树节点ID列表测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testdelcurr(self):
        '''测试删除课程接口delete（https://jumping1.t1.learnta.cn/__api/library/newCourse/byId/20120）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/newCourse/byId/20120'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        TestResult = list(deleteRequestTest(url, headers))
        print('删除课程测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testdelunit(self):
        '''测试删除单元接口delete（https://jumping1.t1.learnta.cn/__api/library/unit/118660）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/unit/118660'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        TestResult = list(deleteRequestTest(url, headers))
        print('删除单元测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")


    def testdelstep(self):
        '''测试删除模块接口delete（https://jumping1.t1.learnta.cn/__api/library/step/575362）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/step/575362'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        TestResult = list(deleteRequestTest(url, headers))
        print('删除模块测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testdeltask(self):
        '''测试删除任务卡接口delete（https://jumping1.t1.learnta.cn/__api/library/task/2292210）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/task/2292199'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        TestResult = list(deleteRequestTest(url, headers))
        print('删除任务卡测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testdeltaskelement(self):
        '''测试删除讲义卡子卡接口delete（https://jumping1.t1.learnta.cn/__api/library/task/element/4598）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/task/element/4598'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        TestResult = list(deleteRequestTest(url, headers))
        print('删除讲义卡子卡测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")


    def testupunit(self):
        '''测试修改单元接口put（https://jumping1.t1.learnta.cn/__api/library/unit/118659?unitName=测试修改呀we）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/unit/118659?unitName=测试修改呀w'
        headers = {'content-type': 'application/json;charset=UTF-8','authorization': authorizations}
        putdata = {"unitName":"修改单元名2测试"}
        TestResult = list(putRequestTest(url, headers, putdata))
        print('修改单元测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testupstep(self):
        '''测试修改模块接口put（https://jumping1.t1.learnta.cn/__api/library/step/575363?stepName=测试修改呀呀s）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/step/575363?stepName=测试修改呀呀s'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        putdata = {"stepName":"无标题模块呀"}
        TestResult = list(putRequestTest(url, headers, putdata))
        print('修改模块测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def teststepdrgg(self):
        '''测试模块拖拽接口put（https://jumping1.t1.learnta.cn/__api/library/step/118630/order）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/step/575364/order'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        putdata = [2290147,2290148,2290149]
        TestResult = list(putRequestTest(url, headers, putdata))
        print('模块拖拽测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")


    def testunitdrgg(self):
        '''测试单元拖拽接口put（https://jumping1.t1.learnta.cn/__api/library/unit/20118/order）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/unit/20118/order'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        putdata = [118660,118658]
        TestResult = list(putRequestTest(url, headers, putdata))
        print('单元拖拽测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")


    def testuptask(self):
        '''测试修改任务卡接口put（https://jumping1.t1.learnta.cn/__api/library/task/2292205）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/task/2292205'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        putdata = {"eventId":"edittask","courseId":"20117","taskType":4,"taskId":"2292205","orgId":1000142,"assignedUserId":128435,"terminal":1}
        TestResult = list(putRequestTest(url, headers, putdata))
        print('修改任务卡测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testtaskorder(self):
        '''测试任务卡拖拽接口put（https://jumping1.t1.learnta.cn/__api/library/task/575520/order}）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/task/575520/order'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        putdata = {"order": [{"stepId":575520,"taskIds":[2292202,2292203,2292205,2292204,2292208]}]}
        TestResult = list(putRequestTest(url, headers, putdata))
        print('任务卡拖拽测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testuptaskelement(self):
        '''测试编辑讲义卡子卡接口put（https://jumping1.t1.learnta.cn/__api/library/task/update/element}）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/task/element'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        putdata = {"kpointId":6000000007,"type":1,"taskName":"空白卡片","taskData":"<div>水水水水水</div>","id":4597}
        TestResult = list(putRequestTest(url, headers, putdata))
        print('编辑讲义卡子卡测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")


    def testcopycurr(self):
        '''测试拷贝模块接口post（https://jumping1.t1.learnta.cn/__api/library/step/{id}/copy）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/step/1000142/copy'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        postdata = {"orgId": 1000142,"operationId": 50038}
        TestResult = list(postRequestTest(url, headers, postdata))
        print('拷贝模块测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testxinstunit(self):
        '''测试新建单元接口post（https://jumping1.t1.learnta.cn/__api/library/unit/）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/unit/'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        postdata = {"courseId": 20117, "name": "test"}
        TestResult = list(postRequestTest(url, headers, postdata))
        print('新建单元测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testxinststep(self):
        '''测试新建模块接口post（https://jumping1.t1.learnta.cn/__api/library/step/）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/step/'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        postdata = {"orgId":1000142, "unitId":118762, "name":"test", "type":1, "pressId":6000000001, "kpointIds": []}
        TestResult = list(postRequestTest(url, headers, postdata))
        print('新建模块测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testxinsttask(self):
        '''测试新建任务卡接口post（https://jumping1.t1.learnta.cn/__api/library/task）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/task'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        postdata = {"eventId":"edittask","courseId":"20117","taskType":1,"orgId":1000142,"assignedUserId":128435,"terminal":1}
        TestResult = list(postRequestTest(url, headers, postdata))
        print('新建任务卡测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testxinstorder(self):
        '''测试新建空白任务卡接口post（https://jumping1.t1.learnta.cn/__api/library/task/insertBlankTaskCard）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/task/insertBlankTaskCard'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        postdata = {"stepId":575331,"id":2290053}
        TestResult = list(postRequestTest(url, headers, postdata))
        print('新建空白任务卡测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testelemreorder(self):
        '''测试重新排序讲义卡子卡接口post（https://jumping1.t1.learnta.cn/__api/library/task/element/reorder）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/task/element/reorder'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        postdata = {"elementId":3466,"orderDirection":1}
        TestResult = list(postRequestTest(url, headers, postdata))
        print('重新排序讲义卡子卡测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")


    def testxinstblankelement(self):
        '''测试插入空白讲义卡子卡接口post（https://jumping1.t1.learnta.cn/__api/library/task/blankelement/）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/task/blankelement/'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        postdata = {"taskId": 4598}
        TestResult = list(postRequestTest(url, headers, postdata))
        print('插入空白讲义卡子卡测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")


    def testkpointtitle(self):
        '''测试根据知识点拼接年级作为标题接口post（https://jumping1.t1.learnta.cn/__api/library/task/kpointtitle）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/task/kpointtitle'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        postdata = 	{"kpointIds":[1,2,3]}
        TestResult = list(postRequestTest(url, headers, postdata))
        print('根据知识点拼接年级作为标题测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

    def testkpointtitle(self):
        '''测试根据题目ID列表获取题目详情，并分类接口post（https://jumping1.t1.learnta.cn/__api/library/question/map）'''
        url = 'https://jumping1.t1.learnta.cn/__api/library/question/map'
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': authorizations}
        postdata = 	{"groupByField":4,"questions":[{"id":104488,"source":1},{"id":105060,"source":1},{"id":162005,"source":1},{"id":162006,"source":1},{"id":158,"source":2},{"id":159,"source":2},{"id":160,"source":2},{"id":161,"source":2},{"id":5012,"source":3},{"id":5013,"source":3},{"id":5014,"source":3},{"id":5015,"source":3}]}
        TestResult = list(postRequestTest(url, headers, postdata))
        print('根据题目ID列表获取题目详情，并分类测试结果:' + str(TestResult))
        print('\n')
        self.assertEqual(str(TestResult[0]), 'pass', msg="测试失败")

testsuite = unittest.TestSuite()
testsuite.addTests(unittest.makeSuite(demoApiTest))

runner = BeautifulReport((testsuite))
runner.report(filename='备课系统项目新接口测试.html', description='备课系统项目新接口测试用例', report_dir=report_dir)