from selenium import webdriver
import unittest, time
from HTMLTestRunner import HTMLTestRunner
import unittestCase
from unittestCase import ParametrizedTestCase
from unittestCase import TestOne
from getData_17_5_26 import getData_17_5_26
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


def sendFile(filename,filepath):
    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户/密码
    user = 'shixuehuaireal@163.com'
    password = 'Wangyi123456'
    # 发送邮箱
    sender = 'shixuehuaireal@163.com'
    # 接收邮箱
    receiver = '18303974@qq.com'
    # 发送邮件主题
    subject = '这是一个带附件的邮件_石雪怀测试文件'

    # 发送的附件
    sendfile = open(filepath, 'rb').read()

    # 创建一个带附件的实例
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = Header(subject, 'utf-8')                         # 定义邮件标题
    # 需要添加这两个赋值
    msgRoot['From'] = sender
    msgRoot['To'] = receiver

    # 邮件正文内容
    msgRoot.attach(MIMEText('你好，石雪怀测试文件', 'plain', 'utf-8'))

    # 构造附件
    att = MIMEText(sendfile, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename='+'"'+filename+'"'
    msgRoot.attach(att)

    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()


if __name__ == "__main__":
    '''测试'''
    file_path = 'D:\\code\\python\\FormalSAST\\shhe_result\\testcase2'
    answer_path = 'D:\\code\\python\\FormalSAST\\shhe_result\\anwser\\anwser2'
    '''Question1'''
    new_results = getData_17_5_26.getTheLastResults(file_path)
    print('this is the new results:'+str(len(new_results)))
    print(new_results)
    '''Question2'''
    getData_17_5_26.find_path_all(4,0,file_path)
    '''Question3'''
    suite = unittest.TestSuite()  
    suite.addTest(ParametrizedTestCase.parametrize(TestOne, results=new_results,answer_path=answer_path)) 

    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # 定义报告存放路径
    # filename = './report/result.html'
    filepath = 'D:/code/python/FormalSAST/report/shixuehuai-' + now + '-result.html'
    filename = 'shixuehuai-' + now + '-result.html'
    fp = open(filepath, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,                  # 指定测试报告文件
                        title='百度搜索测试报告',        # 定义测试报告标题 
                        description='用例执行状况：')    # 定义测试报告副标题
    runner.run(suite)    # 运行测试用例
    fp.close()  # 关闭报告文件

    sendFile(filename,filepath)