#coding:utf-8
import sys
import json
import requests
import platform
import unittest
import configparser
from BeautifulReport import BeautifulReport

# 根据系统环境判断需要读取的目录路径
if(platform.system()=='Windows'):
    print(platform.system())
    report_dir = "D:\\uitest\\report"
    configInfo = "D:\\uitest\\chenjun\\ApiTest\\config.ini"
    # 读配置文件信息
    config = configparser.ConfigParser()
    config.read(configInfo, encoding='gbk')
    env = config.get("Info", "env")
    vcode = config.get("Info", "vcode")
    token = config.get("Info", "token")
    version = config.get("Info", "version")
    print(env, vcode, token, version)
    headers = {
        'authorization': 'Bearer ' + str(token),
        'content-type': 'application/json;charset=UTF-8',
    }
    print(report_dir)
elif(platform.system()=='Linux'):
    report_dir = '/opt/uitest/report'
    configInfo = '/opt/uitest/chenjun/ApiTest/config.ini'
    token = sys.argv[2]
    version = str(sys.argv[1])
    headers = {
        'authorization': 'Bearer ' + str(token),
        'content-type': 'application/json;charset=UTF-8',
        'version': str(version)
    }
    print(platform.system())
else:
    print(platform.system())


# 自定义函数
def postRequestToken(url, postdata):
    postResponsedata = requests.post(url, data=json.dumps(postdata), headers=headers)
    dict_postResponsedata = json.loads(postResponsedata.text)
    print(url)
    return dict_postResponsedata['data']['access_token']

def getResonseCode(url):
    getResonsedata = requests.get(url, headers=headers)
    print('url:'+str(url))
    print('status_code:' + str(getResonsedata.status_code))
    print('headers:' + str(headers))
    print('Resonsedata:' + str(getResonsedata.text))
    return getResonsedata.status_code

def postResonseCode(url, postdata):
    postResonsedata = requests.post(url, data=json.dumps(postdata), headers=headers)
    print('url:'+str(url))
    print('status_code:' + str(postResonsedata.status_code))
    print('headers:' + str(headers))
    print('Resonsedata:' + str(postResonsedata.text))
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
class apiAllTestFormal(unittest.TestCase):

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
        AuthRequestStatusCode = getResonseCode('https://bcq.learnta.cn/__api/auth/role/rolelist/100240/11/0')
        self.assertEqual(AuthRequestStatusCode, 200, msg="Authservice 运行失败")

    def testTeach(self):
        '''测试Teachservice是否正常'''
        TeachRequestStatusCode = getResonseCode('https://bcq.learnta.cn/__api/beatV3/topic/getCategoryPress?type=1&orgId=100240')
        self.assertEqual(TeachRequestStatusCode, 200, msg="Teachservice 运行失败")

    def testLibrary(self):
        '''测试Libraryservice是否正常'''
        LibraryRequestStatusCode = getResonseCode('https://bcq.learnta.cn/__api/library/newCourse/getPress')
        self.assertEqual(LibraryRequestStatusCode, 200, msg="Libraryservice 运行失败")

    def testWechat(self):
        '''测试wechatservice是否正常'''
        WechatRequestStatusCode = getResonseCode('https://learnta.cn/__api/wechat/go/subjects/go/enroll')
        self.assertEqual(WechatRequestStatusCode, 200, msg="Wechatservice 运行失败")

    def testBd(self):
        '''测试BDservice是否正常'''
        BdRequestStatusCode = getResonseCode('https://bcq.learnta.cn/__api/bd/org/notity/getOrgNotity?orgId=100240')
        self.assertEqual(BdRequestStatusCode, 200, msg="Bdservice 运行失败")

    def testMaterial(self):
        '''测试Materialservice是否正常'''
        MaterialRequestStatusCode = getResonseCode('https://bcq.learnta.cn/__api/material/folder/getCreatedByList?orgId=100240&category=1')
        self.assertEqual(MaterialRequestStatusCode, 200, msg="Materialservice 运行失败")

    def testManage(self):
        '''测试Manageservice是否正常'''
        ManageRequestStatusCode = getResonseCode('https://bcq.learnta.cn/__api/manage/examOrder/income/100240')
        self.assertEqual(ManageRequestStatusCode, 200, msg="Manageservice 运行失败")

    def testAdmin(self):
        '''测试Adminservice是否正常'''
        AdminRequestStatusCode = getResonseCode('https://bcq.learnta.cn/__api/admin/question/orgQuestion/createdBy?orgId=100240')
        self.assertEqual(AdminRequestStatusCode, 200, msg="Adminservice 运行失败")

    def testAnalytics(self):
        '''测试Analyticsservice是否正常'''
        AnalyticsTestData = {
            "eventId": 'enterCourse',
            "orgId": 100240,
            "assignedUserId": 75057,
            "terminal": 1,
            "courseId": 62571,
            "classType": 2,
            "classroomId": 68773
        }
        AnalyticsRequestStatusCode = postResonseCode('https://bcq.learnta.cn/__api/analytics/statistic/eventTracking', AnalyticsTestData)
        self.assertEqual(AnalyticsRequestStatusCode, 200, msg="Analyticsservice 运行失败")

    def testDataanalysis(self):
        '''测试Dataanalysisservice是否正常'''
        DataanalysisRequestStatusCode = getResonseCode('https://bcq.learnta.cn/__api/dataanalysis/student/page?orgId=100240&name=&pageSize=10&pageNo=1')
        self.assertEqual(DataanalysisRequestStatusCode, 200, msg="Dataanalysisservice 运行失败")

    def testCourseware(self):
        '''测试Coursewareservice是否正常'''
        CoursewareTestData = {
            "state": 1,
            "executionId": 4701815
        }
        CoursewareRequestStatusCode = postResonseCode('https://learnta.cn/__api/courseware/mobileTask/video/view', CoursewareTestData)
        self.assertEqual(CoursewareRequestStatusCode, 200, msg="Coursewareservice 运行失败")

    def testCrm(self):
        '''测试Crmservice是否正常'''
        CrmRequestStatusCode = getResonseCode('https://learnta.cn/__api/crm/leads/my/todo')
        self.assertEqual(CrmRequestStatusCode, 200, msg="Crmservice 运行失败")

    def testCsm(self):
        '''测试Csmservice是否正常'''
        CrmRequestStatusCode = getResonseCode('https://learnta.cn/__api/csm/dashboard/mine')
        self.assertEqual(CrmRequestStatusCode, 200, msg="Csmservice 运行失败")

    def testInternaluser(self):
        '''测试Internaluserservice是否正常'''
        InternaluserRequestStatusCode = getResonseCode('https://learnta.cn/__api/internaluser/group/children')
        self.assertEqual(InternaluserRequestStatusCode, 200, msg="Internaluserservice 运行失败")

    def testOfficialsite(self):
        '''测试Officialsiteservice是否正常'''
        OfficialsiteRequestStatusCode = getResonseCode('https://learnta.cn/__api/officialsite/article/list?state=0&pageNo=1')
        self.assertEqual(OfficialsiteRequestStatusCode, 200, msg="Officialsiteservice 运行失败")

    def testTrainingcamp(self):
        '''测试Trainingcampservice是否正常'''
        TrainingcampRequestStatusCode = getResonseCode('https://bd.kupeiai.com/__api/trainingcamp/userCenter/getExpiresType')
        self.assertEqual(TrainingcampRequestStatusCode, 200, msg="Trainingcampservice 运行失败")

    def testKupeiai(self):
        '''测试Kupeiaiservice是否正常'''
        KupeiaiRequestStatusCode = getResonseCode('https://partners.kupeiai.com/__api/kupeiai/userCenter/getExpiresType')
        self.assertEqual(KupeiaiRequestStatusCode, 200, msg="Kupeiaiservice 运行失败")

    def testTraining(self):
        '''测试Trainingservice是否正常'''
        TrainingRequestStatusCode = getResonseCode('https://bd.learnta.com/__api/training/userCenter/getExpiresType')
        self.assertEqual(TrainingRequestStatusCode, 200, msg="Trainingservice 运行失败")

    def testActivity(self):
        '''测试Activityservice是否正常'''
        url = 'https://www.learnta.com/__api/activity/public/activity/saveBusinessUser'
        headers = {
            'content-type': 'application/json;charset=UTF-8',
            'version': str(version)
        }
        ActivityData = {
            "orgName": "测试不要联系我",
            "userName": "测试",
            "mobile": 18616215375,
            "code": 1111,
            "utmSource": "wechat01"
        }
        ActivityResponse = requests.post(url, data=json.dumps(ActivityData), headers=headers)
        print('url:'+str(url))
        print('status_code:' + str(ActivityResponse.status_code))
        print('version:' + str(version))
        print('headers:' + str(headers))
        print('response_data:' + str(ActivityResponse.text))
        self.assertEqual(ActivityResponse.status_code, 200, msg="Activityservice 运行失败")

testsuite = unittest.TestSuite()
testsuite.addTests(unittest.makeSuite(apiAllTestFormal))

runner = BeautifulReport((testsuite))
runner.report(filename='正服检查后端所有服务是否正常.html', description='正服检查后端所有服务是否正常测试用例', report_dir=report_dir)