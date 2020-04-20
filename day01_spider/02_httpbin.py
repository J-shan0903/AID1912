"""
测试网站‘http://httpbin.org/get’发送请求
"""

import requests

url = 'http://httpbin.org/get'
html = requests.get(url=url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}).text
print(html)
