from PyQt5 import QtWidgets, QtCore, QtGui

class RoundedDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(RoundedDialog, self).__init__(parent, QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(0.95)  # 设置窗口透明度
        self.setStyleSheet("background-color: white;")  # 设置窗口背景颜色
        self.resize(400, 300)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), 15, 15)  # 15是圆角的半径
        region = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)  # 使用QRegion设置形状

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = RoundedDialog()
    dialog.show()
    sys.exit(app.exec_())
