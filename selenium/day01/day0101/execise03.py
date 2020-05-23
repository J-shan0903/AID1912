# 导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 实例化Chrome类
driver = webdriver.Chrome()
# 打开测试网页
driver.get('http://127.0.0.1:8060')

# mylink = driver.find_element(By.LINK_TEXT,"游客进入")

# 部分文本打开链接
mylink = driver.find_element(By.PARTIAL_LINK_TEXT,"游客")

mylink.click()

# 准备数据
name = "王晓明"
mail = "wangxiaoming@com"
comments = "你好，小名"

# 定位class方式页面元素
myname = driver.find_element(By.CLASS_NAME,"name")
mymail = driver.find_element(By.CLASS_NAME,"mail")
mycomment = driver.find_element(By.CLASS_NAME,"comments")
mysubimt = driver.find_element(By.CLASS_NAME,"submit1")

# 发布留言
myname.clear()
myname.send_keys(name)
mymail.clear()
mymail.send_keys(mail)
mycomment.clear()
mycomment.send_keys(comments)
mysubimt.click()

