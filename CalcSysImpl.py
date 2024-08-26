from PySide6.QtWidgets import QWidget, QMainWindow

from CalcSys import Ui_MainWindow


class CalcSysImpl(Ui_MainWindow, QWidget):
    def __init__(self, w):
        super().__init__()
        self.setupUi(w)
        self.setObjectName('CalcSysImpl')
