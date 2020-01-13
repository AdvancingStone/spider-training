import pymysql

# 使用 connect 方法，传入数据库地址，账号密码，数据库名就可以得到你的数据库对象
db = pymysql.connect("localhost", 'root', '', 'avidol')

# 接着我们获取 cursor 来操作我们的 avIdol 这个数据库
cursor = db.cursor()

sql = """create table if not exists beautyGirls (
    name varchar(20) not null,
    age int
    )"""
cursor.execute(sql)

sql2 = "insert into beautyGirls(name, age) values('brother', 18)"

try:
    cursor.execute(sql2)
    db.commit()
except:
    db.rollback()

db.close()
