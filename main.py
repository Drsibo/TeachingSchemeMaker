import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from workers.download_worker import DownloadWorker
from workers.csvprocess_worker import CSVProcessWorker
from workers.makeword_worker import MakeWordWorker
from workers.clean_worker import CleanWorker
from workers.batch_replace_worker import BatchReplaceWorker

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    # 初始化工作线程
    download_worker = DownloadWorker()
    csvprocess_worker = CSVProcessWorker()
    makeword_worker = MakeWordWorker()
    clean_worker = CleanWorker()
    batch_replace_worker = BatchReplaceWorker()  # 创建 BatchReplaceWorker 实例

    # 将工作线程设置到主窗口
    window.set_workers(download_worker, csvprocess_worker, makeword_worker, clean_worker, batch_replace_worker)
    # 显示主窗口
    window.show()
    sys.exit(app.exec())