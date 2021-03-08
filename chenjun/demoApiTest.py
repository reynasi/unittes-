#coding:utf-8
import json
import requests
import unittest

headers = {'content-type': 'application/json;charset=UTF-8'}
testdatalist = [
    'teststr',
    '',
    '~!@#$%',
    '中 文',
    88888888,
    'longstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstr',
    123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789
]

# 正常业务参数
print('正常业务参数')
postdata1= {'mobile': 18616015760, 'orgId': 1000491}
print(postdata1)
postResponsedata = requests.post('https://cj.t1.learnta.cn/__api/auth/user/verifycode', data=json.dumps(postdata1), headers=headers)
dict_postResponsedata = json.loads(postResponsedata.text)
print('status_code:' + str(postResponsedata.status_code))
print('total_seconds:{:.2f}ms'.format(postResponsedata.elapsed.total_seconds()*1000))
print('dict_postResponsedata:' + str(dict_postResponsedata))
print('\n')

# 异常业务参数
print('异常业务参数')
for num in range(0, len(testdatalist)):
    print('第' + str(num+1) + '条异常业务testcase')
    postdata2= {'mobile': testdatalist[num], 'orgId': testdatalist[num]}
    print('postdata:' + str(postdata2))
    postResponsedata = requests.post('https://cj.t1.learnta.cn/__api/auth/user/verifycode', data=json.dumps(postdata2), headers=headers)
    dict_postResponsedata = json.loads(postResponsedata.text)
    print('status_code:' + str(postResponsedata.status_code))
    print('total_seconds:{:.2f}ms'.format(postResponsedata.elapsed.total_seconds()*1000))
    print('dict_postResponsedata:' + str(dict_postResponsedata))
    print('\n')

# 不传参数
print('不传字段参数')
postdata3= {}
print('postdata:' + str(postdata3))
postResponsedata = requests.post('https://cj.t1.learnta.cn/__api/auth/user/verifycode', data=json.dumps(postdata3), headers=headers)
dict_postResponsedata = json.loads(postResponsedata.text)
print('status_code:' + str(postResponsedata.status_code))
print('total_seconds:{:.2f}ms'.format(postResponsedata.elapsed.total_seconds()*1000))
print('dict_postResponsedata:' + str(dict_postResponsedata))
print('\n')