from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 导入Select类
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("")

h1 = driver.current_window_handle
print("当前窗口的句柄：",h1)

# 定位第二个链接并点击
link2 = driver.find_element(By.XPATH,"//li[2]/a")
sleep(1)
link2.click()

# 获得当前所有打开的窗口的句柄
all_handle = driver.window_handles
print("所有打开窗口的句柄：",all_handle)

# 进入新打开的demo02窗口进行操作
for i in all_handle:
    if i!=h1:
        driver.switch_to.window(i)
        print("当前窗口的标题：",driver.title)
        print("当前页面的地址",driver.current_url)
        h2 = driver.window_handles
        print("所有打开窗口的句柄：",h2)
        # 在但前窗口中操作
        name = driver.find_element(By.ID,"usernam")
        name.send_keys("Tom")
        # driver.switch_to.window("19")
        # print("当前窗口的标题：",driver.title)
# 回到主窗口中继续操作
for j in all_handle:
    if j == h1:
        driver.switch_to.window(j)
        sleep(1)
        link3 = driver.find_element(By.XPATH,"//li[3]/a")
        link3.click()

# 获得当前所有打开窗口的句柄
all_handle2 = driver.window_handles
print("所有打开窗口的句柄：", all_handle)

# 进入打开的demo02窗口进行操作
for m in all_handle2:
    if m!= h1 and m!= h2:
        driver.switch_to.window(m)
        sleep(1)
        count = driver.find_element(By.ID,"count")
        count.send_keys("Tom")
        sleep(2)
        driver.close()