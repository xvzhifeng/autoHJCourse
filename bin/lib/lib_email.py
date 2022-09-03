# coding = utf-8
import smtplib
import sys
import subprocess as sp
from email.mime.text import MIMEText

def send_email(to_email, title, content):
    # 设置服务器所需信息
    # 163邮箱服务器地址
    mail_host = 'smtp.163.com'
    # 163用户名
    mail_user = 'sumutest@163.com'
    # 密码(部分邮箱为授权码)
    mail_pass = 'ZKZSUBJTKCPSUXFA'
    # 邮件发送方邮箱地址
    sender = 'sumutest@163.com'
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = to_email

    # 设置email信息
    # 邮件内容设置
    message = MIMEText(content, 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = title
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]
    for receiver in receivers:
        message['To'] = receiver
        # 登录并发送邮件
        try:
            smtpObj = smtplib.SMTP()
            # 连接到服务器
            smtpObj.connect(mail_host, 25)
            # 登录到服务器
            smtpObj.login(mail_user, mail_pass)
            # 发送
            smtpObj.sendmail(
                sender, receivers, message.as_string())
            # 退出
            smtpObj.quit()
            print('success: to ' + receiver)
        except smtplib.SMTPException as e:
            print('error', e)  # 打印错误

if __name__ == "__main__":
    print(sys.argv)
    print(sys.argv[3:])
    send_email(sys.argv[3:],sys.argv[1],sys.argv[2])
    # command = '../bat/send_email.bat'
    # sp.call(command, shell=True)
    # send_email(["1277245228@qq.com"], "nas ip 监控情况", "test")