#! /usr/bin/python
# coding=utf-8

from email.message import Message
import smtplib


class SmtpServer(object):
    def __init__(self, smtp_server, sendmail_addr, user_name, user_password):
        self.server = smtp_server
        self.user_name = user_name
        self.user_password = user_password
        self.from_addr = sendmail_addr
        self.sm = self.smtp_login()

    def smtp_login(self):
        s = smtplib.SMTP(self.server, port=25)
        s.login(self.user_name, self.user_password)
        return s

    def message_to_string(self, recever_addr, title, text):
        message = Message()
        message['From'] = self.from_addr
        message['Subject'] = title
        message['To'] = recever_addr
        message.set_payload(text, charset='utf-8')
        return message.as_string()

    def send_message(self, to_addr, title, text):
        self.sm.sendmail(self.from_addr, to_addr, self.message_to_string(to_addr, title, text))

    def stmp_conn_close(self):
        self.sm.close()


if __name__ == '__main__':
    smtp_server = 'smtp.server.com'
    sendmail_addr = 'allen@clisp.cn'
    user_name = "allen@clisp.cn"
    user_password = "????????"
    test_server = SmtpServer(smtp_server, sendmail_addr, user_name, user_password)
    test_server.send_message('12345678@163.com', "test", "test")
    test_server.stmp_conn_close()
