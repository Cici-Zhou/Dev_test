#coding: utf-8

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://eks-qa.agspan.com/Beef")

# 登录Thirdparty
loc_username_input = (By.ID, 'logonUser_UserName')
loc_password_input = (By.ID, 'logonUser_Password')
loc_login_button = (By.ID, 'logonUser_LoginButton')

driver.find_element(*loc_username_input).send_keys('Cici.zhou@itlogica.com')
driver.find_element(*loc_password_input).send_keys('Qwe1234!23')
driver.find_element(*loc_login_button).click()

# 进入Beef Landing page
time.sleep(20)
loc_assert_text = (By.XPATH, '//p[@class="CornerTitle"]')
item = driver.find_element(*loc_assert_text).text

print(item)
# 获取Beef Landing page窗口句柄
landing_windows = driver.current_window_handle
print(landing_windows)
loc_profittool_button = (By.XPATH, '//div[@class="Contnr"]/div/div/div[1]/img')
driver.find_element(*loc_profittool_button).click()

# 进入Profit Tool页面
# 获取当前所有打开的窗口的句柄
all_handles = driver.window_handles
profittool_Calculate = (By.XPATH, '//div[@class="cont_wrap"]/div[1]/div[1]/p')
loc_stockreport_button = (By.XPATH, '//div[@class="cont_wrap"]/div[1]/div[2]/div[2]/a')

for handle in all_handles:
    if handle != landing_windows:
        print(handle)
        driver.switch_to.window(handle)
        #hand = driver.current_window_handle
        #print(hand)
        time.sleep(20)
        # profititem = driver.find_element(*profittool_Calculate).text
        # el = driver.find_elements(*profittool_Calculate)
        el = driver.find_elements_by_class_name("cont_wrap")
        #for i in range(len(el)):
        #               print("第"+ str(i) + "个元素")
        #               print(el[i].get_attribute("name"))
        #               print(el[i].get_attribute("class"))
        #               print(el[i].get_attribute("href"))
        print(el)
        driver.find_element(*loc_stockreport_button).click()
        time.sleep(10)

for handle in all_handles:
    if handle == landing_windows:
        driver.switch_to.window(handle)
        time.sleep(5)
        print('new landing window!')
driver.quit()
