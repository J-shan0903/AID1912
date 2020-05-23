from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 导入Select类
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("http://www.sahitest.com/demo/index.html")

# 定位并输入电话
te1 = driver.find_element(By.XPATH,"//input[1]")
te1.send_keys("15030250190")
# 定位并点击按钮
sleep(1)
submit = driver.find_element(By.XPATH,"//input[3]")
submit.click()

# 定位prompt对话框
prompt1 = driver.switch_to.alert

txt1 = prompt1.text
print(txt1)
# 输入验证码并点击确定按钮
sleep(1)
prompt1.send_keys("123456")
sleep(1)
prompt1.accept()

# 定位验证码文本框并操作
checkpin = driver.find_element(By.XPATH,"//input[2]")
checkpin.send_keys("123456")








