# 模拟生产者
import redis
import json

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

json_obj = {'task': 'send_email','from':'guoxiaonao','to':'a@qq.com','content':'xxx' }

json_str =json.dumps(json_obj)

r.lpush('pypc',json_str)

