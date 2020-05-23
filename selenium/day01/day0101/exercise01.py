# 导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 实例化Chrome类
driver = webdriver.Chrome()
# 打开测试网页
driver.get('http://127.0.0.1:8060')
# 准备测试数据
logname = 'admin'
password ='123'

# 使用id方式进行定位
# myname = driver.find_element_by_id('username')
# mypassword = driver.find_element_by_id('password')
# mylogin = driver.find_element_by_id('sumbit')

# 使用find_element方式进行定位
# myname = driver.find_element(By.ID,'username')
# mypassword = driver.find_element(By.ID,'password')
# mylogin = driver.find_element(By.ID,'sumbit')

# 使用name方式进行定位
myname = driver.find_element(By.NAME,'username')
mypassword = driver.find_element(By.NAME,'password')
mylogin = driver.find_element(By.NAME,'sumbit')

# 操作页面元素
sleep(1)
myname.send_keys(logname)
sleep(1)
mypassword.send_keys(password)
sleep(1)
mylogin.click()

# 在控制台输出信息
print('用户名',logname,'密码',password)
