from PySide6.QtCore import QThread, Signal
import os
import shutil

class CleanWorker(QThread):
    log_signal = Signal(str)  # 定义日志信号

    def __init__(self):
        super().__init__()

    def run(self):
        try:
            # 定义要清空的文件夹
            download_dir = 'download'
            csvprocess_dir = 'csvprocess'
            output_dir = 'output'

            # 清空每个文件夹
            self.clear_directory(download_dir)
            self.clear_directory(csvprocess_dir)
            self.clear_directory(output_dir)

            self.log_signal.emit("所有文件夹已清空！")
        except Exception as e:
            self.log_signal.emit(f"清空文件夹时出错：{e}")

    def clear_directory(self, directory):
        """清空指定目录中的所有文件和子目录"""
        try:
            if os.path.exists(directory):
                # 遍历目录中的所有文件和子目录
                for filename in os.listdir(directory):
                    file_path = os.path.join(directory, filename)
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                self.log_signal.emit(f"已清空文件夹：{directory}")
            else:
                self.log_signal.emit(f"文件夹不存在：{directory}")
        except Exception as e:
            self.log_signal.emit(f"清空文件夹 {directory} 时出错：{e}")