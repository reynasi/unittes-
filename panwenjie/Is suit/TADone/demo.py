import requests
import json
import logging
headers = {'content-type': 'application/json;charset=UTF-8'};
# 教师端登录
loginOrgPost = {"branch":"100310","username":"13975353141","code":"1111","systemId":11,"orgId":100310}
loginOrgResponse = requests.post("https://ilearnta.com/__api/auth/user/loginOrg",
                                 data=json.dumps(loginOrgPost), headers=headers)
token = loginOrgResponse.json()['data']
print(token)