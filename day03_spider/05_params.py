
import requests

url = 'http://tieba.baidu.com/f?'
params ={
    'wd':'赵丽颖吧','pn':50
}
headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'}

html = requests.get(url=url,params=params,headers=headers).content.decode('utf-8','ignore')

print(html)


