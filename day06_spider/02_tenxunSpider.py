from urllib import parse

import requests,time,random
from threading import Thread, Lock
from queue import Queue
from fake_useragent import UserAgent

class TencenSpider:
    def __init__(self):
        self.one_url ='https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1563912271089&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.two_url ='https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1563912374645&postId={}&language=zh-cn'

        self.one_q =Queue()
        self.two_q =Queue()
        self.lock1 = Lock()
        self.lock2 = Lock()

        self.count = 0

    def get_html(self,url):
        headers ={'User-Agent':UserAgent.rendom()}
        self.url =requests.get(url=url,headers=headers).text
    def url_in(self):
        """让一级页l地质入队列："""
        keyword = input("请输入职位类别：")
        keyword = parse.quote(keyword)
        for index in range(1,total+1):
            one_url = self.one_url.format(keyword,index)
            self.one_q.put(one_url)
    def get_total(self,keyword):
        url = self.one_url.format(keyword,1)
        html = self.get_html(url=url)
        cou =html['Date']['Count']
