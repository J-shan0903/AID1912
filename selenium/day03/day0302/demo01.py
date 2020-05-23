from selenium import webdriver
from selenium.webdriver.common.by import By

# 导入NoSuchElementException异常类
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
# 设置implictly等待
driver.implicitly_wait(10)
driver.get("")

# 在try-except结构中定位页面元素并操作
try:
    # 定位页面元素并操作
    username = driver.find_element(By.XPATH,"//input[1]")
    password = driver.find_element(By.XPATH,"//input[2]")
    comments = driver.find_element(By.XPATH,"//textarea")
    submit = driver.find_element(By.XPATH,"//input[3]")
    username.send_keys("aaa")
    password.send_keys("123")
    comments.send_keys("zxcf")
    submit.click()
    print("页面操作正常完成")
except NoSuchElementException as e:
    print("已经等待10秒钟时间")
    print(e)
finally:
    print("程序退出")
    driver.quit()

