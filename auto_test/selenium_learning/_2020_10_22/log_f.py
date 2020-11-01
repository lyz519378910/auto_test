
import logging
import time

logger = logging.getLogger()                                    #建立对象

date_now = time.strftime('%Y-%m-%d', time.localtime())
log_path = 'D:\\Python\\report_python'                          #日志位置
log_name = log_path + "/" + 'log_' + date_now + '.log'          #日志名称，将时间加入文件

fh = logging.FileHandler(log_name)                               #创建文件
ch = logging.StreamHandler()                                     #创建控制台
fm = logging.Formatter('%(asctime)s|%(message)s|%(levelname)s')  #格式化

fh.setFormatter(fm)                                              #对文件格式
ch.setFormatter(fm)                                              #对控制台格式
logger.addHandler(fh)                                            #文件句柄加入logger
logger.addHandler(ch)                                            #控制台句柄加入logger
logger.setLevel(logging.DEBUG)                                   #设置打印级别
logger.info('info message')                                      #输入info
logger.removeHandler(fh)                                         #删除文件句柄
logger.removeHandler(ch)                                         #移除控制台对象
fh.close()                                                       #关闭文件













#
#
# logging.basicConfig(format=('%(asctime)s|%(message)s|%(levelname)s'),level=logging.DEBUG)
# try:
#     print(2/0)
# except:
#     logging.debug('debug-message')
#     logging.info('info-message')
#     logging.warning('warning-message')
#     logging.error('error-message')










