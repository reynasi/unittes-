import requests
# import json
#
# headers = {'content-type': 'application/json;charset=UTF-8'};
#
# # t2.learnta.cn登录
# loginOrgPost = {'branch': 1, 'username': 13975353140, 'code': 1111, 'systemId': 11, 'orgId': 1}
# loginOrgResponse = requests.post("https://t2.learnta.cn/__api/auth/user/loginOrg",
#                                  data=json.dumps(loginOrgPost), headers=headers)
# token = loginOrgResponse.json()['data']['access_token']
# headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer ' +token}
# huoqkcid = requests.get('https://t2.learnta.cn/__api/beatV3/topic/goExam/SYb84ATi1U1sUVsX88804',headers=headers)
# print("文本响应内容:",huoqkcid.text)
datatest = requests.get('https://t2.learnta.cn/__api/wechat/public/qRcode/chargeExam/6OhJXmMqh8dfMxPc88987')

print(datatest.status_code)