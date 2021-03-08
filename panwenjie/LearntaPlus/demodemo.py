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

    def testGetstudentsidedata(self):
        '''获取学生端历史数据首页-- 罗志敏'''
        demo = requests.get('https://t1.learnta.cn/__api/ilearnta/student/51113?category=1&orgId=1003215',
                            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="获取学生端历史数据首页")
        self.assertEqual(str(type(demo.json()['data']['id'])), '<class \'int\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['studentName'])), '<class \'NoneType\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['avatar'])), '<class \'NoneType\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['orgId'])), '<class \'int\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['courseId'])), '<class \'int\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['chapterId'])), '<class \'int\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['chapterName'])), '<class \'str\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['kpointId'])), '<class \'int\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['kpointName'])), '<class \'str\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['studyTime'])), '<class \'int\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['questionNum'])), '<class \'int\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['kpointTotalNum'])), '<class \'int\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['lockState'])), '<class \'NoneType\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['kpointKnowNum'])), '<class \'int\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['categoryName'])), '<class \'str\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['pressName'])), '<class \'str\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['gradeName'])), '<class \'str\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['order'])), '<class \'int\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['name'])), '<class \'str\'>', msg="获取学生端历史数据首页测试失败")
        self.assertEqual(str(type(demo.json()['data']['classroomId'])), '<class \'NoneType\'>', msg="获取学生端历史数据首页测试失败")



    # def testhuoquzjie(self):
    #     '''获取章节列表--罗志敏'''
    #     demo = requests.get(
    #         'https://t1.learnta.cn/__api/ilearnta/chapter/chapterList?courseId=2826&studentId=133185&orgId=1000787',
    #         headers=self.headers)
    #     self.assertEqual(demo.status_code, 200, msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']['categoryName'])), '<class \'str\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']['pressName'])), '<class \'str\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']['gradeName'])), '<class \'str\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']['name'])), '<class \'str\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']['order'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']['source'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']['imageUrl'])), '<class \'NoneType\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']['orgId'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']['roomId'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['studentId'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['chapterId'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['name'])), '<class \'str\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['topicInfoId'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['topicState'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['state'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['isStudy'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['pcIsStudy'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['nextKpointId'])), '<class \'NoneType\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['nextKpointName'])), '<class \'NoneType\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['buttonType'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['masteryKpointNum'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['kpointTotalNum'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['taskExecutionId'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['topicInfoType'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['order'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['serialNumber'])), '<class \'str\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['createdAt'])), '<class \'str\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['kpoints'])), '<class \'NoneType\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['continueType'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['nextChapterId'])), '<class \'NoneType\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['nextChapterName'])), '<class \'NoneType\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["chapters"][0]['lockState'])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["courseState"])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["studentName"])), '<class \'str\'>',
    #                      msg="获取章节列表测试失败")
    #     self.assertEqual(str(type(demo.json()['data']["studentId"])), '<class \'int\'>',
    #                      msg="获取章节列表测试失败")



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