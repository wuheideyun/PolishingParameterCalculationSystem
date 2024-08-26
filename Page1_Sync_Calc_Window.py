import math
import os

from PySide6.QtCore import QSettings, Qt
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QMovie, QIcon
from PySide6.QtWidgets import QHBoxLayout, QFrame, QWidget, QGridLayout, QVBoxLayout, QLabel, QMainWindow, QMessageBox
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from qfluentwidgets import PrimaryPushButton, LineEdit, BodyLabel, ImageLabel

from Page1_Sync_Algorithms_Polishing_Distribution_Simulation import Polishing_distribution_Thread
from Page1_Sync_Algorithms_Generate_Animation import Animation_produce
from Page1_Sync_Algorithms_Middle_Line_Plot import middle_line_plot
from Page1_Sync_Algorithms_Equal_Parameter_Calculate import equal_num_calculate


class Page1_Window_Sync_Calc(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.reCalcFlag = True
        self.settings = QSettings("config.ini", QSettings.IniFormat)  # 使用配置文件

        self.hBoxLayout = QVBoxLayout(self)
        self.setObjectName(text.replace(' ', '-'))

        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        # 初始化所有控件（与原代码保持一致）
        # 磨头间距
        self.iconHead = ImageLabel("./images/double2.png", self.centralwidget)
        self.gridLayout.addWidget(self.iconHead, 0, 0, 1, 13)

        self.label_gap = BodyLabel(self.centralwidget)
        self.label_gap.setObjectName(u"label_gap")
        self.gridLayout.addWidget(self.label_gap, 1, 1, 1, 1)

        self.lineedit_gap = LineEdit(self.centralwidget)
        self.lineedit_gap.setObjectName(u"lineedit_gap")
        self.gridLayout.addWidget(self.lineedit_gap, 1, 2, 1, 1)

        # 磨块尺寸
        self.label_size = BodyLabel(self.centralwidget)
        self.label_size.setObjectName(u"label_size")
        self.gridLayout.addWidget(self.label_size, 1, 4, 1, 1)

        self.lineedit_size = LineEdit(self.centralwidget)
        self.lineedit_size.setObjectName(u"lineedit_size")
        self.gridLayout.addWidget(self.lineedit_size, 1, 5, 1, 1)

        # 皮带速度
        self.label_belt_speed = BodyLabel(self.centralwidget)
        self.label_belt_speed.setObjectName(u"label_belt_speed")
        self.gridLayout.addWidget(self.label_belt_speed, 1, 7, 1, 1)

        self.lineedit_belt_speed = LineEdit(self.centralwidget)
        self.lineedit_belt_speed.setObjectName(u"lineedit_belt_speed")
        self.gridLayout.addWidget(self.lineedit_belt_speed, 1, 8, 1, 1)

        # 加速度大小
        self.label_acc = BodyLabel(self.centralwidget)
        self.label_acc.setObjectName(u"label_acc")
        self.gridLayout.addWidget(self.label_acc, 1, 10, 1, 1)

        self.lineedit_acc = LineEdit(self.centralwidget)
        self.lineedit_acc.setObjectName(u"lineedit_acc")
        self.gridLayout.addWidget(self.lineedit_acc, 1, 11, 1, 1)
        self.lineedit_acc.setFixedWidth(80)

        # 磨头间距English
        self.label_gap_english = BodyLabel(self.centralwidget)
        self.label_gap_english.setObjectName(u"label_gap_english")
        self.gridLayout.addWidget(self.label_gap_english, 2, 1, 1, 2)
        self.label_gap_english.setText('Grinding head spacing')
        # 磨块尺寸English
        self.label_size_english = BodyLabel(self.centralwidget)
        self.label_size_english.setObjectName(u"label_size_english")
        self.gridLayout.addWidget(self.label_size_english, 2, 4, 1, 2)
        self.label_size_english.setText('Grinding block size')
        # 皮带速度English
        self.label_belt_speed_english = BodyLabel(self.centralwidget)
        self.label_belt_speed_english.setObjectName(u"label_belt_speed_english")
        self.gridLayout.addWidget(self.label_belt_speed_english, 2, 7, 1, 2)
        self.label_belt_speed_english.setText('Belt speed')
        # 加速度大小English
        self.label_acc_english = BodyLabel(self.centralwidget)
        self.label_acc_english.setObjectName(u"label_acc_english")
        self.gridLayout.addWidget(self.label_acc_english, 2, 10, 1, 2)
        self.label_acc_english.setText('Acceleration')

        # 磨头半径
        self.label_radius = BodyLabel(self.centralwidget)
        self.label_radius.setObjectName(u"label_radius")
        self.gridLayout.addWidget(self.label_radius, 3, 1, 1, 1)

        self.lineedit_radius = LineEdit(self.centralwidget)
        self.lineedit_radius.setObjectName(u"lineedit_radius")
        self.gridLayout.addWidget(self.lineedit_radius, 3, 2, 1, 1)

        # 进砖宽度
        self.label_width = BodyLabel(self.centralwidget)
        self.label_width.setObjectName(u"label_width")
        self.gridLayout.addWidget(self.label_width, 3, 4, 1, 1)

        self.lineedit_width = LineEdit(self.centralwidget)
        self.lineedit_width.setObjectName(u"lineedit_width")
        self.gridLayout.addWidget(self.lineedit_width, 3, 5, 1, 1)

        # 摆动速度上限
        self.label_max_speed = BodyLabel(self.centralwidget)
        self.label_max_speed.setObjectName(u"label_max_speed")
        self.gridLayout.addWidget(self.label_max_speed, 3, 7, 1, 1)

        self.lineedit_max_speed = LineEdit(self.centralwidget)
        self.lineedit_max_speed.setObjectName(u"lineedit_max_speed")
        self.gridLayout.addWidget(self.lineedit_max_speed, 3, 8, 1, 1)

        # 轨迹重叠量
        self.label_overlap = BodyLabel(self.centralwidget)
        self.label_overlap.setObjectName(u"label_overlap")
        self.gridLayout.addWidget(self.label_overlap, 3, 10, 1, 1)

        self.lineedit_overlap = LineEdit(self.centralwidget)
        self.lineedit_overlap.setObjectName(u"lineedit_overlap")
        self.gridLayout.addWidget(self.lineedit_overlap, 3, 11, 1, 1)
        self.lineedit_overlap.setFixedWidth(80)

        # 磨头半径English
        self.label_radius_english = BodyLabel(self.centralwidget)
        self.label_radius_english.setObjectName(u"label_radius_english")
        self.gridLayout.addWidget(self.label_radius_english, 4, 1, 1, 2)
        self.label_radius_english.setText('Grinding head radius')
        # 进砖宽度English
        self.label_width_english = BodyLabel(self.centralwidget)
        self.label_width_english.setObjectName(u"label_width_english")
        self.gridLayout.addWidget(self.label_width_english, 4, 4, 1, 2)
        self.label_width_english.setText('Feed width')
        # 摆动速度上限English
        self.label_max_speed_english = BodyLabel(self.centralwidget)
        self.label_max_speed_english.setObjectName(u"label_max_speed_english")
        self.gridLayout.addWidget(self.label_max_speed_english, 4, 7, 1, 2)
        self.label_max_speed_english.setText('Upper limit of swing speed')
        # 轨迹重叠量English
        self.label_overlap_english = BodyLabel(self.centralwidget)
        self.label_overlap_english.setObjectName(u"label_acc_english")
        self.gridLayout.addWidget(self.label_overlap_english, 4, 10, 1, 2)
        self.label_overlap_english.setText('Overlap')

        self.button_energy = PrimaryPushButton(self.centralwidget)
        self.button_energy.setObjectName(u"energy_button")
        self.gridLayout.addWidget(self.button_energy, 5, 3, 1, 1)

        self.button_save = PrimaryPushButton(self.centralwidget)
        self.button_save.setObjectName(u"button_save")
        self.gridLayout.addWidget(self.button_save, 5, 1, 1, 1)

        self.button_efficient = PrimaryPushButton(self.centralwidget)
        self.button_efficient.setObjectName(u"efficient_button")
        self.gridLayout.addWidget(self.button_efficient, 5, 4, 1, 1)

        self.iconCenter = ImageLabel("./images/middle2.png", self.centralwidget)
        self.gridLayout.addWidget(self.iconCenter, 6, 0, 1, 13)

        # 动画左侧按钮
        self.button_simulation = PrimaryPushButton(self.centralwidget)
        self.button_simulation.setObjectName(u"simulation_button")
        self.gridLayout.addWidget(self.button_simulation, 7, 0, 2, 1)
        self.button_simulation.setFixedWidth(135)

        self.button_middle_line = PrimaryPushButton(self.centralwidget)
        self.button_middle_line.setObjectName(u"middle_line_button")
        self.gridLayout.addWidget(self.button_middle_line, 9, 0, 2, 1)
        self.button_middle_line.setFixedWidth(135)

        self.button_animation = PrimaryPushButton(self.centralwidget)
        self.button_animation.setObjectName(u"animation_button")
        self.gridLayout.addWidget(self.button_animation, 11, 0, 2, 1)
        self.button_animation.setFixedWidth(135)

        # 动画
        self.widget = QWidget(self.centralwidget)
        self.widget.resize(400, 400)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.widget, 7, 1, 8, 10)

        # 动画右侧
        self.label_beam_speed = BodyLabel(self.centralwidget)
        self.label_beam_speed.setObjectName(u"label_beam_speed")
        self.gridLayout.addWidget(self.label_beam_speed, 7, 11, 1, 1)

        self.lineedit_beam_speed = LineEdit(self.centralwidget)
        self.lineedit_beam_speed.setObjectName(u"lineedit_beam_speed")
        self.gridLayout.addWidget(self.lineedit_beam_speed, 7, 12, 1, 1)
        self.lineedit_beam_speed.setEnabled(False)
        self.lineedit_beam_speed.setFixedWidth(80)

        self.label_swing = BodyLabel(self.centralwidget)
        self.label_swing.setObjectName(u"label_swing")
        self.gridLayout.addWidget(self.label_swing, 8, 11, 1, 1)

        self.lineedit_swing = LineEdit(self.centralwidget)
        self.lineedit_swing.setObjectName(u"lineedit_swing")
        self.gridLayout.addWidget(self.lineedit_swing, 8, 12, 1, 1)
        self.lineedit_swing.setEnabled(False)
        self.lineedit_swing.setFixedWidth(80)

        self.label_stop_time = BodyLabel(self.centralwidget)
        self.label_stop_time.setObjectName(u"label_stop_time")
        self.gridLayout.addWidget(self.label_stop_time, 9, 11, 1, 1)

        self.lineedit_stop_time = LineEdit(self.centralwidget)
        self.lineedit_stop_time.setObjectName(u"lineedit_stop_time")
        self.gridLayout.addWidget(self.lineedit_stop_time, 9, 12, 1, 1)
        self.lineedit_stop_time.setEnabled(False)
        self.lineedit_stop_time.setFixedWidth(80)

        self.label_swing_time = BodyLabel(self.centralwidget)
        self.label_swing_time.setObjectName(u"label_swing_time")
        self.gridLayout.addWidget(self.label_swing_time, 10, 11, 1, 1)

        self.lineedit_swing_time = LineEdit(self.centralwidget)
        self.lineedit_swing_time.setObjectName(u"lineedit_swing_time")
        self.gridLayout.addWidget(self.lineedit_swing_time, 10, 12, 1, 1)
        self.lineedit_swing_time.setEnabled(False)
        self.lineedit_swing_time.setFixedWidth(80)

        self.label_amount = BodyLabel(self.centralwidget)
        self.label_amount.setObjectName(u"label_amount")
        self.gridLayout.addWidget(self.label_amount, 11, 11, 1, 1)

        self.lineedit_amount = LineEdit(self.centralwidget)
        self.lineedit_amount.setObjectName(u"lineedit_amount")
        self.gridLayout.addWidget(self.lineedit_amount, 11, 12, 1, 1)
        self.lineedit_amount.setEnabled(False)
        self.lineedit_amount.setFixedWidth(80)

        self.label_coefficient = BodyLabel(self.centralwidget)
        self.label_coefficient.setObjectName(u"label_coefficient")
        self.gridLayout.addWidget(self.label_coefficient, 12, 11, 1, 1)

        self.lineedit_coefficient = LineEdit(self.centralwidget)
        self.lineedit_coefficient.setObjectName(u"lineedit_coefficient")
        self.gridLayout.addWidget(self.lineedit_coefficient, 12, 12, 1, 1)
        self.lineedit_coefficient.setEnabled(False)
        self.lineedit_coefficient.setFixedWidth(80)

        self.iconBottom = ImageLabel("./images/bottom2.png", self.centralwidget)
        self.gridLayout.addWidget(self.iconBottom, 14, 0, 1, 13)

        # self.gridLayout.setContentsMargins(50, 50, 50, 50)

        # self.iconLabel = ImageLabel("./images/double2.png", self.centralwidget)
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

        self.add_text_change_monitor(self.lineedit_gap)
        self.add_text_change_monitor(self.lineedit_size)
        self.add_text_change_monitor(self.lineedit_belt_speed)
        self.add_text_change_monitor(self.lineedit_acc)
        self.add_text_change_monitor(self.lineedit_radius)
        self.add_text_change_monitor(self.lineedit_max_speed)
        self.add_text_change_monitor(self.lineedit_width)
        self.add_text_change_monitor(self.lineedit_overlap)

        self.line_edits = [self.lineedit_gap, self.lineedit_size, self.lineedit_belt_speed, self.lineedit_acc,
                           self.lineedit_radius, self.lineedit_max_speed, self.lineedit_width, self.lineedit_overlap]

        self.initLineEditsWidth()
    def on_button_clicked(self):
        for line_edit in self.line_edits:
            if not line_edit.text().strip():  # 如果任何一个LineEdit为空
                textname = self.on_Find_Label_Name(line_edit.objectName())
                QMessageBox.warning(self, "警告", f"{textname}输入框必须填写数据！")
                return False
        return True

    def initLineEditsWidth(self):
        for line_edit in self.line_edits:
            line_edit.setFixedWidth(100)

    def on_Find_Label_Name(self, lineedit_name):

        # 构造对应的Label的objectName
        label_object_name = lineedit_name.replace("lineedit", "label")

        # 根据objectName找到对应的Label
        label = self.findChild(BodyLabel, label_object_name)

        if label:
            return label.text()

    def addWidget(self, widget):
        self.hBoxLayout.addWidget(widget)

    # 调整动画在界面图框中的位置
    def resize_event(self, event):
        self.label_gif.resize(event.size())

    def add_text_change_monitor(self, line_edit):
        """为QLineEdit控件添加内容变化监控"""
        line_edit.textChanged.connect(self.on_text_changed)

    def on_text_changed(self, text):
        """当LineEdit内容发生变化时触发的回调函数"""
        # print(f"内容发生变化: {text}")
        self.reCalcFlag = True

    def needReCalculation(self):
        if self.reCalcFlag:
            return True
        else:
            return False

    def initReCalculation(self):
        self.reCalcFlag = False

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_gap.setText('磨头间距：')
        self.label_size.setText('磨块尺寸：')
        self.label_belt_speed.setText('皮带速度：')
        self.label_acc.setText('加速度大小：')
        self.label_radius.setText('磨头半径：')
        self.label_width.setText('进砖宽度：')
        self.label_max_speed.setText('摆动速度上限：')
        self.label_overlap.setText('轨迹重叠量：')
        self.label_beam_speed.setText('横梁摆动速度')
        self.label_swing.setText('摆幅')
        self.label_stop_time.setText('边部停留时间')
        self.label_swing_time.setText('横梁匀速摆动时间')
        self.label_amount.setText('同粒度磨头数目')
        self.label_coefficient.setText('均匀系数')
        self.button_energy.setText('节能计算')
        self.button_energy.clicked.connect(self.energy_calculate)
        self.button_efficient.setText('高效计算')
        self.button_efficient.clicked.connect(self.efficient_calculate)
        self.button_simulation.setText('抛磨量分布仿真')
        self.button_simulation.clicked.connect(self.start_computation_Polishing_distribution)  # 抛磨量分布仿真按钮

        self.button_middle_line.setText('轨迹中心线绘制')
        self.button_middle_line.clicked.connect(self.middle_line_figure_plot)

        self.button_animation.setText('动画按钮')
        self.button_animation.clicked.connect(self.start_computation_trajectory_animation)

        self.button_save.setText('保存参数')
        self.button_save.clicked.connect(self.saveSettings)

    def loadSettings(self):
        """加载配置文件中的数据到各个LineEdit控件"""
        self.lineedit_gap.setText(self.settings.value("lineedit_gap1", ""))
        self.lineedit_size.setText(self.settings.value("lineedit_size1", ""))
        self.lineedit_belt_speed.setText(self.settings.value("lineedit_belt_speed1", ""))
        self.lineedit_acc.setText(self.settings.value("lineedit_acc1", ""))
        self.lineedit_radius.setText(self.settings.value("lineedit_radius1", ""))
        self.lineedit_width.setText(self.settings.value("lineedit_width1", ""))
        self.lineedit_max_speed.setText(self.settings.value("lineedit_max_speed1", ""))
        self.lineedit_overlap.setText(self.settings.value("lineedit_overlap1", ""))
        # self.lineedit_beam_speed.setText(self.settings.value("lineedit_beam_speed", ""))
        # self.lineedit_swing.setText(self.settings.value("lineedit_swing", ""))
        # self.lineedit_stop_time.setText(self.settings.value("lineedit_stop_time", ""))
        # self.lineedit_swing_time.setText(self.settings.value("lineedit_swing_time", ""))
        # self.lineedit_coefficient.setText(self.settings.value("lineedit_coefficient", ""))
        # self.lineedit_amount.setText(self.settings.value("lineedit_amount", ""))

    def saveSettings(self):
        """保存各个LineEdit控件的数据到配置文件"""
        self.settings.setValue("lineedit_gap1", self.lineedit_gap.text())
        self.settings.setValue("lineedit_size1", self.lineedit_size.text())
        self.settings.setValue("lineedit_belt_speed1", self.lineedit_belt_speed.text())
        self.settings.setValue("lineedit_acc1", self.lineedit_acc.text())
        self.settings.setValue("lineedit_radius1", self.lineedit_radius.text())
        self.settings.setValue("lineedit_width1", self.lineedit_width.text())
        self.settings.setValue("lineedit_max_speed1", self.lineedit_max_speed.text())
        self.settings.setValue("lineedit_overlap1", self.lineedit_overlap.text())
        # self.settings.setValue("lineedit_beam_speed", self.lineedit_beam_speed.text())
        # self.settings.setValue("lineedit_swing", self.lineedit_swing.text())
        # self.settings.setValue("lineedit_stop_time", self.lineedit_stop_time.text())
        # self.settings.setValue("lineedit_swing_time", self.lineedit_swing_time.text())
        # self.settings.setValue("lineedit_coefficient", self.lineedit_coefficient.text())
        # self.settings.setValue("lineedit_amount", self.lineedit_amount.text())

    def closeEvent(self, event):
        """在窗口关闭时调用保存设置函数"""
        self.saveSettings()
        super().closeEvent(event)

    # 轨迹参数计算（节能计算）
    def energy_calculate(self):
        v1 = float(self.lineedit_belt_speed.text())
        ceramic_width = float(self.lineedit_width.text())
        between = float(self.lineedit_gap.text())
        R = float(self.lineedit_radius.text())
        overlap = float(self.lineedit_overlap.text())
        a = float(self.lineedit_acc.text())
        beam_speed_up = float(self.lineedit_max_speed.text())
        result = equal_num_calculate(v1, ceramic_width, between, R, overlap, a,
                                     beam_speed_up)
        self.lineedit_beam_speed.setText(str(result[0, 1]))
        self.lineedit_amount.setText(str(result[0, 4]))
        self.lineedit_stop_time.setText(str(result[0, 3]))
        self.lineedit_swing_time.setText(str(result[0, 2]))
        self.lineedit_swing.setText(str(result[0, 5]))

        self.initReCalculation()

    # 轨迹参数计算（高效计算）
    def efficient_calculate(self):  # 高效计算
        v1 = float(self.lineedit_belt_speed.text())
        ceramic_width = float(self.lineedit_width.text())
        between = float(self.lineedit_gap.text())
        R = float(self.lineedit_radius.text())
        overlap = float(self.lineedit_overlap.text())
        a = float(self.lineedit_acc.text())
        beam_speed_up = float(self.lineedit_max_speed.text())
        result = equal_num_calculate(v1, ceramic_width, between, R, overlap, a,
                                     beam_speed_up)
        self.lineedit_beam_speed.setText(str(result[1, 1]))
        self.lineedit_amount.setText(str(result[1, 4]))
        self.lineedit_stop_time.setText(str(result[1, 3]))
        self.lineedit_swing_time.setText(str(result[1, 2]))
        self.lineedit_swing.setText(str(result[1, 5]))

        self.initReCalculation()

    def start_computation_Polishing_distribution(self):  # 抛磨量分布仿真子线程
        if self.needReCalculation():
            QMessageBox.information(None, '提示', '参数已经更改，请重新点击【计算】后再执行此操作！')

        # 创建子线程
        self.Polishing_distribution_thread = Polishing_distribution_Thread(float(self.lineedit_belt_speed.text()),
                                                                           float(self.lineedit_beam_speed.text()),
                                                                           float(self.lineedit_swing_time.text()),
                                                                           float(self.lineedit_stop_time.text()),
                                                                           float(self.lineedit_acc.text()),
                                                                           float(self.lineedit_gap.text()),
                                                                           math.ceil(
                                                                               float(self.lineedit_amount.text())),
                                                                           float(self.lineedit_radius.text()),
                                                                           float(self.lineedit_size.text()))
        self.Polishing_distribution_thread.result_ready.connect(self.Polishing_distribution_ready)
        self.button_simulation.setEnabled(False)
        # 运行子线程
        self.Polishing_distribution_thread.start()

    def Polishing_distribution_ready(self, object_matrix, result):  # 子线程回调函数
        # 在主线程中绘图
        plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置微软雅黑字体
        plt.rcParams['axes.unicode_minus'] = False  # 避免坐标轴不能正常的显示负号
        fig = plt.figure('抛磨强度分布仿真')
        ax = fig.add_subplot(111)
        ax.set_aspect('equal', adjustable='box')
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
        if self.needReCalculation():
            QMessageBox.information(None, '提示', '参数已经更改，请重新点击【计算】后再执行此操作！')

        belt_speed = float(self.lineedit_belt_speed.text())
        beam_speed = float(self.lineedit_beam_speed.text())
        constant_time = float(self.lineedit_swing_time.text())
        stay_time = float(self.lineedit_stop_time.text())
        a_speed = float(self.lineedit_acc.text())
        num = math.ceil(float(self.lineedit_amount.text()))
        between = float(self.lineedit_gap.text())
        mid_var = middle_line_plot(belt_speed, beam_speed, constant_time, stay_time, a_speed, num, between)
        mid_var.figure_plot()

    # 轨迹动画生成子线程
    def start_computation_trajectory_animation(self):
        if not self.on_button_clicked():
            return
        if self.needReCalculation():
            QMessageBox.information(None, '提示', '参数已经更改，请重新点击【计算】后再执行此操作！')
            return
        animation_name = ('SyncCalcAnimation-' +
                          self.lineedit_gap.text() + '_' + self.lineedit_belt_speed.text() + '_' + self.lineedit_acc.text() + '_' +
                          self.lineedit_radius.text() + '_' +
                          self.lineedit_beam_speed.text() + '_' +
                          self.lineedit_stop_time.text() + '_' + self.lineedit_swing_time.text() + '_' +
                          self.lineedit_amount.text())

        if not self.check_animation_gif(animation_name):
            self.trajectory_animation_thread = Animation_produce(float(self.lineedit_belt_speed.text()),
                                                                 float(self.lineedit_beam_speed.text()),
                                                                 float(self.lineedit_swing_time.text()),
                                                                 float(self.lineedit_stop_time.text()),
                                                                 float(self.lineedit_acc.text()),
                                                                 float(self.lineedit_radius.text()),
                                                                 float(self.lineedit_gap.text()),
                                                                 math.ceil(float(self.lineedit_amount.text())),
                                                                 animation_name
                                                                 )
            self.trajectory_animation_thread.result_ready.connect(self.trajectory_animation_ready)
            self.button_animation.setEnabled(False)
            # 运行子线程
            self.trajectory_animation_thread.start()
        else:
            self.trajectory_animation_ready(animation_name)

    def check_animation_gif(self, animation_name):
        # 定义文件路径
        file_path = os.path.join(os.getcwd(), 'animation', animation_name + '.gif')

        # 判断文件是否存在
        return os.path.isfile(file_path)

    def trajectory_animation_ready(self, animation_name):
        # 加载GIF动画
        print(animation_name)
        self.movie = QMovie('./animation/' + animation_name + '.gif')
        # self.movie.setloopCount(1)  # 设置只播放一次
        self.label_gif.setMovie(self.movie)
        self.movie.start()
        self.button_animation.setEnabled(True)
