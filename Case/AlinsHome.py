from time import sleep
import unittest
from selenium import webdriver
from EveryPage.SearchPage import Search
import warnings


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