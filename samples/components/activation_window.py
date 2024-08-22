from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSignal

class ActivationWindow(QDialog):
    switch_to_login_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("输入激活码")
        self.init_ui()
        self.is_closed = False  # 添加关闭标志
        self.rejected.connect(self.on_rejected)  # Connect the rejected signal

    def init_ui(self):
        layout = QVBoxLayout()

        # 激活码输入
        self.activation_code_input = QLineEdit()
        self.activation_code_input.setPlaceholderText("请输入激活码")
        self.activation_code_input.setMinimumWidth(300)  # 设置输入框的最小宽度
        layout.addWidget(self.activation_code_input)

        # 确认按钮
        confirm_button = QPushButton("确认")
        confirm_button.clicked.connect(self.confirm_activation)
        layout.addWidget(confirm_button)

        # 跳转到登录窗口的链接
        switch_to_login = QLabel("账号登录")
        switch_to_login.mousePressEvent = self.switch_to_login_window
        layout.addWidget(switch_to_login)

        self.setLayout(layout)

    def on_rejected(self):
        self.is_closed = True  # 设置关闭标志

    def confirm_activation(self):
        # is_activation_code_valid = self.activation_code_input.text() == '6666'
        is_activation_code_valid = True
        if is_activation_code_valid:
            # 验证通过，可以继续执行后续操作
            print("通过激活码成功登录")
            self.accept()  # QDialog 的 accept 方法会使 exec_ 返回 QDialog.Accepted
        else:
            # 验证失败，显示错误消息
            QMessageBox.warning(self, "登录失败", "激活码不正确，请重新输入！")
            self.activation_code_input.clear()

    def switch_to_login_window(self, event):
        self.hide()  # 隐藏当前窗口
        self.switch_to_login_signal.emit()  # 发射信号而不是直接打开新窗口
