# coding: utf-8

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://eks-qa.agspan.com/thirdparty")

# 登录Thirdparty
loc_username_input = (By.ID, 'logonUser_UserName')
loc_password_input = (By.ID, 'logonUser_Password')
loc_login_button = (By.ID, 'logonUser_LoginButton')

driver.find_element(*loc_username_input).send_keys('Cici.zhou@itlogica.com')
driver.find_element(*loc_password_input).send_keys('Qwe0215!@#')
driver.find_element(*loc_login_button).click()

loc_TemplateList_button = (By.XPATH, '//dd[@id="ucMain_ddWeatherDataList"]/a')
loc_SelectContact_list = (By.ID, 'dropContact')
loc_Search_button = (By.ID, 'btnSearchWeatherData')
loc_TemplateName_list = (By.XPATH, '//table[@id="gvTemplateList"]/tbody/tr[2]/td[1]/a')



# 进入TemplateList页面 
driver.find_element(*loc_TemplateList_button).click()

# 切换到当前表单
driver.switch_to.frame('ifrContent')

# 显式等待页面
WebDriverWait(driver,30, 0.5).until(
    EC.presence_of_element_located((By.ID, 'dropContact'))
    )

# 在contact选项框中选择cici.xuan
time.sleep(10)
TemplateList = driver.find_element(*loc_SelectContact_list) 
Select(TemplateList).select_by_value('15876')
driver.find_element(*loc_Search_button).click()
time.sleep(10)
# 进入template Detail页面 
driver.find_element(*loc_TemplateName_list).click()
loc_Update_button = (By.ID, 'btnUpdate')
WebDriverWait(driver, 30, 0.5).until(
    EC.presence_of_element_located((By.ID, 'btnUpdate'))
    )

loc_save_button = (By.XPATH,'//input[@class="btn_3"]')
loc_leftmenu_button = (By.XPATH, '//div[@class="switch"]/a')
loc_ok_button = (By.XPATH,'//input[@id="popup_ok"]')

# 点击Save按钮
time.sleep(10)
save = driver.find_element(*loc_save_button).text
print(save)
driver.find_element(*loc_save_button).click()
time.sleep(5)
driver.find_element(*loc_ok_button).click()

driver.quit()
