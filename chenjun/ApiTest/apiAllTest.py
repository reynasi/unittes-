#coding:utf-8
import json
import socket
import requests
import platform
import unittest
import configparser
from BeautifulReport import BeautifulReport

# 获取IP
#获取计算机名称
hostname=socket.gethostname()
#获取本机IP
ip=socket.gethostbyname(hostname)


# 根据系统环境判断需要读取的目录路径
if(platform.system()=='Windows'):
    print(platform.system())
    report_dir = "D:\\uitest\\report"
    configInfo = "D:\\uitest\\chenjun\\ApiTest\\config.ini"
    print(report_dir)
elif(platform.system()=='Linux'):
    report_dir = '/opt/uitest/report'
    configInfo = '/opt/uitest/chenjun/ApiTest/config.ini'
    print(platform.system())
else:
    print(platform.system())

# 读配置文件信息
config = configparser.ConfigParser()
config.read(configInfo, encoding='gbk')
env = config.get("Info", "env")
vcode = config.get("Info", "vcode")
print(env, vcode)

headers = {
    'authorization': 'Bearer a2c76061-ec5a-3879-8339-787d5f1c48b5',
    'content-type': 'application/json;charset=UTF-8',
    'version': 'v2'
}

# 自定义函数
def postRequestToken(url, postdata):
    postResponsedata = requests.post(url, data=json.dumps(postdata), headers=headers)
    dict_postResponsedata = json.loads(postResponsedata.text)
    print(url)
    return dict_postResponsedata['data']['access_token']

def getResonseCode(url):
    getResonsedata = requests.get(url, headers=headers)
    print(headers)
    print(getResonsedata.text)
    print(ip)
    print(url)
    return getResonsedata.status_code

def postResonseCode(url, postdata):
    postResonsedata = requests.post(url, data=json.dumps(postdata), headers=headers)
    print(url)
    return postResonsedata.status_code

def getRequest(url):
    getResponsedata = requests.get(url, headers=headers)
    dict_getResponsedata = json.loads(getResponsedata.text)
    print(url)
    return dict_getResponsedata['data']

def postRequest(url, postdata):
    postResponsedata = requests.post(url, data=json.dumps(postdata), headers=headers)
    dict_postResponsedata = json.loads(postResponsedata.text)
    print(url)
    return dict_postResponsedata['data']

# 开始测试
class apiAllTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # def testGetToken(self):
    #     '''测试是否可以获取token'''
    #     logindata = {
    #         "username": 18616015761,
    #         "code": vcode,
    #         "systemId": 11,
    #         "orgId": 1000491
    #     }
    #     token = postRequestToken('https://cj.t3.learnta.cn/__api/auth/user/loginOrg', logindata)
    #     print(token)
    #     self.assertEqual(1, token, msg="token获取失败")

    def testAuth(self):
        '''测试Authservice是否正常'''
        AuthRequestStatusCode = getResonseCode('https://cj' + env + '.learnta.cn/__api/auth/role/rolelist/1000491/11/0')
        print('Status Code:' + str(AuthRequestStatusCode))
        self.assertEqual(AuthRequestStatusCode, 200, msg="Authservice 运行失败")

    def testTeach(self):
        '''测试Teachservice是否正常'''
        TeachRequestStatusCode = getResonseCode('https://cj' + env + '.learnta.cn/__api/beatV3/topic/getCategoryPress?type=1&orgId=1000491')
        print('Status Code:' + str(TeachRequestStatusCode))
        self.assertEqual(TeachRequestStatusCode, 200, msg="Teachservice 运行失败")

    def testLibrary(self):
        '''测试Libraryservice是否正常'''
        LibraryRequestStatusCode = getResonseCode('https://cj' + env + '.learnta.cn/__api/library/newCourse/getPress')
        print('Status Code:' + str(LibraryRequestStatusCode))
        self.assertEqual(LibraryRequestStatusCode, 200, msg="Libraryservice 运行失败")

    def testWechat(self):
        '''测试wechatservice是否正常'''
        WechatRequestStatusCode = getResonseCode('https://cj' + env + '.learnta.cn/__api/wechat/public/share/signature?url=https%3A%2F%2Ft3.learnta.cn%2Ftask%3ForgId%3D1000491')
        print('Status Code:' + str(WechatRequestStatusCode))
        self.assertEqual(WechatRequestStatusCode, 200, msg="Wechatservice 运行失败")

    def testBd(self):
        '''测试BDservice是否正常'''
        BdRequestStatusCode = getResonseCode('https://cj' + env + '.learnta.cn/__api/bd/org/notity/getOrgNotity?orgId=1000491')
        print('Status Code:' + str(BdRequestStatusCode))
        self.assertEqual(BdRequestStatusCode, 200, msg="Bdservice 运行失败")

    def testMaterial(self):
        '''测试Materialservice是否正常'''
        MaterialRequestStatusCode = getResonseCode('https://cj' + env + '.learnta.cn/__api/material/folder/getCreatedByList?orgId=1000491&category=1')
        print('Status Code:' + str(MaterialRequestStatusCode))
        self.assertEqual(MaterialRequestStatusCode, 200, msg="Materialservice 运行失败")

    def testManage(self):
        '''测试Manageservice是否正常'''
        ManageRequestStatusCode = getResonseCode('https://cj' + env + '.learnta.cn/__api/manage/examOrder/income/1000491')
        print('Status Code:' + str(ManageRequestStatusCode))
        self.assertEqual(ManageRequestStatusCode, 200, msg="Manageservice 运行失败")

    def testAdmin(self):
        '''测试Adminservice是否正常'''
        AdminRequestStatusCode = getResonseCode('https://cj' + env + '.learnta.cn/__api/admin/question/orgQuestion/createdBy?orgId=1000491')
        print('Status Code:' + str(AdminRequestStatusCode))
        self.assertEqual(AdminRequestStatusCode, 200, msg="Adminservice 运行失败")

    def testAnalytics(self):
        '''测试Analyticsservice是否正常'''
        AnalyticsTestData = {
            "eventId" : 'anaysyviewtaskdetail',
            "orgId" : 1000491,
            "assignedUserId" : 52122,
            "terminal": 1
        }
        AnalyticsRequestStatusCode = postResonseCode('https://cj' + env + '.learnta.cn/__api/analytics/statistic/eventTracking', AnalyticsTestData)
        print('Status Code:' + str(AnalyticsRequestStatusCode))
        self.assertEqual(AnalyticsRequestStatusCode, 200, msg="Analyticsservice 运行失败")

    def testDataanalysis(self):
        '''测试Dataanalysisservice是否正常'''
        DataanalysisRequestStatusCode = getResonseCode('https://cj' + env + '.learnta.cn/__api/dataanalysis/student/page?orgId=1000491&name=&pageSize=10&pageNo=1')
        print('Status Code:' + str(DataanalysisRequestStatusCode))
        self.assertEqual(DataanalysisRequestStatusCode, 200, msg="Dataanalysisservice 运行失败")

    def testCourseware(self):
        '''测试Coursewareservice是否正常'''
        CoursewareTestData = {
            "state": 1,
            "executionId": 181568
        }
        CoursewareRequestStatusCode = postResonseCode('https://cj' + env + '.learnta.cn/__api/courseware/mobileTask/video/view', CoursewareTestData)
        print('Status Code:' + str(CoursewareRequestStatusCode))
        self.assertEqual(CoursewareRequestStatusCode, 200, msg="Coursewareservice 运行失败")

    def testCrm(self):
        '''测试Crmservice是否正常'''
        CrmRequestStatusCode = getResonseCode('https://cj' + env + '.learnta.cn/__api/crm/leads/my/todo')
        print('Status Code:' + str(CrmRequestStatusCode))
        self.assertEqual(CrmRequestStatusCode, 200, msg="Crmservice 运行失败")

testsuite = unittest.TestSuite()
testsuite.addTests(unittest.makeSuite(apiAllTest))

runner = BeautifulReport((testsuite))
runner.report(filename='t3测服检查后端所有服务是否正常.html', description='检查后端所有服务是否正常测试用例', report_dir=report_dir)