# coding:utf-8
import sys
import os

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout, QMainWindow
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, MSFluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, PrimaryPushButton, FluentIcon)
from qfluentwidgets import FluentIcon as FIF

import demo
from CalcSysImpl import CalcSysImpl
from Page2_Sync_Sim_Window import Page2_Window_Sync_Sim
from Page1_Sync_Calc_Window import Page1_Window_Sync_Calc
from Page3_Double_Calc_Window import Page3_Double_Calc_Window
from Page4_Double_Sim_Window import Page4_Double_Sim_Window


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        # self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        # 配置文件路径
        self.config_file = "config.json"

        # setFont(self.label, 24)
        # self.label.setAlignment(Qt.AlignCenter)
        # self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))

    def addWidget(self, widget):
        self.hBoxLayout.addWidget(widget)


class Window(MSFluentWindow):

    def __init__(self):
        super().__init__()
        # create sub interface
        self.sync_calc_Interface = Page1_Window_Sync_Calc('Sync Calc Interface', self)
        self.sync_sim_Interface = Page2_Window_Sync_Sim('Sync Sim Interface', self)
        self.double_calc_Interface = Page3_Double_Calc_Window('Double Calc Interface', self)
        self.double_sim_Interface = Page4_Double_Sim_Window('Double Sim Interface', self)
        self.single_calc_Interface = Page1_Window_Sync_Calc('Single Calc Interface', self)
        self.single_sim_Interface = Page2_Window_Sync_Sim('Single Sim Interface', self)

        self.libraryInterface = Page2_Window_Sync_Sim('Library Interface', self)
        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.sync_calc_Interface, FIF.HOME, '同步摆计算', FIF.HOME_FILL)
        self.addSubInterface(self.sync_sim_Interface, FIF.APPLICATION, '同步摆仿真')
        self.addSubInterface(self.double_calc_Interface, FIF.VIDEO, '双头摆计算')
        self.addSubInterface(self.double_sim_Interface, FIF.UP, '双头摆仿真')
        self.addSubInterface(self.single_calc_Interface, FIF.ZOOM, '单头摆计算')
        self.addSubInterface(self.single_sim_Interface, FIF.ZOOM, '单头摆仿真')

        self.addSubInterface(self.libraryInterface, FIF.BOOK_SHELF, '库', FIF.LIBRARY_FILL,
                             NavigationItemPosition.BOTTOM)
        self.navigationInterface.addItem(
            routeKey='Help',
            icon=FIF.HELP,
            text='帮助',
            onClick=self.showMessageBox,
            selectable=False,
            position=NavigationItemPosition.BOTTOM,
        )

        self.navigationInterface.setCurrentItem(self.sync_calc_Interface.objectName())

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon('./images/kedalogo.png'))
        self.setWindowTitle('Copyright © 2024 科达制造股份有限公司')

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def showMessageBox(self):
        w = MessageBox(
            '支持作者🥰',
            '个人开发不易，如果这个项目帮助到了您，可以考虑请作者喝一瓶快乐水🥤。您的支持就是作者开发和维护项目的动力🚀',
            self
        )
        w.yesButton.setText('来啦老弟')
        w.cancelButton.setText('下次一定')

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://afdian.net/a/zhiyiYo"))


if __name__ == '__main__':
    # setTheme(Theme.DARK)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
