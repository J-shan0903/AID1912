# 导入模块
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import  By
# 实例化Chrome类
driver = webdriver.Chrome()
# 打开测试网页
driver.get('网页地址')

# 准备测试数据
count ='mystesing'
nickname = '冬冬'

# 使用name方式定位页面元素
# mycount = driver.find_element_by_name("count")
# mynickname = driver.find_elements_by_name("nicheng")
# mybutton = driver.find_elements_by_name("subimt")
mycount =driver.find_element(By.NAME,'count')
mynickname =driver.find_element(By.NAME,'nicheng')
mybutton =driver.find_element(By.NAME,'subimt')
# 操作页面元素
sleep(1)
mycount.send_keys(count)
sleep(1)
mynickname.send_keys(nickname)
sleep(1)
mybutton.click()

# 关闭浏览器
driver.quit()
