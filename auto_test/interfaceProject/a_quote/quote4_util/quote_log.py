import logging
import time

# import sys
# import os
#
# base_path = os.getcwd()
# sys.path.append(base_path)

class AutoLog:

    def __init__(self):
        self.logger = logging.getLogger()

    def set_log(self,message,level_param='info'):
        try:
            date_now = time.strftime('%Y-%m-%d', time.localtime())
##################################################################################################################
            #记得改日志路径、名称
            log_path = '../../quote1_log'  # 日志位置
            log_name = log_path + "/" + 'log_' + date_now + '.log'  # 日志名称，将时间加入文件
##################################################################################################################
            fh = logging.FileHandler(log_name)  # 创建文件
            ch = logging.StreamHandler()  # 创建控制台
            fm = logging.Formatter('%(levelname)s|%(asctime)s|%(message)s')  # 格式化

            fh.setFormatter(fm)  # 对文件格式
            ch.setFormatter(fm)  # 对控制台格式
            self.logger.addHandler(fh)  # 文件句柄加入logger
            self.logger.addHandler(ch)  # 控制台句柄加入logger
            self.logger.setLevel(logging.DEBUG)  # 设置打印级别

            if level_param == 'debug':
                self.logger.debug(message)
            elif level_param == 'info':
                self.logger.info(message)
            elif level_param == 'error':
                self.logger.error(message)
            elif level_param == 'warning':
                self.logger.warning(message)

            self.logger.removeHandler(fh)  # 删除文件句柄
            self.logger.removeHandler(ch)  # 移除控制台对象
        except:
            print('file exception')
        finally:
            # fh.close()
            pass
# if __name__ == '__main__':
#     log = AutoLog()
#     url = 'www.baidu.com'
#     log.set_log('打开' + url,'info')