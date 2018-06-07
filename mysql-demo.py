#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import (connection, errorcode)

try:
    cnx = connection.MySQLConnection(user='root', password='',
                                     host='127.0.0.1',
                                     database='test')
    cursor = cnx.cursor()
    # create
    # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    # cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'yyj'])
    # cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'zsf'])
    # print(cursor.rowcount)
    # cnx.commit()

    # query
    cursor.execute('select * from user where id in (%s, %s)', ('1', '2'))
    values = cursor.fetchall()
    print(values)
    cursor.close()
    cnx.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("账号密码错误")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
