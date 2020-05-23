# 导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 实例化Chrome类
driver = webdriver.Chrome()
# 打开测试网页
driver.get('http://127.0.0.1:8060')

mypic1 =driver.find_element(By.ID,'pic1')
sleep(1)
driver.set_window_size(1000,800)
mypic1.click()
sleep(1)
driver.back()
sleep(1)
mypic2 = driver.find_element(By.ID,'pic2')
mypic2.click()