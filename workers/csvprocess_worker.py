from PySide6.QtCore import QThread, Signal
import os
import csv
import shutil
import re
from utils.log_util import LogUtil

class CSVProcessWorker(QThread):
    log_signal = Signal(str)  # 定义日志信号

    def __init__(self):
        super().__init__()
        self.log_util = LogUtil(level='INFO')
        self.logger = self.log_util.get_logger()

    def run(self):
        try:
            # 创建必要的目录
            download_dir = 'download'
            csvprocess_dir = 'csvprocess'
            os.makedirs(download_dir, exist_ok=True)
            os.makedirs(csvprocess_dir, exist_ok=True)

            # 遍历 download 目录中的所有文件
            for filename in os.listdir(download_dir):
                if filename.endswith('.csv'):
                    file_path = os.path.join(download_dir, filename)
                    
                    try:
                        # 打开 CSV 文件并读取第一行的前两个元素
                        with open(file_path, 'r', encoding='utf-8') as file:
                            csv_reader = csv.reader(file)
                            first_row = next(csv_reader, None)  # 获取第一行

                            # 确保第一行至少有两个元素
                            if first_row and len(first_row) >= 2:
                                # 生成新的文件名
                                new_filename = f"{first_row[0]} {first_row[1]}.csv"
                                # 替换不合法的字符为下划线
                                new_filename = re.sub(r'[\\/*?:"<>|]', "_", new_filename)
                                new_file_path = os.path.join(csvprocess_dir, new_filename)

                                # 复制文件到 csvprocess 目录并重命名
                                shutil.copy2(file_path, new_file_path)
                                self.logger.info(f"文件 {filename} 已复制并重命名为: {new_filename}")
                            else:
                                self.logger.warning(f"文件 {filename} 格式不正确或缺少元素，无法重命名")
                    except Exception as e:
                        self.logger.error(f"处理文件 {filename} 时出错: {e}")
        except Exception as e:
            self.logger.error(f"CSV 处理任务出错: {e}")
        finally:
            self.logger.info("CSV 处理任务结束")