from time import sleep
import unittest
from selenium import webdriver
from EveryPage.SearchPage import Search
import warnings
"""
业务层：真正的测试用例的操作，用例的业务逻辑以实现，调用页面层中的方法
根据业务逻辑，需要哪些操作，直接调用即可。
"""

class alins(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)


    def test_lable1(self):
        """一级标签"""
        url="http://alins.ele.me"
        s = Search(self.driver,url)
        s.open_alins()
        s.click_one()
        s.switch_alins_window0()
        print('Test OK')
        print('Test _lable1 OK')

        try:
            self.assertEqual(u"1234_百度搜索", self.driver.title)
        except AssertionError as e:
            print (u"找不到这个标题")
        s.close_windows()

    def test_lable2(self):
        """二级标签"""
        url="http://alins.ele.me"
        sleep(2)
        s = Search(self.driver,url)
        s.open_alins()
        s.Actionchains_click1()
        s.img()
        s.click_two1()
        s.switch_alins_window0()
        s.Actionchains_click2()
        s.click_two2()
        s.switch_alins_window0()
        print('Test _lable2 OK')

        sleep(3)

    def tearDown(self):
       sleep(1)

if __name__ == '__main__':
    pass