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

    def test_1_classincreasew(self):
        '''配置课程-新增测试接口-- 彭刚'''
        data =  {'operatorId':0,"orgId": 1002610,"userId": 133907,"rooms":[{"category": 0,"press": 1, "grade": 8}]}
        demo = requests.put('https://t1.learnta.cn/__api/beatV3/tank/addintelligentrooms', data=json.dumps(data),headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="配置课程-新增测试失败测试失败")
        self.assertEqual(demo.json()['message'], 'success', msg="配置课程-新增测试失败测试失败")

    def test_2_IntelligentClassList(self):
        '''测试智能课堂列表接口-- 彭刚'''
        demo = requests.get('https://t1.learnta.cn/__api/beatV3/tank/getIntelligentRoom?orgId=1002610&studentId=133907',headers = self.headers)
        self.assertEqual(demo.status_code, 200, msg="智能课堂列表接口测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['categoryName'])), '<class \'str\'>', msg="测试智能课堂列表接口categoryName")
        self.assertEqual(str(type(demo.json()['data'][0]['pressName'])), '<class \'str\'>', msg="测试智能课堂列表接口pressName")
        self.assertEqual(str(type(demo.json()['data'][0]['gradeName'])), '<class \'str\'>', msg="测试智能课堂列表接口gradeName")
        self.assertEqual(str(type(demo.json()['data'][0]['imageUrl'])), '<class \'NoneType\'>', msg="测试智能课堂列表接口imageUrl")
        self.assertEqual(str(type(demo.json()['data'][0]['name'])), '<class \'NoneType\'>', msg="测试智能课堂列表接口name")
        self.assertEqual(str(type(demo.json()['data'][0]['source'])), '<class \'int\'>', msg="测试智能课堂列表接口source")
        self.assertEqual(str(type(demo.json()['data'][0]['order'])), '<class \'int\'>', msg="测试智能课堂列表接口order")
        self.assertEqual(str(type(demo.json()['data'][0]['id'])), '<class \'NoneType\'>', msg="测试智能课堂列表接口id")
        self.assertEqual(str(type(demo.json()['data'][0]['orgId'])), '<class \'int\'>', msg="测试智能课堂列表接口orgId")
        self.assertEqual(str(type(demo.json()['data'][0]['roomId'])), '<class \'NoneType\'>', msg="测试智能课堂列表接口roomId")
        self.assertEqual(str(type(demo.json()['data'][0]['intelligentRoomId'])), '<class \'int\'>', msg="测试智能课堂列表接口intelligentRoomId")
        self.assertEqual(str(type(demo.json()['data'][0]['category'])), '<class \'int\'>', msg="测试智能课堂列表接口category")
        self.assertEqual(str(type(demo.json()['data'][0]['press'])), '<class \'int\'>', msg="测试智能课堂列表接口press")
        self.assertEqual(str(type(demo.json()['data'][0]['grade'])), '<class \'int\'>', msg="测试智能课堂列表接口grade")
        self.assertEqual(str(type(demo.json()['data'][0]['state'])), '<class \'int\'>', msg="测试智能课堂列表接口state")
        self.assertEqual(str(type(demo.json()['data'][0]['isStudy'])), '<class \'int\'>', msg="测试智能课堂列表接口isStudy")
        self.assertEqual(str(type(demo.json()['data'][0]['teacherName'])), '<class \'NoneType\'>', msg="测试智能课堂列表接口teacherName")
        self.assertEqual(str(type(demo.json()['data'][0]['kpointTotalNum'])), '<class \'int\'>', msg="测试智能课堂列表接口kpointTotalNum")
        self.assertEqual(str(type(demo.json()['data'][0]['masteryKpointNum'])), '<class \'int\'>', msg="测试智能课堂列表接口masteryKpointNum")
        self.assertEqual(str(type(demo.json()['data'][0]['cover'])), '<class \'str\'>', msg="测试智能课堂列表接口cover")
        self.assertEqual(str(type(demo.json()['data'][0]['createdBy'])), '<class \'str\'>', msg="测试智能课堂列表接口createdBy")
        self.assertEqual(str(type(demo.json()['data'][0]['isExpired'])), '<class \'bool\'>', msg="测试智能课堂列表接口isExpired")
        self.assertEqual(str(type(demo.json()['data'][0]['districtName'])), '<class \'NoneType\'>', msg="测试智能课堂列表接口districtName")
        print(demo.json()['data'][0]['intelligentRoomId'])

    def test_3_Getsthecoursesubjectversionconfiguration(self):
        '''测试获取课程学科版本配置-- 彭刚'''
        demo = requests.get(
            'https://t1.learnta.cn/__api/beatV3/tank/getCategoryConfig?orgId=1002610&studentId=133907',
            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="获取课程学科版本配置失败")
        # print(demo.json())
        # print(demo.json()['data'][0]['grades'][0]['name'])
        self.assertEqual(str(type(demo.json()['data'][0]['category'])), '<class \'int\'>',msg="获取课程学科版本配置测试失败category")
        self.assertEqual(str(type(demo.json()['data'][0]['name'])), '<class \'str\'>',msg="获取课程学科版本配置测试失败name")
        self.assertEqual(str(type(demo.json()['data'][0]['grades'][0]['grade'])), '<class \'int\'>',msg="获取课程学科版本配置测试失败grade")
        self.assertEqual(str(type(demo.json()['data'][0]['grades'][0]['name'])), '<class \'str\'>',msg="获取课程学科版本配置测试失败name")
        self.assertEqual(str(type(demo.json()['data'][0]['grades'][0]['presses'][0]['press'])), '<class \'int\'>',msg="获取课程学科版本配置测试失败press")
        self.assertEqual(str(type(demo.json()['data'][0]['grades'][0]['presses'][0]['name'])), '<class \'str\'>',msg="获取课程学科版本配置测试失败press")
        self.assertEqual(str(type(demo.json()['data'][0]['grades'][0]['presses'][0]['state'])), '<class \'int\'>',msg="获取课程学科版本配置测试失败press")
        self.assertEqual(str(type(demo.json()['data'][0]['grades'][0]['presses'][0]['grades'])), '<class \'NoneType\'>',msg="获取课程学科版本配置测试失败press")


    def test_4_delect(self):
        '''测试删除学习配置的智能课程-- 彭刚'''
        demo = requests.delete(
            'https://t1.learnta.cn/__api/beatV3/tank/deleteIntelligentRoom/2586',
            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="删除学习配置的智能课程失败")
        self.assertEqual(str(type(demo.json()['data'])), '<class \'int\'>',
                         msg="配置课程-删除学习配置的智能课程失败")

    def testtesttest(self):
        '''测一测--刘俊峰'''
        data = {"intelligentStudyRoomTopicId": 40193, "orgId": 1003215}
        demo = requests.post('https://t1.learnta.cn/__api/beatV3/student/task/41', data=json.dumps(data),
                             headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecutionId'])), '<class \'int\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['activityId'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['answer'])), '<class \'NoneType\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['assignmentType'])), '<class \'int\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['bucket'])), '<class \'NoneType\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['category'])), '<class \'int\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['classroomExecutionId'])),
                         '<class \'NoneType\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['classroomId'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['correctNumber'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['costTime'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['courseName'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['createdAt'])), '<class \'int\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['createdBy'])), '<class \'str\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['displayOrder'])), '<class \'int\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['dualTime'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['duration'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['elementId'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['finishTime'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['fristTime'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['grade'])), '<class \'NoneType\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['homeworkId'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['id'])), '<class \'int\'>', msg="测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['intelligentStudyRoomTopicId'])),
                         '<class \'NoneType\'>', msg="测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['isDeleted'])), '<class \'bool\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['activityId'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointId'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointMastery'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointName'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointState'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointTotal'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['masteryRate'])), '<class \'float\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['miniProgramCourseId'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['mobile'])), '<class \'NoneType\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['orgId'])), '<class \'int\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['organizer'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['questionNumber'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['questions'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['readoverTime'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['recordId'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['reportUrl'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")

        self.assertEqual(str(type(demo.json()['data']['taskExecution']['roleId'])), '<class \'NoneType\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['roleName'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['scoreTime'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['source'])), '<class \'NoneType\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['startTime'])), '<class \'str\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['status'])), '<class \'int\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['studentId'])), '<class \'int\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['studentName'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['studyItemId'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskEvaluation'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskGroupId'])), '<class \'int\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskId'])), '<class \'int\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskName'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskScore'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskType'])), '<class \'int\'>', msg="测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['teacherId'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")

        self.assertEqual(str(type(demo.json()['data']['taskExecution']['teacherName'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['teachingModuleId'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['topicId'])), '<class \'int\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['topicInfoId'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['topicInfoType'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['topicName'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['type'])), '<class \'NoneType\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['updatedAt'])), '<class \'int\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['updatedBy'])), '<class \'str\'>', msg="测一测测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['videoUrl'])), '<class \'NoneType\'>',
                         msg="测一测测试失败")


    def testbigengiist(self):
        '''英语综合题型卡--刘俊峰'''
        data = {"intelligentStudyRoomTopicId": 40192, "orgId": 1003215}
        demo = requests.post('https://t1.learnta.cn/__api/beatV3/student/task/42', data=json.dumps(data),
                             headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecutionId'])), '<class \'int\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['activityId'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['answer'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['assignmentType'])), '<class \'int\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['bucket'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['category'])), '<class \'int\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['classroomExecutionId'])), '<class \'NoneType\'>',
                         msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['classroomId'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['correctNumber'])), '<class \'NoneType\'>',
                         msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['costTime'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['courseName'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['createdAt'])), '<class \'int\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['createdBy'])), '<class \'str\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['displayOrder'])), '<class \'int\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['dualTime'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['duration'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['elementId'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['finishTime'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['fristTime'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['grade'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['homeworkId'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['id'])), '<class \'int\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['intelligentStudyRoomTopicId'])),
                         '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['isDeleted'])), '<class \'bool\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointId'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointMastery'])), '<class \'NoneType\'>',
                         msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointName'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointState'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointTotal'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['masteryRate'])), '<class \'float\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['miniProgramCourseId'])), '<class \'NoneType\'>',
                         msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['mobile'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['orgId'])), '<class \'int\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['organizer'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['questionNumber'])), '<class \'NoneType\'>',
                         msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['questions'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['readoverTime'])), '<class \'NoneType\'>',
                         msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['recordId'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['reportUrl'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['roleId'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['roleName'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['scoreTime'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['startTime'])), '<class \'str\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['studentId'])), '<class \'int\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['studentName'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['studyItemId'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskEvaluation'])), '<class \'NoneType\'>',
                         msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskGroupId'])), '<class \'int\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskId'])), '<class \'int\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskName'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskScore'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskType'])), '<class \'int\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['teacherId'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['teacherName'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['teachingModuleId'])), '<class \'NoneType\'>',
                         msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['topicId'])), '<class \'int\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['topicInfoId'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['topicInfoType'])), '<class \'NoneType\'>',
                         msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['topicName'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['type'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['updatedAt'])), '<class \'int\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['updatedBy'])), '<class \'str\'>', msg="英语综合题型卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['videoUrl'])), '<class \'NoneType\'>', msg="英语综合题型卡测试失败")

    def testenglistlijigk(self):
        '''英语综合题型立即攻克卡--刘俊峰'''
        data = {"intelligentStudyRoomTopicId":40192,"orgId":1003215,"kpointId":6000029437}
        demo = requests.post('https://t1.learnta.cn/__api/beatV3/student/task/43', data=json.dumps(data),
                             headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecutionId'])), '<class \'int\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['activityId'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['answer'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['assignmentType'])), '<class \'int\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['bucket'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['category'])), '<class \'int\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['classroomExecutionId'])), '<class \'NoneType\'>',
        msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['classroomId'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['correctNumber'])), '<class \'NoneType\'>',
        msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['costTime'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['courseName'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['createdAt'])), '<class \'int\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['createdBy'])), '<class \'str\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['displayOrder'])), '<class \'int\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['dualTime'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['duration'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['elementId'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['finishTime'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['fristTime'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['grade'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['homeworkId'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['id'])), '<class \'int\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['intelligentStudyRoomTopicId'])),
        '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['isDeleted'])), '<class \'bool\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointId'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointMastery'])), '<class \'NoneType\'>',
        msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointName'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointState'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointTotal'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['masteryRate'])), '<class \'float\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['miniProgramCourseId'])), '<class \'NoneType\'>',
        msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['mobile'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['orgId'])), '<class \'int\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['organizer'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['questionNumber'])), '<class \'NoneType\'>',
        msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['questions'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['readoverTime'])), '<class \'NoneType\'>',
        msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['recordId'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['reportUrl'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['roleId'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['roleName'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['scoreTime'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['startTime'])), '<class \'str\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['studentId'])), '<class \'int\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['studentName'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['studyItemId'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskEvaluation'])), '<class \'NoneType\'>',
        msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskGroupId'])), '<class \'int\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskId'])), '<class \'int\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskName'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskScore'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskType'])), '<class \'int\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['teacherId'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['teacherName'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['teachingModuleId'])), '<class \'NoneType\'>',
        msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['topicId'])), '<class \'int\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['topicInfoId'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['topicInfoType'])), '<class \'NoneType\'>',
        msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['topicName'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['type'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['updatedAt'])), '<class \'int\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['updatedBy'])), '<class \'str\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['videoUrl'])), '<class \'NoneType\'>', msg="英语综合题型立即攻克卡测试失败")


    def testlijigk(self):
        '''立即攻克卡--刘俊峰'''
        data = {"intelligentStudyRoomTopicId": 40223, "orgId": 1003215, "kpointId": 6000010699}
        demo = requests.post('https://t1.learnta.cn/__api/beatV3/student/task/40', data=json.dumps(data),
                             headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecutionId'])), '<class \'int\'>', msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['activityId'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['answer'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['assignmentType'])), '<class \'int\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['bucket'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['category'])), '<class \'int\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['classroomExecutionId'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['classroomId'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['correctNumber'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['costTime'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['courseName'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['createdAt'])), '<class \'int\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['createdBy'])), '<class \'str\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['displayOrder'])), '<class \'int\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['dualTime'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['duration'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['elementId'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['finishTime'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['fristTime'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['grade'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['homeworkId'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['id'])), '<class \'int\'>', msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['intelligentStudyRoomTopicId'])),
                         '<class \'NoneType\'>', msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['isDeleted'])), '<class \'bool\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointId'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointMastery'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointName'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointState'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['kpointTotal'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['masteryRate'])), '<class \'float\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['miniProgramCourseId'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['mobile'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['orgId'])), '<class \'int\'>', msg="英语综合题型立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['organizer'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['questionNumber'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['questions'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['readoverTime'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['recordId'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['reportUrl'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['roleId'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['roleName'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['scoreTime'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['startTime'])), '<class \'str\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['studentId'])), '<class \'int\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['studentName'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['studyItemId'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskEvaluation'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskGroupId'])), '<class \'int\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskId'])), '<class \'int\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskName'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskScore'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['taskType'])), '<class \'int\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['teacherId'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['teacherName'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['teachingModuleId'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['topicId'])), '<class \'int\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['topicInfoId'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['topicInfoType'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['topicName'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['type'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['updatedAt'])), '<class \'int\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['updatedBy'])), '<class \'str\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['videoUrl'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
        self.assertEqual(str(type(demo.json()['data']['taskExecution']['recordId'])), '<class \'NoneType\'>',
                         msg="立即攻克卡测试失败")
    def testtestpush(self):
        '''测一测推题--刘俊峰'''
        data = {"intelligentStudyRoomTopicId": 40203, "orgId": 1003215}
        demo1 = requests.post('https://t1.learnta.cn/__api/beatV3/student/task/41', data=json.dumps(data),
                             headers=self.headers)
        taskExecutionId=demo1.json()['data']['taskExecutionId']
        data = {"userAnswers":[],"isEvaluated":'true',"taskExecutionId":taskExecutionId}
        demo2 = requests.post('https://t1.learnta.cn/__api/beatV3/student/task/41/'+str(taskExecutionId)+'/question',data=json.dumps(data),
                            headers=self.headers)

        self.assertEqual(demo2.status_code, 200, msg="测一测question测试失败")
        question=demo2.json()['data']['questions'][0]['id']

        data = {"questionId":question,"answer":["","","",""]}
        demo3 = requests.put('https://t1.learnta.cn/__api/beatV3/student/task/41/' + str(taskExecutionId) + '/answer',
                              data=json.dumps(data),headers=self.headers)
        self.assertEqual(demo3.status_code, 200, msg="测一测answer测试失败")

    def testlijigkpush(self):
        '''立即攻克卡推题--刘俊峰'''
        data = {"intelligentStudyRoomTopicId": 40223, "orgId": 1003215, "kpointId": 6000010699}
        demo1 = requests.post('https://t1.learnta.cn/__api/beatV3/student/task/40', data=json.dumps(data),
                              headers=self.headers)
        taskExecutionId = demo1.json()['data']['taskExecutionId']
        data = {"userAnswers": [], "isEvaluated": 'true', "taskExecutionId": taskExecutionId}
        demo2 = requests.post(
            'https://t1.learnta.cn/__api/beatV3/student/task/40/' + str(taskExecutionId) + '/question',
            data=json.dumps(data),
            headers=self.headers)

        self.assertEqual(demo2.status_code, 200, msg="立即攻克卡questions")
        question = demo2.json()['data']['questions'][0]['id']

        data = {"questionId": question, "answer": [""]}
        demo3 = requests.put('https://t1.learnta.cn/__api/beatV3/student/task/40/' + str(taskExecutionId) + '/answer',
                             data=json.dumps(data), headers=self.headers)
        self.assertEqual(demo3.status_code, 200, msg="立即攻克卡answer")

    def testenglistlijigkpush(self):
        '''英语综合题型立即攻克卡推题--刘俊峰'''
        data = {"intelligentStudyRoomTopicId": 40192, "orgId": 1003215, "kpointId": 6000029437}
        demo1 = requests.post('https://t1.learnta.cn/__api/beatV3/student/task/43', data=json.dumps(data),
                              headers=self.headers)
        taskExecutionId = demo1.json()['data']['taskExecutionId']
        data = {"userAnswers": [], "isEvaluated": 'true', "taskExecutionId": taskExecutionId}
        demo2 = requests.post(
            'https://t1.learnta.cn/__api/beatV3/student/task/43/' + str(taskExecutionId) + '/question',
            data=json.dumps(data),
            headers=self.headers)

        self.assertEqual(demo2.status_code, 200, msg="英语综合题型立即攻克卡question测试失败")
        question = demo2.json()['data']['questions'][0]['id']
        data = {"questionId": question, "answer": [""]}
        demo3 = requests.put('https://t1.learnta.cn/__api/beatV3/student/task/43/' + str(taskExecutionId) + '/answer',
                             data=json.dumps(data), headers=self.headers)
        self.assertEqual(demo3.status_code, 200, msg="英语综合题型立即攻克卡answer测试失败")

    def testbigengiistpush(self):
        '''英语综合题型卡推题--刘俊峰'''
        data = {"intelligentStudyRoomTopicId": 40192, "orgId": 1003215}
        demo1 = requests.post('https://t1.learnta.cn/__api/beatV3/student/task/42', data=json.dumps(data),
                              headers=self.headers)
        taskExecutionId = demo1.json()['data']['taskExecutionId']
        data = {"userAnswers": [], "isEvaluated": 'true', "taskExecutionId": taskExecutionId}
        demo2 = requests.post(
            'https://t1.learnta.cn/__api/beatV3/student/task/42/' + str(taskExecutionId) + '/question',
            data=json.dumps(data),
            headers=self.headers)

        self.assertEqual(demo2.status_code, 200, msg="英语综合题型卡question测试失败")
        question = demo2.json()['data']['questions'][0]['id']

        data = {"questionId": question, "answer": [""]}
        demo3 = requests.put('https://t1.learnta.cn/__api/beatV3/student/task/42/' + str(taskExecutionId) + '/answer',
                             data=json.dumps(data), headers=self.headers)
        self.assertEqual(demo3.status_code, 200, msg="英语综合题型卡answer测试失败")

    def testUnlockallchapterslessonsbelow(self):
        '''关掉全部章节/课程下面--罗志敏'''
        data = {"courseId":2554,"teacherId":133185,"lockState":1}
        demo = requests.put('https://t1.learnta.cn/__api/ilearnta/chapter/allChapters',data=json.dumps(data),
                            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="关掉全部章节/课程下面测试失败")
        self.assertEqual(str(demo.json()['data']),  'True', msg="关掉全部章节/课程下面测试失败")
    def testOpenallchapterslessonsbelow(self):
        '''解锁全部章节/课程下面--罗志敏'''
        data = {"courseId":2554,"teacherId":133185,"lockState":0}
        demo = requests.put('https://t1.learnta.cn/__api/ilearnta/chapter/allChapters',data=json.dumps(data),
                            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="解锁全部章节/课程下面测试失败")
        self.assertEqual(str(demo.json()['data']),  'True', msg="解锁全部章节/课程下面测试失败")

    def testUnlockunlocksinglesection(self):
        '''关锁->单个章节--罗志敏'''
        data = {"chapterId":40193,"teacherId":133185,"lockState":1}
        demo = requests.put('https://t1.learnta.cn/__api/ilearnta/chapter/chapterState',data=json.dumps(data),
                            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="关锁->单个章节测试失败")
        self.assertEqual(str(demo.json()['data']), 'True', msg="关锁->单个章节测试失败")

    def testOpenlocksinglesection(self):
        '''解锁/开锁->单个章节--罗志敏'''
        data = {"chapterId": 40193, "teacherId": 133185, "lockState": 0}
        demo = requests.put('https://t1.learnta.cn/__api/ilearnta/chapter/chapterState', data=json.dumps(data),
                            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="解锁/开锁->单个章节测试失败")
        self.assertEqual(str(demo.json()['data']), 'True', msg="解锁/开锁->单个章节测试失败")

    def testNOStartstopclasses(self):
        '''班级内暂停课程--罗志敏'''
        data = {"id":100001,"state":1}
        demo = requests.put('https://t1.learnta.cn/__api/ilearnta/classroom/state',data=json.dumps(data),
                            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="暂停课程测试失败")
        self.assertEqual(str(demo.json()['data']), 'True', msg="暂停课程测试失败")

    def testStartstopclasses(self):
        '''班级内开启课程--罗志敏'''
        data = {"id": 100001, "state": 0}
        demo = requests.put('https://t1.learnta.cn/__api/ilearnta/classroom/state', data=json.dumps(data),
                            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="开启课程测试失败")
        self.assertEqual(str(demo.json()['data']), 'True', msg="开启课程测试失败")


    def testSwitchingcourse(self):
        '''切换课程记录当前学习课程--罗志敏'''
        data = {"courseId": 2811, "teacherId": 50500, "studentId": 128229, "id": 100035}
        demo = requests.put('https://t1.learnta.cn/__api/ilearnta/student/switch/2811', data=json.dumps(data),
                            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="切换课程记录当前学习课程测试通过")
        self.assertEqual(str(demo.json()['data']), "True", msg="切换课程记录当前学习课程测试通过")
    def testquerylist(self):
        '''学生管理列表查询学生信息--彭刚'''
        data = {"pageSize":10,"name":"","roleId":34,"orgId":1,"isStudent":1,"systemId":11}
        demo = requests.post('https://t1.learnta.cn/__api/auth/user/org/userlist?pageNo=1', data=json.dumps(data),
                             headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="学生管理列表查询学生信息测试失败")
        self.assertEqual(str(type(demo.json()['data']['items'][0]['configResultList'])),'<class \'NoneType\'>', msg="学生管理列表查询学生信息测试失败")

    def testhuoquzjie(self):
        '''获取章节列表--罗志敏'''
        demo = requests.get(
            'https://t1.learnta.cn/__api/ilearnta/chapter/chapterList?courseId=2826&studentId=133185&orgId=1000787',
            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']['categoryName'])), '<class \'str\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']['pressName'])), '<class \'str\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']['gradeName'])), '<class \'str\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']['name'])), '<class \'str\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']['order'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']['source'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']['imageUrl'])), '<class \'NoneType\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']['orgId'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']['roomId'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['studentId'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['chapterId'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['name'])), '<class \'str\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['topicInfoId'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['topicState'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['state'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['isStudy'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['pcIsStudy'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['nextKpointId'])), '<class \'NoneType\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['nextKpointName'])), '<class \'NoneType\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['buttonType'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['masteryKpointNum'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['kpointTotalNum'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['taskExecutionId'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['topicInfoType'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['order'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['serialNumber'])), '<class \'str\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['createdAt'])), '<class \'str\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['kpoints'])), '<class \'NoneType\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['continueType'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['nextChapterId'])), '<class \'NoneType\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['nextChapterName'])), '<class \'NoneType\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapters"][0]['lockState'])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["courseState"])), '<class \'int\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["studentName"])), '<class \'str\'>',
                         msg="获取章节列表测试失败")
        self.assertEqual(str(type(demo.json()['data']["studentId"])), '<class \'int\'>',
                         msg="获取章节列表测试失败")

    def testhuoquzhenzxuex(self):
        '''获取正在学习的知识点--刘俊峰'''
        demo = requests.get('https://t1.learnta.cn/__api/beatV3/tank/learningKpoint?roomId=2554',
                            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="获取正在学习的知识点测试失败")
        self.assertEqual(str(type(demo.json()['data']["chapterId"])), '<class \'NoneType\'>', msg="获取正在学习的知识点")
        self.assertEqual(str(type(demo.json()['data']["kpointId"])), '<class \'NoneType\'>', msg="获取正在学习的知识点")
        self.assertEqual(str(type(demo.json()['data']["name"])), '<class \'NoneType\'>', msg="获取正在学习的知识点")
        self.assertEqual(str(type(demo.json()['data']["date"])), '<class \'NoneType\'>', msg="获取正在学习的知识点")
        self.assertEqual(str(type(demo.json()['data']["masteryRate"])), '<class \'NoneType\'>', msg="获取正在学习的知识点")
        self.assertEqual(str(type(demo.json()['data']["intelligenceState"])), '<class \'NoneType\'>', msg="获取正在学习的知识点")
        self.assertEqual(str(type(demo.json()['data']["mediaInfo"])), '<class \'NoneType\'>', msg="获取正在学习的知识点")
        self.assertEqual(str(type(demo.json()['data']["intelligenceBNState"])), '<class \'NoneType\'>', msg="获取正在学习的知识点")
        self.assertEqual(str(type(demo.json()['data']["questions"])), '<class \'NoneType\'>', msg="获取正在学习的知识点")
        self.assertEqual(str(type(demo.json()['data']["questionNum"])), '<class \'NoneType\'>', msg="获取正在学习的知识点")
        self.assertEqual(str(type(demo.json()['data']["topicInfoType"])), '<class \'NoneType\'>', msg="获取正在学习的知识点")
        self.assertEqual(str(type(demo.json()['data']["enabled"])), '<class \'bool\'>', msg="获取正在学习的知识点")
        self.assertEqual(str(type(demo.json()['data']["video"])), '<class \'NoneType\'>', msg="获取正在学习的知识点")
        self.assertEqual(str(type(demo.json()['data']["lockState"])), '<class \'NoneType\'>', msg="获取正在学习的知识点")
        self.assertEqual(str(type(demo.json()['data']["studyNum"])), '<class \'NoneType\'>', msg="获取正在学习的知识点")
        self.assertEqual(str(type(demo.json()['data']["learnState"])), '<class \'NoneType\'>', msg="获取正在学习的知识点")
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


    def test_5_Createaclass(self):
        '''创建班级--林佳欣'''
        data = {"orgId": 1002769,"name": "lspljx"}
        demo = requests.post('https://t1.learnta.cn/__api/ilearnta/classroom/create', data=json.dumps(data),
                             headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="创建班级测试失败")
        self.assertEqual(str(demo.json()['data']),'True', msg="创建班级测试失败")
    def test_6_shoushuoxues(self):
        '''搜索学生--林佳欣'''
        demo = requests.get(
            'https://t1.learnta.cn/__api/ilearnta/student/search?orgId=1002769&classroomId=100035&name=17602183921',
            headers=self.headers)
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
    def test_7_Getsectionlist(self):
        '''添加学生进入课堂--林佳欣'''
        data = {"orgId": 1002769, "studentId": 128227, "classroomId": 100092}
        demo = requests.post('https://t1.learnta.cn/__api/ilearnta/student/addStudent', data=json.dumps(data),
                             headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="添加学生进入课堂测试失败")
        self.assertEqual(str(demo.json()['data']), 'True',
                         msg="添加学生进入课堂测试失败")

    def test_8_Teacherendclasslist(self):
        '''老师端班级列表(搜索)-- 林佳欣'''

        demo = requests.get('https://t1.learnta.cn/__api/ilearnta/classroom/teacher/list?orgId=1002769&name=lspljx&studentId=128227&teacherId=133185',
                            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="老师端班级列表(搜索)")
        self.assertEqual(str(type(demo.json()['data'][0]['id'])), '<class \'int\'>', msg="老师端班级列表(搜索)测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['studentId'])), '<class \'NoneType\'>', msg="老师端班级列表(搜索)测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['orgId'])), '<class \'NoneType\'>', msg="老师端班级列表(搜索)测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['name'])), '<class \'str\'>', msg="老师端班级列表(搜索)测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['creator'])), '<class \'str\'>', msg="老师端班级列表(搜索)测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['createTime'])), '<class \'str\'>', msg="老师端班级列表(搜索)测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['id'])), '<class \'int\'>', msg="老师端班级列表(搜索)测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['userId'])), '<class \'NoneType\'>',
                         msg="老师端班级列表(搜索)测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['orgId'])), '<class \'NoneType\'>',
                         msg="老师端班级列表(搜索)测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['avatar'])), '<class \'NoneType\'>',
                         msg="老师端班级列表(搜索)测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['name'])), '<class \'NoneType\'>',
                         msg="老师端班级列表(搜索)测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['mobile'])), '<class \'NoneType\'>',
                         msg="老师端班级列表(搜索)测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['category'])), '<class \'NoneType\'>',
                         msg="老师端班级列表(搜索)测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['press'])), '<class \'NoneType\'>',
                         msg="老师端班级列表(搜索)测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['grade'])), '<class \'NoneType\'>',
                         msg="老师端班级列表(搜索)测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['isExist'])), '<class \'NoneType\'>',
                         msg="老师端班级列表(搜索)测试失败")
    def test_9_Teachersidescreening(self):
        '''老师端筛选--林佳欣'''
        demo = requests.get('https://t1.learnta.cn/__api/ilearnta/classroom/1002769',
                             headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="老师端筛选测试失败")
        self.assertEqual(str(type(demo.json()['data']['students'])), '<class \'list\'>',
                         msg="老师端筛选测试失败")
        self.assertEqual(str(type(demo.json()['data']['teachers'][0]['id'])), '<class \'int\'>',
                         msg="老师端筛选测试失败")
        self.assertEqual(str(type(demo.json()['data']['teachers'][0]['name'])), '<class \'str\'>',
                         msg="老师端筛选测试失败")

    def test_10_Studentendclasslist(self):
        '''学生端班级列表-- 林佳欣'''

        demo = requests.get('https://t1.learnta.cn/__api/ilearnta/classroom/student/list?orgId=1002769',
                            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['id'])), '<class \'int\'>', msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['orgId'])), '<class \'int\'>', msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['avatar'])), '<class \'NoneType\'>', msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['className'])), '<class \'str\'>', msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['currentIntelligentRoomId'])), '<class \'NoneType\'>',
                         msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['teacherName'])), '<class \'str\'>', msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['createTime'])), '<class \'NoneType\'>', msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['category'])), '<class \'NoneType\'>', msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['press'])), '<class \'NoneType\'>', msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['grade'])), '<class \'NoneType\'>', msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['id'])), '<class \'NoneType\'>',
                         msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['userId'])), '<class \'int\'>',
                         msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['orgId'])), '<class \'NoneType\'>',
                         msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['avatar'])), '<class \'NoneType\'>',
                         msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['name'])), '<class \'NoneType\'>',
                         msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['mobile'])), '<class \'NoneType\'>',
                         msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['category'])), '<class \'NoneType\'>',
                         msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['press'])), '<class \'NoneType\'>',
                         msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['grade'])), '<class \'NoneType\'>',
                         msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['students'][0]['isExist'])), '<class \'NoneType\'>',
                         msg="学生端班级列表测试失败")

    def test_11_Studentlistdetailsintheclass(self):
        '''班级内学生列表详情-- 林佳欣'''

        demo = requests.get('https://t1.learnta.cn/__api/ilearnta/classroom/100092/detail',
                            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="学生端班级列表测试失败")
        self.assertEqual(str(type(demo.json()['data']['id'])), '<class \'int\'>', msg="班级内学生列表详情测试失败")
        self.assertEqual(str(type(demo.json()['data']['studentId'])), '<class \'NoneType\'>', msg="班级内学生列表详情测试失败")
        self.assertEqual(str(type(demo.json()['data']['orgId'])), '<class \'int\'>', msg="班级内学生列表详情测试失败")
        self.assertEqual(str(type(demo.json()['data']['name'])), '<class \'str\'>', msg="班级内学生列表详情测试失败")
        self.assertEqual(str(type(demo.json()['data']['creator'])), '<class \'str\'>', msg="班级内学生列表详情测试失败")
        self.assertEqual(str(type(demo.json()['data']['createTime'])), '<class \'str\'>', msg="班级内学生列表详情测试失败")
        self.assertEqual(str(type(demo.json()['data']['students'][0]['id'])), '<class \'NoneType\'>', msg="班级内学生列表详情测试失败")
        self.assertEqual(str(type(demo.json()['data']['students'][0]['userId'])), '<class \'int\'>', msg="班级内学生列表详情测试失败")
        self.assertEqual(str(type(demo.json()['data']['students'][0]['orgId'])), '<class \'NoneType\'>', msg="班级内学生列表详情测试失败")
        self.assertEqual(str(type(demo.json()['data']['students'][0]['avatar'])), '<class \'NoneType\'>', msg="班级内学生列表详情测试失败")
        self.assertEqual(str(type(demo.json()['data']['students'][0]['name'])), '<class \'NoneType\'>', msg="班级内学生列表详情测试失败")
        self.assertEqual(str(type(demo.json()['data']['students'][0]['mobile'])), '<class \'NoneType\'>', msg="班级内学生列表详情测试失败")
        self.assertEqual(str(type(demo.json()['data']['students'][0]['category'])), '<class \'NoneType\'>', msg="班级内学生列表详情测试失败")
        self.assertEqual(str(type(demo.json()['data']['students'][0]['press'])), '<class \'NoneType\'>', msg="班级内学生列表详情测试失败")
        self.assertEqual(str(type(demo.json()['data']['students'][0]['grade'])), '<class \'NoneType\'>', msg="班级内学生列表详情测试失败")
        self.assertEqual(str(type(demo.json()['data']['students'][0]['isExist'])), '<class \'NoneType\'>', msg="班级内学生列表详情测试失败")

    def test_12_Getsectionlist(self):
        '''删除学生--林佳欣'''
        data = {"studentId":128227,"classroomId":100092}
        demo = requests.delete('https://t1.learnta.cn/__api/ilearnta/student/byId/128227',data=json.dumps(data),headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="删除学生测试失败")
        self.assertEqual(str(demo.json()['data']), 'True', msg="删除学生测试失败")

    def testGetasnapshot(self):
        '''获取生图一览学生列表--罗志敏'''
        demo = requests.get('https://t1.learnta.cn/__api/ilearnta/classroom/studentList/100087',
                            headers=self.headers)
        self.assertEqual(demo.status_code, 200, msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['id'])), '<class \'int\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['studentName'])), '<class \'str\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['avatar'])), '<class \'str\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['orgId'])), '<class \'int\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['courseId'])), '<class \'int\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['chapterId'])), '<class \'int\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['chapterName'])), '<class \'NoneType\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['kpointId'])), '<class \'NoneType\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['kpointName'])), '<class \'NoneType\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['studyTime'])), '<class \'NoneType\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['questionNum'])), '<class \'NoneType\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['kpointTotalNum'])), '<class \'NoneType\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['lockState'])), '<class \'NoneType\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['kpointKnowNum'])), '<class \'NoneType\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['categoryName'])), '<class \'str\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['gradeName'])), '<class \'str\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['name'])), '<class \'NoneType\'>', msg="获取生图一览学生列表测试失败")
        self.assertEqual(str(type(demo.json()['data'][0]['classroomId'])), '<class \'int\'>', msg="获取生图一览学生列表测试失败")

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
    runner.report(filename='learntaplus.html', description='learntaplus测试', log_path=report_dir)
    print(report_dir)
    print(filename)
elif(platform.system()=='Linux'):
    report_dir = "/opt/uitest/report"
    filename = '/opt/uitest/img'
    runner.report(filename='learntaplus.html', description='learntaplus测试', report_dir=report_dir)
    print(report_dir)
    print(filename)
    print(platform.system())
else:
    print(platform.system())