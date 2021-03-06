import csv
import time
import random
import re
import requests

class MaoyanSpider:
    def __init__(self):
        """定义常用变量"""
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    #     打开文件、
        self.f = open('maoyan.csv','w',newline='')
        self.writer = csv.writer(self.f)
        self.all_list =[]

    def get_html(self,url):
        """请求功能函数 -获取html"""
        html = requests.get(url=url,headers=self.headers).text

        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self,html):
        """解析功能函数 -数据解析提取"""
        regex = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
        pattern = re.compile(regex,re.S)
        r_list = pattern.findall(html)
        self.save_html(r_list)

    def save_html(self,r_list):
        """数据处理功能函数"""
        for r in r_list:
            t = (r[0].strip(),r[1].strip(),r[2].strip())
            self.all_list.append(t)
            print(t)

    def run(self):
        """程序入口函数 -整个程序的逻辑调用"""
        for offset in range(0,9,10):
            url = self.url.format(offset)
            self.get_html(url=url)
            # 控制数据抓取频率 ：uniform（）生成指定范围内的浮点数
            time.sleep(random.uniform(0,1))
        self.writer.writerows(self.all_list)
        self.f.close()

if __name__ == '__main__':
    spider =MaoyanSpider()
    spider.run()





