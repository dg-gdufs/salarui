# encoding: utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class Mail():
    
    def __init__(self, sender='', receivers=[], passwd='', smtp='', subject='', text='') -> None:
        self.msgRoot = MIMEMultipart()
        self.msgRoot['Subject'] = subject
        self.msgRoot['From'] = sender
        self.msgRoot['To'] = ','.join(receivers)
        self.msgRoot.attach(MIMEText(text, _charset="utf-8"))
        self.sender = sender
        self.receivers = receivers
        self.passwd = passwd
        self.smtp = smtp

    def attach_file(self, pathlist):
        if not isinstance(pathlist, list):
            pathlist = [pathlist]           
        for path in pathlist:
            part = MIMEApplication(open(path, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=path.split('\\')[-1])
            self.msgRoot.attach(part)

    def send(self):
        try:
            s = smtplib.SMTP_SSL(self.smtp, 465)
            s.login(self.sender, self.passwd)
            s.sendmail(self.sender, self.receivers, self.msgRoot.as_string())
            print("发送成功")
            s.quit()
        except smtplib.SMTPException as e:
            print("发送失败 ==> {}".format(e))