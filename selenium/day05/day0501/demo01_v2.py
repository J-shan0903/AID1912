from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()

# 打开浏览器
def open(url):
    base_url=url
    driver.get(base_url)

# 操作页面函数mycase1
def mycase1():

    name = driver.find_element(By.XPATH, "//input[@name='username']")
    name.send_keys("张鲜明")
    password = driver.find_element(By.XPATH, "//input[@name='password']")

    password.send_keys("12356")
    male = driver.find_element(By.XPATH, "//input[@name='sex']")
    male.send_keys("男")
    email = driver.find_element(By.XPATH, "//input[@name='email']")
    email.send_keys("zhangxianming@126.com")
    profession = driver.find_element(By.XPATH, "//input[@name='profession']")

    p1 = Select(profession)
    p1.select_by_visible_text("法律相关")
    film = driver.find_element(By.XPATH, "//input[@name='film']")
    if film.is_selected() == False:
        film.click()
    painting = driver.find_element(By.XPATH, "//input[@name='painting']")

    if painting.is_selected() == False:
        painting.click()

    comments = driver.find_element(By.XPATH, "//textarea")
    comments.send_keys("软件测试")
    sleep(1)
    submit = driver.find_element(By.XPATH, "//input[@name='submit']")
    submit.click()
def bye_bye():
    driver.quit()

if __name__ == '__main__':
    base_url =""
    open(base_url)
    mycase1()
    bye_bye()