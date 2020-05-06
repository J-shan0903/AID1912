from selenium import webdriver

# driver = webdriver.PhantomJS()
driver = webdriver.Chrome()
driver.maximize_window()#窗口最大化
driver.get('http://www.baidu.com/')
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('赵丽颖')#输入文本信息
driver.find_element_by_xpath('//*[@id="su"]').click()#点击按钮
driver.save_screenshot('baidu.png')#截图

driver.quit()#关闭浏览器
