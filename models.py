from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    like = Column(Boolean, nullable=False)
    status = Column(Integer, nullable=False)


class Contact(Base):
    __tablename__ = 'Contact'
    id=Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    userID = Column(Integer, primary_key=False)
    userToID = Column(Integer, nullable=False)




