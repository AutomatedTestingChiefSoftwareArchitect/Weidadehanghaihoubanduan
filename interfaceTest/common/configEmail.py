import os
import win32com.client as win32
import datetime
import readConfig
import getpathInfo
from common.Log import logger


read_conf = readConfig.ReadConfig()
subject = read_conf.get_email('subject')#从配置文件中读取，邮件主题
app = str(read_conf.get_email('app'))#从配置文件中读取，邮件类型
addressee = read_conf.get_email('addressee')#从配置文件中读取，邮件收件人
cc = read_conf.get_email('cc')#从配置文件中读取，邮件抄送人
mail_path = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')#获取测试报告路径
logger = logger

class send_email():
    def outlook(self):
        olook = win32.Dispatch("%s.Application" % app)
        mail = olook.CreateItem(win32.constants.olMailItem)
        mail.To = addressee # 收件人
        mail.CC = cc # 抄送
        mail.Subject = str(datetime.datetime.now())[0:19]+'%s' %subject#邮件主题
        mail.Attachments.Add(mail_path, 1, 1, "myFile")
        content = """
                    执行测试中……
                    测试已完成！！
                    生成报告中……
                    报告已生成……
                    报告已邮件发送！！
                    """
        mail.Body = content
        mail.Send()
        print('send email ok!!!!')
        logger.info('send email ok!!!!')


if __name__ == '__main__':# 运营此文件来验证写的send_email是否正确
    print(subject)
    send_email().outlook()
    print("send email ok!!!!!!!!!!")