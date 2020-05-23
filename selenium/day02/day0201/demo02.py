from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("")

# 使用绝对路径xpath定位方式
# myname = driver.find_elements_by_xpath("/html/body/form/input[@value='姓名']")
# mypassword = driver.find_elements_by_xpath("/html/body/form/input[@id='password']")
# mycomments = driver.find_element(By.XPATH,"/html/body/form/textarea")
# mysubimt = driver.find_element(By.XPATH,"/html/body/form/input[@type='sumbit']")

# 使用相对路径xpath定位方式
# 使用标记的属性名=属性值进行筛选说明
# myname = driver.find_elements_by_xpath("//input[@value='姓名']")
# mypassword = driver.find_elements_by_xpath("//input[@id='password']")
# mycomments = driver.find_element(By.XPATH,"//textarea")
# mysubimt = driver.find_element(By.XPATH,"//input[@type='sumbit']")

# 使用标记的索引号进行筛选说明
myname = driver.find_elements_by_xpath("//input[1]")
mypassword = driver.find_elements_by_xpath("//input[2]")
mycomments = driver.find_element(By.XPATH, "//textarea")
mysubimt = driver.find_element(By.XPATH, "//input[3]")

myname.clear()
myname.send_keys("aaa")
mypassword.clear()

mypassword.send_keys("asfc")
mycomments.clear()#清楚文本框内的内容
mycomments.send_keys("你好")
sleep(1)
mysubimt.click()
driver.quit()#关闭浏览器
