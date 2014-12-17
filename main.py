# coding: UTF-8

from com.boccaro.utils import stringutil
from com.boccaro.network.email import easymail

if __name__ == '__main__':
    s = stringutil.StringUtil.getRandomString(1024)
#     f = open("out.txt", "w")
#     print >> f, s;
#     f.close()
    e = easymail.EasyMail()
    e.mailto_list = ['bxu@cybozu.net.cn']
    e.mail_host = "smtp.cybozu.net.cn"  # 设置服务器
    e.mail_user = "bxu@cybozu.net.cn"  # 用户名
    e.mail_pass = "cybozu201109"  # 口令 
    e.mail_postfix = "cybozu.net.cn"  # 发件箱的后缀
    e.mail_subject = 'size test1'
    e.mail_sender_name = 'Ach'
    e.mail_context = s
    e.send()
    pass
