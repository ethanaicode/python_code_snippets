import sys
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCalendarWidget

class DateRangeSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)

        self.label_start = QLabel('开始日期:')
        self.layout.addWidget(self.label_start)

        self.calendar_start = QCalendarWidget(self)
        self.calendar_start.setGridVisible(True)
        self.calendar_start.clicked.connect(self.update_start_date)
        self.layout.addWidget(self.calendar_start)

        self.label_end = QLabel('结束日期:')
        self.layout.addWidget(self.label_end)

        self.calendar_end = QCalendarWidget(self)
        self.calendar_end.setGridVisible(True)
        self.calendar_end.clicked.connect(self.update_end_date)
        self.layout.addWidget(self.calendar_end)

        self.update_start_date()
        self.update_end_date()

    def update_start_date(self):
        date = self.calendar_start.selectedDate()
        self.label_start.setText(f'开始日期: {date.toString("yyyy-MM-dd")}')

    def update_end_date(self):
        date = self.calendar_end.selectedDate()
        self.label_end.setText(f'结束日期: {date.toString("yyyy-MM-dd")}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DateRangeSelector()
    ex.show()
    sys.exit(app.exec_())
