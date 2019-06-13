# -*- coding:utf-8 -*-

import os
import sys
import time
# base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(base_dir)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from test.common.Page import Page


class ThirdPartyMainPage(Page):

    log_username_input = (By.ID, 'logonUser_UserName')
    log_password_input = (By.ID, 'logonUser_Password')
    log_login_button = (By.ID, 'logonUser_LoginButton')
    # Add New Template page
    add_AddNewTemplate_button = (By.XPATH, "//dd[@id='ucMain_ddWeatherDataAdd']/a")
    add_StartDate_input = (By.ID, 'inputStartDate')
    add_EndDate_input = (By.ID, 'inputEndDate')
    add_WeatherVariables_checkbox = (By.CLASS_NAME, 'checkbox')
    add_TemplateName_input = (By.ID, 'txtTemplateName')

    # Template List page
    tem_TemplateList_button = (By.XPATH, '//dd[@id="ucMain_ddWeatherDataList"]/a')
    tem_SelectContact_list = (By.ID, 'dropContact')
    tem_Search_button = (By.ID, 'btnSearchWeatherData')
    tem_TemplateName_list = (By.CSS_SELECTOR, 'table#gvTemplateList>tbody>tr:nth-child(2)>td>a')

    # Template List Detail page
    tem_MeasureI = (By.CSS_SELECTOR, '#UpdatePanelElement>div>table>tbody>tr:nth-child(3)>td:nth-child(2)>span')
    tem_MeasureM = (By.CSS_SELECTOR, '#UpdatePanelElement>div>table>tbody>tr:nth-child(3)>td:nth-child(4)>span')
    tem_DMD = (By.CSS_SELECTOR, '#UpdatePanelElement>div>table>tbody>tr:nth-child(4)>td:nth-child(2)>span')
    tem_DMH = (By.CSS_SELECTOR, '#UpdatePanelElement>div>table>tbody>tr:nth-child(4)>td:nth-child(4)>span')
    tem_DewPoint_radiobutton = (By.CSS_SELECTOR,'table#chklistElements>tbody>tr:nth-child(1)>td:nth-child(1)>span.checkbox')
    tem_TemplateN = (By.ID, 'txtTemplateName')
    com_save_button = (By.XPATH, '//tr[@class="last"]/td/input[8]')
    com_ok_button = (By.XPATH, '//input[@id="popup_ok"]')
    tem_generate_button = (By.CSS_SELECTOR, '#UpdatePanelElement>div:nth-child(3)>table>tbody>tr:nth-child(3)>td>input:nth-child(10)')
    tem_save_button = (By.XPATH, '//input[@class="btn_3"]')


    def login(self, usr, pws):
        """ 搜索功能 """
        self.find_element(*self.log_username_input).send_keys(usr)
        self.find_element(*self.log_password_input).send_keys(pws)
        self.find_element(*self.log_login_button).click()

    def addnew(self):
        """进入Add New Template页面"""

        self.find_element(*self.add_AddNewTemplate_button).click()
        time.sleep(35)
        self.switch_to_frame('ifrContent')
        self.find_element(*self.add_StartDate_input).send_keys('01/11/2018')
        self.find_element(*self.add_EndDate_input).send_keys('01/11/2018')
        self.find_element(*self.add_WeatherVariables_checkbox).click()
        self.find_element(*self.add_TemplateName_input).send_keys('ll')
        self.find_element(*self.com_save_button).click()
        self.find_element(*self.com_ok_button).click()

    def templatelist(self):
        """进入Template List页面"""
        self.find_element(*self.tem_TemplateList_button).click()
        time.sleep(10)
        # 切换iframe
        self.switch_to_frame('ifrContent')
        time.sleep(5)
        # 定位 contact下拉框
        templatelist = self.find_element(*self.tem_SelectContact_list)
        Select(templatelist).select_by_value('15876')
        time.sleep(5)
        self.find_element(*self.tem_Search_button).click()
        time.sleep(5)
        # 进入Template Detail页面
        self.find_element(*self.tem_TemplateName_list).click()
        time.sleep(10)
        # Measurement system: Metric System
        self.find_element(*self.tem_MeasureM).click()
        # 1 0
        # 1 0
        if self.self.find_element(*self.tem_MeasureI).is_selected():
            print('is selected')
        else:
            print('not selected')

        MeasureIS = self.find_element(*self.tem_MeasureI).is_selected()
        DataModeD = self.find_element(*self.tem_DMD).is_selected()
        print(MeasureIS,DataModeD)
        self.find_element(*self.tem_MeasureI).click()
        self.find_element(*self.tem_DMD).click()
        time.sleep(5)
        MeasureIS2 = self.find_element(*self.tem_MeasureI).is_selected()
        DataModeD2 = self.find_element(*self.tem_DMD).is_selected()
        print(MeasureIS2, DataModeD2)
        """
        if MeasureIS is True and DataModeD is True:
            self.find_element(*self.tem_MeasureM).click()
            self.find_element(*self.tem_DMH).click()
            time.sleep(10)
            self.find_element(*self.tem_TemplateN).send_keys('1MMDH')
        elif MeasureIS is True and DataModeD is False:
            self.find_element(*self.tem_MeasureM).click()
            self.find_element(*self.tem_DMD).click()
            self.find_element(*self.tem_TemplateN).send_keys('1MMDD')
        elif MeasureIS is False and DataModeD is False:
            self.find_element(*self.tem_MeasureI).click()
            self.find_element(*self.tem_DMD).click()
            self.find_element(*self.tem_TemplateN).send_keys('1MIDH')
        else :
            self.find_element(*self.tem_MeasureI).click()
            self.find_element(*self.tem_DMH).click()
            time.sleep(10)
            self.find_element(*self.tem_TemplateN).send_keys('1MIDD')
        """
        # Data Mode

        time.sleep(10)
        # Select Weather Variables区域
        self.find_element(*self.tem_DewPoint_radiobutton).click()
        time.sleep(3)


        # 点击Save按钮
        self.find_element(*self.tem_save_button).click()
        time.sleep(5)
        self.find_element(*self.com_ok_button).click()
        time.sleep(5)
        # self.find_element(*self.tem_generate_button).click()
        # time.sleep(5)
        # self.find_element(*self.com_ok_button).click()
