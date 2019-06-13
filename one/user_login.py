# coding:utf-8

from selenium import webdriver
import os

driver = webdriver.Chrome()

url = "https://qa.agspan.com/CIMS/Login.aspx"
driver.implicitly_wait(10)
driver.get(url)


def Login(username, password):
    driver.find_element_by_id("txtUserName").send_keys(username)
    driver.find_element_by_id("txtPWD").send_keys(password)
    driver.find_element_by_id("btnLogin").click()


def insert_img(driver,file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('cims_traverse')[0]
    file_path = base + '/picture' + file_name
    driver.get_screenshot_as_file(file_path)


def message_result(road):
    message = driver.find_element_by_css_selector(road).get_attribute("value")
    return message
