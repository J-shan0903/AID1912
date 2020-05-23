# 导入模块
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import  By
# 实例化Chrome类
driver = webdriver.Chrome()
# 打开测试网页
driver.get('http://www.baidu.com')

# 使用lincktext方式定位超级链接
mylick1 = driver.find_element_by_link_text('')
sleep(1)

# 点击超链接
mylick1.click()
sleep(1)

# 浏览器后退
driver.back()
mylick2 = driver.find_element(By.LINK_TEXT,'')
sleep(1)
mylick2.click()


