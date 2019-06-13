#-*- coding:utf-8 -*-

import os
import time
import sys
# base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(base_dir)

from selenium.webdriver.common.by import By
from test.page_obj.thirdparty_main_page import ThirdPartyMainPage
from test.models.config import DATA_PATH
from test.models.filereader import ExcelReader
import time

from selenium.webdriver.support.wait import WebDriverWait


class ThirdPartyResultPage(ThirdPartyMainPage):
    excel = DATA_PATH + '/ThirdPaertyuser.xlsx'

    @property
    def login_result_links(self):
        datas = ExcelReader(self.excel.data)
        for d in datas: 
            loginmessage = self.find_elements(*(By.XPATH,d['Locator']))
            return (loginmessage)
        
    loc_AddNewTemplate_button = (By.XPATH, "//dd[@id='ucMain_ddWeatherDataAdd']/a")

    @property
    def addnew_result_links(self):
        self.switch_to_parent_frame()
        self.find_element(*self.loc_AddNewTemplate_button).click()
        time.sleep(35)
        self.switch_to_frame('ifrContent')
       
        addnewmessage = self.find_element(By.ID, 'btnAdd').get_attribute("value")
        return addnewmessage

    @property
    def templatelist_result_links(self):
        time.sleep(20)
        addnewmessage = self.find_element(By.ID, 'btnAdd').get_attribute("value")
        return addnewmessage

    


