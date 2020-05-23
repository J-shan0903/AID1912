from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("")

h1 =driver.find_element(By.XPATH,"//a[text()='链接到demo01']")

sleep(2)
h1.click()

sleep(1)
driver.back()
sleep(1)
h2 = driver.find_element(By.XPATH,"//a[text()='链接到demo02']")
h2.click()