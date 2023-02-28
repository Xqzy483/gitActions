import smtplib
from email.header import Header
from email.mime.text import MIMEText

if __name__ == '__main__':
    # 创建 SMTP 对象test1.
    smtp = smtplib.SMTP()
    # 连接（connect）指定服务器
    smtp.connect("smtp.163.com", port=25)
    # 登录，需要：登录邮箱和授权码
    smtp.login(user="m13937681691@163.com", password="OCSMJCNZMJATLPAN")

    # 构造MIMEText对象，参数为：正文，MIME的subtype，编码方式
    message = MIMEText('atukoon 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("fairly", 'utf-8')  # 发件人的昵称
    message['To'] = Header("Qyy", 'utf-8')  # 收件人的昵称
    message['Subject'] = Header('Python SMTP 邮件测试', 'utf-8')  # 定义主题内容
    print(message)

    smtp.sendmail(from_addr="m13937681691@163.com", to_addrs="1228383439@qq.com", msg=message.as_string())