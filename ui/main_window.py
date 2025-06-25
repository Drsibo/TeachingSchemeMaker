from PySide6.QtWidgets import QWidget
from ui.Ui_TeachingSchemeMakerWindow import Ui_Form  # 引入由Qt Designer生成的UI类

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 工作线程
        self.download_worker = None
        self.csvprocess_worker = None
        self.makeword_worker = None
        self.clean_worker = None
        self.batch_replace_worker = None

        # 连接按钮的点击事件到槽函数
        self.ui.download_btn.clicked.connect(self.download_button_clicked)
        self.ui.csvprocess_btn.clicked.connect(self.csvprocess_button_clicked)
        self.ui.makeword_btn.clicked.connect(self.makeword_button_clicked)
        self.ui.clean_btn.clicked.connect(self.clean_button_clicked)
        self.ui.batch_replace_btn.clicked.connect(self.batch_replace_button_clicked)

    def set_workers(self, download_worker, csvprocess_worker, makeword_worker, clean_worker, batch_replace_worker):
        """设置工作线程"""
        self.download_worker = download_worker
        self.csvprocess_worker = csvprocess_worker
        self.makeword_worker = makeword_worker
        self.clean_worker = clean_worker
        self.batch_replace_worker = batch_replace_worker

        # 连接工作线程的信号与槽
        self.download_worker.log_signal.connect(self.append_log)
        self.download_worker.finished.connect(self.on_download_finished)
        self.csvprocess_worker.log_signal.connect(self.append_log)
        self.csvprocess_worker.finished.connect(self.on_csvprocess_finished)
        self.makeword_worker.log_signal.connect(self.append_log)
        self.makeword_worker.finished.connect(self.on_makeword_finished)
        self.clean_worker.log_signal.connect(self.append_log)
        self.batch_replace_worker.log_signal.connect(self.append_log)

    def append_log(self, log):
        """追加日志到文本区域"""
        self.ui.log_text_edit.append(log)

    def download_button_clicked(self):
        """下载按钮槽函数"""
        self.append_log("开始下载任务...")
        self.download_worker.start()

    def csvprocess_button_clicked(self):
        """CSV处理按钮槽函数"""
        self.append_log("开始CSV处理任务...")
        self.csvprocess_worker.start()

    def makeword_button_clicked(self):
        """生成Word按钮槽函数"""
        self.append_log("开始Word生成任务...")
        self.makeword_worker.start()

    def clean_button_clicked(self):
        """清空按钮槽函数"""
        self.append_log("开始清空文件夹...")
        self.clean_worker.start()

    def batch_replace_button_clicked(self):
        """批量替换按钮槽函数"""
        old_text = self.ui.lineEdit.text()
        new_text = self.ui.lineEdit_2.text()
        if not old_text or not new_text:
            self.append_log("请输入待替换内容和替换后的内容")
            return
        self.append_log(f"开始批量替换Word内容: 将 '{old_text}' 替换为 '{new_text}'")
        self.batch_replace_worker.set_replace_text(old_text, new_text)
        self.batch_replace_worker.start()

    def on_download_finished(self):
        """下载完成槽函数"""
        self.append_log("下载任务完成！")

    def on_csvprocess_finished(self):
        """CSV处理完成槽函数"""
        self.append_log("CSV处理任务完成！")

    def on_makeword_finished(self):
        """Word生成完成槽函数"""
        self.append_log("Word生成任务完成！")