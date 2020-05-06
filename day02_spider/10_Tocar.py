"""
sudo pip3 install fake_useragent

In [3]: from fake_useragent import UserAgent

In [4]: UserAgent().random
Out[4]: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'

"""
import time
import requests
import re
import random
from fake_useragent import UserAgent

class CarSpider:
    def __init__(self):
        self.url = 'https://www.che168.com/beijing/a0_0msdgscncgpi1lto1csp{}exx0/'

    def get_html(self,url):
        """获取函数1-获取html"""
        headers ={'User-Agent':UserAgent().random}
        html = requests.get(url=url,headers=headers).text

        return html

    def re_html(self,regex,html):
        """功能函数2-正则解析函数"""
        pattern = re.compile(regex,re.S)
        r_list = pattern.findall(html)

        return r_list

    def parse_html(self,one_url):
        """爬虫逻辑函数"""
        one_html = self.get_html(url=one_url)
        one_regex = '<li class="cards-li list-photo-li".*?<a href="(.*?)".*?</li>'
        car_list = self.re_func(one_regex, one_html)
        for href in car_list:
            two_url ='https://www.che168.com' + href
            self.get_car_info(two_url)
            time.sleep(random.randint(1,2))

    def get_car_info(self,two_url):
        """获取1辆汽车的具体信息"""
        two_html = self.get_html(url=two_url)
        two_regex = ':<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<ul class="brand-unit-item fn-clear">.*?<li>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span class="price" id="overlayPrice">￥(.*?)<b>'

        car_list = self.re_func(two_regex,two_html)
        item = {}
        item['name']= car_list[0][0].strip()
        item['km']= car_list[0][1].strip()
        item['time']= car_list[0][2].strip()
        item['type']= car_list[0][3].strip('/') [0].strip()
        item['displace']= car_list[0][3].strip('/')[1].strip()
        item['address']= car_list[0][4].strip()
        item['price']= car_list[0][5].strip()
        print(item)

    def run(self):
        for i in range(1,5):
            url = self.url.format(i)
            self.parse_html(url)


if __name__ == '__main__':
    spider = CarSpider()
    spider.run()






























