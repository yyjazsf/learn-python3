# -*- coding: utf-8 -*-
from datetime import datetime, timezone

now = datetime.utcnow()
now = str(now)

sql = '''
USE blog;
DELETE FROM user;
'''

with open('data/12306.txt', 'rb') as f:
    for line in f.readlines():
        # test /(\w+@\w+\.\w+).+(\w+@\w+\.\w+)[\r\n]/gm ?
        row = line.decode('utf8', 'ignore').strip().split('----')[:-1]
        row.append(now)
        row[1] = row[0]
        sql += r'''
INSERT INTO user (`email`, `username`, `real_name`, `card_number`, `password`, `telphone`, `create_time`)
VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');''' % tuple(row)

with open('data/12306.sql', 'w') as f:
    f.write(sql)

print('sql生成成功')
