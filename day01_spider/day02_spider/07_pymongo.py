import pymongo

conn = pymongo.MongoClient('localhost', 27017)
db = conn['maoyandb']
myset = db['maoyanset']
myset.insert_one({'name': '战狼', 'star': '123', 'time': '2017-2-15'})
