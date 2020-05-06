from queue import Queue
import requests
from threading import Thread,Lock
import time,re,json,random
from fake_useragent import UserAgent


class DoubanSpider:
    def __init__(self):
        self.url ='https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20'

        self.q = Queue()

        self.lock =Lock()

    def url_in(self):
        for start in range(0,692,20):
            page_url =self.url.format(start)
            self.q.put(page_url)
    def get_html(self,url):
        headers ={'User-Agent':UserAgent().random}
        html = requests.get(url=url,headers=headers).json()


    def parse_html(self):
       while True:
            self.lock.acquire()
            if not self.q.empty():
                url = self.q.get()
                self.lock.release()
                html = self.get_html(url=url)
                for one_film in html:
                    item = {}
                    item['rank'] = one_film['rank']
                    item['name'] = one_film['title']
                    item['time'] = one_film['release_date']
                    item['score'] = one_film['score']
                    print(item)
            else:
                self.lock.release()
                break

    def run(self):
        """程序入口函数"""
        self.url_in()
        t_list =[]
        for i in range(2):
            t = Thread(target=t_list)
            t.start()
            t.join()



if __name__ == '__main__':
    stare = time.time()
    spider = DoubanSpider()
    end = time.time()
    spider.run()
    print("time%s:"%(end-stare))










