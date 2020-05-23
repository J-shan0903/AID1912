# 导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 实例化Chrome类
driver = webdriver.Chrome()
# 打开测试网页
driver.get('http://127.0.0.1:8060')

name = 'testing'
password ='1223'

# 使用classname定位页面元素
myname = driver.find_element(By.CLASS_NAME,'username')
mypassword = driver.find_element(By.CLASS_NAME,'password')
mybutton = driver.find_element(By.CLASS_NAME,'subimt')

myname.send_keys(name)
mypassword.send_keys(password)
sleep(1)
mybutton.click()