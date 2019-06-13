# coding:utf-8

from selenium import webdriver
import time
from one.user_login import Login, message_result, driver

user = Login("cici.zhou@itlogica.com", "Qwe0301!@#")
time.sleep(2)
# Account Management
driver.find_element_by_css_selector("#menu0").click()
driver.switch_to.frame("indexFrame")
driver.implicitly_wait(10)
driver.switch_to.frame("leftFrame")
driver.implicitly_wait(10)
# ETAMS
print(message_result("#tvModuleTreet48"))
# 点击AccountList
driver.find_element_by_css_selector("div#tvModuleTreen0Nodes>table:nth-child(2)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
time.sleep(3)
driver.find_element_by_css_selector("div#tvModuleTreen0Nodes>table:nth-child(1)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
time.sleep(3)
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
driver.find_element_by_css_selector("#txtAccountName").send_keys('0614Test Account')
driver.find_element_by_css_selector(".list_1>th>a").click()
driver.find_element_by_css_selector("#btnSearch").click()
# Account Name
print(message_result(".list_1>th:nth-child(1)>a"))
# 进入Account Overview页面
driver.find_element_by_css_selector("#gvAccountList>tbody>tr:nth-child(2)>td:nth-child(1)>div>a").click()
time.sleep(3)
print(message_result('.x1_1>tbody>tr>td:nth-child(1)'))

'''

#滚动到底部
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
time.sleep(5)
driver.implicitly_wait(10)

#滚动到顶部
js = "window.scrollTo(0,0)"
driver.execute_script(js)

#聚焦元素
#target = driver.find_element_by_id("gvContactList_ctl05_ibtnChangePassword").click()
#driver.execute_script("arguments[0].scrollIntoView();", target)
'''
#Report Management
'''
driver.find_element_by_link_text("Report Management").click()
driver.switch_to_frame("indexFrame")
driver.implicitly_wait(10)
driver.switch_to_frame("leftFrame")
driver.implicitly_wait(10)
#Sdriver.find_element_by_css_selector("div#tvModuleTreen0Nodes>table:nth-child(2)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.find_element_by_xpath("//div[@id='tvModuleTreen0Nodes']/table[2]/tbody/tr/td[4]/a[2]").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
driver.find_element_by_name("txtTemplateName").send_keys("qa")
driver.find_element_by_id("ibtnSearch").click()
driver.implicitly_wait(10)
driver.find_element_by_css_selector('[title="Preview"]').click()

'''
driver.quit()
