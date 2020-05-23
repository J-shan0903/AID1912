from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://mail.qq.com/')

name = "369618935"
password = "353597jss"

myname = driver.find_element_by_id('name')
mypassword = driver.find_element_by_id('password')
mybutton = driver.find_element_by_id('登陆')

myname.send_keys(name)
sleep(1)
mypassword.send_keys(password)
sleep(1)
mybutton.click()

print('我是', name, '密码', password)

driver.quit()
