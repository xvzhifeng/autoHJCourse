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
driverPath = r"G:\code\gitee\xy\XYBank\bin\driver\chromedriver"

class AutoWeChatTest():

    def __init__(self):
        driver = None

    def find(self, by, locate):
        print("find")
        time.sleep(waitTime)
        count = 0
        while True:
            isExist = self.is_exist_element(by, locate)
            if not isExist and count <= retryCount:
                # log.logger.debug("find element by " + by + " location: " + locate + " . retry count " + str(count))
                print("find element by " + by + " location: " + locate + " . retry count " + str(count))
                time.sleep(waitTime)
                count += 1
            elif isExist:
                return self.driver.find_element(by, locate)
            else:
                # log.logger.debug("current element not found, element by " + by + " location: " + locate)
                print("current element not found, element by " + by + " location: " + locate)
                exit(1)

    def open_weixin(self, host='127.0.0.1', port=4723):
        # 打开WinAppDriver服务
        # 注意：如果手动开启，则可以注释掉
        # os.system(r'start "" /d "C:\Program Files\Windows Application Driver\"  "WinAppDriver.exe"')
        print("open_weixin")
        # 配置信息
        # 包含：平台名、系统、应用程序绝对路径
        desired_capabilities = {'platformName': 'Windows', 'deviceName': 'WindowsPC','automationName':'Windows',
                        'app': r"E:\tool\WeChat\WeChat.exe"}

        try:
            # 连接WinAppDriver服务，打开目标软件
            self.driver = webdriver.Remote('http://{}:{}'.format(host, port), desired_capabilities)
            # self.weixin_driver = self.driver
        except Exception as e:
            raise AssertionError(e)


    # 给文件传输助手发送一条信息
    def send_msg(self, element_name, msg):
        """
        :param element_name:元素name值
        :param msg:
        :return:
        """
        # 通过name属性，找到目标元素
        chat_element = self.driver.find_element(By.NAME, element_name)

        # 点击元素，进入聊天界面
        chat_element.click()

        # 找到输入框，并输入
        self.driver.find_element(By.NAME, "输入").send_keys(msg)
        time.sleep(5)
        self.driver.find_element(By.NAME, "sendBtn").click()
        self.driver.find_element(By.NAME, "输入").send_keys(msg)
        time.sleep(5)
        self.driver.find_element(By.NAME, "sendBtn").click()
        self.driver.find_element(By.NAME, "输入").send_keys(msg)
        time.sleep(5)
        self.driver.find_element(By.NAME, "sendBtn").click()
        # 点击右下角的发送，发送消息出去
        self.driver.find_element(By.NAME, "sendBtn").click()

if __name__ == "__main__":
    weChat_tool = AutoWeChatTest()
    weChat_tool.open_weixin()
    weChat_tool.send_msg('圆滚滚的进厂人', "you are dog!")