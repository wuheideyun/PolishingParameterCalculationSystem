import sys

from PySide6.QtCore import Qt, QTranslator, QLocale
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6.QtWidgets import QApplication
from qfluentwidgets import setThemeColor, FluentTranslator, setTheme, Theme, SplitTitleBar, isDarkTheme
from Ui_LoginWindow import Ui_Form


def isWin11():
    return sys.platform == 'win32' and sys.getwindowsversion().build >= 22000


if isWin11():
    from qframelesswindow import AcrylicWindow as Window
else:
    from qframelesswindow import FramelessWindow as Window


class LoginWindow(Window, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # setTheme(Theme.DARK)
        setThemeColor('#28afe9')

        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()

        self.label.setScaledContents(False)
        self.setWindowTitle('Copyright © 2024 科达制造股份有限公司')
        # self.setWindowIcon(QIcon("./images/kedalogo.jpg"))
        self.resize(1000, 650)

        self.windowEffect.setMicaEffect(self.winId(), isDarkMode=isDarkTheme())
        if not isWin11():
            color = QColor(25, 33, 42) if isDarkTheme() else QColor(240, 244, 249)
            self.setStyleSheet(f"LoginWindow{{background: {color.name()}}}")

        self.titleBar.titleLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 13px 'Segoe UI';
                padding: 0 4px;
                color: white
            }
        """)

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap("./images/keda.jpg").scaled(
            self.label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Internationalization
    translator = FluentTranslator(QLocale())
    app.installTranslator(translator)

    w = LoginWindow()
    w.show()
    app.exec()