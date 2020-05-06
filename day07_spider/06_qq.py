from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url='https://mail.qq.com/')

driver.switch_to.frame('login_frame')

driver.find_element_by_id('u').send_keys('369618935@qq.com')
driver.find_element_by_id('p').send_keys('353597jss')
driver.find_elements_by_class_name('btn').click()