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
    configInfo = "C:\shh\\uitest\\panwenjie\\yufabu\\config.ini"
    # 读配置文件信息
    config = configparser.ConfigParser()
    config.read(configInfo, encoding='gbk')
    env = config.get("Info", "env")
    vcode = config.get("Info", "vcode")
    token = config.get("Info", "token")
    version = config.get("Info", "version")
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
    # print('Resonsedata:' + str(getResonsedata.text))
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

    def testanalytics_service(self):
        '''测试analytics-service是否正常'''
        CoursewareTestData = {"device":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36","orgId":101260,"systemId":"12"}
        CoursewareRequestStatusCode = postResonseCode('https://www.kupeiai.cn/__api/analytics/usermonitor/device',
                                                      CoursewareTestData)
        self.assertEqual(CoursewareRequestStatusCode, 200, msg="analytics-service 运行失败")



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