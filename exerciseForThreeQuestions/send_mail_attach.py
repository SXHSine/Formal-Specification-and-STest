import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱服务器
smtpserver = 'smtp.163.com'
# 发送邮箱用户/密码
user = 'shixuehuaireal@163.com'
password = 'Wangyi123456'
# 发送邮箱
sender = 'shixuehuaireal@163.com'
# 接收邮箱
receiver = '841319534@qq.com'
# 发送邮件主题
subject = '这是一个带附件的邮件'

# 发送的附件
sendfile = open('D:/code/python/FormalSAST/report/baidu-2017-06-07 20-00-58-result.html', 'rb').read()

# 创建一个带附件的实例
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = Header(subject, 'utf-8')                         # 定义邮件标题
# 需要添加这两个赋值
msgRoot['From'] = sender
msgRoot['To'] = receiver

# 邮件正文内容
msgRoot.attach(MIMEText('你好，今天是星期六，天气不错，适合出去玩!', 'plain', 'utf-8'))

# 构造附件
att = MIMEText(sendfile, 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="help.txt"'
msgRoot.attach(att)

# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()