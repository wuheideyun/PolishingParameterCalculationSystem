# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CalcSys.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

from qfluentwidgets import (BodyLabel, LineEdit, PrimaryPushButton)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(834, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = BodyLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.between = LineEdit(self.centralwidget)
        self.between.setObjectName(u"between")

        self.gridLayout.addWidget(self.between, 0, 1, 1, 1)

        self.label_5 = BodyLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.grind_size = LineEdit(self.centralwidget)
        self.grind_size.setObjectName(u"grind_size")

        self.gridLayout.addWidget(self.grind_size, 0, 3, 1, 2)

        self.label_8 = BodyLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 5, 1, 1)

        self.belt_speed = LineEdit(self.centralwidget)
        self.belt_speed.setObjectName(u"belt_speed")

        self.gridLayout.addWidget(self.belt_speed, 0, 6, 1, 1)

        self.label_4 = BodyLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 7, 1, 1)

        self.a_speed = LineEdit(self.centralwidget)
        self.a_speed.setObjectName(u"a_speed")

        self.gridLayout.addWidget(self.a_speed, 0, 8, 1, 2)

        self.label_2 = BodyLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.radius = LineEdit(self.centralwidget)
        self.radius.setObjectName(u"radius")

        self.gridLayout.addWidget(self.radius, 1, 1, 1, 1)

        self.label_6 = BodyLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)

        self.ceramic_width = LineEdit(self.centralwidget)
        self.ceramic_width.setObjectName(u"ceramic_width")

        self.gridLayout.addWidget(self.ceramic_width, 1, 3, 1, 2)

        self.label_7 = BodyLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 5, 1, 1)

        self.beam_speed_up = LineEdit(self.centralwidget)
        self.beam_speed_up.setObjectName(u"beam_speed_up")

        self.gridLayout.addWidget(self.beam_speed_up, 1, 6, 1, 1)

        self.label_3 = BodyLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 7, 1, 1)

        self.overlap = LineEdit(self.centralwidget)
        self.overlap.setObjectName(u"overlap")

        self.gridLayout.addWidget(self.overlap, 1, 8, 1, 2)

        self.energy_button = PrimaryPushButton(self.centralwidget)
        self.energy_button.setObjectName(u"energy_button")

        self.gridLayout.addWidget(self.energy_button, 2, 1, 1, 1)

        self.efficient_button = PrimaryPushButton(self.centralwidget)
        self.efficient_button.setObjectName(u"efficient_button")

        self.gridLayout.addWidget(self.efficient_button, 2, 3, 1, 2)

        self.simulation_button = PrimaryPushButton(self.centralwidget)
        self.simulation_button.setObjectName(u"simulation_button")

        self.gridLayout.addWidget(self.simulation_button, 2, 6, 1, 1)

        self.middle_line_button = PrimaryPushButton(self.centralwidget)
        self.middle_line_button.setObjectName(u"middle_line_button")

        self.gridLayout.addWidget(self.middle_line_button, 2, 7, 1, 2)

        self.animation_button = PrimaryPushButton(self.centralwidget)
        self.animation_button.setObjectName(u"animation_button")

        self.gridLayout.addWidget(self.animation_button, 2, 9, 1, 1)

        self.label_9 = BodyLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)

        self.beam_speed = LineEdit(self.centralwidget)
        self.beam_speed.setObjectName(u"beam_speed")

        self.gridLayout.addWidget(self.beam_speed, 3, 1, 1, 1)

        self.label_13 = BodyLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 3, 2, 1, 1)

        self.swing = LineEdit(self.centralwidget)
        self.swing.setObjectName(u"swing")

        self.gridLayout.addWidget(self.swing, 3, 4, 1, 1)

        self.label_11 = BodyLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)

        self.stay_time = LineEdit(self.centralwidget)
        self.stay_time.setObjectName(u"stay_time")

        self.gridLayout.addWidget(self.stay_time, 4, 1, 1, 1)

        self.label_10 = BodyLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 4, 2, 1, 2)

        self.constant_time = LineEdit(self.centralwidget)
        self.constant_time.setObjectName(u"constant_time")

        self.gridLayout.addWidget(self.constant_time, 4, 4, 1, 1)

        self.label_12 = BodyLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)

        self.num = LineEdit(self.centralwidget)
        self.num.setObjectName(u"num")

        self.gridLayout.addWidget(self.num, 5, 1, 1, 1)

        self.label_14 = BodyLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 5, 2, 1, 1)

        self.equal_coefficient = LineEdit(self.centralwidget)
        self.equal_coefficient.setObjectName(u"equal_coefficient")

        self.gridLayout.addWidget(self.equal_coefficient, 5, 4, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(0, 170, 255);")

        self.gridLayout.addWidget(self.widget, 6, 0, 1, 10)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 834, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u78e8\u5934\u95f4\u8ddd\uff1a</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u78e8\u5757\u5c3a\u5bf8\uff1a</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u76ae\u5e26\u901f\u5ea6\uff1a</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u52a0\u901f\u5ea6\u5927\u5c0f\uff1a</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u78e8\u5934\u534a\u5f84\uff1a</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u8fdb\u7816\u5bbd\u5ea6\uff1a</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u6446\u52a8\u901f\u5ea6\u4e0a\u9650\uff1a</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u8f68\u8ff9\u91cd\u53e0\u91cf\uff1a</p></body></html>", None))
        self.energy_button.setText(QCoreApplication.translate("MainWindow", u"\u8282\u80fd\u8ba1\u7b97", None))
        self.efficient_button.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u6548\u8ba1\u7b97", None))
        self.simulation_button.setText(QCoreApplication.translate("MainWindow", u"\u629b\u78e8\u91cf\u5206\u5e03\u4eff\u771f", None))
        self.middle_line_button.setText(QCoreApplication.translate("MainWindow", u"\u8f68\u8ff9\u4e2d\u5fc3\u7ebf\u7ed8\u5236", None))
        self.animation_button.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u753b\u6309\u94ae", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6a2a\u6881\u6446\u52a8\u901f\u5ea6</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u6446\u5e45", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u8fb9\u90e8\u505c\u7559\u65f6\u95f4", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u6a2a\u6881\u5300\u901f\u6446\u52a8\u65f6\u95f4", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u540c\u7c92\u5ea6\u78e8\u5934\u6570\u76ee", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u5747\u5300\u7cfb\u6570", None))
    # retranslateUi

