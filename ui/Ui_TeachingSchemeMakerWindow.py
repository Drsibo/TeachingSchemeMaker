# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TeachingSchemeMakerWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(485, 453)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.download_btn = QPushButton(Form)
        self.download_btn.setObjectName(u"download_btn")

        self.gridLayout.addWidget(self.download_btn, 0, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.csvprocess_btn = QPushButton(Form)
        self.csvprocess_btn.setObjectName(u"csvprocess_btn")

        self.gridLayout.addWidget(self.csvprocess_btn, 1, 0, 1, 1)

        self.makeword_btn = QPushButton(Form)
        self.makeword_btn.setObjectName(u"makeword_btn")

        self.gridLayout.addWidget(self.makeword_btn, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.clean_btn = QPushButton(Form)
        self.clean_btn.setObjectName(u"clean_btn")

        self.verticalLayout.addWidget(self.clean_btn)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.batch_replace_btn = QPushButton(Form)
        self.batch_replace_btn.setObjectName(u"batch_replace_btn")

        self.verticalLayout_2.addWidget(self.batch_replace_btn)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.log_text_edit = QTextEdit(Form)
        self.log_text_edit.setObjectName(u"log_text_edit")

        self.verticalLayout.addWidget(self.log_text_edit)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.download_btn.setText(QCoreApplication.translate("Form", u"2.\u4e0b\u8f7d\u5de5\u4f5c\u6d41CSV", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"1.\u4f7f\u7528\u5de5\u4f5c\u6d41", None))
        self.csvprocess_btn.setText(QCoreApplication.translate("Form", u"3.\u5904\u7406CSV\u547d\u540d", None))
        self.makeword_btn.setText(QCoreApplication.translate("Form", u"4.\u4e00\u952e\u751f\u6210\u6559\u6848", None))
        self.clean_btn.setText(QCoreApplication.translate("Form", u"\u4e00\u952e\u6e05\u7a7a", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6279\u91cf\u66ff\u6362\u6587\u4ef6\u5939\u4e0bword\u6587\u5b57\u529f\u80fd", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5f85\u66ff\u6362\u7684\u5185\u5bb9", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u66ff\u6362\u540e\u7684\u5185\u5bb9", None))
        self.batch_replace_btn.setText(QCoreApplication.translate("Form", u"\u4e00\u952e\u6279\u91cf\u66ff\u6362Word\u5185\u5bb9", None))
    # retranslateUi

