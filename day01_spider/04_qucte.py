
import requests
from urllib import parse

# 1拼接url地址
keyworld = input("请输入关键字：")
params = parse.quote(keyworld)
url = 'http://www.baidu.com/s?wd={}'.format(params)
headers ={'User-Agent':'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'}
# 2发送请求 获取响应内容
html = requests.get(url=url,headers=headers).text

# 3保存在本地文件
filename = '{}.html'.format(keyworld)
with open(filename,'w',encoding='utf-8') as f:
    f.write(html)