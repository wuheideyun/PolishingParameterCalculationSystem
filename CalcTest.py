import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from CalcSysImpl import CalcSysImpl

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QMainWindow()
    mc = CalcSysImpl(w)
    w.show()
    sys.exit(app.exec())