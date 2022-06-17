from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains   #鼠标操作
from time import sleep
import os
class BasePage():
    '''BasePage封装所有界面都公用的方法。例如driver,find_element等'''
    '''实例化BasePage类时，事先执行的__init__方法，该方法需要传递参数'''
    def __init__(self,driver,url):
        self.driver = driver
        self.base_url = url

    #def setUp(self):
       # self.driver.maximize_window()
    # 进入网址
    def get(self):
        self.driver.get(self.base_url)

    #元素定位,替代八大定位
    def get_element(self,*locator):
        return self.driver.find_element(*locator)
    #点击
    def right_click(self,*locator):
        self.driver.find_element(*locator).click()
    #悬浮
    def Action_click(self,*locator):
        ActionChains(self.driver).click(self.get_element(*locator)).perform()
    #输入
    def send_text(self,text,*locator):
        self.driver.find_element(*locator).send_keys(text)
    #清除
    def clear_text(self,*locator):
        self.driver.find_element(*locator).clear()

    #切换表单
    def switch_iframe(self,*locator):
        self.driver.switch_to.frame(self.driver.find_element(*locator))
        self.driver.switch_to_default_content()

    #窗口切换
    def switch_windows_test(self,n):
        self.driver.switch_to.window(self.driver.window_handles[n])

    #断言
    def _open(self, url, page_title):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            #           通过断言输入的title是否在当前title中
            assert page_title in self.driver.title, u'打开页面失败：%s' % url
        except:
            print('Pass')

    #截屏
    def img_save(self,img_name):
        self.driver.get_screenshot_as_file(
            '{}/{}.png'.format(os.path.abspath(r'C:\Users\LuckyHo\PycharmProjects\pythonProject1\IMG'), img_name))
    #关闭
    def close_window(self):
        self.driver.close()


    def tearDown(self):
        self.driver.quit()