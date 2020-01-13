import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('xsb.csv')

engine = create_engine('mysql://root@localhost/xsb?charset=utf8')
# 当engine连接的时候我们就插入数据
with engine.connect() as conn, conn.begin():
    df.to_sql('xsb', conn, if_exists='replace')