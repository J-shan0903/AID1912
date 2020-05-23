from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 导入Select类
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("")

# 定位支付方式
pay = driver.find_elements(By.NAME,"pay")
print(pay)
# 操作支付方式
for i in pay:
    if not i.is_selected():
        i.click()
        print("点击：",i.get_attribute("value"))
print('--------------------------------------------')
# 定位爱好
hobby = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
list1 =[]
list2 =[]
list3 =[]

# 操作爱好
# 1、取出复选框的状态和文本值
for m in hobby:
    # list1.append(m.is_selected())
    f = m.is_selected()
    list1.append(f)
    n = m.get_attribute("name")
    list2.append(n)
print(list1)
print(list2)

# 2、操作复选框
# 3、输出所有选择的复选框
for k in hobby:
    k.click()
    if k.is_selected():
        h = k.get_attribute("name")
        list3.append(h)
print("选择的爱好：",list3)


