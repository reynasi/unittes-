import configparser
import os
import sys
import traceback

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append('/opt/')
sys.path.append('/opt/uitest/shuping/common/config/config.ini/')

class Common:

    # def getPath(self):
    #     try:
    #         root_path = os.path.dirname(os.path.abspath('.') + '/config/chromedriver/chromedriver')
    #         return root_path
    #     except:
    #         print("获取path失败!")

    def getUrl(self, TypeUrl, urlName):
        try:
            config = configparser.ConfigParser()
            platf = sys.platform
            print("platform:" + platf)
            if platf != 'darwin':
                urlconfig = '/opt/uitest/shuping/common/config/config.ini'
            else:
                # 服务器配置文件路径地址
                urlconfig = os.path.dirname(os.path.abspath('.') + '/common/config/config.ini/config.ini')
            config.read(urlconfig)
            urlstr = ""
            urlstr = config.get(TypeUrl, urlName)
        except:
            print("获取url失败!")
        return urlstr

    def getToken(self, browser, tokenKey):
        try:
            authorization=""
            # 获取token
            stoken = ""
            stokenspr = []
            stoken = browser.execute_script(tokenKey)
            stoken.encode('utf-8')
            # strstoken = str(stoken)
            stokenspr = stoken.split('[\"', 2)
            studenttoken = str(stokenspr[1]).split('\",', 2)
            authorization = "Bearer" + " " + str(studenttoken[0])
        except Exception as e:
            traceback.print_exc()
            print(e)
        return authorization

    # 判断元素是否存在的方法
    def isElementExist(self, browser, element):
        flag = True
        try:
            if browser.find_element_by_xpath(element):
                return flag
        except:
            flag = False
            return flag

    # 判断元素s
    def isElementsExist(self, browser, xpath):
        flag = True
        try:
            locator = (By.XPATH, xpath)
            element = WebDriverWait(browser, 3).until(EC.presence_of_all_elements_located(locator))
            return flag
        except:
            flag = False
            return flag
            traceback.print_exc()

    # 获取元素后点击
    def findElementClick(self, browser, locator):
        try:
            browser.implicitly_wait(3)
            element = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, locator)),
                                                      message="等待元素失败")
            element.click()
            browser.implicitly_wait(5)
        except:
            traceback.print_exc()
            print("点击" + locator + "元素失败！")

    # 获取元素后点击
    def findElementClickLongTime(self, browser, locator):
        try:
            browser.implicitly_wait(18)
            element = WebDriverWait(browser, 18).until(EC.presence_of_element_located((By.XPATH, locator)),
                                                      message="等待元素失败")
            element.click()
            browser.implicitly_wait(5)
        except:
            traceback.print_exc()
            print("点击" + locator + "元素失败！")

    def findElementActionClick(self, browser, locator):
        try:
            action = ActionChains(browser)
            above = browser.find_element_by_xpath(locator)
            action.move_to_element(above).perform()
            action.click(above).perform()
        except:
            traceback.print_exc()
            print("点击Action元素" + locator + "失败！\n")

    def findElementAction(self, browser, locator):
        try:
            action = ActionChains(browser)
            above = browser.find_element_by_xpath(locator)
            action.move_to_element(above).perform()
        except:
            traceback.print_exc()
            print("定位到Action元素" + locator + "失败！\n")

    def findElementActionDoubleClick(self, browser, locator):
        try:
            action = ActionChains(browser)
            above = browser.find_element_by_xpath(locator)
            action.double_click(above).perform()
        except:
            traceback.print_exc()
            print("双击元素" + locator + "失败！\n")

    def findElementActionContextClick(self, browser, locator):
        try:
            action = ActionChains(browser)
            above = browser.find_element_by_xpath(locator)
            action.context_click(above).perform()
        except:
            traceback.print_exc()
            print("右击元素" + locator + "失败！\n")

    def findElementActionDragAndDrop(self, browser, locator):
        try:
            action = ActionChains(browser)
            above = browser.find_element_by_xpath(locator)
            action.drag_and_drop(above).perform()
        except:
            traceback.print_exc()
            print("拖动元素" + locator + "失败！\n")


    def isElementExist2(self, browser, xpath):
        flag = True
        try:
            locator = (By.XPATH, xpath)
            element = WebDriverWait(browser, 3).until(EC.presence_of_element_located(locator))
            return flag
        except:
            flag = False
            return flag
            traceback.print_exc()

    def isElementExist3(self, browser, xpath):
        flag = True
        try:
            browser.implicitly_wait(1)
            locator = (By.XPATH, xpath)
            element = WebDriverWait(browser, 1).until(EC.presence_of_element_located(locator))
            browser.implicitly_wait(5)
            return flag
        except:
            flag = False
            return flag
            traceback.print_exc()

    def getElementsTextExpectStr(self, browser, xpath, expectStr):
        tempList=[]
        try:
            elements = browser.find_elements_by_xpath(xpath)
            for i in range(len(elements)):
                if elements[i].text != "" and elements[i].text == expectStr:
                    tempList.append(elements[i].text)
            return tempList
        except:
            return tempList
            traceback.print_exc()
            print("查找列表元素的text" + locator + "失败！\n")

    def getElementsText(self, browser, xpath):
        tempList=[]
        try:
            elements = browser.find_elements_by_xpath(xpath)
            for i in range(len(elements)):
                if elements[i].text != "":
                    tempList.append(elements[i].text)
            return tempList
        except:
            return tempList
            traceback.print_exc()
            print("查找列表元素的text" + locator + "失败！\n")


    def getDirectPath(self):
        directList = []
        try:
            platf = sys.platform
            print("platform:" + platf)
            if platf != 'darwin':
                report_dir = "/opt/uitest/report"
                img_path = "/opt/uitest/img"
            else:
                report_dir = "./report"
                img_path = "./img"
            directList.append(report_dir)
            directList.append(img_path)
            return directList
        except:
            return directList
            traceback.print_exc()
            print("" + locator + "失败！\n")



# if __name__ == '__main__':
#     url2 = Common.getUrl("TypeUrl", "teacher4Url")
#     print("url2: " + url2)


