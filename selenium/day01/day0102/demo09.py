# 导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 实例化Chrome类
driver = webdriver.Chrome()
# 打开测试网页
driver.get('http://127.0.0.1:8060')

mylink1 = driver.find_element(By.LINK_TEXT,"链接到demo07")
print(mylink1.text)
sleep(2)
mylink1.click()
# 回退
driver.back()

mylink2 = driver.find_element(By.LINK_TEXT,"链接到demo08")
print(mylink2.text)
mylink2.click()