#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


smtp_server = 'smtp.gmail.com'
mail_addr = 'yyjzry@gmail.com'
mail_pwd = ''

mail_to_addr = '602988068@qq.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % mail_addr)
msg['To'] = _format_addr('管理员 <%s>' % mail_to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 587)  # SMTP协议默认端口是25
server.starttls()
server.set_debuglevel(1)
server.login(mail_addr, mail_pwd)
server.sendmail(mail_addr, [mail_to_addr], msg.as_string())
server.quit()
