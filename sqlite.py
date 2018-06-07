#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('data/sqlite.db')

cursor = conn.cursor()

# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#
# cursor.execute("insert into user (id, name) values ('2', 'zsf')")
# cursor.execute("insert into user (id, name) values ('1', 'yyj')")

cursor.execute('select * from user where id in (?, ?)', ('2', '1'))
values = cursor.fetchall()
print(values)

cursor.close()

conn.commit()

conn.close()
