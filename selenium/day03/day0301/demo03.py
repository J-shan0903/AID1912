from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 导入Select类
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("")

submit = driver.find_element(By.XPATH,"//input[2]")
submit.click()

# 定位alert
alert1 = driver.switch_to.alert

# 获取alert中的文本
text1 = alert1.text
print(text1)
# 点击确定按钮
sleep(1)
alert1.accept()
print("点击确定按钮")
sleep(1)
submit.click()
alert1.dismiss()
print("点击取消按钮")


