from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize
from PyQt5.QtCore import pyqtSignal

from components.qr_code_widow import QRCodeWindow

import logging

logger = logging.getLogger('DuiPin')

class LoginWindow(QDialog):
    switch_to_activation_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("账号登录")
        self.init_ui()
        self.is_closed = False  # 添加关闭标志
        self.rejected.connect(self.on_rejected)  # Connect the rejected signal

    def init_ui(self):
        layout = QVBoxLayout()

        # 账号输入
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("输入邮箱/用户名")
        self.email_input.setMinimumWidth(300)  # 设置输入框的最小宽度
        layout.addWidget(self.email_input)

        # 激活码输入框和按钮的水平布局
        hbox = QHBoxLayout()

        # 激活码输入
        self.activation_code_input = QLineEdit()
        self.activation_code_input.setPlaceholderText("请输入激活码")
        hbox.addWidget(self.activation_code_input)

        # 二维码打开按钮
        qr_code_button = QPushButton()
        qr_code_button.setIcon(QIcon('samples/assets/icons/qrcode.svg'))  # 设置按钮图标
        qr_code_button.setIconSize(QSize(16, 16))  # 设置图标大小
        qr_code_button.clicked.connect(self.open_qr_code)
        qr_code_button.setToolTip("打开二维码")  # 鼠标悬停时显示的提示文字
        hbox.addWidget(qr_code_button)

        layout.addLayout(hbox)

        # 登录按钮
        login_button = QPushButton("登录")
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)

        # 跳转到激活码窗口的链接
        switch_to_login = QLabel("输入激活码")
        switch_to_login.mousePressEvent = self.switch_to_activation_window
        layout.addWidget(switch_to_login)

        self.setLayout(layout)
    
    def on_rejected(self):
        self.is_closed = True  # 设置关闭标志

    def open_qr_code(self):
        # 显示二维码图片
        qr_code_pixmap = QPixmap("samples/assets/images/media_qr_code.jpg")
        qr_window = QRCodeWindow(self)
        qr_window.set_qr_code(qr_code_pixmap)
        qr_window.show()  # 尝试用 show() 代替 exec_() 查看是否改善问题

    def handle_login(self):
        # 验证激活码
        is_login_successful = self.email_input.text() == '6666'
        if is_login_successful:
            # 验证通过，可以继续执行后续操作
            logger.info("通过邮箱或用户名成功登录")
            self.accept()  # QDialog 的 accept 方法会使 exec_ 返回 QDialog.Accepted
        else:
            # 验证失败，显示错误消息
            logger.error("激活码不正确，请重新输入！")
            QMessageBox.warning(self, "登录失败", "激活码不正确，请重新输入！")
            self.email_input.clear()
            self.activation_code_input.clear()

    def switch_to_activation_window(self, event):
        self.hide()  # 隐藏当前窗口
        self.switch_to_activation_signal.emit()  # 发射信号而不是直接打开新窗口