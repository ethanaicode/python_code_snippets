from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout

class QRCodeWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("二维码")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.qr_code_label = QLabel(self)
        layout.addWidget(self.qr_code_label)
        self.setLayout(layout)

    def set_qr_code(self, pixmap):
        self.qr_code_label.setPixmap(pixmap)
        self.qr_code_label.setScaledContents(True)  # 确保图片适应窗口大小
        self.resize(pixmap.size())  # 调整窗口大小以适应图片
