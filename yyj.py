#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class User(Base):
    # 表名称
    __tablename__ = 'user'

    # 表结构
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    name = Column(String(20))
    books = relationship('Book')

    def __repr__(self):
        return "<User(id=%s, name='%s')>" % (self.id, self.name)


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    name = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.id'))


engine = create_engine('mysql+pymysql://root@localhost:3306/test?charset=utf8mb4&use_unicode=0')

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Table.delete().where()
# session.execute('DROP table %s;DROP table %s;' % ('user', 'book'))

#
session.add(User(id=1, name='yyj'))
session.add(User(id=2, name='zsf'))
session.add(User(id=5, name='Bob'))

session.add(Book(id=1, name="🚀js是世界上最好的语言", user_id=1))
session.add(Book(id=2, name="🚀python从入门到放弃", user_id=2))
session.add(Book(id=3, name="🚀php 才是最好的语言", user_id=5))

# session.rollback()
session.commit()

for instance in session.query(User).order_by(User.id):
    print(instance.id, instance.name)

session.close()
