#coding:utf-8
import json
import requests

# 封装post接口正常&&异常请求参数测试方法
def postRequestTest(url, headers, postdata):
    # 定义一个测试结果list，用于返回测试方法最终的结果
    testResultList = []
    # 定义一个testcodelist,用于遍历所有用例的pass和failed情况，只要有一个failed，总用例就failed
    testCodeList = []
    # 定义一个测试异常参数集合
    testdatalist = [
        'teststr',
        '',
        '~!@#$%',
        '中 文',
        88888888,
        -888888,
        [1, 2, 3],
        ['test1', 'test2', 'test3'],
        [],
        'longstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstr',
        123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789
    ]
    print('测试POST接口:' + url)

    # 正常业务参数
    print('--------测试正常业务参数--------')
    postResponsedata = requests.post(url, data=json.dumps(postdata), headers=headers)
    testResult = '请求参数:' + str(postdata) + ',状态码:' + str(postResponsedata.status_code) + ',响应时间:' + str(postResponsedata.elapsed.total_seconds()*1000)
    # 如果测试接口的状态码不是200并且响应时间小于400ms就写入failed，如果是就pass，并且写入testcode
    if ((postResponsedata.status_code in (200, 403)) & (postResponsedata.elapsed.total_seconds()*1000 < 400)):
        testCode = 'pass'
        print('正常业务参数测试通过，请求正常参数:' + str(postdata))
        print('单接口性能测试通过, 响应时间为:' + str(postResponsedata.elapsed.total_seconds()*1000) + 'ms')
        print('\n')
    else:
        testCode = 'failed'
        print('测试失败，状态码非200或者响应时间超过400ms'+ str(postdata))
        print('状态码:' + str(postResponsedata.status_code))
        print('响应时间:' + str(postResponsedata.elapsed.total_seconds() * 1000) + 'ms')
        print('\n')
    testCodeList.append(testCode)
    testResultList.append(testResult)  # 最后返回的测试结果list

    # 异常业务参数
    print('--------测试异常参数--------')
    for num in range(0, len(testdatalist)):
        keys = list(postdata.keys())
        postErrorData = dict.fromkeys(keys, testdatalist[num])
        postResponsedata = requests.post(url, data=json.dumps(postErrorData), headers=headers)
        # print(postResponsedata.text)
        testResult = '请求参数:' + str(postErrorData) + '状态码:' + str(postResponsedata.status_code) + ',响应时间:' + str(postResponsedata.elapsed.total_seconds()*1000)
        # 如果测试接口的状态码不是200就写入failed，如果是就pass，并且写入testcode
        if (postResponsedata.status_code in (200, 403)) :
            testCode = 'pass'
            print('第' + str(num + 1) + '条异常业务testcase，测试通过')
            print(' 请求异常参数:' + str(postErrorData))
        else:
            testCode = 'failed'
            print('第' + str(num + 1) + '条异常业务testcase，测试失败')
            print(' 请求异常参数:' + str(postErrorData))
            print('测试失败，状态码非200或者响应时间超过400ms')
            print('状态码:' + str(postResponsedata.status_code))
            print('响应时间:' + str(postResponsedata.elapsed.total_seconds() * 1000) + 'ms')
        testCodeList.append(testCode)
        testResultList.append(testResult)  # 最后返回的测试结果list
    print('\n')

    # 不传参数
    print('--------测试空参数--------')
    postdata = {}
    postResponsedata = requests.post(url, data=json.dumps(postdata), headers=headers)
    testResult = '请求参数:' + str(postdata) + '状态码:' + str(postResponsedata.status_code) + ',响应时间:' + str(postResponsedata.elapsed.total_seconds()*1000)
    # 如果测试接口的状态码不是200就写入failed，如果是就pass，并且写入testcode
    if (postResponsedata.status_code in (200, 403)):
        testCode = 'pass'
        print('空参数测试通过')
        print('请求空参数:' + str(postdata))
    else:
        testCode = 'failed'
        print('测试失败，状态码非200或者响应时间超过400ms')
        print('请求空参数:' + str(postdata))
        print('状态码:' + str(postResponsedata.status_code))
        print('响应时间:' + str(postResponsedata.elapsed.total_seconds()*1000) + 'ms')
    testCodeList.append(testCode)
    testResultList.append(testResult)  # 最后返回的测试结果list
    # print(testCodeList) # 用于调试打印所有testcodelist中的状态是pass还是failed
    if 'failed' not in testCodeList:
        testFinalCode = 'pass'
    else:
        testFinalCode = 'failed'
    return testFinalCode, testResultList  # 返回两个参数，第一个表示测试状态，第二个表示测试结果list

# 封装get接口正常&&异常请求参数测试方法
def getRequestTest(url, headers):
    # 定义一个测试结果list，用于返回测试方法最终的结果
    testResultList = []
    # 定义一个testcodelist,用于遍历所有用例的pass和failed情况，只要有一个failed，总用例就failed
    testCodeList = []
    print('测试GET接口:' + url)
    getResponsedata = requests.get(url, headers=headers)
    testResult = '请求参数:' + str(url) + ',状态码:' + str(getResponsedata.status_code) + ',响应时间:' + str(getResponsedata.elapsed.total_seconds() * 1000)
    # 如果测试接口的状态码不是200并且响应时间小于400ms就写入failed，如果是就pass，并且写入testcode
    if ((getResponsedata.status_code in (200, 403)) & (getResponsedata.elapsed.total_seconds() * 1000 < 400)):
        testCode = 'pass'
        print('测试通过，请求正常参数:' + str(url))
        print('单接口性能测试通过, 响应时间为:' + str(getResponsedata.elapsed.total_seconds() * 1000) + 'ms')
    else:
        testCode = 'failed'
        print('测试失败，状态码非200或者响应时间超过400ms')
        print('状态码:' + str(getResponsedata.status_code))
        print('响应时间:' + str(getResponsedata.elapsed.total_seconds() * 1000) + 'ms')
        print('响应信息:' + str(getResponsedata.text))
    return testCode, testResult

# 封装新get接口正常&&异常请求参数测试方法
def getErrorRequestTest(url, testurl, headers):
    # 定义一个测试结果list，用于返回测试方法最终的结果
    testResultList = []
    # 定义一个testcodelist,用于遍历所有用例的pass和failed情况，只要有一个failed，总用例就failed
    testCodeList = []
    print('测试GET接口:' + url)

    # 正常业务参数
    getResponsedata = requests.get(url, headers=headers)
    testResult = '请求参数:' + str(url) + ',状态码:' + str(getResponsedata.status_code) + ',响应时间:' + str(getResponsedata.elapsed.total_seconds() * 1000)
    # 如果测试接口的状态码不是200并且响应时间小于400ms就写入failed，如果是就pass，并且写入testcode
    if ((getResponsedata.status_code in (200, 403)) & (getResponsedata.elapsed.total_seconds() * 1000 < 400)):
        testCode = 'pass'
        print('测试通过，请求正常参数:' + str(url))
        print('状态码:' + str(getResponsedata.status_code))
        print('单接口性能测试通过, 响应时间为:' + str(getResponsedata.elapsed.total_seconds() * 1000) + 'ms')
    else:
        testCode = 'failed'
        print('测试失败，状态码非200或者响应时间超过400ms')
        print('状态码:' + str(getResponsedata.status_code))
        print('响应时间:' + str(getResponsedata.elapsed.total_seconds() * 1000) + 'ms')
        print('响应信息:' + str(getResponsedata.text))
        print('\n')
    testCodeList.append(testCode)
    testResultList.append(testResult)  # 最后返回的测试结果list

    # 异常业务参数
    print('--------测试异常参数--------')
    # 定义一个测试异常参数集合
    testdatalist = [
        'teststr',
        '',
        '~!@#$%',
        '中 文',
        88888888,
        -888888,
        [1, 2, 3],
        ['test1', 'test2', 'test3'],
        [],
        'longstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstr',
        123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789
    ]
    testParameterNum = testurl.count("{}")  # 统计URL中{}出现的次数，用testParameterNum接收统计
    formatNum = []  # 定义一个格式化参数数量的list用于接收需要格式化几次，有几个{}就要格式化几次

    # 开始循环调用异常接口
    for num in range(0, len(testdatalist)):
        formatNum.clear()
        for i in range(testParameterNum):
            formatNum.append(testdatalist[num])
        getResponsedata = requests.get(testurl.format(*formatNum), headers=headers)
        testResult = '请求参数:' + str(testurl.format(*formatNum)) + '状态码:' + str(getResponsedata.status_code) + ',响应时间:' + str(getResponsedata.elapsed.total_seconds() * 1000)
        # 如果测试接口的状态码不是200就写入failed，如果是就pass，并且写入testcode
        if (getResponsedata.status_code in (200, 403, 404)):
            testCode = 'pass'
            print('第' + str(num + 1) + '条异常业务testcase，测试通过')
            print('状态码:' + str(getResponsedata.status_code))
            print(' 请求异常参数:' + str(testurl.format(*formatNum)))
        else:
            testCode = 'failed'
            print('第' + str(num + 1) + '条异常业务testcase，测试失败')
            print(' 请求异常参数:' + (testurl.format(*formatNum)))
            print('测试失败，状态码非200或者响应时间超过400ms')
            print('状态码:' + str(getResponsedata.status_code))
            print('响应信息:' + str(getResponsedata.text))
            print('响应时间:' + str(getResponsedata.elapsed.total_seconds() * 1000) + 'ms')
            testCodeList.append(testCode)
            testResultList.append(testResult)  # 最后返回的测试结果list
        if 'failed' not in testCodeList:
            testFinalCode = 'pass'
        else:
            testFinalCode = 'failed'
        print('\n')
    return testFinalCode, testResultList

# 封装put接口正常&&异常请求参数测试方法
def putRequestTest(url, headers, putdata):
    # 定义一个测试结果list，用于返回测试方法最终的结果
    testResultList = []
    # 定义一个testcodelist,用于遍历所有用例的pass和failed情况，只要有一个failed，总用例就failed
    testCodeList = []
    # 定义一个测试异常参数集合
    testdatalist = [
        'teststr',
        '',
        '~!@#$%',
        '中 文',
        88888888,
        -888888,
        [1, 2, 3],
        ['test1', 'test2', 'test3'],
        ['', '', ''],
        [],
        'longstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstr',
        123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789
    ]
    print('测试PUT接口:' + url)

    # 正常业务参数
    print('--------测试正常业务参数--------')
    putResponsedata = requests.put(url, data=json.dumps(putdata), headers=headers)
    testResult = '请求参数:' + str(putdata) + ',状态码:' + str(putResponsedata.status_code) + ',响应时间:' + str(putResponsedata.elapsed.total_seconds()*1000)
    # 如果测试接口的状态码不是200并且响应时间小于400ms就写入failed，如果是就pass，并且写入testcode
    if ((putResponsedata.status_code in (200, 403)) & (putResponsedata.elapsed.total_seconds()*1000 < 400)):
        testCode = 'pass'
        print('正常业务参数测试通过，请求正常参数:' + str(putdata))
        print('单接口性能测试通过, 响应时间为:' + str(putResponsedata.elapsed.total_seconds()*1000) + 'ms')
        print('\n')
    else:
        testCode = 'failed'
        print('测试失败，状态码非200或者响应时间超过400ms')
        print('状态码:' + str(putResponsedata.status_code))
        print('响应时间:' + str(putResponsedata.elapsed.total_seconds() * 1000) + 'ms')
        print('\n')
    testCodeList.append(testCode)
    testResultList.append(testResult)  # 最后返回的测试结果list

    if type(putdata) is list:
        # 异常业务参数putdata为list类型，举例：[1008,1006,888]
        print('--------测试putdata为list类型的异常参数--------')
        for num in range(0, len(testdatalist)):
            putErrorData = [testdatalist[num] for num in range(len(putdata))]  # 利用python列表生成式，生成测试put请求参数
            putResponsedata = requests.put(url, data=json.dumps(putErrorData), headers=headers)
            # print(putResponsedata.text)
            testResult = '请求参数:' + str(putErrorData) + '状态码:' + str(putResponsedata.status_code) + ',响应时间:' + str(
                putResponsedata.elapsed.total_seconds() * 1000)
            # 如果测试接口的状态码不是200就写入failed，如果是就pass，并且写入testcode
            if (putResponsedata.status_code in (200, 403)):
                testCode = 'pass'
                print('第' + str(num + 1) + '条异常业务testcase，测试通过')
                print(' 请求异常参数:' + str(putErrorData))
            else:
                testCode = 'failed'
                print('第' + str(num + 1) + '条异常业务testcase，测试失败')
                print(' 请求异常参数:' + str(putErrorData))
                print('测试失败，状态码非200或者响应时间超过400ms')
                print('状态码:' + str(putResponsedata.status_code))
                print('响应时间:' + str(putResponsedata.elapsed.total_seconds() * 1000) + 'ms')
            testCodeList.append(testCode)
            testResultList.append(testResult)  # 最后返回的测试结果list
        print('\n')

        # 不传参数
        print('--------测试空参数--------')
        putdata = {}
        putResponsedata = requests.put(url, data=json.dumps(putdata), headers=headers)
        testResult = '请求参数:' + str(putdata) + '状态码:' + str(putResponsedata.status_code) + ',响应时间:' + str(
            putResponsedata.elapsed.total_seconds() * 1000)
        # 如果测试接口的状态码不是200就写入failed，如果是就pass，并且写入testcode
        if (putResponsedata.status_code in (200, 403)):
            testCode = 'pass'
            print('空参数测试通过')
            print('状态码:' + str(putResponsedata.status_code))
            print('请求空参数:' + str(putdata))
        else:
            testCode = 'failed'
            print('测试失败，状态码非200或者响应时间超过400ms')
            print('请求空参数:' + str(putdata))
            print('状态码:' + str(putResponsedata.status_code))
            print('响应时间:' + str(putResponsedata.elapsed.total_seconds() * 1000) + 'ms')
        testCodeList.append(testCode)
        testResultList.append(testResult)  # 最后返回的测试结果list
        # print(testCodeList) # 用于调试打印所有testcodelist中的状态是pass还是failed
        if 'failed' not in testCodeList:
            testFinalCode = 'pass'
        else:
            testFinalCode = 'failed'

    else:
        # 异常业务参数
        print('--------测试异常参数--------')
        for num in range(0, len(testdatalist)):
            keys = list(putdata.keys())
            putErrorData = dict.fromkeys(keys, testdatalist[num])
            putResponsedata = requests.put(url, data=json.dumps(putErrorData), headers=headers)
            # print(putResponsedata.text)
            testResult = '请求参数:' + str(putErrorData) + '状态码:' + str(putResponsedata.status_code) + ',响应时间:' + str(putResponsedata.elapsed.total_seconds()*1000)
            # 如果测试接口的状态码不是200就写入failed，如果是就pass，并且写入testcode
            if (putResponsedata.status_code in (200, 403)) :
                testCode = 'pass'
                print('第' + str(num + 1) + '条异常业务testcase，测试通过')
                print(' 请求异常参数:' + str(putErrorData))
            else:
                testCode = 'failed'
                print('第' + str(num + 1) + '条异常业务testcase，测试失败')
                print(' 请求异常参数:' + str(putErrorData))
                print('测试失败，状态码非200或者响应时间超过400ms')
                print('状态码:' + str(putResponsedata.status_code))
                print('响应时间:' + str(putResponsedata.elapsed.total_seconds() * 1000) + 'ms')
            testCodeList.append(testCode)
            testResultList.append(testResult)  # 最后返回的测试结果list
        print('\n')

        # 不传参数
        print('--------测试空参数--------')
        putdata = {}
        putResponsedata = requests.put(url, data=json.dumps(putdata), headers=headers)
        testResult = '请求参数:' + str(putdata) + '状态码:' + str(putResponsedata.status_code) + ',响应时间:' + str(putResponsedata.elapsed.total_seconds()*1000)
        # 如果测试接口的状态码不是200就写入failed，如果是就pass，并且写入testcode
        if (putResponsedata.status_code in (200, 403)):
            testCode = 'pass'
            print('空参数测试通过')
            print('状态码:' + str(putResponsedata.status_code))
            print('请求空参数:' + str(putdata))
        else:
            testCode = 'failed'
            print('测试失败，状态码非200或者响应时间超过400ms')
            print('请求空参数:' + str(putdata))
            print('状态码:' + str(putResponsedata.status_code))
            print('响应时间:' + str(putResponsedata.elapsed.total_seconds()*1000) + 'ms')
        testCodeList.append(testCode)
        testResultList.append(testResult)  # 最后返回的测试结果list
        # print(testCodeList) # 用于调试打印所有testcodelist中的状态是pass还是failed
        if 'failed' not in testCodeList:
            testFinalCode = 'pass'
        else:
            testFinalCode = 'failed'
    return testFinalCode, testResultList  # 返回两个参数，第一个表示测试状态，第二个表示测试结果list

# 封装delete接口正常&&异常请求参数测试方法
def deleteRequestTest(url, headers):
    # 定义一个测试结果list，用于返回测试方法最终的结果
    testResultList = []
    # 定义一个testcodelist,用于遍历所有用例的pass和failed情况，只要有一个failed，总用例就failed
    testCodeList = []
    print('测试GET接口:' + url)
    deleteResponsedata = requests.delete(url, headers=headers)
    testResult = '请求参数:' + str(url) + ',状态码:' + str(deleteResponsedata.status_code) + ',响应时间:' + str(deleteResponsedata.elapsed.total_seconds() * 1000)
    # 如果测试接口的状态码不是200并且响应时间小于400ms就写入failed，如果是就pass，并且写入testcode
    if ((deleteResponsedata.status_code in (200, 403)) & (deleteResponsedata.elapsed.total_seconds() * 1000 < 400)):
        testCode = 'pass'
        print('测试通过，请求正常参数:' + str(url))
        print('单接口性能测试通过, 响应时间为:' + str(deleteResponsedata.elapsed.total_seconds() * 1000) + 'ms')
    else:
        testCode = 'failed'
        print('测试失败，状态码非200或者响应时间超过400ms')
        print('状态码:' + str(deleteResponsedata.status_code))
        print('响应时间:' + str(deleteResponsedata.elapsed.total_seconds() * 1000) + 'ms')
        print('响应信息:' + str(deleteResponsedata.text))
    return testCode, testResult

# 封装新delete接口正常&&异常请求参数测试方法
def deleteErrorRequestTest(url, testurl, headers):
    # 定义一个测试结果list，用于返回测试方法最终的结果
    testResultList = []
    # 定义一个testcodelist,用于遍历所有用例的pass和failed情况，只要有一个failed，总用例就failed
    testCodeList = []
    print('测试GET接口:' + url)

    # 正常业务参数
    deleteResponsedata = requests.delete(url, headers=headers)
    testResult = '请求参数:' + str(url) + ',状态码:' + str(deleteResponsedata.status_code) + ',响应时间:' + str(deleteResponsedata.elapsed.total_seconds() * 1000)
    # 如果测试接口的状态码不是200并且响应时间小于400ms就写入failed，如果是就pass，并且写入testcode
    if ((deleteResponsedata.status_code in (200, 403)) & (deleteResponsedata.elapsed.total_seconds() * 1000 < 400)):
        testCode = 'pass'
        print('测试通过，请求正常参数:' + str(url))
        print('状态码:' + str(deleteResponsedata.status_code))
        print('单接口性能测试通过, 响应时间为:' + str(deleteResponsedata.elapsed.total_seconds() * 1000) + 'ms')
    else:
        testCode = 'failed'
        print('测试失败，状态码非200或者响应时间超过400ms')
        print('状态码:' + str(deleteResponsedata.status_code))
        print('响应时间:' + str(deleteResponsedata.elapsed.total_seconds() * 1000) + 'ms')
        print('响应信息:' + str(deleteResponsedata.text))
        print('\n')
    testCodeList.append(testCode)
    testResultList.append(testResult)  # 最后返回的测试结果list

    # 异常业务参数
    print('--------测试异常参数--------')
    # 定义一个测试异常参数集合
    testdatalist = [
        'teststr',
        '',
        '~!@#$%',
        '中 文',
        88888888,
        -888888,
        [1, 2, 3],
        ['test1', 'test2', 'test3'],
        [],
        'longstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstrlongstr',
        123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789
    ]
    testParameterNum = testurl.count("{}")  # 统计URL中{}出现的次数，用testParameterNum接收统计
    formatNum = []  # 定义一个格式化参数数量的list用于接收需要格式化几次，有几个{}就要格式化几次

    # 开始循环调用异常接口
    for num in range(0, len(testdatalist)):
        formatNum.clear()
        for i in range(testParameterNum):
            formatNum.append(testdatalist[num])
        deleteResponsedata = requests.delete(testurl.format(*formatNum), headers=headers)
        testResult = '请求参数:' + str(testurl.format(*formatNum)) + '状态码:' + str(deleteResponsedata.status_code) + ',响应时间:' + str(deleteResponsedata.elapsed.total_seconds() * 1000)
        # 如果测试接口的状态码不是200就写入failed，如果是就pass，并且写入testcode
        if (deleteResponsedata.status_code in (200, 403, 404)):
            testCode = 'pass'
            print('第' + str(num + 1) + '条异常业务testcase，测试通过')
            print('状态码:' + str(deleteResponsedata.status_code))
            print(' 请求异常参数:' + str(testurl.format(*formatNum)))
        else:
            testCode = 'failed'
            print('第' + str(num + 1) + '条异常业务testcase，测试失败')
            print(' 请求异常参数:' + (testurl.format(*formatNum)))
            print('测试失败，状态码非200或者响应时间超过400ms')
            print('状态码:' + str(deleteResponsedata.status_code))
            print('响应信息:' + str(deleteResponsedata.text))
            print('响应时间:' + str(deleteResponsedata.elapsed.total_seconds() * 1000) + 'ms')
            testCodeList.append(testCode)
            testResultList.append(testResult)  # 最后返回的测试结果list
        if 'failed' not in testCodeList:
            testFinalCode = 'pass'
        else:
            testFinalCode = 'failed'
        print('\n')
    return testFinalCode, testResultList