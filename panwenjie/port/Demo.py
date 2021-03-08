import requests
import json

headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer 65526c68-611e-3101-ad69-1e84eea6d8e0'}

asdasdf = {'intelligentStudyRoomTopicId': 1416122, 'orgId': 101260}
saad = requests.post('https://www.kupeiai.cn/__api/beatV3/student/task/24', json=asdasdf,
                     headers=headers)
# print(saad.status_code)
taskExecutionId = saad.json()['data']['taskExecution']['id']
print(taskExecutionId)



ijsji = {'userAnswers': [], 'isEvaluated': 'true', 'isRecommIfNoWeakPoints': 'false',
                     'taskExecutionId': taskExecutionId}
huoqkeid = requests.post(
    'https://www.kupeiai.cn/__api/beatV3/student/task/24/'+str(taskExecutionId)+'/question'
    , data=json.dumps(ijsji), headers=headers)
print(huoqkeid.status_code)

# questionId = huoqkeid.json()['data']['questions'][0]['id']
# question = huoqkeid.json()['data']['questions']