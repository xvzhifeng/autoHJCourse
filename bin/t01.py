import os
import subprocess as sp
import sys
import bin.ope.operator as ope
import bin.lib.lib_log as log

if __name__ == "__main__":
    print(os.path.dirname(os.path.abspath(__file__)))
    # ope.send_email()
    log.logger.debug("test")
    # os.getcwd()  # 获得当前工作目录
    # print(os.path.abspath('..') + '\\bat\\send_email.bat')
    # command = os.path.abspath('..') + '\\bat\\send_email.bat'
    # os.system(command)
    c = 'python ' + os.path.abspath('..') + "/lib/lib_email.py 沪江刷课 '刷课程序卡住了，需要处理！！！'  xvzhifeng@qq.com"
    # print(c)
    # os.system(c)
    # sp.call(command, shell=True)
    # send_email(["1277245228@qq.com"], "nas ip 监控情况", "test")