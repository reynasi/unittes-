# import os
import unittest
import sys
sys.path.append('/opt/uitest/')
sys.path.append('/opt/uitest/zhangjinjin/')
sys.path.append('/opt/uitest/zhangjinjin/test/case/common/')
from BeautifulReport import BeautifulReport
from zhangjinjin.test.case.common import *


if __name__ == '__main__':
    report_path = getreport()
    case_dirs = getcase()
    print(case_dirs)
    discover = unittest.defaultTestLoader.discover(case_dirs, "*Test.py")
    run = BeautifulReport(discover)
    run.report(filename='test测试报告', description='test测试用例', report_dir=report_path)



