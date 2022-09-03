import time, os
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from playsound import playsound
import subprocess as sp
import bin.ope.operator as operator
import bin.lib.lib_exception as exp
import bin.lib.lib_log as log

retryCount = 3
waitTime = 3
implicitlyWait = 30
# chromed-101.0.4951.67
driver = None


class AutoHJAppCourse():

    def __init__(self,account,passwd):
        self.driver = None
        self.practice_count = 1
        self.unkown_count = 1
        self.reboot_count = 1
        self.spide_count = 25
        self.open()
        self.width = self.driver.get_window_size()['width']
        self.height = self.driver.get_window_size()['height']
        self.play_course_name = '2019.7N3真题词汇'
        self.account = account
        self.password = passwd

    def open(self, host='127.0.0.1', port=4723):
        # 打开WinAppDriver服务
        # 注意：如果手动开启，则可以注释掉
        # os.system(r'start "" /d "C:\Program Files\Windows Application Driver\"  "WinAppDriver.exe"')
        log.logger.debug("open_HJ")
        # 配置信息
        # 包含：平台名、系统、应用程序绝对路径
        desired_capabilities = {'platformName': 'Android', 'deviceName': '127.0.0.1:21503',
                                'appPackage': 'com.hujiang.hjclass',
                                'appActivity': "com.hujiang.hjclass.activity.SplashActivity"}

        try:
            # 连接WinAppDriver服务，打开目标软件
            self.driver = webdriver.Remote('http://{}:{}/wd/hub'.format(host, port), desired_capabilities)
            # self.weixin_driver = self.driver
        except Exception as e:
            raise AssertionError(e)
            pass

    def go_course(self):
        try:
            self.open()
            time.sleep(3)
            el1 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/btn_ok")
            el1.click()
            time.sleep(3)
            el2 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/tv_start_permission_request_dialog")
            el2.click()
            time.sleep(23)
            el5 = self.driver.find_element(by=By.XPATH,
                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.widget.Button")
            el5.click()
            time.sleep(3)
            el6 = self.driver.find_element(by=By.XPATH,
                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]/android.widget.EditText")
            el6.send_keys(self.account)
            time.sleep(3)
            el7 = self.driver.find_element(by=By.XPATH,
                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View[2]/android.widget.EditText")
            el7.send_keys(self.password)
            time.sleep(3)
            el8 = self.driver.find_element(by=By.XPATH,
                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.widget.Button[1]")
            el8.click()
            time.sleep(3)
            el9 = self.driver.find_element(by=By.XPATH,
                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[7]")
            el9.click()
            el9.click()
            time.sleep(3)
            el10 = self.driver.find_element(by=By.XPATH,
                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[6]/android.view.View/android.widget.Button[1]")
            el10.click()
            time.sleep(3)
            el11 = self.driver.find_element(by=By.XPATH,
                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.widget.Button[1]")
            el11.click()
            time.sleep(3)
            el12 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/img_myclass")
            el12.click()
            time.sleep(3)
            el13 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/btn_left_common_dialog")
            el13.click()
            time.sleep(3)
            el14 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/action_btn")
            el14.click()
            time.sleep(3)
            el15 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/tv_start_btn")
            el15.click()
            time.sleep(3)
            el16 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/iv_new_class_index_guide_course")
            el16.click()
            time.sleep(3)
            el17 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/iv_new_class_index_guide_service")
            el17.click()
            time.sleep(3)
            el18 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/dont_add_teacher_wechat")
            el18.click()
            time.sleep(3)
            el19 = self.driver.find_element(by=By.XPATH,
                                            value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ImageView")
            el19.click()
            time.sleep(3)
            # 点击服务
            el20 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/topTitle_tool")
            el20.click()
            # 点击课程
            el21 = self.driver.find_element(by=By.XPATH,
                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView")
            el21.click()
            sleep(3)
            flag = True
        except Exception:
            flag = False
        return flag

    def always_study(self):
        try:
            while True:
                sleep(5)
                list_lesson_detail = self.driver.find_elements(By.ID,
                                                               value='com.hujiang.hjclass:id/item_text')
                sleep(2)
                # text = list_lesson_detail[0].find_element(By.ID, 'com.hujiang.hjclass:id/item_text').text
                begin = False
                current = self.play_course_name
                for lesson in list_lesson_detail:
                    if self.isElement(By.ID, "com.hujiang.hjclass:id/wx_authorization_title"):
                        self.driver.find_element(By.ID, "com.hujiang.hjclass:id/btn_close").click()
                        sleep(2)
                    # if not self.isElement_from_element(lesson,By.ID, 'com.hujiang.hjclass:id/item_text'):
                    #     continue
                    # lesson = lesson.find_element(By.ID, 'com.hujiang.hjclass:id/item_text')
                    text = lesson.text
                    if "测试" in text:
                        continue
                    log.logger.info("当前寻找的课程 {0}".format(text))
                    if self.play_course_name in text:
                        # 开始学习
                        begin = True
                        lesson.click()
                        self.start_course()
                    elif begin:
                        # 学习
                        lesson.click()
                        self.start_course()
                        current = text
                    else:
                        # 继续寻找需要学习的课程
                        pass
                    sleep(1)
                self.play_course_name = current
                self.spide_lesson()
                sleep(3)
            flag = True
        except Exception as e:
            flag = False
        return flag

    def process(self):

        while not self.go_course():
            pass
        sleep(3)
        for i in range(self.spide_count):
            self.spide_lesson()
            sleep(3)
        while not self.always_study():
            # study
            self.go_course()
            for i in range(self.spide_count):
                self.spide_lesson()
                sleep(3)
            pass
        # while True:
        #     sleep(5)
        #     list_lesson_detail = self.driver.find_elements(By.ID,
        #                                                    value='com.hujiang.hjclass:id/item_text')
        #     sleep(2)
        #     # text = list_lesson_detail[0].find_element(By.ID, 'com.hujiang.hjclass:id/item_text').text
        #     begin = False
        #     current = self.play_course_name
        #     for lesson in list_lesson_detail:
        #         if self.isElement(By.ID,"com.hujiang.hjclass:id/wx_authorization_title"):
        #             self.driver.find_element(By.ID,"com.hujiang.hjclass:id/btn_close").click()
        #             sleep(2)
        #         # if not self.isElement_from_element(lesson,By.ID, 'com.hujiang.hjclass:id/item_text'):
        #         #     continue
        #         # lesson = lesson.find_element(By.ID, 'com.hujiang.hjclass:id/item_text')
        #         text = lesson.text
        #         if "单元测试" in text:
        #             continue
        #         log.logger.debug(text)
        #         if self.play_course_name in text:
        #             # 开始学习
        #             begin = True
        #             lesson.click()
        #             self.start_course()
        #         elif begin:
        #             # 学习
        #             lesson.click()
        #             self.start_course()
        #             current = text
        #         else:
        #             # 继续寻找需要学习的课程
        #             pass
        #         sleep(3)
        #     self.play_course_name = current
        #     self.spide_lesson()
        #     sleep(3)
        # time.sleep(3)

    def get_skip_pratice(self):
        # 跳过的标志
        return True

    def handle_practice(self):
        log.logger.debug('handle practice {0}'.format(self.practice_count))
        self.reboot_count += 1
        self.practice_count += 1
        self.unkown_count = 1
        if self.practice_count >= 3:
            self.skip_spacial_practice()
        elif self.practice_count >= 20:
            log.logger.debug('handle practice {0}, send email'.format(self.practice_count))
            operator.send_email()
            try:
                playsound('../resource/mp3/快来做题啊.mp3')
            except Exception as e:
                log.logger.error(" ../resource/mp3/快来做题啊.mp3 语音播放失败")
            sleep(3)

    def handle_unkown(self):
        self.reboot_count += 1
        self.practice_count = 1
        self.unkown_count += 1
        if self.unkown_count >= 13:
            operator.send_email()
            try:
                playsound('../resource/mp3/出现未知错误.mp3')
            except:
                log.logger.error(" ../resource/mp3/出现未知错误.mp3 语音播放失败")
            sleep(3)

    def start_course(self):

        sleep(3)
        log.logger.debug("start_course")
        self.set_2x()
        while True:
            sleep(15)
            try:
                # todo 中间有可能出现课程评价的弹窗，需要判断
                if self.is_practice_not_study() or self.is_practice_study():
                    self.handle_practice()
                    # 练习
                    if self.get_skip_pratice():
                        sleep(2)
                        self.skip_practice()
                    else:
                        sleep(10)
                        continue
                elif self.is_play_page():
                    self.reboot_count = 0
                    if self.is_complete():
                        log.logger.debug("already complete")
                        self.exit_play()
                        break
                    if self.judge_is_pause():
                        self.click_pause()
                        time.sleep(3)
                elif self.is_course_valuate_page():
                    self.handle_unkown()
                    # try:
                    #     playsound('../resource/mp3/快来帮帮我.mp3')
                    # except Exception:
                    #     pass
                    sleep(3)
                    self.driver.find_element(By.ID, "com.hujiang.hjclass:id/btn_exit").click()
                else:
                    self.reboot_count += 1
                    # 未知情况
                    self.handle_unkown()
                    if self.unkown_count > 3:
                        try:
                            playsound('../resource/mp3/出现未知错误.mp3')
                        except Exception:
                            pass
                    sleep(3)
            except Exception as e:
                self.reboot_count += 1
                log.logger.error(e)
            if self.reboot_count >= 50:
                raise exp.CycleError('强制重启')
        sleep(10)

    def is_course_valuate_page(self):
        if self.isElement(By.XPATH, "//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[5]"):
            return True
        else:
            return False

    def spide(self, x, y, nx, ny):
        """
            move to new lesson
        :return:
        """
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(nx, ny)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def spide_lesson(self):
        self.spide(self.width / 2, self.height * 2 / 3, self.width / 2, self.height / 3)

    def exit_play(self):
        log.logger.debug("exit_play")
        if self.isElement(By.ID, "com.hujiang.hjclass:id/btn_exit_play"):
            pass
        else:
            self.click(self.width / 2, self.height / 2)
        el15 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/btn_exit_play")
        el15.click()

    def is_play_page(self):
        log.logger.debug("judge whether play page ?")
        sleep(5)
        if self.isElement(By.ID, "com.hujiang.hjclass:id/tv_play_time"):
            pass
        else:
            self.click(self.width / 2, self.height / 2)
            time.sleep(1)
        if self.isElement(By.ID, "com.hujiang.hjclass:id/tv_play_time"):
            return True
        else:
            return False

    def is_complete(self):
        sleep(5)
        log.logger.debug('is_complete ?')
        if self.isElement(By.ID, "com.hujiang.hjclass:id/tv_play_time"):
            pass
        else:
            self.click(self.width / 2, self.height / 2)
            time.sleep(2)
        # 进度条信息 text 01:34/20:54
        els1 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/tv_play_time")
        log.logger.debug(els1.text)
        date1 = els1.text.split('/')
        log.logger.debug(date1[0] + " " + date1[1])
        time.sleep(2)
        return date1[0] == date1[1]

    # todo 习题判断有误
    def is_practice_not_study(self):
        log.logger.debug("is_practice_not_study")
        if self.isElement(By.XPATH,
                          "//android.view.View[2]/android.view.View[2]/android.view.View[3]/android.view.View/android.view.View[1][@text(),'下一题']"):
            return True
        else:
            return False

    def is_practice_study(self):
        log.logger.debug("is_practice_study")
        if self.isElement(By.XPATH,
                          "//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]"):
            return True
        else:
            return False

    def skip_practice(self):
        """
        click practice page skip and confirmskip
        :return:
        """
        log.logger.debug("skip_practice")
        if self.is_practice_not_study():
            el13 = self.driver.find_elements(by=By.XPATH,value="//android.view.View[2]/android.view.View[1]/android.view.View[2]")[0]
            el13.click()
            time.sleep(2)
            try:
                self.driver.find_element(by=By.XPATH,
                                         value="//android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
            except Exception as e:
                log.logger.error(e)
            if self.is_practice_not_study():
                try:
                    el14 = self.driver.find_element(by=By.XPATH,
                                                    value="//android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]")
                    el14.click()
                except Exception as e:
                    log.logger.error(e)
            # self.driver.find_element(By.XPATH,"//*[@text(),'确认跳过']").click()

            time.sleep(2)
        else:
            try:
                el15 = self.driver.find_element(By.XPATH,
                                                "//android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]")
                el15.click()
            except Exception as e:
                self.driver.find_element_by_xpath(
                    "android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]").click()
                log.logger.error(e)
            time.sleep(2)

    def click_now_go(self):
        if self.isElement(By.ID, "com.hujiang.hjclass:id/right_button"):
            log.logger.debug("出现互动环节，点击现在就去！！！")
            el2 = driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/right_button")
            el2.click()

    def skip_spacial_practice(self):
        log.logger.debug("skip_spacial_practice")
        count = 0
        while self.isElement(By.XPATH, "//android.view.View[2]/android.view.View[2]/android.view.View[3]/android.view.View/android.view.View[1][@text(),'下一题']") and count < 50:
            count+=1
            w = self.driver.get_window_size()['width']
            h = self.driver.get_window_size()['height']
            self.spide(w * 2 / 3, h / 2, w / 3, h / 2)
            sleep(2)
            self.click_now_go()
            if self.isElement(By.XPATH, "//android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]"):
                try:
                    # click submit
                    self.driver.find_element_by_xpath("//android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]").click()
                    sleep(3)
                except Exception as e:
                    log.logger.error(e)
                if self.isElement(By.XPATH, "//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]"):
                    self.spide(w * 2 / 3, h / 2, w / 3, h / 2)
                else:
                    break
                try:
                    # click continue learning
                    self.driver.find_element_by_xpath(
                        "//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]").click()
                    sleep(3)
                except Exception as e:
                    log.logger.error(e)



    def judge_is_pause(self):
        log.logger.debug('wheater pause ?')
        if self.isElement(By.ID, "com.hujiang.hjclass:id/tv_play_time"):
            pass
        else:
            self.discovery_play_line()
        # 进度条信息 text 01:34/20:54
        els1 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/tv_play_time")
        date1 = els1.text
        time.sleep(5)
        els2 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/tv_play_time")
        date2 = els2.text
        log.logger.debug('进度条信息 ' + date1 + ' ' + date2)
        return date1 == date2

    def click_pause(self):
        log.logger.debug("click_pause")
        if self.isElement(By.ID, "com.hujiang.hjclass:id/fl_landscape_play_pause_container"):
            pass
        else:
            self.discovery_play_line()
        # 点击暂停
        el8 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/fl_landscape_play_pause_container")
        el8.click()
        time.sleep(2)

    def next_page(self):
        if self.isElement(By.ID, "com.hujiang.hjclass:id/iv_page_down"):
            pass
        else:
            self.discovery_play_line()
        # 点击当前课程的下一页
        el9 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/iv_page_down")
        el9.click()

    def findItem(self, el):
        source = self.driver.page_source
        if el in source:
            return True
        else:
            return False

    def isElement_from_element(self, element, identifyBy, c):
        '''
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        '''
        sleep(1)
        flag = None
        try:
            if identifyBy == "id":
                # self.driver.implicitly_wait(60)
                element.find_element_by_id(c)
            elif identifyBy == "xpath":
                # self.driver.implicitly_wait(60)
                element.find_element_by_xpath(c)
            elif identifyBy == "class":
                element.find_element_by_class_name(c)
            elif identifyBy == "link text":
                element.find_element_by_link_text(c)
            elif identifyBy == "partial link text":
                element.find_element_by_partial_link_text(c)
            elif identifyBy == "name":
                element.find_element_by_name(c)
            elif identifyBy == "tag name":
                element.find_element_by_tag_name(c)
            elif identifyBy == "css selector":
                element.find_element_by_css_selector(c)
            flag = True
        except NoSuchElementException as e:
            flag = False
        finally:
            return flag

    def isElement(self, identifyBy, c):
        '''
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        '''
        log.logger.debug(identifyBy + " " + c)
        sleep(1)
        flag = None
        try:
            if identifyBy == "id":
                # self.driver.implicitly_wait(60)
                self.driver.find_element_by_id(c)
            elif identifyBy == "xpath":
                # self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath(c)
            elif identifyBy == "class":
                self.driver.find_element_by_class_name(c)
            elif identifyBy == "link text":
                self.driver.find_element_by_link_text(c)
            elif identifyBy == "partial link text":
                self.driver.find_element_by_partial_link_text(c)
            elif identifyBy == "name":
                self.driver.find_element_by_name(c)
            elif identifyBy == "tag name":
                self.driver.find_element_by_tag_name(c)
            elif identifyBy == "css selector":
                self.driver.find_element_by_css_selector(c)
            flag = True
        except NoSuchElementException as e:
            flag = False
        finally:
            return flag

    def discovery_play_line(self):
        w = self.driver.get_window_size()['width']
        h = self.driver.get_window_size()['height']
        self.click(w * 9 / 10, h * 3 / 5)
        sleep(1)

    def set_2x(self):
        sleep(13)
        try:
            log.logger.debug("set 2x")
            if self.isElement(By.ID, "com.hujiang.hjclass:id/iv_more"):
                pass
            else:
                self.discovery_play_line()
            el10 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/iv_more")
            el10.click()
            sleep(3)
            el11 = self.driver.find_element(by=By.ID, value="com.hujiang.hjclass:id/rb_speed_2")
            el11.click()
            sleep(3)
            x = el11.location.get('x')
            y = el11.location.get('y')
            self.click(x + 140, y)
        except Exception as e:
            log.logger.error(e)

    def click(self, x, y):

        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def choice_course(self):
        pass


if __name__ == "__main__":
    ope = AutoHJAppCourse("test", "passwd")
    ope.process()
