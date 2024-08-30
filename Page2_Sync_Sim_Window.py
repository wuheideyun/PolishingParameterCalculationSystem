import math
import os

from PySide6.QtCore import QSettings, Qt, QRect
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QMovie, QIcon
from PySide6.QtWidgets import QHBoxLayout, QFrame, QWidget, QGridLayout, QVBoxLayout, QLabel, QMainWindow, QMenuBar
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from qfluentwidgets import PrimaryPushButton, LineEdit, BodyLabel, ImageLabel


from Page2_Sync_Algorithms_Polishing_Distribution_Simulation import Polishing_distribution_Thread
from Page2_Sync_Algorithms_Generate_Animation import Animation_produce
from Page2_Sync_Algorithms_Middle_Line_Plot import middle_line_plot



class Page2_Window_Sync_Sim(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.settings = QSettings("config.ini", QSettings.IniFormat)  # 使用配置文件

        self.customWidth = 150  # 自定义宽度
        self.hBoxLayout = QVBoxLayout(self)
        self.setObjectName(text.replace(' ', '-'))

        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        # 初始化所有控件（与原代码保持一致）
        self.iconHead = ImageLabel("./images/equal_calc2.png", self.centralwidget)
        self.gridLayout.addWidget(self.iconHead, 0, 0, 1, 10)


        self.label_gap = BodyLabel(self.centralwidget)
        self.label_gap.setObjectName(u"label_gap")
        self.gridLayout.addWidget(self.label_gap, 1, 1, 1, 1)
        self.lineedit_gap = LineEdit(self.centralwidget)
        self.lineedit_gap.setFixedWidth(self.customWidth)
        self.lineedit_gap.setObjectName(u"lineedit_gap")
        self.gridLayout.addWidget(self.lineedit_gap, 1, 2, 1, 1)

        self.label_size = BodyLabel(self.centralwidget)
        self.label_size.setObjectName(u"label_size")

        self.gridLayout.addWidget(self.label_size, 1, 4, 1, 1)

        self.lineedit_size = LineEdit(self.centralwidget)
        self.lineedit_size.setObjectName(u"lineedit_size")
        self.lineedit_size.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineedit_size, 1, 5, 1, 1)

        self.label_radius = BodyLabel(self.centralwidget)
        self.label_radius.setObjectName(u"label_radius")

        self.gridLayout.addWidget(self.label_radius, 1, 7, 1, 1)

        self.lineedit_radius = LineEdit(self.centralwidget)
        self.lineedit_radius.setObjectName(u"lineedit_radius")
        self.lineedit_radius.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineedit_radius, 1, 8, 1, 1)

        self.label_acc = BodyLabel(self.centralwidget)
        self.label_acc.setObjectName(u"label_acc")

        self.gridLayout.addWidget(self.label_acc, 2, 1, 1, 1)

        self.lineedit_acc = LineEdit(self.centralwidget)
        self.lineedit_acc.setObjectName(u"lineedit_acc")
        self.lineedit_acc.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineedit_acc, 2, 2, 1, 2)

        self.label_amount = BodyLabel(self.centralwidget)
        self.label_amount.setObjectName(u"label_amount")

        self.gridLayout.addWidget(self.label_amount, 2, 4, 1, 1)

        self.lineedit_amount = LineEdit(self.centralwidget)
        self.lineedit_amount.setObjectName(u"lineedit_amount")
        self.lineedit_amount.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineedit_amount, 2, 5, 1, 1)

        self.label_belt_speed = BodyLabel(self.centralwidget)
        self.label_belt_speed.setObjectName(u"label_belt_speed")

        self.gridLayout.addWidget(self.label_belt_speed, 3, 1, 1, 1)

        self.lineedit_belt_speed = LineEdit(self.centralwidget)
        self.lineedit_belt_speed.setObjectName(u"lineedit_belt_speed")
        self.lineedit_belt_speed.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineedit_belt_speed, 3, 2, 1, 2)

        self.label_stop_time = BodyLabel(self.centralwidget)
        self.label_stop_time.setObjectName(u"label_stop_time")

        self.gridLayout.addWidget(self.label_stop_time, 3, 4, 1, 1)

        self.lineedit_stop_time = LineEdit(self.centralwidget)
        self.lineedit_stop_time.setObjectName(u"lineedit_stop_time")
        self.lineedit_stop_time.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineedit_stop_time, 3, 5, 1, 1)

        self.label_coefficient = BodyLabel(self.centralwidget)
        self.label_coefficient.setObjectName(u"label_coefficient")
        self.gridLayout.addWidget(self.label_coefficient, 3, 7, 1, 1)
        self.lineedit_coefficient = LineEdit(self.centralwidget)
        self.lineedit_coefficient.setObjectName(u"lineedit_coefficient")
        self.lineedit_coefficient.setEnabled(False)
        self.lineedit_coefficient.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineedit_coefficient, 3, 8, 1, 1)

        self.label_swing_speed = BodyLabel(self.centralwidget)
        self.label_swing_speed.setObjectName(u"label_swing_speed")

        self.gridLayout.addWidget(self.label_swing_speed, 4, 1, 1, 1)

        self.lineedit_swing_speed = LineEdit(self.centralwidget)
        self.lineedit_swing_speed.setObjectName(u"lineedit_swing_speed")
        self.lineedit_swing_speed.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineedit_swing_speed, 4, 2, 1, 2)

        self.label_swing_time = BodyLabel(self.centralwidget)
        self.label_swing_time.setObjectName(u"label_swing_time")

        self.gridLayout.addWidget(self.label_swing_time, 4, 4, 1, 1)

        self.lineedit_swing_time = LineEdit(self.centralwidget)
        self.lineedit_swing_time.setObjectName(u"lineedit_swing_time")
        self.lineedit_swing_time.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineedit_swing_time, 4, 5, 1, 1)

        self.button_save = PrimaryPushButton(self.centralwidget)
        self.button_save.setObjectName(u"button_save")
        self.gridLayout.addWidget(self.button_save, 4, 7, 1, 1)

        # 中间图标
        self.iconCenter = ImageLabel("./images/middle2.png", self.centralwidget)
        self.gridLayout.addWidget(self.iconCenter, 5, 0, 1, 10)


        self.button_animation = PrimaryPushButton(self.centralwidget)
        self.button_animation.setObjectName(u"button_animation")

        self.gridLayout.addWidget(self.button_animation, 6, 3, 1, 1)

        self.button_middle_line = PrimaryPushButton(self.centralwidget)
        self.button_middle_line.setObjectName(u"button_middle_line")

        self.gridLayout.addWidget(self.button_middle_line, 6, 4, 1, 1)

        self.button_simulation = PrimaryPushButton(self.centralwidget)
        self.button_simulation.setObjectName(u"button_simulation")

        self.gridLayout.addWidget(self.button_simulation, 6, 5, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.widget, 7, 0, 1, 7)

        self.iconBottom = ImageLabel("./images/bottom2.png", self.centralwidget)
        self.gridLayout.addWidget(self.iconBottom, 8, 0, 1, 10)

        self.retranslateUi(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 940, 22))

        # self.iconLabel = ImageLabel("./images/double3.png", self.centralwidget)
        # self.hBoxLayout.addWidget(self.iconLabel)
        self.hBoxLayout.addWidget(self.centralwidget)

        self.retranslateUi(self.centralwidget)
        self.loadSettings()  # 在初始化时加载设置

        # 在程序中创建一个显示图框 播放gif动画
        self.label_gif = BodyLabel(self.widget)
        self.label_gif.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # 调整gif_label的大小以适应widget
        self.label_gif.resize(self.widget.size())
        # 确保gif_label随widget大小变化而变化
        self.widget.resizeEvent = self.resize_event

        # 按钮操作
        self.button_animation.clicked.connect(self.start_computation_trajectory_animation)  # 动画按钮
        self.button_simulation.clicked.connect(self.start_computation_Polishing_distribution)  # 抛磨量分布仿真按钮
        self.button_middle_line.clicked.connect(self.middle_line_figure_plot)  # 磨头中心线绘制按钮

    def addWidget(self, widget):
        self.hBoxLayout.addWidget(widget)

    # 调整动画在界面图框中的位置
    def resize_event(self, event):
        self.label_gif.resize(event.size())

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_gap.setText('磨头间距：')
        self.label_size.setText('磨块尺寸：')
        self.label_belt_speed.setText('皮带速度：')
        self.label_acc.setText('加速度大小：')
        self.label_radius.setText('磨头半径：')
        self.label_swing_speed.setText('横梁摆动速度')
        self.label_stop_time.setText('边部停留时间')
        self.label_swing_time.setText('横梁匀速摆动时间')
        self.label_amount.setText('同粒度磨头数目')
        self.label_coefficient.setText('均匀系数')
        self.button_simulation.setText('抛磨量分布仿真')
        # self.button_simulation.clicked.connect(self.start_computation_Polishing_distribution)  # 抛磨量分布仿真按钮

        self.button_middle_line.setText('轨迹中心线绘制')
        # self.button_middle_line.clicked.connect(self.middle_line_figure_plot)

        self.button_animation.setText('动画按钮')
        # self.button_animation.clicked.connect(self.start_computation_trajectory_animation)

        self.button_save.setText('保存参数')
        self.button_save.clicked.connect(self.saveSettings)

    def loadSettings(self):
        """加载配置文件中的数据到各个LineEdit控件"""
        self.lineedit_gap.setText(self.settings.value("lineedit_gap2", ""))
        self.lineedit_size.setText(self.settings.value("lineedit_size2", ""))
        self.lineedit_radius.setText(self.settings.value("lineedit_radius2", ""))
        self.lineedit_acc.setText(self.settings.value("lineedit_acc2", ""))
        self.lineedit_amount.setText(self.settings.value("lineedit_amount2", ""))
        self.lineedit_belt_speed.setText(self.settings.value("lineedit_belt_speed2", ""))
        self.lineedit_stop_time.setText(self.settings.value("lineedit_stop_time2", ""))
        self.lineedit_swing_speed.setText(self.settings.value("lineedit_swing_speed2", ""))
        self.lineedit_swing_time.setText(self.settings.value("lineedit_swing_time2", ""))

    def saveSettings(self):
        """保存各个LineEdit控件的数据到配置文件"""
        self.settings.setValue("lineedit_gap2", self.lineedit_gap.text())
        self.settings.setValue("lineedit_size2", self.lineedit_size.text())
        self.settings.setValue("lineedit_radius2", self.lineedit_radius.text())
        self.settings.setValue("lineedit_acc2", self.lineedit_acc.text())
        self.settings.setValue("lineedit_amount2", self.lineedit_amount.text())
        self.settings.setValue("lineedit_belt_speed2", self.lineedit_belt_speed.text())
        self.settings.setValue("lineedit_stop_time2", self.lineedit_stop_time.text())
        self.settings.setValue("lineedit_swing_speed2", self.lineedit_swing_speed.text())
        self.settings.setValue("lineedit_swing_time2", self.lineedit_swing_time.text())

    def closeEvent(self, event):
        """在窗口关闭时调用保存设置函数"""
        self.saveSettings()
        super().closeEvent(event)

    # 轨迹动画生成子线程
    def start_computation_trajectory_animation(self):
        self.trajectory_animation_thread = Animation_produce(float(self.lineedit_belt_speed.text()),
                                                             float(self.lineedit_swing_speed.text()),
                                                             float(self.lineedit_swing_time.text()),
                                                             float(self.lineedit_stop_time.text()),
                                                             float(self.lineedit_acc.text()),
                                                             float(self.lineedit_radius.text()),
                                                             float(self.lineedit_gap.text()),
                                                             math.ceil(float(self.lineedit_amount.text()))
                                                             )
        self.trajectory_animation_thread.result_ready.connect(self.trajectory_animation_ready)
        self.button_animation.setEnabled(False)
        # 运行子线程
        self.trajectory_animation_thread.start()

    def trajectory_animation_ready(self,str_222):
        # 加载GIF动画
        print(str_222)
        self.movie = QMovie("./animation2.gif")
        #self.movie.setloopCount(1)  # 设置只播放一次
        self.label_gif.setMovie(self.movie)
        self.movie.start()
        self.button_animation.setEnabled(True)

    # 抛磨量分布仿真子线程
    def start_computation_Polishing_distribution(self):      # 抛磨量分布仿真子线程
        # 创建子线程
        self.Polishing_distribution_thread = Polishing_distribution_Thread(float(self.lineedit_belt_speed.text()),
                                                                           float(self.lineedit_swing_speed.text()),
                                                                           float(self.lineedit_swing_time.text()),
                                                                           float(self.lineedit_stop_time.text()),
                                                                           float(self.lineedit_acc.text()),
                                                                           float(self.lineedit_gap.text()),
                                                                           math.ceil(float(self.lineedit_amount.text())),
                                                                           float(self.lineedit_radius.text()),
                                                                           float(self.lineedit_size.text()))
        self.Polishing_distribution_thread.result_ready.connect(self.Polishing_distribution_ready)
        self.button_simulation.setEnabled(False)
        # 运行子线程
        self.Polishing_distribution_thread.start()

    def Polishing_distribution_ready(self,object_matrix, result):     # 子线程回调函数
        # 在主线程中绘图
        plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置微软雅黑字体
        plt.rcParams['axes.unicode_minus'] = False  # 避免坐标轴不能正常的显示负号
        fig = plt.figure('抛磨强度分布仿真')
        ax = fig.add_subplot(111)
        ax.set_aspect('equal', adjustable='box')
        #plt.gca().set_aspect(1)  # x、y轴等刻度
        im = ax.contourf(object_matrix, 15, alpha=1, cmap='jet')
        plt.xlabel('Tile feed direction')
        plt.ylabel('Beam swing direction')
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.1)
        plt.colorbar(im, cax=cax)
        plt.show()  # 显示函数图像
        self.lineedit_coefficient.setText(result)
        self.button_simulation.setEnabled(True)

    # 绘制磨头中心轨迹线
    def middle_line_figure_plot(self):
        belt_speed = float(self.lineedit_belt_speed.text())
        beam_speed = float(self.lineedit_swing_speed.text())
        constant_time = float(self.lineedit_swing_time.text())
        stay_time = float(self.lineedit_stop_time.text())
        a_speed = float(self.lineedit_acc.text())
        num = math.ceil(float(self.lineedit_amount.text()))
        between = float(self.lineedit_gap.text())
        mid_var = middle_line_plot(belt_speed, beam_speed, constant_time, stay_time, a_speed, num, between)
        mid_var.figure_plot()