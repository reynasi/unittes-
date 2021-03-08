# -*- coding:utf-8 -*-
import time
import traceback
import unittest
import requests
import json


class ApiTestCasePro(unittest.TestCase):
    # def setUp(self):
    #     url = 'https://learnta.learnta.cn/__api/7/classroom/org/byTeacherId?_t=1527591382217'  # url:接口地址

    def get_answer(self, authorization, urlstr, prequestionId):
        url= "https://" + urlstr + "/__api/admin/qlib/getQById/" + prequestionId
        headers = {
            "authorization": authorization,
            "Content-Type": 'application/json'
        }

        try:
            response = requests.get(url=url, headers=headers)
            json_response = json.loads(response.text)
            # print("Response_code：", response.status_code, "\n")

            answer = json_response["data"]["answer"]
            # type = json_response["data"]["type"]
            # qulist= []
            # qulist.append(answer)
            # qulist.append(type)
        except:
            traceback.print_exc()
            print("接口调用失败，答案获取失败～～～")
        return answer

    # 登录后获取token
    def test_get_token(self, urlstr, systemId, orgId):
        url = "https://" + urlstr + "/__api/auth/user/loginOrg?_t=1571994373113"
        headers = {
                    # "authorization": 'Bearer 7ff41bf8-377f-35bf-ba3b-e317e771969a',
                   "Content-Type": 'application/json'
                   }
        # test_data_url_encode = urllib.parse.urlencode(params)
        params = {"username": "18817572035", "code": "1111", "systemId": systemId,
                  "orgId": orgId, "logo": "FhLrrWcTqHoA99rgkE0nZIATUDTe",
                  "evaluateLogo": "FnKHpcybMyk7gEOaTxl6Q3g0iCn6"}
        try:
            response = requests.post(url=url, json=params, headers=headers)
            json_response = json.loads(response.text)
            #print("Response_code：", response.status_code, "\n")

            result = json_response["data"]
            token_type = result["tokenType"]
            access_token = result["access_token"]
            token = token_type + " " + access_token
        except:
            traceback.print_exc()
            print("呵呵啦～～～")

        return token


    def test_get_01(self, authorization, urlstr):
        url = "https://" + urlstr + "/__api/wechat/go/next/8330/go?_t=1571992835662"
        #authorization = self.test_get_token()

        headers = {"authorization": authorization,
                   "Content-Type": 'application/json'
                   }
        # test_data_url_encode = urllib.parse.urlencode(params)
        try:
            response = requests.get(url=url, headers=headers)
            json_response = json.loads(response.text)
            #print("Response_code：", response.status_code, "\n")

            result = json_response["data"]
            questionId = result["questionId"]
            #print(questionId)
        except:
            print("呵呵啦～～～")

        return questionId

    def test_post_01(self, authorization, urlstr, questionId):
        #print("start post......")
        url3 = "https://" + urlstr + "/__api/wechat/go/subject/study/item/quest?_t=1547541055913"

        #authorization = self.test_get_token()
        params = {"questionId": questionId}

        headers = {"authorization": authorization,
                    "Content-Type": 'application/json'
                  }
        #ssl._create_default_https_context = ssl._create_unverified_context

        #test_data_url_encode = urllib.parse.urlencode(params)
        datalist=[]
        try:
            response = requests.post(url=url3, json=params, headers=headers)
            json_response = json.loads(response.text)
            #print("Response_code：", response.status_code, "\n")
            questionId = json_response["data"]["questionId"]
            questiontype = json_response["data"]["type"]
            #print(questionId)
            datalist=[]
            datalist.append(questionId)
            datalist.append(questiontype)

        except:
            print("呵呵啦～～～")

        return datalist


    # def test_getClassroomId(self, authorization, urlstr, orgId):
    #     url = "https://" + urlstr + "/__api/beatV3/classroom/org/byTeacherId?_t=1574749722262"
    #     headers = {"authorization": authorization,
    #                "Content-Type": 'application/json'
    #                }
    #     param = {"state": 0,
    #               "orgId": orgId
    #             }
    #     try:
    #         response = requests.post(url=url, json=param, headers=headers)
    #         json_response = json.loads(response.text)
    #         # print("Response_code：", response.status_code, "\n")
    #         classroomId = json_response[0]["id"]
    #     except:
    #         traceback.print_exc()
    #     return classroomId

    def test_getClassroomId(self, authorization, urlstr, orgId, searchName):
        url = "https://" + urlstr + "/__api/beatV3/classroom/org/byTeacherId?_t=1574749722262"
        headers = {"authorization": authorization,
                   "Content-Type": 'application/json'
                   }
        param = {"state": 0,
                 "orgId": orgId,
                 "studentId": [],
                 "searchName": searchName
                 }
        try:
            response = requests.post(url=url, json=param, headers=headers)
            json_response = json.loads(response.text)
            # print("Response_code：", response.status_code, "\n")
            classroomId = json_response[0]["id"]
        except:
            traceback.print_exc()
        return classroomId

    def test_getTeacherxClassroomId(self, authorization, urlstr, orgId):
        url = "https://" + urlstr + "/__api/beatV3/ppt/classroom/org/byTeacherId?_t=1577263935148"
        headers = {"authorization": authorization,
                   "Content-Type": 'application/json'
                   }
        param = {"state": 0,
                  "orgId": orgId,
                  "tags": "null"
                }
        try:
            response = requests.post(url=url, json=param, headers=headers)
            json_response = json.loads(response.text)
            # print("Response_code：", response.status_code, "\n")
            classroomId = json_response[0]["id"]
        except:
            traceback.print_exc()
        return classroomId


    def test_getTaskExecutionId(self, authorization, urlstr, classroomId):
        url = "https://" + urlstr + "/__api/beatV3/classroom/byStudentId/" + classroomId

        headers = {"authorization": authorization,
                   "Content-Type": 'application/json'
                   }
        try:
            response = requests.get(url=url, headers=headers)
            json_response = json.loads(response.text)
            # print("Response_code：", response.status_code, "\n")
            taskExecutionId = json_response["classroomExecutions"][0]["classroomTask"]["id"]
            taskType = json_response["classroomExecutions"][0]["classroomTask"]["taskType"]
            taskList=[]
            taskList.append(taskExecutionId)
            taskList.append(taskType)
        except:
            traceback.print_exc()
        return taskList

    # 学生端获取questionId
    def test_get_studentquestion(self, authorization,urlstr, taskExecutionId):
        url4 = "https://" + urlstr + "/__api/beatV3/classroom/task/diygo/question"

        headers = {"authorization": authorization,
                   "Content-Type": 'application/json'
                   }

        param = {"taskExecutionId": taskExecutionId}

        try:
            response = requests.post(url=url4, json=param, headers=headers)
            json_response = json.loads(response.text)
            # print("Response_code：", response.status_code, "\n")
            questionId = json_response["id"]
            type = json_response["type"]
            qlist = []
            qlist.append(questionId)
            qlist.append(type)
        except:
            traceback.print_exc()
        return qlist

    def test_getIntelligentquestion(self, authorization, urlstr, taskExecutionId):   #
        url = "https://" + urlstr + "/__api/beatV3/classroom/task/recommendation/question"


        headers = {"authorization": authorization,
                   "Content-Type": 'application/json;charset=utf-8'
                   }

        param = {"taskExecutionId": taskExecutionId,
                 "isEvaluated": 'true'
                 }
        try:
            response = requests.post(url=url, json=param, headers=headers)
            json_response = json.loads(response.text)
            #print("Response_code：", response.status_code, "\n")
            Response_code = response.status_code
            if Response_code == 200:
                response_code = response.status_code
                questionId = json_response["id"]
                type = json_response["type"]
                kpointId = json_response["kpointId"]
                previousKpointId = json_response["previousKpointId"]
                qlist = []
                qlist.append(response_code)
                qlist.append(questionId)
                qlist.append(type)
                qlist.append(kpointId)
                qlist.append(previousKpointId)
            elif Response_code == 403:
                response_code = response.status_code
                qlist = []
                qlist.append(response_code)
        except:
            traceback.print_exc()
        return qlist

    def getIntelligentQuestion(self, authorization, urlstr, taskExecutionId, taskType):   #
        url = "https://" + urlstr + "/__api/beatV3/student/task/"+ taskType +"/"+taskExecutionId+"/question"

        headers = {"authorization": authorization,
                   "Content-Type": 'application/json;charset=utf-8'
                   }

        param = {"userAnswers": [],
                 "isEvaluated": "true",
                 "isRecommIfNoWeakPoints": "false",
                 "taskExecutionId": taskExecutionId
                 }
        try:
            response = requests.post(url=url, json=param, headers=headers)
            json_response = json.loads(response.text)
            code = response.status_code
            hasNextQuestion = json_response["data"]["hasNextQuestion"]
            qlist = []
            if hasNextQuestion==True:
                questionId = json_response["data"]["questions"][0]["id"]
                type = json_response["data"]["questions"][0]["type"]
                kpointId = json_response["data"]["questions"][0]["kpointId"]
                previousKpointId = json_response["data"]["questions"][0]["previousKpointId"]
                ordinal = json_response["data"]["questions"][0]["ordinal"]
                qlist.append(hasNextQuestion)
                qlist.append(questionId)
                qlist.append(type)
                qlist.append(kpointId)
                qlist.append(previousKpointId)
                qlist.append(code)
                qlist.append(ordinal)
            else:
                qlist.append(hasNextQuestion)
        except:
            traceback.print_exc()
        return qlist

    #  获取测评卡的topicId
    def test_getTopicId(self, authorization, urlstr, taskExecutionId):
        url = "https://" + urlstr + "/__api/beatV3/classroom/task/taskDetail/"+ taskExecutionId +"?_t=1574144699938"

        headers = {"authorization": authorization,
                   "Content-Type": 'application/json'
                    }
        try:
            response = requests.get(url=url, headers=headers)
            json_response = json.loads(response.text)
            # print("Response_code：", response.status_code, "\n")
            topicId = json_response["task"]["topicId"]
            #type = json_response["type"]
            topiclist = []
            topiclist.append(topicId)

        except:
            traceback.print_exc()
        return topiclist

        #  获取测评卡的topicId

    # 获取测评卡的goquestionId
    def test_getGoquestionId(self, authorization, urlstr, topicId):
        url = "https://" + urlstr + "/__api/wechat/go/next/"+ topicId +"/go?_t=1574151192987"

        headers = {"authorization": authorization,
                   "Content-Type": 'application/json'
                   }
        try:
            response = requests.get(url=url, headers=headers)
            json_response = json.loads(response.text)
            # print("Response_code：", response.status_code, "\n")
            goquestionId = json_response["data"]["id"]
        except:
            traceback.print_exc()
        return goquestionId

    # 获取测评卡的questionId Diygo teacherx发智能测评卡
    def test_getRequestionId(self, authorization, urlstr, taskExecutionId):
        url = "https://" + urlstr + "/__api/beatV3/custom/diygo/question"

        headers = {"authorization": authorization,
                   "Content-Type": 'application/json'
                   }
        param = {"taskExecutionId": taskExecutionId,
                 }
        try:
            response = requests.post(url=url, headers=headers, json=param)
            json_response = json.loads(response.text)
            # print("Response_code：", response.status_code, "\n")
            requestionId = json_response["data"]["id"]
        except:
            traceback.print_exc()
        return requestionId

    # 获取真正的题目Id 从预发布获取，但是发现预发布没有这个接口
    def test_getDiyGoquestionId(self, authorization='Bearer 90de49c0-7c43-3c42-9547-1f397ec2c8ca', urlstr='shupingorg.learnta.cn', requestionId='409485'):
        url = "https://" + urlstr + "/__api/qatestapi/public/getQuestionId/" + requestionId

        headers = {"authorization": authorization,
                   "Content-Type": 'application/json'
                   }
        proxy = {'https': '47.98.242.163:443'}
        try:
            response = requests.post(url=url, proxies=proxy, headers=headers)
            json_response = json.loads(response.text)
            # print("Response_code：", response.status_code, "\n")
            questionId = json_response["data"]["id"]
        except:
            traceback.print_exc()
        return questionId

    # 获取招生测评ActivityId(创建的招生测评活动Id)
    def test_getActivityId(self, authorization, urlstr):  #
        url = urlstr + "/__api/beatV3/recruit/activityList?pageNo=1&itemsPerPage=10" \
              "&name=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%84%E5%9F%B9%E4%BC%9820200218&orgId=100040&_t=1582090976388"

        headers = {"authorization": authorization,
                   "Content-Type": 'application/json'
                   }
        try:
            response = requests.get(url=url, headers=headers)
            json_response = json.loads(response.text)
            # print("Response_code：", response.status_code, "\n")
            activityId = json_response["items"][0]["id"]
        except:
            traceback.print_exc()
        return activityId

    # 获取招生测评teacherxActivityId(创建的招生测评活动Id)
    def test_getTeacherxActivityId(self, authorization, urlstr):  #
        url = urlstr + "/__api/beatV3/recruit/activityList?pageNo=1&itemsPerPage=10&" \
                       "name=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%84%E5%9F%BA%E7%A1%8020200219&orgId=100067&_t=1582101966671"

        headers = {"authorization": authorization,
                   "Content-Type": 'application/json'
                   }
        try:
            response = requests.get(url=url, headers=headers)
            json_response = json.loads(response.text)
            # print("Response_code：", response.status_code, "\n")
            activityId = json_response["items"][0]["id"]
        except:
            traceback.print_exc()
        return activityId

    # 获取教学测评的executionId
    def test_getTestingExecutionId(self, authorization, topicNum):
        url = "https://learnta.cn/__api/beatV3/topic/goExam/"+topicNum+""

        headers = {"authorization": authorization,
                   "Content-Type": 'application/json'
                   }
        try:
            response = requests.get(url=url, headers=headers)
            json_response = json.loads(response.text)
            # print("Response_code：", response.status_code, "\n")
            executionId = json_response["cste"]
        except:
            traceback.print_exc()
        return executionId

    # 获取招生测评的ExecutionId
    def test_getRecruitExecutionId(self, authorization, activityId, category, grade): #category 代表科目 ， 每次获取的值都会变
        url = "https://www.learnta.cn/__api/beatV3/recruit/goExam"

        headers = {"authorization": authorization,
                   "Content-Type": 'application/json'
                   }
        param = {"category": category,   # 1表示数学 ，0表示英语
                 "activityId": activityId,
                 "grade": grade}
        try:
            response = requests.post(url=url, headers=headers, json=param)
            json_response = json.loads(response.text)
            # print("Response_code：", response.status_code, "\n")
            executionId = json_response["executionId"]
        except:
            traceback.print_exc()
        return executionId

    # 获取招生测评的topicId
    def test_getRecruitTopicId(self, authorization, executionId):
        url = "https://www.learnta.cn/__api/beatV3/public/classroom/task/taskDetail/"+executionId+""

        headers = {"authorization": authorization,
                   "Content-Type": 'application/json'
                   }
        try:
            response = requests.get(url=url, headers=headers)
            json_response = json.loads(response.text)
            # print("Response_code：", response.status_code, "\n")
            topicId = json_response["task"]["topicId"]
        except:
            traceback.print_exc()
        return topicId

    # 获取招生测评的questiontype
    def test_getQuestionType(self, authorization, topicId):
        url = "https://www.learnta.cn/__api/wechat/go/next/"+topicId+"/go"

        headers = {"authorization": authorization,
                   "Content-Type": 'application/json'
                   }
        try:
            response = requests.get(url=url, headers=headers)
            json_response = json.loads(response.text)
            # print("Response_code：", response.status_code, "\n")
            questiontype = json_response["data"]["type"]
        except:
            traceback.print_exc()
        return questiontype

    # 获取测评卡的questionId
    def test_getTestingquestionId(self, authorization, urlstr, goQuestionId):
        url = urlstr + "/__api/wechat/go/subject/study/item/quest"

        headers = {"authorization": authorization,
                   "Content-Type": 'application/json'
                   }
        param = { "questionId": goQuestionId
                }
        try:
            response = requests.post(url=url, headers=headers, json=param)
            json_response = json.loads(response.text)
            # print("Response_code：", response.status_code, "\n")
            questionId = json_response["data"]["questionId"]
            type = json_response["data"]["type"]
            qlist = []
            qlist.append(questionId)
            qlist.append(type)
        except:
            traceback.print_exc()
        return qlist

#下面调用两个方法：
# if __name__ == '__main__':
#     unittest.main()
    #suite = unittest.TestSuite()
# now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

#方法1
# testsuite = unittest.TestSuite()
# testsuite.addTest(ApiTestCasePro("test_getTopicId"))

# 方法2
#test_cases = unittest.TestRunner().loadTestsFromTestCase(ApiTestCase)
# test_cases = unittest.TextTestRunner().run()
# suite = unittest.TestSuite()
# suite.addTest(test_cases)
# runner = unittest.TextTestRunner()
# runner.run(suite)

#公共部分
# run = BeautifulReport(testsuite)
# run.report(filename='Api接口测试.html', description='备课系统测试', report_dir='report')


#---------------------------------- Mac存放路径 -------------------------------
#filename = "/Users/shuping/Report/report.html"  # 定义个报告存放路径，支持相对路径


#---------------------------------- linux存放路径 ------------------------------
# linux 存放路径
#filename = "/usr/local/Apireport.html"  # 定义个报告存放路径，支持相对路径
# f = open(filename, 'wb')  # 结果写入HTML 文件
# runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='suping的接口自动化测试报告', description='用例执行情况：')
# runner.run(testsuite)
# f.close()
