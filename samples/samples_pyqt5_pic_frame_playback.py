import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

class ImageLoader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.images = ["frame1.svg", "frame2.svg", "frame3.svg", "frame4.svg"]  # 图片列表
        self.current_image = 0

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_image)
        self.timer.start(100)  # 更新频率，单位毫秒

        self.update_image()  # 初始化图片显示

    def update_image(self):
        self.label.setPixmap(QPixmap(self.images[self.current_image]))
        self.current_image = (self.current_image + 1) % len(self.images)

app = QApplication(sys.argv)
loader = ImageLoader()
loader.show()
sys.exit(app.exec_())
