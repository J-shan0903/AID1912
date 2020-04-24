"""
免费代理IP测试
"""
import requests

url = 'http://httpbin.org/get'
headers ={'User-Agent':'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'}
# proxies ={
#     'http':'http://171.35.168.177:9999',
#     'https':'https://171.35.168.177:9999'
# }
# html = requests.get(url=url,headers=headers,proxies=proxies).text
# print(html)

proxies = {
    'http': 'http://112.85.164.220:9999',
    'https': 'https://112.85.164.220:9999'
}
html = requests.get(url, proxies=proxies, headers=headers, timeout=5).text
print(html)