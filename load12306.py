# -*- coding: utf-8 -*-
sql = '''
use blog;
'''

with open('data/12306.txt', 'r') as f:
    for line in f.readlines():
        # test /(\w+@\w+\.\w+).+(\w+@\w+\.\w+)[\r\n]/gm ?
        text = line.strip().split('----')
        sql += r'''
insert user (email, username, real_name, card_number, password, telphone) 
    VALUES (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`)''' % tuple(text)[:-1]

with open('data/12306.sql', 'w') as f:
    f.write(sql)
    print('sql生成成功')
