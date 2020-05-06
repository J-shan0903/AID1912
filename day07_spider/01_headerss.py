
from selenium  import  webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')


driver = webdriver.Chrome(options=options)
driver.get(url='http://www.baidu.com/')

driver.save_screenshot('baidu.png')