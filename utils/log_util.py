import logging
from logging.handlers import RotatingFileHandler
import os
import sys
import datetime

class LogUtil:
    _instance = None  # 单例实例
    _log_dir = "logs"  # 日志目录

    def __new__(cls, *args, **kwargs):
        """创建单例实例"""
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, level='DEBUG'):
        if self.__initialized:
            return
        self.__initialized = True

        # 创建日志目录
        self.create_dir_if_not_exists(self._log_dir)

        # 获取当前时间
        now = datetime.datetime.now()
        date_str = now.strftime("%Y-%m-%d")

        # 设置日志文件路径
        log_file_path = os.path.join(self._log_dir, f"app_{date_str}.log")

        # 设置日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 创建日志记录器
        self.logger = logging.getLogger('app_logger')
        self.logger.setLevel(self.get_level(level))

        # 创建文件处理器，指定编码为 utf-8
        file_handler = RotatingFileHandler(
            log_file_path,
            maxBytes=1024 * 1024 * 5,  # 5MB
            backupCount=5,
            encoding='utf-8'  # 指定编码为 utf-8
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def get_level(self, level):
        """获取日志级别"""
        LEVELS = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        return LEVELS.get(level, logging.DEBUG)

    def get_logger(self):
        """获取日志记录器"""
        return self.logger

    @staticmethod
    def create_dir_if_not_exists(dir_path):
        """如果目录不存在，则创建目录"""
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            return True
        return False