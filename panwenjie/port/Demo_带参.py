'''
目标 GET请求演练
案例:http://www.baidu.com
    1、http://www.baidu.com? id = 1001
    2、http://www.baidu.com? id = 1001,1002
    2、http://www.baidu.com? id = 1001&kw=北京
请求:
    1.请求方法去:get
参数：
    params：字典或字符串 （推荐使用字典）
响应:
    2.响应对象.url #获取请求url
    3.响应对象.status_code #获取响应状态码
    4.响应对象.text #以文本形式显示响应内容
'''
#1.导包
import requests

#2.调用get
url = "https://www.baidu.com"
#不推荐写法
# url = "https://www.baidu.com?id=1001"

#案例一 定义字典
# params = {"id": 1001}

#案例二v
#params = {"id": {1001, 1002}} #不推荐
# params = {"id": "1001,1002"} # %2C为 ASCI值为逗号

#案例三
params = {"id": 1001,"kw":"北京"}# 多个键值使用方式

#字符串形式案例编写
#r = requests.get(url, params="id=1001")#不推荐使用
#请求时带参数 params
r = requests.get(url, params=params) #r:为响应数据对象

#3.获取请求url地址
print("请求url:",r.url)#响应对象.r

#4.获取响应状态码
print("状态码",r.status_code)

#5.获取响应请求信息 文本形式
print("文本响应内容:",r.text)
