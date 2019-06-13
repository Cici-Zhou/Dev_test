# coding:utf-8

import time
from one.user_login import Login, message_result, driver
import logging
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

logger = logging.getLogger() #创建默认logger
logger1 = logging.getLogger("testlog")
logger1.setLevel(logging.DEBUG)
user = Login("cici.zhou@itlogica.com", "Qwe0416!@#")
time.sleep(2)

# Report Management
driver.find_element_by_css_selector("#menu5").click()
driver.switch_to.frame("indexFrame")
driver.implicitly_wait(10)
driver.switch_to.frame("leftFrame")
driver.implicitly_wait(10)
# Send Report
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(1)").click()
time.sleep(3)
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
time.sleep(5)
sendreportmeassge = driver.find_element_by_id('btnRemove').get_attribute("value")
print(sendreportmeassge)

# Email Template
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
time.sleep(1)
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(2)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
time.sleep(6)
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")

driver.find_element_by_css_selector("#ibtnChange").click()
time.sleep(4)
report_message = driver.find_element_by_id('btCancel').get_attribute('value')
print(report_message)
time.sleep(6)
driver.find_element_by_id('btCancel').click()
time.sleep(10)

# New Email Templage
'''
driver.find_element_by_css_selector("#btCancel").click()
time.sleep(1)

# Report
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(3)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
time.sleep(10)
driver.find_element_by_css_selector("#gvReport_ctl02_ibtnEdit").click()
time.sleep(8)
driver.find_element_by_css_selector("#gvReport_ctl02_ibtnCancel").click()
time.sleep(1)

# DDAS Report Notification
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(4)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
time.sleep(2)

# Report Parameter
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(5)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
driver.find_element_by_css_selector("#paging>input:nth-child(3)").click()
time.sleep(4)

# Report History
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(6)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
Contact = driver.find_element_by_css_selector("#dropContact")

Select(Contact).select_by_value("15876")
time.sleep(3)
driver.find_element_by_css_selector("#ibtnSearch").click()
time.sleep(5)
# 获取句柄失败
# driver.find_element_by_css_selector("#gvContactEmail_ctl02_lnkPreview").click()
# time.sleep(2)
# 获取当前所有打开的窗口的句柄
# all_handles = driver.window_handles
# print(all_handles)
# time.sleep(6)
#
# 进入 Email Preview 窗口
# for handle in all_handles:
#     if handle != report_history_handle:
#         driver.switch_to.window(handle)
#         print("now Email Preview window!")
#         driver.find_element_by_css_selector("#btnSendReport").click()
#         time.sleep(2)
#         driver.find_element_by_css_selector("#tblrTitle>td:nth-child(2)>input").click()

# 回到 Report History 窗口
# for handle in all_handles:
#    if handle == report_history_handle:
#       driver.switch_to.window(handle)

# ETool Group
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(7)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()

# ETook SexType
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(8)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
EtoolType = driver.find_element_by_css_selector("#dropEToolType")
# Days on Feed Calculator
Select(EtoolType).select_by_value("367")
time.sleep(4)

# ETool Security
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(9)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
Contact = driver.find_element_by_css_selector("#dropContact")
Select(Contact).select_by_value("15876")
time.sleep(6)
driver.find_element_by_css_selector("#ibtnSearch").click()
time.sleep(1)
# Generate按钮
# driver.find_element_by_css_selector("#gvEToolSecurity_ctl13_ibtnGenerate").click()

# ETool Web Access
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(10)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
ETool = driver.find_element_by_css_selector("#dropETool")
Select(ETool).select_by_value("760")
time.sleep(2)
Contact = driver.find_element_by_css_selector("#dropContact")
Select(Contact).select_by_value("15876")
time.sleep(2)
Account = driver.find_element_by_css_selector("#dropAccount")
Select(Account).select_by_value("10233")
time.sleep(1)

# Sent Emails
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(11)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
SE_Contact = driver.find_element_by_css_selector("#dropContactEmail")
Select(SE_Contact).select_by_value("15876")
driver.find_element_by_css_selector("#btnSearch").click()
time.sleep(1)

# LotMatching
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(12)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
LM_BA = driver.find_element_by_css_selector("#Table1>tbody>tr:nth-child(3)>td>select")
Select(LM_BA).select_by_value("15876")
time.sleep(2)

# LotMatching History
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(13)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
driver.find_element_by_css_selector("#btnSearch").click()
time.sleep(1)

# Code Manager
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(14)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
time.sleep(1)

# SystemField
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(15)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()

# Field Mapping
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(16)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
FM_DT = driver.find_element_by_css_selector("#dropFileType")
Select(FM_DT).select_by_value("CloseoutCore")
FM_Account = driver.find_element_by_css_selector("#dropAccount")
Select(FM_Account).select_by_value("89008")
time.sleep(1)
# radio button
driver.find_element_by_css_selector("#radlType_1").send_keys(Keys.SPACE)
time.sleep(1)

# My Report
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(17)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
MR_Report = driver.find_element_by_css_selector("#dropReport")
Select(MR_Report).select_by_value("4")

# HTSiDataQualityReport
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(18)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
HT_RN = driver.find_element_by_css_selector("#dropReportName")
Select(HT_RN).select_by_value("699")
time.sleep(1)

# PoultryExcelReport
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(19)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()

# HTSi Data Extract
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(20)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
HDE_TO = driver.find_element_by_css_selector("#dropTemplateOwner")
Select(HDE_TO).select_by_value("10777")
driver.find_element_by_css_selector("#ibtnAddNew").click()

# ReportSecurity
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(21)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
driver.implicitly_wait(10)
RS_Contact = driver.find_element_by_css_selector("#dropContact")
Select(RS_Contact).select_by_value("15876")
driver.implicitly_wait(20)
driver.find_element_by_css_selector("#btnSearch").click()

# FTP Management
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreen0Nodes>table:nth-child(22)>tbody>tr>td:nth-child(4)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
FTPM_Contact = driver.find_element_by_css_selector("#dropContactEmail")
Select(FTPM_Contact).select_by_value("15876")
driver.find_element_by_css_selector("#btnSearch").click()
driver.implicitly_wait(10)

# Reports
driver.implicitly_wait(10)
driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.find_element_by_css_selector("#tvModuleTreet23").click()
time.sleep(20)
driver.find_element_by_css_selector("#tvModuleTreet23").click()
driver.implicitly_wait(10)
el = driver.find_elements_by_css_selector("#tvModuleTreet24")
print(len(el))
driver.implicitly_wait(10)
driver.find_element_by_id("tvModuleTreet24").click()
time.sleep(8)
driver.find_element_by_css_selector("#tvModuleTreen23Nodes>div>table>tbody>tr>td:nth-child(6)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
driver.implicitly_wait(30)
# AccountGroup
RBB_AG = driver.find_element_by_css_selector("#rpwDisplay_ctl00_ctl03_ddValue")
Select(RBB_AG).select_by_value("1")
# View Report
driver.find_element_by_css_selector("#rpwDisplay_ctl00_ctl00").click()
time.sleep(15)
# 下一页
driver.find_element_by_css_selector("#rpwDisplay_ctl01_ctl01_ctl05_ctl00>tbody>tr>td>input").click()
time.sleep(5)
# PDF
format_select = driver.find_element_by_css_selector("#rpwDisplay_ctl01_ctl05_ctl00")
Select(format_select).select_by_value("PDF")
# Export
driver.find_element_by_css_selector("#rpwDisplay_ctl01_ctl05_ctl01").click()
driver.implicitly_wait(10)

driver.switch_to.parent_frame()
driver.switch_to.frame("leftFrame")
driver.implicitly_wait(10)
driver.find_element_by_css_selector("#tvModuleTreen24Nodes>table:nth-child(2)>tbody>tr>td:nth-child(6)>a:nth-child(2)").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("contentFrame")
time.sleep(10)
# GroupName
GroupName = driver.find_element_by_css_selector("#rpwDisplay_ctl00_ctl03_ddValue")
Select(GroupName).select_by_value("2")
driver.find_element_by_css_selector("#rpwDisplay_ctl00_ctl00").click()
time.sleep(15)
# 下一页
driver.find_element_by_css_selector("#rpwDisplay_ctl01_ctl01_ctl05_ctl00>tbody>tr>td>input").click()
time.sleep(5)
# PDF
format_select = driver.find_element_by_css_selector("#rpwDisplay_ctl01_ctl05_ctl00")
Select(format_select).select_by_value("PDF")
# Export
driver.find_element_by_css_selector("#rpwDisplay_ctl01_ctl05_ctl01").click()
time.sleep(15)
'''
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
# Report Management
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
