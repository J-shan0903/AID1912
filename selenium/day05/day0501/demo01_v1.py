from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get("")

name = driver.find_element(By.XPATH,"//input[@name='username']")
password = driver.find_element(By.XPATH,"//input[@name='password']")
male = driver.find_element(By.XPATH,"//input[@name='sex']")
female= driver.find_element(By.XPATH,"//input[@name='female']")
email = driver.find_element(By.XPATH,"//input[@name='email']")
profession = driver.find_element(By.XPATH,"//input[@name='profession']")
computer = driver.find_element(By.XPATH,"//input[@name='computer']")
film = driver.find_element(By.XPATH,"//input[@name='film']")
chess = driver.find_element(By.XPATH,"//input[@name='chess']")
read = driver.find_element(By.XPATH,"//input[@name='read']")
food = driver.find_element(By.XPATH,"//input[@name='food']")
painting = driver.find_element(By.XPATH,"//input[@name='painting']")
comments = driver.find_element(By.XPATH,"//textarea")
submit= driver.find_element(By.XPATH,"//input[@name='submit']")

name.send_keys("张鲜明")
password.send_keys("12356")
male.send_keys("男")
email.send_keys("zhangxianming@126.com")
p1=Select(profession)
p1.select_by_visible_text("法律相关")
if film.is_selected()==False:
    film.click()
if painting.is_selected()==False:
    painting.click()
comments.send_keys("软件测试")
sleep(1)
submit.click()
driver.quit()