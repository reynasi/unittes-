# import os
import unittest
import sys

sys.path.append('/opt/uitest/')
sys.path.append('/opt/uitest/zhangjinjin/')
sys.path.append('/opt/uitest/zhangjinjin/render/case/common/')

from BeautifulReport import BeautifulReport

from zhangjinjin.render.case.teacher4Test import teacher4Test
from zhangjinjin.render.case.common import getreport, getcase

if __name__ == '__main__':
    report_path = getreport()
    case_dirs = getcase()
    discover = unittest.defaultTestLoader.discover(case_dirs, "*Test.py")
    run = BeautifulReport(discover)
    run.report(filename='render测试报告', description='render测试用例', report_dir=report_path)

# if __name__ == '__main__':
#     testsuit = unittest.TestSuite()
#     testsuit.addTests(unittest.makeSuite(teacher4Test))
#     run = BeautifulReport(testsuit)
#     run.report(filename='teacher4测试报告', description='teacher4测试用例', report_dir=getreport())



