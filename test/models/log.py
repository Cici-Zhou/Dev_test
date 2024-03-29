import logging
import os 
from logging.handlers import TimedRotatingFileHandler
from test.models.config import LOG_PATH, Config


class Logger(object):
    def __init__(self, logger_name='framework'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        c = Config().yaml_get('log') # 获取log.yml文件
        self.log_file_name = c.get('file_name') if c.get('file_name') else 'test.log'
        self.backup_count = c.get('bcakup') if c.get('bcakup') else 5
        # 日志输出级别
        self.console_output_level = c.get('console_level') if c.get('console_level') else 'DEBUG'
        self.file_output_level = c.get('file_level') if c.get('file_level') else 'DEBUG'

        # 日志输出格式
        pattern = c.get('pattern') if c.get('pattern') else '%(asctime) - %(name)s - %(levlename)s - %(message)s'
        self.formatter = logging.Formatter(pattern)

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers: #避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.log_file_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger


logger = Logger().get_logger()
