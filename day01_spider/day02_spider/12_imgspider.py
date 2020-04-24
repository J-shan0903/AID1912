
import requests
import os

url ='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1587471304041&di=6972d7fafa76a7c95a371e500b7ddf8c&imgtype=0&src=http%3A%2F%2Fdingyue.nosdn.127.net%2FGJf%3D1TlLkuDKIhXDkXjTQ2ovC9SEPs9EwsEWhRX3fvg9E1528245818078.jpg'
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

html = requests.get(url=url,headers=headers).content
directory ='/home/tarena/images/赵丽颖'
if not os.path.exists(directory):
    os.makedirs(directory)



with open('英.jpg','wb') as f:
    f.write(html)