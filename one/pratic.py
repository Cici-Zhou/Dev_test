from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

# 获得百度搜索窗口句柄
search_windows = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()

all_handles = driver.window_handles
print(all_handles)

for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
        print('Now is register window!')

for handle in all_handles:
    if handle == search_windows:
        driver.switch_to.window(handle)
        print('Now is search window!')

driver.quit()