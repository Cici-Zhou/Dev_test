#coding: utf-8

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)


import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from models.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
from models.log import logger
from models.filereader import ExcelReader
from models.HTMLTestRunner_PY3 import HTMLTestRunner
from page_obj.thirdparty_result_page import ThirdPartyMainPage, ThirdPartyResultPage

class TestBeef(unittest.TestCase):
    URL = Config().yaml_get('BeefURL')
    excel = DATA_PATH + '/Beefuser.xlsx'

    def sub_setUp(self):
        self.page = ThirdPartyMainPage(browser_type='chrome').get(self.URL, maximize_window=False)

    def sub_tearDown(self):
        self.page.quit()

    def login_success(self):
        self.page.login('Cici.zhou@itlogica.com','Qwe1234!23')
        
    def test_login(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            self.sub_setUp()
            self.page.login(d['User'],d['Password'])
            items = self.page.find_elements(*(By.XPATH,d['Locator']))
                
            for item in items:
                self.assertEqual(item.text, d['Message'])
                logger.info(item.text)
            self.sub_tearDown()


    def test_addnew(self):
        self.sub_setUp()
        self.login_success()
        self.page.addnew()
        self.Resultpage = ThirdPartyResultPage(self.page)
        addnewmessage = self.Resultpage.addnew_result_links
        self.assertEqual(addnewmessage, 'Add New Location')
        logger.info(addnewmessage)
        self.sub_tearDown()


    def test_templatelist(self):
        self.sub_setUp()
        self.login_success()
        
        self.page.templatelist()
        self.page = ThirdPartyResultPage(self.page)
        templatelistmessage = self.page.templatelist_result_links
        self.assertEqual(templatelistmessage, 'Add New Location')
        logger.info(templatelistmessage)
        self.sub_tearDown()
        

if __name__ == '__main__':
    #a=TestThirdparty()
    #b=a.test_templatelist()
    report = REPORT_PATH + '\\report.html'

    testsuite = unittest.TestSuite()
    testsuite.addTest(TestBeef('test_login'))
    #testsuite.addTest(TestThirdparty('test_addnew'))
    #testsuite.addTest(TestThirdparty('test_templatelist'))
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f,title=u'从0搭建测试框架 灰蓝', description='修改HTML报告')
        runner.run(testsuite)

        
   
