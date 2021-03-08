import requests

#定义请求url
#
# headers = {'content-type': 'application/json;charset=UTF-8'};
# loginOrgPostdata={"openId": "", "randomCode": "2173", "shareType": "homework", "username": "1231", "mobile": "13975353140"}
#
# r = requests.post("https://t2.learnta.cn/__api/wechat/public/wechat/qRcode/login/",data=loginOrgPostdata,headers=headers)
# print("状态码", r.status_code)
# #print(self.token)
import json

datatest = requests.get('https://t2.learnta.cn/__api/wechat/public/qRcode/chargeExam/snDeY4smKaNoPif488908')
print(datatest.status_code)
# put请求
# url = "https://api.learnta.cn/v1/dms/demoAccount/0/6/220793/reset/"
# headers = {'content-type': 'application/json;charset=UTF-8','authorization':'Bearer '+token}
#
# r = requests.put(url, headers=headers)
# # print("请求url:", r.url)  # 响应对象.r

# 4.获取响应状态码
# print("状态码", r.status_code)