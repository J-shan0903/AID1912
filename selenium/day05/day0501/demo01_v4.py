from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()

# 打开浏览器
def open(url):
    base_url = url
    driver.get(base_url)


# 输入姓名
def type_name(n):
    name = driver.find_element(By.XPATH, "//input[@name='username']")
    name.send_keys(n)
# 输入密码
def type_password(p):
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys(p)

# 点击性别男
def click_male():
    male = driver.find_element(By.XPATH, "//input[@name='sex']")
    male.click()

# 点击性别女
def click_female():
    female = driver.find_element(By.XPATH, "//input[@name='sex'][2]")
    female.click()

# 输入邮箱
def type_email(e):
    email = driver.find_element(By.XPATH, "//input[@name='email']")
    email.send_keys(e)

# 选择专业
def select_profession(t):
    profession = driver.find_element(By.XPATH, "//input[@name='profession']")
    p1 = Select(profession)
    p1.select_by_visible_text(t)
#选择爱好（6个）

# 点击影视娱乐
def click_film():
    film = driver.find_element(By.XPATH, "//input[@name='film']")
    if film.is_selected() == False:
        film.click()
#点击绘画书法
def click_painting():
    painting = driver.find_element(By.XPATH, "//input[@name='painting']")
    if painting.is_selected() == False:
        painting.click()

#输入留言
def type_comment(c):
    comments = driver.find_element(By.XPATH, "//textarea")
    comments.send_keys(c)

# 点击提交
def click_submit():
    submit = driver.find_element(By.XPATH, "//input[@name='submit']")
    submit.click()

# 关闭浏览器
def bye_bye():
    driver.quit()


if __name__ == '__main__':

    # 打开页面
    base_url = ""
    open(base_url)
    # 测试数据
    mydata = {"姓名": "张孝明", "密码": "123456", "邮箱": "zhangxiaming@126.com", "专业": "法律相关", "留言": "软件测试工程师"}
    type_name(mydata["姓名"])
    type_password(mydata["密码"])
    click_female()
    type_email(mydata["邮箱"])
    select_profession(mydata["专业"])
    click_film()
    click_painting()
    type_comment("留言")
    sleep(1)
    click_submit()
    bye_bye()