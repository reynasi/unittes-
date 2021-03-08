# import os
import unittest
import sys

sys.path.append('/opt/uitest/')
sys.path.append('/opt/uitest/zhangjinjin/')
sys.path.append('/opt/uitest/zhangjinjin/go/case/common/')
from BeautifulReport import BeautifulReport
from zhangjinjin.go.case.common import getreport, getcase

if __name__ == '__main__':
    report_path = getreport()
    case_dirs = getcase()
    discover = unittest.defaultTestLoader.discover(case_dirs, "*Test.py")
    run = BeautifulReport(discover)
    run.report(filename='公众号测评', description='公众号测评', report_dir=report_path)
