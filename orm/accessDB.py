# 数据库连接，字段类型
from sqlalchemy import create_engine, String, Integer, Column
# 创建表的基类
from sqlalchemy.ext.declarative import declarative_base
# 连接会话
from sqlalchemy.orm import sessionmaker

db_name = 'mysql+mysqlconnector://hive:q1w2e3r4@spark3:3306/gmall'
Base = declarative_base()


# 继承基类
class User(Base):
    __tablename__ = 'user'  # DB中表名
    id = Column(Integer, primary_key=True)  # 主键
    name = Column(String(50))  # 栏位，对应mysql中varchar


engine = create_engine(db_name)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


