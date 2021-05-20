# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText


class SendEmail:
    global send_user
    global email_host
    global email_password
    email_host = 'smtp.qq.com'
    send_user = '519328539@qq.com'
    email_password = 'jqmarfxppnmzbjhc'

# 构建模块
    def send_email(self, user_list, sub, content):
        user = '刘斌' + '<' + send_user + '>'
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['from'] = user
        message['to'] = ';'.join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, email_password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def send_main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        pass_result = '%.2f%%' % (pass_num / count_num * 100)
        fail_result = '%.2f%%' % (fail_num / count_num * 100)
        user_list = ['13215207907@163.com']
        sub = '接口自动化测试报告'
        content = '此次运行接口个数%s个，通过个数为%s个，失败个数为%s个，通过率为%s，失败率为%s' % (count_num, pass_num, fail_num,
                                                                   pass_result, fail_result)
        self.send_email(user_list, sub, content)


if __name__ == '__main__':
    sen = SendEmail()
    sen.send_main()
