from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()

# 测试数据
mydate1 ={"姓名":"张孝明","密码":"123456","邮箱":"zhangxiaming@126.com","专业":"法律相关","留言":"软件测试工程师",}

# 打开浏览器
def open(url):
    base_url = url
    driver.get(base_url)


# 操作页面函数mycase1
def mycase1():
    name = driver.find_element(By.XPATH, "//input[@name='username']")
    name.send_keys(mydate1["姓名"])
    password = driver.find_element(By.XPATH, "//input[@name='password']")

    password.send_keys(mydate1["密码"])
    male = driver.find_element(By.XPATH, "//input[@name='sex']")
    male.click()
    email = driver.find_element(By.XPATH, "//input[@name='email']")
    email.send_keys(mydate1["邮箱"])
    profession = driver.find_element(By.XPATH, "//input[@name='profession']")

    p1 = Select(profession)
    p1.select_by_visible_text(mydate1["专业"])
    film = driver.find_element(By.XPATH, "//input[@name='film']")
    if film.is_selected() == False:
        film.click()
    painting = driver.find_element(By.XPATH, "//input[@name='painting']")

    if painting.is_selected() == False:
        painting.click()

    comments = driver.find_element(By.XPATH, "//textarea")
    comments.send_keys(mydate1["留言"])
    sleep(1)
    submit = driver.find_element(By.XPATH, "//input[@name='submit']")
    submit.click()


def bye_bye():
    driver.quit()


if __name__ == '__main__':
    base_url = ""
    open(base_url)
    mycase1()
    bye_bye()