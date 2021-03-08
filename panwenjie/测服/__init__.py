import requests
import json

headers = {'content-type': 'application/json;charset=UTF-8'};
asdad = {"username": 13975353140, "code": 1111, "systemCode": "dms"}
asdsada = requests.post("https://api.t2.learnta.cn/v1/auth/crm/user/login",
                                     data=json.dumps(asdad), headers=headers)
print(asdsada.status_code)