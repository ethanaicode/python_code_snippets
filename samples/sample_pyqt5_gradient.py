import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout()

# 创建一个按钮，并设置CSS样式
button = QPushButton("Click Me")
button.setStyleSheet("""
QPushButton {
    min-height: 50px;
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                      stop:0 white, stop:1 green);
    border: 10px solid;
    border-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                  stop:0 red, stop:1 blue);
    border-radius: 10px;
    padding: 5px;
    font-size: 16px;
}
""")
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
