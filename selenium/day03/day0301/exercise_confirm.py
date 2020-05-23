from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 导入Select类
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("http://www.sahitest.com/demo/index.html")
# 定位超级链接
confirmlink = driver.find_element(By.LINK_TEXT,"Confirm Page")
confirmlink.click()

#定位按钮
sleep(1)
btn1 =driver.find_element(By.XPATH,"//input[1]")
btn1.click()

#获得confirm 对话框
confirm1 = driver.switch_to.alert
sleep(1)
t1 = confirm1.text
confirm1.accept()

txt1 = driver.find_element(By.XPATH,"//input[2]")
if txt1.get_attribute("value") == "oked":
    print("点击确定按钮")
    print("提示信息：",t1)
sleep(1)
btn1.click()
c1 = driver.switch_to.alert
sleep(1)
c1.dismiss()#点击取消按钮
if txt1.get_attribute("value") =="canceled":
    print("点击取消按钮")



