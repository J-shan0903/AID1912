# 导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 实例化Chrome类
driver = webdriver.Chrome()
# 打开测试网页
driver.get('http://127.0.0.1:8060')

# mylink = driver.find_element(By.LINK_TEXT,"游客进入")

# 部分文字打开链接
mylink = driver.find_element(By.PARTIAL_LINK_TEXT,"游客")

mylink.click()