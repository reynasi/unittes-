import time
import traceback
import unittest

from selenium import webdriver
from BeautifulReport import BeautifulReport

from zhangjinjin.test.case.common import *


class PrepareLessonsTest(unittest.TestCase):

    def save_img(self, img_name):
        driver.get_screenshot_as_file('{}/{}.png'.format(getimg(), img_name))

    @classmethod
    def setUpClass(cls):
        global driver
        project = 'teacher4'
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options=options)
        try:
            new_tab_cn(driver, project)
            is_element_exist(driver, '//*[@id="root"]/div/div[1]/div/div[1]/p/b', 'teacher4登录页')
            mobil_xpath = "//*[@id='username']"
            code_xpath = "//*[@id='code']"
            branch = is_branch_exist(driver, '//*[@id="root"]/div/div[1]/div/form', project)
            if branch == 'true':
                obvious_wait_click(driver, '//*[@id="root"]/div/div[1]/div/form/div[1]/div/div/div/div/span', '选择校区')
                obvious_wait_click(driver, '/html/body/div[4]/div/div/div/ul/li[1]', '选择总校区')
                btn_xpath = '//*[@id="root"]/div/div[1]/div/form/div[4]/button'
            else:
                btn_xpath = "//*[@id='root']/div/div[1]/div/form/div[3]/button/span"
            login(driver, mobil_xpath, code_xpath, btn_xpath, 'teacher4')
        except:
            traceback.print_exc()

    @classmethod
    def tearDownClass(cls):
        try:
            driver.close()
            driver.quit()
        except:
            traceback.print_exc()

    @BeautifulReport.add_test_img('test_create_task')
    def test_create_task(self):
        """测试备课系统创建新题型卡是否正常"""
        second_num = 0
        first_num = 0
        r = 'false'
        try:
            obvious_wait_click(driver, '//div[@class="prepare"]', "备课系统")
            is_element_exist(driver, '//*[@id="root"]/div/header/div[1]/div[2]/span[1][contains(text(),'
                                     '"备课系统")]', "备课系统")
            obvious_wait_click(driver, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div['
                                       '2]/div/div/a', '进入课程')

            first_num = get_elements(driver, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[3]/div/div[3]/div['
                                             '1]/div/div/div', '创建卡前查询任务卡数量')
            obvious_wait_click(driver, '//div[contains(@class,"lTaskCard-type-add")]', '添加任务卡弹窗')

            obvious_wait_click(driver, '//div[contains(@class, "lTaskCardTypes")]/div[last()]/a', '添加新题型卡')

            while is_element_exist2(driver, '//span[contains(@class, "ant-tree-noline_close")]', '查询展开知识点树元素是否存在') == \
                    'true':
                obvious_wait_click(driver, '//span[contains(@class, "ant-tree-noline_close")]', '展开知识点树')
            obvious_wait_click(driver, '//ul[contains(@class, "ant-tree-child-tree ant-tree-child-tree-open")]/li['
                                       'last()-1]/a', '点击知识点列表')

            obvious_wait_click(driver, '//*[@class="addQuestions"]/div/div/div/div/div/div/table/tbody/tr['
                                       '1]/td/span/label/span', '选择题目1')
            obvious_wait_click(driver, '//*[@class="bodyWrap"]/div[2]/button[2]', '下一步')
            obvious_wait_click(driver, '//*[@class="stepWrap"]/div[2]/div[2]/button', '确定')
            result = is_element_exist(driver, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[3]/div/div[3]/div['
                                              '1]/div/div/div/div[last()-1]/div/div/div/div/div[2][contains(text(),'
                                              '"新题型卡")]', '判定最后一个是否是新题型卡')
            obvious_wait_click(driver, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[3]/div/div[3]/div['
                                       '1]/div/div/div/div[32]/div/a', '预览')
            obvious_wait_click(driver, '//*[@class="ant-modal-close"]', '关闭预览弹窗')
            # time.sleep(1)
            second_num = get_elements(driver, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[3]/div/div[3]/div['
                                              '1]/div/div/div', '创建卡后查询任务卡数量')
        except:
            traceback.print_exc()
        finally:
            if (first_num == (second_num-1)) & (result == 'true'):
                self.r = 'true'
            self.assertEqual(self.r, 'true')

    @BeautifulReport.add_test_img('test_verify_task')
    def test_verify_task(self):
        """测试审核新题型卡是否正常"""
        result = 'false'
        try:
            # obvious_wait_click(driver, '//*[@id="root"]/div/header/div[1]/div[1]/div[2]/div[2]', "备课系统")
            # is_element_exist(driver, '//*[@id="root"]/div/header/div[1]/div[2]/span[1][contains(text(),'
            #                          '"备课系统")]', "备课系统")
            # obvious_wait_click(driver, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div['
            #                            '1]/div/div/a', '进入课程')

            obvious_wait_click(driver, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[1]/div/div/a', '点击更多')
            obvious_wait_click(driver, '//*[@class="ant-dropdown ant-dropdown-placement-bottomCenter"]/ul/li[1]',
                               '触发提交审核弹窗')
            is_have_verify(driver)

            obvious_wait_sendkeys(driver, '//*[@id="marks"]', '测试提交审核新题型卡', '输入提交信息')
            obvious_wait_click(driver, '//*[@class="ant-form-item-control-wrapper"]/div/div/button[2]', '确认提交审核')
            obvious_wait_click(driver, '//*[@id="2$Menu"]/li[4]', '点击课程审核')
            obvious_wait_click(driver, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div['
                                       '1]/div/div/a/div[1]/div[1]', '进入审核课程')
            obvious_wait_click(driver, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[4]/div/div['
                                       '3]/div/div/div/div/div[last()-1]/div/div', '预览最后一个新题型卡')
            is_element_exist(driver, '//*[@class="wModalContent"]', '判断是否出现预览弹窗')
            obvious_wait_click(driver, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[1]/div/div/div/button[1]',
                               '触发审核通过弹窗')
            obvious_wait_click(driver, '//*[@class="ant-confirm-body-wrapper"]/div[2]/button[2]',
                               '审核通过')
            obvious_wait_click(driver, '//*[@id="2$Menu"]/li[2]', '进入学校课程')
            obvious_wait_click(driver, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[3]/div/div[1]/div/div['
                                       '1]/div/div/a/div[1]/div[1]', '进入课程')
            obvious_wait_click(driver, '//*[@id="root"]/div/div/main/div/div[1]/div/div/div[3]/div/div['
                                       '3]/div/div/div/div/div[last()-1]/div/div/div', '预览最后一个新题型卡')
            result = is_element_exist(driver, '//*[@class="wModalContent"]', '判断是否出现预览弹窗')
        except:
            traceback.print_exc()
        finally:
            self.assertEqual(result, 'true')


if __name__ == '__main__':
    unittest.main()
