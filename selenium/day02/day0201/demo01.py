from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("")

# 准备测试数据
name ="testing"
password = "123456"
comments ="你好，selenium"
'''
# 使用xpath方式定位页面元素
myname = driver.find_elements_by_xpath(".//*[@id='username']")
mypassword = driver.find_elements_by_xpath(".//*[@id='password']")

mycomments = driver.find_element(By.XPATH,".//*[@id='comments']")
mysubimt = driver.find_element(By.XPATH,".//*[@id='submit']")
'''
# 使用selenium IDE方式生成的表达式
myname = driver.find_elements_by_xpath("//input[@id='username']")
mypassword = driver.find_elements_by_xpath("//input[@id='password']")
mycomments = driver.find_element(By.XPATH,"//input[@id='comments']")
mysubimt = driver.find_element(By.XPATH,"//input[@id='submit']")
# 操作页面元素
myname.clear()
myname.send_keys(name)
sleep(1)
mypassword.clear()
mypassword.send_keys(password)
sleep(1)
mycomments.clear()
mycomments.send_keys(comments)
sleep(1)
mysubimt.click()




