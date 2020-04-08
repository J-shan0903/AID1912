import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

# 通用命令演示
# key_list = r.keys('*')
# for key in key_list:
#     print(key)

# 返回值1 代表存在 0 表示不存在
# print(r.exists('i1'))

# 1.list
# 字符串返回值为字节串
# r.lpush('pyl1','a','b','c')
# print(r.lrange('pyl1',0,-1))#[b'c', b'b', b'a']

# 返回值为字节串
# print(r.rpop('pyl1'))  # b'a'
# print(r.lpop('pyl1'))  # b'c'

# print(r.ltrim('pyl1', 0, 1))  # True
# print(r.lrange('pyl1', 0, -1))

# 2.string
# r.set('pyusername','guoxiaonao')
# print(r.get('pyusername'))
#
# r.mset({'pyusername1':'wanglaoshi','pyusername2':'lvzlaoshi'})
# print(r.mget('pyusername1','pyusername2'))

# r.incr('pyage')
# # 返回值为 int
# print(r.incrby('pyage',10))

# 3.hash
# r.hset('pyh1','name','guoxiaonao')
# print(r.hget('pyh1','name'))

# r.hmset('pyh1',{'age':18,'desc':'hahah'})
# print(r.hgetall('pyh1'))

#4. 集合
# r.sadd('pys1','a','b','c','d','e')
# # 返回值python的集合 {b'e', b'c', b'd', b'a', b'b'}
# print(r.smembers('pys1'))
#
# # 返回值字节串
# m1 =r.spop('pys1')
# print(m1)

# r.sadd('pys2','a','b','c','d')
# # {b'a', b'b', b'd'}
# print(r.sinter('pys1','pys2'))

# 5.有序集合
# r.zadd('pyz1',{'guoxiaonao':8000,'lvz':12000})
# print(r.zrange('pyz1',0,-1,withscores=True))

r.zadd('pyz2',{'guoxiaonao':6000})
r.zinterstore('pyz3',('pyz1','pyz2'),aggregate='max')
print(r.zrange('pyz3',0,-1,withscores=True))