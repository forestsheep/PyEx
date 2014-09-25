# coding: UTF-8
'''
Created on 2014-9-25

@author: bxu
'''
import smtplib
from email.mime.text import MIMEText


def sendMailTest():
    e = EasyMail()
    e.mailto_list = ['forestsheep911@163.com'] 
    e.mail_host = "smtp.163.com"  # 设置服务器
    e.mail_user = "forestsheep"  # 用户名
    e.mail_pass = "xxx"  # 口令 
    e.mail_postfix = "163.com"  # 发件箱的后缀
    e.mail_context = 'abcdefghijklmnopqrstuvwxyz'
    e.send()

class EasyMail(object):
    mailto_list = None
    mail_host = None
    mail_user = None
    mail_pass = None
    mail_postfix = None
    mail_context = None

    def __init__(self):
        pass
    
    def send(self):
        if self.send_mail(self.mailto_list, "hello", self.mail_context):
            print 'successed'
        else:
            print 'failed'
        
    def send_mail(self, to_list, sub, content):
        me = "hello" + "<" + self.mail_user + "@" + self.mail_postfix + ">"
        msg = MIMEText(content, _subtype='plain', _charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
            server = smtplib.SMTP()
            server.connect(self.mail_host)
    #         server.starttls()
            server.login(self.mail_user, self.mail_pass)
            server.sendmail(me, to_list, msg.as_string())
            server.close()
            return True
        except Exception, e:
            print str(e)
            return False