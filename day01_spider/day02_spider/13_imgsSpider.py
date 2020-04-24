import requests
import re
import time
import random
from fake_useragent import UserAgent
import os
from urllib import parse


class BaiduImageSpider(object):
    def __init__(self):
        self.url = 'https://image.baidu.com/search/index?tn=baiduimage&word={}'
        self.word = input('请输入关键字:')
        self.directory = '/home/tarena/images/{}/'.format(self.word)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        self.i = 1

    def get_images(self, one_url):
        # 使用随机的User-Agent
        headers = {'User-Agent': UserAgent().random}
        one_html = requests.get(url=one_url, headers=headers).text
        regex = '"thumbURL":"(.*?)"'
        pattern = re.compile(regex, re.S)
        image_src_list = pattern.findall(one_html)
        for image_src in image_src_list:
            self.save_image(image_src)
            # 控制爬取速度
            time.sleep(random.uniform(0, 1))

    def save_image(self, image_src):
        # 每次请求使用随机的User-Agent
        headers = {'User-Agent': UserAgent().random}
        image_html = requests.get(url=image_src, headers=headers).content
        filename = '{}{}_{}.jpg'.format(self.directory, self.word, self.i)
        with open(filename, 'wb') as f:
            f.write(image_html)
        print(filename, '下载成功')
        self.i += 1

    def run(self):
        params = parse.quote(self.word)
        one_url = self.url.format(params)
        self.get_images(one_url)


if __name__ == '__main__':
    spider = BaiduImageSpider()
    spider.run()