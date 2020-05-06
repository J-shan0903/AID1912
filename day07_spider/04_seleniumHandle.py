import time,redis,sys
from hashlib import md5

from  selenium import webdriver

class MzbSpider:
    def __init__(self):
        self.url ='http://www.mca.gov.cn/article/sj/xzqh/2020/'
        self.driver = webdriver.Chrome()
        self.driver.get(url=self.url)
        self.r =redis.Redis(host='localhost',port="6379",db=0)

    def md5_url(self,url):
        s =md5()
        s.update(url.encode())
        return s.hexdigest()


    def parse_html(self):
        self.driver.find_element_by_partial_link_text('中华人民共和国县以上行政区划代码').click()
        time.sleep(1)

        all = self.driver.window_handles
        self.driver.switch_to.window(all[1])

        tr_list = self.driver.find_elements_by_xpath('//tr[@height="19"]')
        for tr in tr_list:
            item ={}
            item['name'] = tr.find_elements_by_xpath('./td[3]').text.strip()
            item['code'] = tr.find_elements_by_xpath('./td[2]').text.strip()
            print(item)

    def run(self):
        self.parse_html()


if __name__ == '__main__':
    spider = MzbSpider()
    spider.run()