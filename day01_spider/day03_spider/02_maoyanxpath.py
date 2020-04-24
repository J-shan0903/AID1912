
import time
import random
import requests
from lxml import etree

class MaoyanSpider:
    def __init__(self):
        """定义常用变量"""
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

    def get_html(self,url):
        """请求功能函数 -获取html"""
        html = requests.get(url=url,headers=self.headers).text

        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self,html):
        """解析数据解析提取  -xpath"""
        p = etree.HTML(html)
        dd_list = p.xpath('//d1[@class="board-wrapper"]/dd')
        item = {}
        for dd in dd_list:
            item['name'] = dd.xpath('./p[@class="name"]/a/@title')[0].strip()
            item['star'] = dd.xpath('./p[@class="star"]/text()')[0].strip()
            item['time'] = dd.xpath('./p[@class="releasetime"]/text()')[0].strip()
            print(item)

    # def save_html(self,r_list):
    #     """数据处理功能函数"""
    #     item ={}
    #     for r in r_list:
    #         item['name'] = r[0].strip()
    #         item['star'] = r[1].strip()
    #         item['time'] = r[2].strip()
    #         print(item)

    def run(self):
        """程序入口函数 -整个程序的逻辑调用"""
        for offset in range(0,9,10):
            url = self.url.format(offset)
            self.get_html(url=url)
            # 控制数据抓取频率 ：uniform（）生成指定范围内的浮点数
            time.sleep(random.uniform(0,1))


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()





