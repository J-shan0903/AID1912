# 导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 实例化Chrome类
driver = webdriver.Chrome()
# 打开测试网页
driver.get('http://127.0.0.1:8060')

# 准备测试数据
mydata1 ={'姓名':'testing',"密码":'123',"留言":'I am a tester'}
mydata2 ={}

# 定位页面元素
myname = driver.find_element(By.ID,'username')
mypassword = driver.find_element(By.ID,"pasword")
mycommits = driver.find_element(By.ID,"connents")
mybutton = driver.find_element(By.ID,"submit")

# 操作页面元素
myname.clear()
myname.send_keys(mydata1["姓名"])
mypassword.clear()
mypassword.send_keys(mydata1["密码"])
mycommits.clear()
mycommits.send_keys(mydata1["留言"])
sleep(2)

# 获得文本框填写的内容
mydata2["姓名"] = myname.get_attribute("value")
mydata2["密码"] = mypassword.get_attribute("value")
mydata2["留言"] = mycommits.get_attribute('value')

print('姓名',mydata2["姓名"],"长度:",len(mydata2["姓名"]))
print('密码',mydata2["密码"],"长度",len(mydata2["密码"]))
print('留言内容',mydata2["留言"],"长度",len(mydata2["留言"]))
# 判断输入的姓名是否正确
if mydata2["姓名"] ==mydata1["姓名"]:
    print("姓名正确")
else:
    print('姓名错误')


# 判断提交按钮如果可用 点击,不可用 提示信息
p1 =mybutton.get_attribute("value")
if mybutton.is_enabled():
    print("点击",p1,"按钮")
    mybutton.click()
else:
    print("按钮不可用!")