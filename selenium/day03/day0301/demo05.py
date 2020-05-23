from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 导入Select类
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("")
link = driver.find_element(By.XPATH,"//a[1]")
print("当前页面的标题：",driver.title)
print("当前页面的地址：",driver.current_url)
sleep(1)
link.click()

sleep(1)
driver.refresh()
sleep(2)
driver.set_window_size(1200,500)
print("当前页面的标题：",driver.title)
print("当前页面的地址：",driver.current_url)
sleep(1)
driver.close()

