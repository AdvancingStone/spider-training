from pymongo import MongoClient

conn = MongoClient('mongodb://localhost:27017')
# 创建一个 avIdol 数据库，如果 mongodb 没有会自行创建
db = conn.avIdol

# db.col.insert({"name": '波多野結衣', 'bwh': '{ "b": 90, "w": 59, "h": 85}' , 'age': 30})
# print(db.col.find_one())

db.col.insert_many([
    {"name": '波多野結衣', 'bwh': '{ "b": 90, "w": 59, "h": 85}' , 'age': 30},
    {"name": '吉泽明步', 'bwh': '{ "b": 86, "w": 58, "h": 86}' , 'age': 35},
    {"name": '桃乃木香奈', 'bwh': '{ "b": 80, "w": 54, "h": 80}' , 'age': 22},
    {"name": '西宫梦', 'bwh': '{ "b": 85, "w": 56, "h": 86}' , 'age': 22},
    {"name": '松下纱荣子', 'bwh': '{ "b": 88, "w": 57, "h": 86}' , 'age': 28}
])

for item in db.col.find():
    print(item)

print(db.col.find({'name' : '松下纱荣子'}))
db.col.update_many({'name':'吉泽明步'},{'$set':{'name':'苍井空'}})
db.col.delete_one({'name' : '吉泽明步'})
db.col.delete_many({'name':'西宫梦'})
# 删除所有数据
db.col.delete_many({})

