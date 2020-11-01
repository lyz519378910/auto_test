import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "lj2899366@qq.com"  # 用户名
mail_pass = "tcxfccrafiyecaij"  # 口令

sender = 'lj2899366@qq.com'
receivers = ['lj2899366@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

send_subject = '带附件的邮件'
send_file = open('/auto_test/seleniumProject/crm/crm_report/report_crm.html', 'rb').read()

msg = MIMEText(send_file, 'base64', 'utf-8')
# 邮件内容
msg['Content-Type'] = 'application/octet-stream'
msg['Content-Disposition'] = 'attachment;filename="Test_1230_07_txtData"'


msg['From'] = Header("菜鸟教程", 'utf-8')
msg['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
msg['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL('smtp.exmail.qq.com')
    smtpObj.connect(mail_host, 465)  # 25 为 SMTP 端口号

    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, msg.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)
    print("Error: 无法发送邮件")