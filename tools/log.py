"""https://guobaoyuan.gitee.io/new_book/Python/20-2%20logging.html"""
import logging
from logging import handlers


class MyLog(object):
    def __init__(self):
        self.my_logger = logging.getLogger("phil")  # # 获取logger并命名,不然就是默认名root.也是实例化getLogger,日志器的实例化 phil 是记录者
        self.fh = logging.FileHandler(filename='../log/test.log', encoding='utf-8')  # handler类文件句柄 输出到文件

        # backupCount 是保留日志的文件个数 0 不会自动删除文件的 "S"：Second 秒
        # "M"：Minutes 分钟
        # "H"：Hour 小时
        # "D"：Days 天
        # "W"：Week day（0 = Monday）
        # "midnight"：Roll over at midnigh
        # interval 是间隔时间单位的个数，指等待多少个 when 的时间后

        # self.fh = logging.handlers.TimedRotatingFileHandler(filename="../log/test.log", when="D", interval=1,
        #                                                     backupCount=0, encoding='utf-8')
        self.sh = logging.StreamHandler()  # 输出到控制台
        self.fm = logging.Formatter(
            '%(asctime)s - %(name)s-%(module)s-%(filename)s-%(levelname)s-%(lineno)d-%(message)s')  # 格式器 输出样式
        self.my_logger.setLevel(logging.DEBUG)  # 全局设置格式,一般设置为error
        # fh.setLevel(logging.DEBUG) 对某个文件设置格式
        self.fh.setFormatter(self.fm)  # 给内容绑定格式
        self.sh.setFormatter(self.fm)
        self.my_logger.addHandler(self.fh)  # 给日志器绑定日志输出的方向及内容
        self.my_logger.addHandler(self.sh)

    def info(self, message):
        self.my_logger.info(message)

    def debug(self, message):
        self.my_logger.debug(message)

    def warning(self, message):
        self.my_logger.warning(message)

    def error(self, message):
        self.my_logger.error(message)


log = MyLog()

if __name__ == '__main__':
    log = MyLog()
    log.debug("123")

# my_logger.debug('logger debug message')
# my_logger.info('logger info message')
# my_logger.warning('logger warning message')
# my_logger.error('logger error message')
# my_logger.critical('logger critical message')

"""一个小demo"""
# try:
#     int(input("请输入"))
# except:
#     my_logger.error("报错")
