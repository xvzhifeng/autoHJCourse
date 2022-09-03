import os
import subprocess as sp
import sys
import bin.ope.operator as ope

if __name__ == "__main__":
    ope.send_email()
    os.getcwd()  # 获得当前工作目录
    print(os.path.abspath('..') + '\\bat\\send_email.bat')
    # command = os.path.abspath('..') + '\\bat\\send_email.bat'
    # os.system(command)
    c = 'python ' + os.path.abspath('..') + "/lib/lib_email.py 沪江刷课 '刷课程序卡住了，需要处理！！！'  xvzhifeng@qq.com"
    # print(c)
    # os.system(c)
    # sp.call(command, shell=True)
    # send_email(["1277245228@qq.com"], "nas ip 监控情况", "test")