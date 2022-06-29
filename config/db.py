from sqlalchemy import create_engine, MetaData
import pymysql

engine = create_engine("mysql+pymysql://root@localhost:3306/test")
# engine = create_engine("sqlite:///test.db")
conn = engine.connect()
meta = MetaData()


# # database connection
# connection = pymysql.connect(host="localhost", port=8889, user="root", passwd="root", database="SELECTION_DB")
# cursor = connection.cursor()
# # some other statements  with the help of cursor
# connection.close()