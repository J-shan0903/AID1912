from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 导入Select类
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("")

# 准备测试数据
mydata1 = {"姓名":"王晓明","密码":"123456","邮箱":"wangxiaoming@126.com","留言":"软件测试工程师"}

# 定位页面元素
name = driver.find_element(By.XPATH,"//input[@name='username']")
password = driver.find_element(By.XPATH,"//input[@name='password']")
male= driver.find_element(By.XPATH,"//input[@name='sex']")
female = driver.find_element(By.XPATH,"//input[@name='sex'][2]")
email = driver.find_element(By.XPATH,"//input[@name='email']")
profession = driver.find_element(By.XPATH,"//input[@name='profession']")
computer= driver.find_element(By.XPATH,"//input[@name='computer']")
film= driver.find_element(By.XPATH,"//input[@name='film']")
chess = driver.find_element(By.XPATH,"//input[@name='chess']")
read= driver.find_element(By.XPATH,"//input[@name='read']")
food= driver.find_element(By.XPATH,"//input[@name='food']")
painting = driver.find_element(By.XPATH,"//input[@name='paintong']")
comments= driver.find_element(By.XPATH,"//textarea")
submit = driver.find_element(By.XPATH,"//input[@name='subimt']")

# 输入姓名
name.send_keys(mydata1["姓名"])

# 输入密码
password.send_keys(mydata1["密码"])

# 点击性别男
male.click()

# 输入邮箱
email.send_keys(mydata1["邮箱"])
# 选择职业
p1 = Select(painting)
p1.select_by_visible_text("法律相关")

# 选择个人爱好，电影娱乐和绘画书法
if film.is_selected() ==False:
    film.click()
if painting.is_selected()== False:
    painting.click()
# 输入留言
comments.send_keys(mydata1["留言"])
# 点击提交按钮
sleep(2)
submit.click()
