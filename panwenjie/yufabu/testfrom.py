#coding:utf-8
import sys
import json
import requests
import platform
import unittest
import configparser
import logging
from BeautifulReport import BeautifulReport

# 根据系统环境判断需要读取的目录路径
if(platform.system()=='Windows'):
    print(platform.system())
    report_dir = "D:\\uitest\\report"
    configInfo = "C:\shh\\uitest\\panwenjie\\yufabu\\config.ini"
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
        'version': str(version)
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
    #     token = postRequestToken('httpcs://cj.t3.learnta.cn/__api/auth/user/loginOrg', logindata)
    #     print(token)
    #     self.assertEqual(1, token, msg="token获取失败")

    def testdms_service(self):
        '''测试dms-service是否正常'''
        AuthRequestStatusCode = getResonseCode('https://api.learnta.cn/v1/dms/area/v2/1/0/children?isOnShelf=true')
        logging.info(AuthRequestStatusCode.json())
        self.assertEqual(AuthRequestStatusCode, 200, msg="dms_service 运行失败")

    def testcrm_redis(self):
        '''测试be_crm_redis是否正常'''
        TeachRequestStatusCode = getResonseCode('https://admin.learnta.work/__api/crm/table/config/getByTableId/leadPoolList62')
        logging.info(TeachRequestStatusCode.json())
        self.assertEqual(TeachRequestStatusCode, 200, msg="be_crm_redis 运行失败")

    def testcrm_service(self):
        '''测试be_crm_service是否正常'''
        TeachRequestStatusCode = getResonseCode('https://admin.learnta.work/__api/crm/table/config/getByTableId/leadPoolList62')
        logging.info(TeachRequestStatusCode.json())
        self.assertEqual(TeachRequestStatusCode, 200, msg="be_crm_service 运行失败")

    def testaccount_service(self):
        '''测试be-account-service是否正常'''
        CoursewareTestData = {"page":1,"size":50,"districtCode":12347,"createdBy":1000196}
        CoursewareRequestStatusCode = postResonseCode('https://admin.learnta.work/__api/dms/account/2/1/trial/page', CoursewareTestData)
        logging.info(CoursewareRequestStatusCode.json())
        self.assertEqual(CoursewareRequestStatusCode, 200, msg="account_service 运行失败")

    def testadmin_service(self):
        '''测试admin_service是否正常'''
        TeachRequestStatusCode = getResonseCode('https://api.learnta.cn/v1/beatV3/task/getTree')
        logging.info(TeachRequestStatusCode.json())
        self.assertEqual(TeachRequestStatusCode, 200, msg="admin_service 运行失败")

    def testadmin_redis(self):
        '''测试admin_redis是否正常'''
        TeachRequestStatusCode = getResonseCode('https://api.learnta.cn/v1/admin/tree/node/children?category=0&learningPhase=10&parentId=&isShowHidden=false&isShowClosed=true&_t=1607572524745')
        self.assertEqual(TeachRequestStatusCode, 200, msg="admin_redis 运行失败")

    def testanalytics_service(self):
        '''测试analytics-service是否正常'''
        CoursewareTestData = {"device":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36","orgId":101260,"systemId":"12"}
        CoursewareRequestStatusCode = postResonseCode('https://www.kupeiai.cn/__api/analytics/usermonitor/device',
                                                      CoursewareTestData)
        self.assertEqual(CoursewareRequestStatusCode, 200, msg="analytics-service 运行失败")

    def testauth_service(self):
        '''测试auth_service是否正常'''
        CoursewareTestData = {"username":"13975353140","password":"123qweasd","systemId":4,"orgId":100515}
        CoursewareRequestStatusCode = postResonseCode('https://www.kupeiai.cn/__api/auth/user/loginKupeiStudent',
                                                      CoursewareTestData)
        self.assertEqual(CoursewareRequestStatusCode, 200, msg="auth-service 运行失败")

    def testbd_redis(self):
        '''测试bd-redis是否正常'''
        TeachRequestStatusCode = getResonseCode('https://api.learnta.cn/v1/bd/org/getOrgModule/102104')
        self.assertEqual(TeachRequestStatusCode, 200, msg="bd-redis 运行失败")

    def testbd_service(self):
        '''测试bd_service是否正常'''
        TeachRequestStatusCode = getResonseCode('https://api.learnta.cn/v1/bd/org/getParentOrglist')
        self.assertEqual(TeachRequestStatusCode, 200, msg="bd_service 运行失败")

    def testcommon_service(self):
        '''测试common-service是否正常'''
        TeachRequestStatusCode = getResonseCode('https://api.learnta.cn/v1/dms/areaInfo/0/4/teachingMaterial/1/120101')
        self.assertEqual(TeachRequestStatusCode, 200, msg="common-service 运行失败")

    def testcourseware_service(self):
        '''测试courseware_service是否正常'''
        TeachRequestStatusCode = getResonseCode('https://www.kupeiai.cn/__api/courseware/public/video/?kPointId=6000033470&page=1&size=10')
        self.assertEqual(TeachRequestStatusCode, 200, msg="courseware-service 运行失败")

    def testcsm_service(self):
        '''测试csm_service是否正常'''
        TeachRequestStatusCode = getResonseCode('https://admin.learnta.work/__api/csm/alarm?page=1&size=-1&dateType=1')
        self.assertEqual(TeachRequestStatusCode, 200, msg="csm_service 运行失败")


    # 没找到
    # def testdataanalysis_service(self):
    #     '''测试dataanalysis_service是否正常'''
    #     TeachRequestStatusCode = getResonseCode('https://staging.learnta.cn/__api/analytics/usermonitor/device')
    #     self.assertEqual(TeachRequestStatusCode, 200, msg="dataanalysis_service 运行失败")



    def testinternalusermanage_service(self):
        '''测试internalusermanage_service是否正常'''
        TeachRequestStatusCode = getResonseCode('https://api.learnta.cn/v1/internaluser/group/children')
        self.assertEqual(TeachRequestStatusCode, 200, msg="internalusermanage_service 运行失败")

    def testkpl(self):
        '''测试kpl是否正常'''
        TeachRequestStatusCode = getResonseCode('https://kp-price.kupeiai.cn/kpl/province/120300/cities-by-level')
        self.assertEqual(TeachRequestStatusCode, 200, msg="kpl 运行失败")

    def testjob_execution(self):
        '''测试job_execution是否正常'''
        TeachRequestStatusCode = getResonseCode('http://job-admin.sit.learnta.work/job-admin/static/plugins/layer/theme/default/layer.css?v=3.1.1')
        self.assertEqual(TeachRequestStatusCode, 200, msg="job_execution 运行失败")

    def testjob_admin(self):
        '''测试job-admin是否正常'''
        TeachRequestStatusCode = getResonseCode('http://job-admin.sit.learnta.work/job-admin/static/plugins/layer/theme/default/layer.css?v=3.1.1')
        self.assertEqual(TeachRequestStatusCode, 200, msg="job-admin 运行失败")

    def testlibrary_service(self):
        '''测试library_service是否正常'''
        TeachRequestStatusCode = getResonseCode('https://learnta.cn/__api/library/newCourse/getPress')
        self.assertEqual(TeachRequestStatusCode, 200, msg="library_service 运行失败")

    def testmanage_service(self):
        '''测试manage_service是否正常'''
        CoursewareTestData = {"orgId":102090,"operationId":50038}
        CoursewareRequestStatusCode = postResonseCode('https://staging.learnta.cn/__api/manage/public/checkOrgServiceStatus?_t=1607590116912',
                                                      CoursewareTestData)
        self.assertEqual(CoursewareRequestStatusCode, 200, msg="manage_service 运行失败")

    def testmaterial_service(self):
        '''测试material-service是否正常'''
        TeachRequestStatusCode = getResonseCode('https://learnta.cn/__api/material/job/question/list?name=&operatorId=&state=1&page=1&pageSize=20&type=3&own=0')
        self.assertEqual(TeachRequestStatusCode, 200, msg="material_service 运行失败")

    def testmaterial_redis(self):
        '''测试material-redis是否正常'''
        TeachRequestStatusCode = getResonseCode('https://learnta.cn/__api/material/job/question/getJobStateNum?type=3&own=0')
        self.assertEqual(TeachRequestStatusCode, 200, msg="material-redis 运行失败")

    def testofficial_site(self):
        '''测试official_site是否正常'''
        TeachRequestStatusCode = getResonseCode('https://api.learnta.cn/v1/officialsite/public/articleList?pageNo=1&itemsPerPage=10&type=1')
        self.assertEqual(TeachRequestStatusCode, 200, msg="official_site 运行失败")

    def testtraining_camp(self):
        '''测试training_camp是否正常'''
        TeachRequestStatusCode = getResonseCode(
            'https://api.learnta.cn/v1/trainingcamp/userCenter/getExpiresType')
        self.assertEqual(TeachRequestStatusCode, 200, msg="training_camp 运行失败")
    def testtraining_site(self):
        '''测试training_site是否正常'''
        TeachRequestStatusCode = getResonseCode(
            'https://api.learnta.cn/v1/training/userCenter/getTree/0')
        self.assertEqual(TeachRequestStatusCode, 200, msg="training_site 运行失败")
    def testtree_service(self):
        '''测试tree_service是否正常'''
        TeachRequestStatusCode = getResonseCode(
            'https://api.learnta.cn/v1/dms/area/v2/1/0/childrenWithStatus')
        self.assertEqual(TeachRequestStatusCode, 200, msg="tree_service 运行失败")

    def testwechat_service(self):
        '''测试wechat_service是否正常'''
        TeachRequestStatusCode = getResonseCode(
            'https://www.kupeiai.com/__api/wechat/public/getAllArea')
        self.assertEqual(TeachRequestStatusCode, 200, msg="wechat_service 运行失败")

    def testwechat_redis(self):
        '''测试wechat_redis是否正常'''
        TeachRequestStatusCode = getResonseCode(
            'https://www.kupeiai.com/__api/wechat/public/getAllArea')
        self.assertEqual(TeachRequestStatusCode, 200, msg="wechat_redis 运行失败")
    def testauth_service(self):
        '''测试auth_service是否正常'''
        CoursewareTestData ={"userName": "测试", "code": "1111", "mobile": "13975353141", "grade": "四年级",
                              "province": "12345", "city": "12346", "area": "12347", "sourceChannel": "酷培官网（c端）"}
        CoursewareRequestStatusCode = postResonseCode('https://www.kupeiai.com/__api/activity/public/kupei/freeTry',
                                                      CoursewareTestData)
        self.assertEqual(CoursewareRequestStatusCode, 200, msg="auth-service 运行失败")

    def testmicrobusinesssiteService(self):
        '''测试microbusinesssiteService是否正常'''
        TeachRequestStatusCode = getResonseCode(
            'https://api.learnta.cn/v1/kupeiai/userCenter/getExpiresType')
        self.assertEqual(TeachRequestStatusCode, 200, msg="microbusinesssiteService 运行失败")

    def testcustomersuccesssiteService(self):
        '''测试customersuccesssiteService是否正常'''
        TeachRequestStatusCode = getResonseCode(
            'https://api.learnta.cn/v1/kupeiai/userCenter/getExpiresType')
        self.assertEqual(TeachRequestStatusCode, 200, msg="customersuccesssiteService 运行失败")

    def testofficialsiteService(self):
        '''测试officialsiteService是否正常'''
        TeachRequestStatusCode = getResonseCode(
            'https://api.learnta.cn/v1/officialsite/userCenter/getDocs/41')
        self.assertEqual(TeachRequestStatusCode, 200, msg="officialsiteService 运行失败")



testsuite = unittest.TestSuite()
testsuite.addTests(unittest.makeSuite(apiAllTestFormal))

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