from selenium import webdriver
from selenium.webdriver.common.by import By
# 步骤1：导入WebDriverWait 类和expected_conditions模块
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Chrome()
# 设置implictly等待
driver.implicitly_wait(10)
driver.get("")

# 步骤2：实例化WebDriverWait类
w1 = WebDriverWait(driver,10,1)

# 步骤3 对页面元素进行定位并操作
# 姓名文本框
# （1）调用expected_conditions模块的方法判断元素是否存在
username_locator =(By.XPATH,".//*[@id='username']")
username=expected_conditions.presence_of_element_located(username_locator)
# 方式2
# username=expected_conditions.presence_of_element_located(By.XPATH,".//*[@id='username']")

# （2）调用 WebDriverWait类中的函数进行等待
username = w1.until(username)
# （3）操作页面元素
username.send_keys("张三")
# 密码
password_locator =(By.XPATH,".//*[@id='password']")
password = expected_conditions.presence_of_element_located(password_locator)
password = w1.until(password)
password.send_keys("123456")
# 留言
comments_locator =(By.XPATH,".//*[@id='comments']")
comments = expected_conditions.presence_of_element_located(comments_locator)
comments = w1.until(comments)
comments.send_keys("软件测试！")
# 提交按钮
sumbit_locator =(By.XPATH,".//*[@id='sumbit']")
sumbit= expected_conditions.presence_of_element_located(sumbit_locator)
sumbit = w1.until(sumbit)
sumbit.click()