__author__ = 'zhouzhishuai'

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from json import JSONEncoder


# class init method
def __init__():






# sender = 'from@runoob.com'
# receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
sender = 'zhouzhishuai@le.com'
receivers = ['zhouzhishuai@le.com']

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
subject = '【主题写这里】'

# message = MIMEText('邮件内容', 'plain', 'utf-8')
# message['From'] = Header(sender, 'utf-8')
# message['To'] =  Header(receivers, 'utf-8')
# message['Subject'] = Header(subject, 'utf-8')

def sendmail():
	message = MIMEMultipart()
	message["Subject"] = subject
	msgBody = "Failed/Error task in last 24 hours. "
	message['From'] = sender
	message['To'] = ';'.join(receivers)
	message.attach(MIMEText(msgBody, 'plain'))

	#添加附件
	# message.attach(attachment)

	try:
	    server = smtplib.SMTP('mail.le.com','25')
	    # server.ehlo()
	    # server.login()
	    server.sendmail(sender, receivers, message.as_string())
	    print("邮件发送成功")
	except smtplib.SMTPException:
	    print("Error: 无法发送邮件")
	finally:
		server.quit()


if __name__ == "__main__":
	print("this is main..")
	obj = smtpTest()

