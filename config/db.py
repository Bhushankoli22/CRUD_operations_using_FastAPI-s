from sqlalchemy import create_engine, MetaData

# engine = create_engine("mysql+pymysql://root@localhost: 3306/test")
engine = create_engine("sqlite:///name.db")
conn = engine.connect()
meta = MetaData()