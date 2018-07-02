# -*- coding: utf-8 -*-
import re
from datetime import datetime

count = 0
now = datetime.utcnow()
now = str(now)

sql = '''
USE blog;
DELETE FROM user;

INSERT INTO user (`email`, `username`, `real_name`, `card_number`, `password`, `telphone`, `create_time`)
VALUES
'''

with open('data/12306.txt', 'r') as f:
    for line in f.readlines():
        # test /(\w+@\w+\.\w+).+(\w+@\w+\.\w+)[\r\n]/gm ?
        text = line.strip()
        text = re.sub(r'\\+', '', text)
        row = text.split('----')[: -1]
        row.append(now)
        row[1] = row[0]
        count += 1
        sql += r'''('%s', '%s', '%s', '%s', '%s', '%s', '%s'),
''' % tuple(row)

sql = sql[: -1] + ';'

with open('data/12306.sql', 'w') as f:
    f.write(sql)

print('sql生成成功, 一共 %d 条记录' % count)
