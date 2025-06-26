from PySide6.QtCore import QThread, Signal
import csv
import requests
import os
import re
from utils.log_util import LogUtil

class DownloadWorker(QThread):
    log_signal = Signal(str)  # 定义日志信号

    def __init__(self):
        super().__init__()
        self.log_util = LogUtil(level='INFO')
        self.logger = self.log_util.get_logger()
        self.csv_file_path = 'csvDownloadURL.csv'  # 默认值

    def run(self):
        try:
            # 创建下载目录
            download_dir = 'download'
            os.makedirs(download_dir, exist_ok=True)

            # 读取 CSV 文件
            with open(self.csv_file_path, 'r') as csvfile:
                # 按行读取 CSV 文件
                for line in csvfile:
                    # 去除行末的换行符，并按逗号分隔 URLs
                    urls = line.strip().split(',')
                    for url in urls:
                        try:
                            # 从链接中提取文件名
                            file_name = url.split('/')[-1].split('?')[0]
                            # 替换不合法的字符为下划线
                            file_name = re.sub(r'[\\/*?:"<>|]', "_", file_name)
                            file_path = os.path.join(download_dir, file_name)
                            
                            # 下载文件
                            response = requests.get(url, stream=True)
                            if response.status_code == 200:
                                with open(file_path, 'wb') as file:
                                    for chunk in response.iter_content(chunk_size=8192):
                                        if chunk:
                                            file.write(chunk)
                                self.logger.info(f"文件已下载: {file_name}")
                            else:
                                self.logger.error(f"下载失败，状态码: {response.status_code}, URL: {url}")
                        except Exception as e:
                            self.logger.error(f"下载文件时出错: {e}, URL: {url}")
        except Exception as e:
            self.logger.error(f"下载任务出错: {e}")
        finally:
            self.logger.info("下载任务结束")