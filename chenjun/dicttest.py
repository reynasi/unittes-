#coding:utf-8

testdatalist = [
    'teststr',
    '',
    '~!@#$%',
    '中 文',
    88888888,
    'longstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstr',
    123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789
]
postdata1= {'mobile': 18616015760, 'orgId': 1000491}
# print(type(postdata1))
# print(postdata1.keys())
keys = list(postdata1.keys())
# print(keys)
# print(type(keys))
# seq = ('mobile', 'orgId')
# print(type(seq))
# tuplekeys = tuple(keys)
# print(tuplekeys)
# print(type(tuplekeys))
# dict = dict.fromkeys(tuplekeys, testdatalist[2])
# print(str(dict))
postdata2 = dict.fromkeys(keys,testdatalist[3])
print(str(postdata2))


testdatalist = [
        'teststr',
        '',
        '~!@#$%',
        88888888,
        -888888
    ]
strlist = [100240, 11, 0]
testurl = 'https://bcq.learnta.cn/__api/auth/role/rolelist/' + str(testdatalist[0]) + '/'+ str(strlist[1]) + '/' + str(strlist[2]) + ''
print(str(testurl))
print(type(testurl))
strlist2 = [1, 100240]
testurl2 = 'https://bcq.learnta.cn/__api/beatV3/topic/getCategoryPress?type=' + str(strlist2[0]) + '&orgId=' + str(strlist2[1]) + ''
print(str(testurl2))

num = 3
testdatalist = [
        'teststr',
        '',
        '~!@#$%',
        88888888,
        -888888
    ]
testurlpingjie = 'https://bcq.learnta.cn/__api/auth/role/rolelist/' + str(testdatalist[num]) + '/' + str(testdatalist[num]) + '/' + str(testdatalist[num]) + ''
print(testurlpingjie)

def pingjie(url, list):
    for num in range(0, len(testdatalist)):
        truetesturl = testurlpingjie
        print(truetesturl)

pingjie(testurlpingjie, testdatalist)


testinstr = 200
print(type(testinstr))
if testinstr in (200,401):
    print('ok')
else:
    print('no')


def geturltest(url):
    testdatalist = [
        'teststr',
        '',
        '~!@#$%',
        88888888,
        -888888
    ]
    num = 4
    listformat = []
    for i in range(2):
        listformat.append(testdatalist[num])
    print(url.format(*listformat))

url = "http://learnta.cn/{}/?test={}"
geturltest(url)

x = "https://bcq.learnta.cn/__api/auth/role/rolelist/{}/{}/{}"
print(x.count("{}"))

putlist = [123, 321, 2265]
dictlist = {"test": 123, "test2": "test"}
print(type(putlist))
print(type(dictlist))

if type(putlist) is list:
    print('yes')

print([123 for num in range(len(putlist))])