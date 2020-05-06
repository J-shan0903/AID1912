from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://maoyan.com.board/4?offset=0')

def parse_html():
    dd_list =driver.find_element_by_xpath('')
