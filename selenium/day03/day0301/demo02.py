from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 导入Select类
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("")

# 定位并点击提交按钮
submit = driver.find_element(By.XPATH,"//input[2]")
submit.click()

# 定位alert
alert1 = driver.switch_to.alert
# 获取alert文本
txt1 = alert1.text
print("提示信息：",txt1)
# 点击确定按钮
alert1.accept()
