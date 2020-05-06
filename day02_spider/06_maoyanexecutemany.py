# import pymysql
# import time
# import random
# import re
# import requests
#
# class MaoyanSpider:
#     def __init__(self):
#         """定义常用变量"""
#         self.url = 'https://maoyan.com/board/4?offset={}'
#         self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
#         self.db = pymysql.connect('127.0.0.1', 'mysql', '123456', 'maoyandb', charset='utf8')
#         self.cur = self.db.cursor()
#         self.all_list = []
#
#
#     def get_html(self,url):
#         """请求功能函数 -获取html"""
#         html = requests.get(url=url,headers=self.headers).text
#
#         # 直接调用解析函数
#         self.parse_html(html)
#
#     def parse_html(self,html):
#         """解析功能函数 -数据解析提取"""
#         regex = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
#         pattern = re.compile(regex,re.S)
#         r_list = pattern.findall(html)
#         self.save_html(r_list)
#
#     def save_html(self,r_list):
#         """数据处理功能函数"""
#         for r in r_list:
#             t = (r[0].strip(), r[1].strip(), r[2].strip())
#             self.all_list.append(t)
#
#     def run(self):
#         """程序入口函数 -整个程序的逻辑调用"""
#         for offset in range(0,49,10):
#             url = self.url.format(offset)
#             self.get_html(url=url)
#             # 控制数据抓取频率 ：uniform（）生成指定范围内的浮点数
#             time.sleep(random.uniform(1,2))
#         ins = 'insert into maoyantab values(%s,%s,%s)'
#         self.cur.executemany(ins,self.all_list)
#         self.db.commit()
#         self.db.close()
#         self.cur.close()
#
#
# if __name__ == '__main__':
#     spider =MaoyanSpider()
#     spider.run()
#
#
#
#
#
"""
猫眼电影top100抓取（电影名称、主演、上映时间）
使用 executemany() - 减少了数据库IO次数,效率高
"""
import requests
import re
import time
import random
import pymysql

class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        # self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
        self.db = pymysql.connect('127.0.0.1', 'mysql', '123456', 'maoyandb', charset='utf8')
        self.cur = self.db.cursor()
        self.all_list = []

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """解析提取数据"""
        regex = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        # r_list: [('活着','牛犇','2000-01-01'),(),(),...,()]
        self.save_html(r_list)

    def save_html(self, r_list):
        """数据处理函数"""
        for r in r_list:
            t = ( r[0].strip(), r[1].strip(), r[2].strip() )
            self.all_list.append(t)

    def run(self):
        """程序入口函数"""
        for offset in range(0, 41, 10):
            url = self.url.format(offset)
            self.get_html(url=url)
            # 控制数据抓取频率:uniform()生成指定范围内的浮点数
            time.sleep(random.uniform(1,2))
        # 一次性存入MySQL数据库
        ins = 'insert into maoyantab values(%s,%s,%s)'
        self.cur.executemany(ins, self.all_list)
        self.db.commit()
        self.cur.close()
        self.db.close()

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()


