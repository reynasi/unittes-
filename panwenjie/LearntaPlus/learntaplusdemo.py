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
    def test_1_shoushuoxues(self):
        '''搜索学生--林佳欣'''
        demo = requests.get('https://t1.learnta.cn/__api/tank/student/search?orgId=1002769&classroomId=100035&name=17602183921',headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="搜索学生测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['id'])), '<class \'NoneType\'>',
                         msg="搜索学生测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['userId'])), '<class \'int\'>',
                         msg="搜索学生测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['avatar'])), '<class \'NoneType\'>',
                         msg="搜索学生测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['name'])), '<class \'str\'>',
                         msg="搜索学生测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['mobile'])), '<class \'str\'>',
                         msg="搜索学生测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['category'])), '<class \'NoneType\'>',
                         msg="搜索学生测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['press'])), '<class \'NoneType\'>',
                         msg="搜索学生测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['grade'])), '<class \'NoneType\'>',
                         msg="搜索学生测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['orgId'])), '<class \'int\'>',
                         msg="搜索学生测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['isExist'])), '<class \'bool\'>',
                         msg="搜索学生测试失败")

    def test_2_Getsectionlist(self):
        '''添加学生进入课堂--林佳欣'''
        data = {"orgId": 1002769,"studentId": 128227,"classroomId": 100035}
        demo = requests.post('https://t1.learnta.cn/__api/tank/student/addStudent',data=json.dumps(data),headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="添加学生进入课堂测试失败")
        self.assertEqual(str(demo.json()['data']), 'True',
        msg="添加学生进入课堂测试失败")


    def test_3_Getsectionlist(self):
        '''删除学生--林佳欣'''
        data = {"studentId":128227,"classroomId":100035}
        demo = requests.delete('https://t1.learnta.cn/__api/tank/student/byId/128227',data=json.dumps(data),headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="删除学生测试失败")
        self.assertEqual(str(demo.json()['data']), 'True', msg="删除学生测试失败")




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