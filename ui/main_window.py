from PySide6.QtWidgets import QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("轻纺教案生成器 QQ:1717823")

        # 创建一个文本区域用于显示日志
        self.log_text_edit = QTextEdit(self)
        self.log_text_edit.setReadOnly(True)

        # 创建四个按钮
        self.download_btn = QPushButton("下载文件", self)
        self.csvprocess_btn = QPushButton("处理CSV", self)
        self.makeword_btn = QPushButton("生成Word", self)
        self.clean_btn = QPushButton("一键清空", self)
        self.batch_replace_btn = QPushButton("一键批量替换Word内容", self)  # 新增的按钮

        # 创建两个输入框
        self.old_text_edit = QLineEdit(self)
        self.old_text_edit.setPlaceholderText("请输入待替换的内容")
        self.new_text_edit = QLineEdit(self)
        self.new_text_edit.setPlaceholderText("请输入替换后的内容")

        # 创建一个布局管理器
        layout = QVBoxLayout()

        # 创建一个水平布局用于放置输入框和按钮
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.old_text_edit)
        input_layout.addWidget(self.new_text_edit)
        input_layout.addWidget(self.batch_replace_btn)

        # 将按钮和文本区域添加到布局中
        layout.addWidget(self.download_btn)
        layout.addWidget(self.csvprocess_btn)
        layout.addWidget(self.makeword_btn)
        layout.addWidget(self.clean_btn)
        layout.addLayout(input_layout)  # 添加输入框和按钮的布局
        layout.addWidget(self.log_text_edit)

        # 创建一个中心小部件，并将布局设置给它
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # 设置中心小部件
        self.setCentralWidget(central_widget)

        # 工作线程
        self.download_worker = None
        self.csvprocess_worker = None
        self.makeword_worker = None
        self.clean_worker = None
        self.batch_replace_worker = None  # 新增的 BatchReplaceWorker

        # 连接按钮的点击事件到槽函数
        self.download_btn.clicked.connect(self.download_button_clicked)
        self.csvprocess_btn.clicked.connect(self.csvprocess_button_clicked)
        self.makeword_btn.clicked.connect(self.makeword_button_clicked)
        self.clean_btn.clicked.connect(self.clean_button_clicked)
        self.batch_replace_btn.clicked.connect(self.batch_replace_button_clicked)  # 绑定新按钮的点击事件

    def set_workers(self, download_worker, csvprocess_worker, makeword_worker, clean_worker, batch_replace_worker):
        """设置工作线程"""
        self.download_worker = download_worker
        self.csvprocess_worker = csvprocess_worker
        self.makeword_worker = makeword_worker
        self.clean_worker = clean_worker
        self.batch_replace_worker = batch_replace_worker  # 设置 BatchReplaceWorker

        # 连接工作线程的信号与槽
        self.download_worker.log_signal.connect(self.append_log)
        self.download_worker.finished.connect(self.on_download_finished)
        self.csvprocess_worker.log_signal.connect(self.append_log)
        self.csvprocess_worker.finished.connect(self.on_csvprocess_finished)
        self.makeword_worker.log_signal.connect(self.append_log)
        self.makeword_worker.finished.connect(self.on_makeword_finished)
        self.clean_worker.log_signal.connect(self.append_log)
        self.batch_replace_worker.log_signal.connect(self.append_log)  # 连接 BatchReplaceWorker 的日志信号

    def append_log(self, log):
        """追加日志到文本区域"""
        self.log_text_edit.append(log)

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
        old_text = self.old_text_edit.text()
        new_text = self.new_text_edit.text()
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