from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("")

h1 = driver.find_element(By.XPATH,"//input[@checked]")

sleep(1)
h1.click()