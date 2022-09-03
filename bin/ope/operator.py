import os
import sys
import subprocess as sp
import bin.lib.lib_log as log

path = os.getcwd()

def send_email():
   try:
       # print(path)
       # print(os.getcwd())  # 获得当前工作目录
       command = path + '\\bat\\send_email.bat'
       log.logger.debug(command)
       sp.call(command, shell=True)
   except Exception as e:
       log.logger.error(e)