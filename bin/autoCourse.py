import time, os
from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
retryCount = 3
waitTime = 3
implicitlyWait = 30
# chromed-101.0.4951.67

class AutoHJTest():

    def __init__(self):
        driver = None

    def open(self, host='127.0.0.1', port=4723):
        # 打开WinAppDriver服务
        # 注意：如果手动开启，则可以注释掉
        # os.system(r'start "" /d "C:\Program Files\Windows Application Driver\"  "WinAppDriver.exe"')
        print("open_weixin")
        # 配置信息
        # 包含：平台名、系统、应用程序绝对路径
        desired_capabilities = {'platformName': 'Windows', 'deviceName': 'WindowsPC','automationName':'Windows',
                        'app': r"E:\tool\HuJiangClass\HujiangClass.exe"}

        try:
            # 连接WinAppDriver服务，打开目标软件
            self.driver = webdriver.Remote('http://{}:{}'.format(host, port), desired_capabilities)
            # self.weixin_driver = self.driver
        except Exception as e:
            raise AssertionError(e)

    def goto_course_page(self):
        self.driver.find_elements(By.NAME, '第19課（2）スキー').click()
        # self.driver.find_element(By.NAME,'首页').click()
        time.sleep(3)
        # jrbj = self.driver.find_elements(By.NAME, '进入班级')
        # # self.driver.find_element(By.NAME, '进入班级').click()
        # jrbj[1].click()
        # time.sleep(3)

if __name__ == "__main__":
    hj_tool = AutoHJTest()
    hj_tool.open()
    hj_tool.goto_course_page()
