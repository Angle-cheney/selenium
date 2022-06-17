'''
实现步骤:(1)继承basepage,(2)元素传参,(3)调取方法
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains   #鼠标操作
from time import sleep
from BasePage.BasePage import BasePage
class Search(BasePage):
    def __init__(self,driver,url):
        BasePage.__init__(self,driver,url)

    def setUp(self):
        sleep(2)
     #进入官网
    def open_alins(self):
        self.get()

    #输入搜索内容
    def input_search_content(self,text):
        self.send_text(text,By.XPATH,"/html/body/div/div/div[1]/div[2]/div/input")

    #点击一级标签
    def click_one(self):
        self.right_click(By.CSS_SELECTOR,"#layout-main > div.banner-container > div > div.label-container > div > div:nth-child(1) > span")

    #一级标签鼠标悬浮1
    def Actionchains_click1(self):
        s = self.driver.find_element(By.XPATH,"//*[@id='layout-main']/div[1]/div/div[2]/div/div[1]/span")
        ActionChains(self.driver).move_to_element(s).perform()

    #一级标签鼠标悬浮2
    def Actionchains_click2(self):
        s = self.driver.find_element(By.XPATH,"//*[@id='layout-main']/div[1]/div/div[2]/div/div[2]/span")
        ActionChains(self.driver).move_to_element(s).perform()

    # 点击二级标签1
    def click_two1(self):
        self.right_click(By.XPATH, "//span[contains(text(),'基础操作')]")

    # 点击二级标签2
    def click_two2(self):
        self.right_click(By.XPATH, "//span[contains(text(),'经营指导')]")

    # 切换窗口
    def switch_alins_window0(self):
        self.switch_windows_test(0)

    def switch_alins_window1(self):
        self.switch_windows_test(1)

    def switch_alins_window2(self):
        self.switch_windows_test(2)

    def switch_alins_window3(self):
        self.switch_windows_test(3)
    def MaxWindows(self):
        self.MaxWindow()

    #截屏
    def img(self):
        self.img_save('鼠标悬浮截屏')

    #切换表单
    def switch_baidu_iframe(self):
        self.switch_iframe(By.ID,"KW")

    #关闭
    def close_windows(self):
        self.close_window()

    def tearDown(self):
        self.driver.quit()
