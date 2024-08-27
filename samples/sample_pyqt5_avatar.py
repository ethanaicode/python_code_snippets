from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt, QRect

class CircularAvatarWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 主布局
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # 创建圆形头像标签
        avatar_label = QLabel(self)
        avatar_pixmap = QPixmap("samples/assets/images/avatar.jpg").scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        circular_pixmap = self.get_circular_pixmap(avatar_pixmap)
        avatar_label.setPixmap(circular_pixmap)

        # 创建右上角的小图标标签
        icon_label = QLabel(self)
        icon_pixmap = QPixmap("samples/assets/icons/qrcode.svg").scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_label.setPixmap(icon_pixmap)   # 如果这一步不设置，icon_label 的大小会根据图片大小自动调整
        icon_label.setStyleSheet("background-color: transparent;")  # 设置背景透明

        # 将小图标设置为头像的子控件，并移动到右上角
        icon_label.setParent(avatar_label)
        # icon_label.move(avatar_label.width() - icon_label.width(), 0)  # 定位在右上角
        icon_label.move(70, 0)  # 素材原因，直接控制 x 坐标
        
        # 将头像添加到主布局
        layout.addWidget(avatar_label)

    def get_circular_pixmap(self, pixmap):
        """将普通的头像图像裁剪为圆形图像"""
        size = min(pixmap.width(), pixmap.height())
        circular_pixmap = QPixmap(size, size)
        circular_pixmap.fill(Qt.transparent)  # 背景透明

        painter = QPainter(circular_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(pixmap)
        
        # 绘制圆形
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, size, size)
        painter.end()

        return circular_pixmap

if __name__ == "__main__":
    app = QApplication([])

    widget = CircularAvatarWidget()
    widget.show()

    app.exec_()
