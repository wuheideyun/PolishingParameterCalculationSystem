import math
import os

from PySide6.QtCore import QSettings, Qt
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QMovie, QIcon
from PySide6.QtWidgets import QHBoxLayout, QFrame, QWidget, QGridLayout, QVBoxLayout, QMainWindow, QMessageBox
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from qfluentwidgets import PrimaryPushButton, LineEdit, BodyLabel, ImageLabel

from Page5_Self_Define_Calculate import self_define_calculate
from Page5_Single_Generate_Animation import Animation_produce_order
from Page5_Single_Middle_Line_Plot import middle_line_plot_order, middle_line_plot_self_define_order
from Page5_Single_Parameter_Calculate import single_num_calculate
from Page5_Single_Polishing_Distribution_Simulation import Polishing_distribution_Thread_order_unequal, \
    Polishing_distribution_Thread_order


class Page5_Single_Calc_Window(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.customWidth = 100  # 自定义宽度
        self.reCalcFlag = True
        self.settings = QSettings("config.ini", QSettings.IniFormat)  # 使用配置文件

        self.hBoxLayout = QVBoxLayout(self)
        self.setObjectName(text.replace(' ', '-'))

        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        # 初始化所有控件（与原代码保持一致）

        self.iconHead = ImageLabel("./images/single2.png", self.centralwidget)
        self.gridLayout.addWidget(self.iconHead, 0, 0, 1, 10)

        # 1.1横梁间距
        self.label_beam_between = BodyLabel(self.centralwidget)
        self.label_beam_between.setObjectName(u"label_beam_between")
        self.label_beam_between.setFixedWidth(60)
        self.gridLayout.addWidget(self.label_beam_between, 1, 0, 1, 1)
        self.lineEdit_beam_between = LineEdit(self.centralwidget)
        self.lineEdit_beam_between.setObjectName(u"lineEdit_beam_between")
        self.lineEdit_beam_between.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_beam_between, 1, 1, 1, 1)

        # 1.2磨块尺寸
        self.label_grind_size = BodyLabel(self.centralwidget)
        self.label_grind_size.setObjectName(u"label_grind_size")
        self.label_grind_size.setFixedWidth(60)
        self.gridLayout.addWidget(self.label_grind_size, 1, 2, 1, 1)
        self.lineEdit_grind_size = LineEdit(self.centralwidget)
        self.lineEdit_grind_size.setObjectName(u"lineEdit_grind_size")
        self.lineEdit_grind_size.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_grind_size, 1, 3, 1, 1)

        # 1.3皮带速度
        self.label_belt_speed = BodyLabel(self.centralwidget)
        self.label_belt_speed.setObjectName(u"label_belt_speed")
        self.label_belt_speed.setFixedWidth(80)
        self.gridLayout.addWidget(self.label_belt_speed, 1, 4, 1, 1)
        self.lineEdit_belt_speed = LineEdit(self.centralwidget)
        self.lineEdit_belt_speed.setObjectName(u"lineEdit_belt_speed")
        self.lineEdit_belt_speed.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_belt_speed, 1, 5, 1, 1)

        # 1.4加速度大小
        self.label_accelerate = BodyLabel(self.centralwidget)
        self.label_accelerate.setObjectName(u"label_accelerate")
        self.label_accelerate.setFixedWidth(80)
        self.gridLayout.addWidget(self.label_accelerate, 1, 6, 1, 1)
        self.lineEdit_accelerate = LineEdit(self.centralwidget)
        self.lineEdit_accelerate.setObjectName(u"lineEdit_accelerate")
        self.lineEdit_accelerate.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_accelerate, 1, 7, 1, 1)

        # 1.5单组磨头数设定
        self.label_num_set = BodyLabel(self.centralwidget)
        self.label_num_set.setObjectName(u"label_num_set")
        self.label_num_set.setFixedWidth(100)
        self.gridLayout.addWidget(self.label_num_set, 1, 8, 1, 1)
        self.lineEdit_num_set = LineEdit(self.centralwidget)
        self.lineEdit_num_set.setObjectName(u"lineEdit_num_set")
        self.lineEdit_num_set.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_num_set, 1, 9, 1, 1)

        # 2.1磨头半径
        self.label_radius = BodyLabel(self.centralwidget)
        self.label_radius.setObjectName(u"label_radius")
        self.label_radius.setFixedWidth(60)
        self.gridLayout.addWidget(self.label_radius, 2, 0, 1, 1)
        self.lineEdit_radius = LineEdit(self.centralwidget)
        self.lineEdit_radius.setObjectName(u"lineEdit_radius")
        self.lineEdit_radius.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_radius, 2, 1, 1, 1)

        # 2.2进砖宽度
        self.label_cerimatic_width = BodyLabel(self.centralwidget)
        self.label_cerimatic_width.setObjectName(u"label_cerimatic_width")
        self.label_cerimatic_width.setFixedWidth(80)
        self.gridLayout.addWidget(self.label_cerimatic_width, 2, 2, 1, 1)
        self.lineEdit_ceramic_width = LineEdit(self.centralwidget)
        self.lineEdit_ceramic_width.setObjectName(u"lineEdit_ceramic_width")
        self.lineEdit_ceramic_width.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_ceramic_width, 2, 3, 1, 1)

        # 2.3横梁摆动速度上限
        self.label_beam_speed_up = BodyLabel(self.centralwidget)
        self.label_beam_speed_up.setObjectName(u"label_beam_speed_up")
        self.label_beam_speed_up.setFixedWidth(120)
        self.gridLayout.addWidget(self.label_beam_speed_up, 2, 4, 1, 1)
        self.lineEdit_beam_speed_up = LineEdit(self.centralwidget)
        self.lineEdit_beam_speed_up.setObjectName(u"lineEdit_beam_speed_up")
        self.lineEdit_beam_speed_up.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_beam_speed_up, 2, 5, 1, 1)

        # 2.4轨迹重叠量
        self.label_overlap = BodyLabel(self.centralwidget)
        self.label_overlap.setObjectName(u"label_overlap")
        self.label_overlap.setFixedWidth(80)
        self.gridLayout.addWidget(self.label_overlap, 2, 6, 1, 1)
        self.lineEdit_overlap = LineEdit(self.centralwidget)
        self.lineEdit_overlap.setObjectName(u"lineEdit_overlap")
        self.lineEdit_overlap.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_overlap, 2, 7, 1, 1)

        # 2.5组数
        self.label_group_count = BodyLabel(self.centralwidget)
        self.label_group_count.setObjectName(u"label_group_count")
        self.label_group_count.setFixedWidth(80)
        self.gridLayout.addWidget(self.label_group_count, 2, 8, 1, 1)
        self.lineEdit_group_count = LineEdit(self.centralwidget)
        self.lineEdit_group_count.setObjectName(u"lineEdit_group_count")
        self.lineEdit_group_count.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_group_count, 2, 9, 1, 1)

        # 保存参数
        self.button_save = PrimaryPushButton(self.centralwidget)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setFixedWidth(90)
        self.gridLayout.addWidget(self.button_save, 3, 0, 1, 1)

        # 3.1节能计算
        self.button_energy_calculate = PrimaryPushButton(self.centralwidget)
        self.button_energy_calculate.setObjectName(u"button_energy_calculate")
        self.button_energy_calculate.setFixedWidth(100)
        self.gridLayout.addWidget(self.button_energy_calculate, 3, 1, 1, 1)
        self.button_energy_calculate.clicked.connect(self.energy_calculate)  # 节能计算

        # 3.2高效计算
        self.button_efficient_calculate = PrimaryPushButton(self.centralwidget)
        self.button_efficient_calculate.setObjectName(u"button_efficient_calculate")
        self.button_efficient_calculate.setFixedWidth(90)
        self.gridLayout.addWidget(self.button_efficient_calculate, 3, 2, 1, 1)
        self.button_efficient_calculate.clicked.connect(self.efficient_calculate)     # 高效计算

        # 3.3顺序摆动画
        self.button_animation_order = PrimaryPushButton(self.centralwidget)
        self.button_animation_order.setObjectName(u"button_animation_order")
        self.button_animation_order.setFixedWidth(100)
        self.gridLayout.addWidget(self.button_animation_order, 3, 3, 1, 1)
        self.button_animation_order.clicked.connect(self.start_computation_trajectory_animation_order)

        # 3.4顺序摆抛磨量分布仿真
        self.button_simulation_order = PrimaryPushButton(self.centralwidget)
        self.button_simulation_order.setObjectName(u"button_simulation_order")
        self.button_simulation_order.setFixedWidth(190)
        self.gridLayout.addWidget(self.button_simulation_order, 3, 4, 1, 1)
        self.button_simulation_order.clicked.connect(self.start_computation_Polishing_distribution_order)
        # 3.5顺序摆轨迹中心线绘制
        self.button_middle_line_order = PrimaryPushButton(self.centralwidget)
        self.button_middle_line_order.setObjectName(u"button_middle_line_order")
        self.button_middle_line_order.setFixedWidth(190)
        self.gridLayout.addWidget(self.button_middle_line_order, 3, 5, 1, 1)
        self.button_middle_line_order.clicked.connect(self.middle_line_figure_plot_order)

        # 3.6 提示
        self.label_tips = BodyLabel(self.centralwidget)
        self.label_tips.setObjectName(u"label_tips")
        self.label_tips.setFixedWidth(200)
        self.gridLayout.addWidget(self.label_tips, 3, 8, 1, 2)

        # 4.1自定义计算
        self.button_selfdefine_calculate = PrimaryPushButton(self.centralwidget)
        self.button_selfdefine_calculate.setObjectName(u"button_selfdefine_calculate")
        self.button_selfdefine_calculate.setFixedWidth(100)
        self.gridLayout.addWidget(self.button_selfdefine_calculate, 4, 1, 1, 1)
        self.button_selfdefine_calculate.clicked.connect(self.define_calculate)       # 自定义计算计算



        # 4.2顺序摆动画(自定义模式)
        self.button_animation_order_define = PrimaryPushButton(self.centralwidget)
        self.button_animation_order_define.setObjectName(u"button_animation_order_define")
        self.button_animation_order_define.setFixedWidth(180)
        self.gridLayout.addWidget(self.button_animation_order_define, 4, 3, 1, 1)
        self.button_animation_order_define.clicked.connect(self.start_computation_trajectory_animation_order_define)

        # 4.3顺序摆(自定义)抛磨量分布
        self.button_simulation_order_define = PrimaryPushButton(self.centralwidget)
        self.button_simulation_order_define.setObjectName(u"button_simulation_order_define")
        self.button_simulation_order_define.setFixedWidth(190)
        self.gridLayout.addWidget(self.button_simulation_order_define, 4, 4, 1, 1)
        self.button_simulation_order_define.clicked.connect(self.start_computation_Polishing_distribution_order_define)
        # 4.4顺序摆(自定义)中心线绘制
        self.button_middle_line_order_define = PrimaryPushButton(self.centralwidget)
        self.button_middle_line_order_define.setObjectName(u"button_middle_line_order_define")
        self.button_middle_line_order_define.setFixedWidth(190)
        self.gridLayout.addWidget(self.button_middle_line_order_define, 4, 5, 1, 1)
        self.button_middle_line_order_define.clicked.connect(self.middle_line_figure_plot_order_selfdefine)
        # 5.1横梁匀速摆动时间
        self.label_beam_constant_time = BodyLabel(self.centralwidget)
        self.label_beam_constant_time.setObjectName(u"label_beam_constant_time")
        self.label_beam_constant_time.setFixedWidth(120)
        self.gridLayout.addWidget(self.label_beam_constant_time, 5, 1, 1, 1)
        self.lineEdit_beam_constant_time = LineEdit(self.centralwidget)
        self.lineEdit_beam_constant_time.setObjectName(u"lineEdit_beam_constant_time")
        self.lineEdit_beam_constant_time.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_beam_constant_time, 5, 2, 1, 1)

        # 5.2横梁摆动速度
        self.label_beam_swing_speed = BodyLabel(self.centralwidget)
        self.label_beam_swing_speed.setObjectName(u"label_beam_swing_speed")
        self.label_beam_swing_speed.setFixedWidth(120)
        self.gridLayout.addWidget(self.label_beam_swing_speed, 5, 3, 1, 1)
        self.lineEdit_beam_swing_speed = LineEdit(self.centralwidget)
        self.lineEdit_beam_swing_speed.setObjectName(u"lineEdit_beam_swing_speed")
        self.lineEdit_beam_swing_speed.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_beam_swing_speed, 5, 4, 1, 1)

        # 5.3同粒度磨头数目
        self.label_num = BodyLabel(self.centralwidget)
        self.label_num.setObjectName(u"label_num")
        self.gridLayout.addWidget(self.label_num, 5, 5, 1, 1)
        self.lineEdit_num = LineEdit(self.centralwidget)
        self.lineEdit_num.setObjectName(u"lineEdit_num")
        self.lineEdit_num.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_num, 5, 6, 1, 1)

        # 5.4磨头间距
        self.label_between = BodyLabel(self.centralwidget)
        self.label_between.setObjectName(u"label_between")
        self.gridLayout.addWidget(self.label_between, 5, 7, 1, 1)
        self.lineEdit_between = LineEdit(self.centralwidget)
        self.lineEdit_between.setObjectName(u"lineEdit_between")
        self.lineEdit_between.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_between, 5, 8, 1, 1)

        # 6.1边部停留时间
        self.label_stay_time = BodyLabel(self.centralwidget)
        self.label_stay_time.setObjectName(u"label_stay_time")
        self.label_stay_time.setFixedWidth(120)
        self.gridLayout.addWidget(self.label_stay_time, 6, 1, 1, 1)
        self.lineEdit_stay_time = LineEdit(self.centralwidget)
        self.lineEdit_stay_time.setObjectName(u"lineEdit_stay_time")
        self.lineEdit_stay_time.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_stay_time, 6, 2, 1, 1)

        # 6.2摆幅
        self.label_swing = BodyLabel(self.centralwidget)
        self.label_swing.setObjectName(u"label_swing")
        self.gridLayout.addWidget(self.label_swing, 6, 3, 1, 1)
        self.lineEdit_swing = LineEdit(self.centralwidget)
        self.lineEdit_swing.setObjectName(u"lineEdit_swing")
        self.lineEdit_swing.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_swing, 6, 4, 1, 1)

        # 6.3延时时间
        self.label_delay_time = BodyLabel(self.centralwidget)
        self.label_delay_time.setObjectName(u"label_delay_time")
        self.gridLayout.addWidget(self.label_delay_time, 6, 5, 1, 1)
        self.lineEdit_delay_time = LineEdit(self.centralwidget)
        self.lineEdit_delay_time.setObjectName(u"lineEdit_delay_time")
        self.lineEdit_delay_time.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_delay_time, 6, 6, 1, 1)

        # 6.4均匀系数
        self.label_coefficient = BodyLabel(self.centralwidget)
        self.label_coefficient.setObjectName(u"label_coefficient")
        self.gridLayout.addWidget(self.label_coefficient, 6, 7, 1, 1)
        self.lineEdit_coefficient = LineEdit(self.centralwidget)
        self.lineEdit_coefficient.setObjectName(u"lineEdit_coefficient")
        self.lineEdit_coefficient.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_coefficient, 6, 8, 1, 1)

        # 中间图标
        self.iconCenter = ImageLabel("./images/middle2.png", self.centralwidget)
        self.gridLayout.addWidget(self.iconCenter, 7, 0, 1, 10)

        # 动画
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.widget, 8, 0, 1, 10)





        self.iconBottom = ImageLabel("./images/bottom2.png", self.centralwidget)
        self.gridLayout.addWidget(self.iconBottom, 9, 0, 1, 10)

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

        # self.add_text_change_monitor(self.lineEdit_gap)
        # self.add_text_change_monitor(self.lineEdit_size)
        # self.add_text_change_monitor(self.lineEdit_belt_speed)
        # self.add_text_change_monitor(self.lineEdit_acc)
        # self.add_text_change_monitor(self.lineEdit_radius)
        # self.add_text_change_monitor(self.lineEdit_max_speed)
        # self.add_text_change_monitor(self.lineEdit_width)
        # self.add_text_change_monitor(self.lineEdit_overlap)

        # self.line_edits = [self.lineEdit_belt_speed, self.lineEdit_beam_swing_speed, self.lineEdit_beam_swing_time,
        #                    self.lineEdit_stay_time,
        #                    self.lineEdit_acc, self.lineEdit_radius, self.lineEdit_mod_between,
        #                    self.lineEdit_beam_between, self.lineEdit_num, self.lineEdit_delay_time_one]
        # self.initLineEditsWidth()

    # def on_button_clicked(self):
    #     for line_edit in self.line_edits:
    #         if not line_edit.text().strip():  # 如果任何一个LineEdit为空
    #             textname = self.on_Find_Label_Name(line_edit.objectName())
    #             QMessageBox.warning(self, "警告", f"{textname}输入框必须填写数据！")
    #             return False
    #     return True

    # def initLineEditsWidth(self):
    #     for line_edit in self.line_edits:
    #         line_edit.setFixedWidth(100)

    # def on_Find_Label_Name(self, lineEdit_name):
    #
    #     # 构造对应的Label的objectName
    #     label_object_name = lineEdit_name.replace("lineedit", "label")
    #
    #     # 根据objectName找到对应的Label
    #     label = self.findChild(BodyLabel, label_object_name)
    #
    #     if label:
    #         return label.text()

    def addWidget(self, widget):
        self.hBoxLayout.addWidget(widget)

    # 调整动画在界面图框中的位置
    def resize_event(self, event):
        self.label_gif.resize(event.size())

    def add_text_change_monitor(self, line_edit):
        """为LineEdit控件添加内容变化监控"""
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

        self.label_beam_between.setText('横梁间距：')
        self.label_grind_size.setText('磨块尺寸：')
        self.label_belt_speed.setText('皮带速度：')
        self.label_accelerate.setText('加速度大小：')
        self.label_num_set.setText('单组磨头数设定：')
        self.label_radius.setText('磨头半径：')
        self.label_cerimatic_width.setText('进砖宽度：')
        self.label_beam_speed_up.setText('横梁摆动速度上限：')
        self.label_overlap.setText('轨迹重叠量：')
        self.label_group_count.setText('组数：')
        self.label_tips.setText('此项仅在自定义计算模式使用')
        self.label_between.setText('磨头间距')

        self.label_beam_constant_time.setText('横梁匀速摆动时间')
        self.label_beam_swing_speed.setText('横梁摆动速度')
        self.label_num.setText('同粒度磨头数目')
        self.label_stay_time.setText('边部停留时间')
        self.label_swing.setText('摆幅')
        self.label_delay_time.setText('延时时间')
        self.label_coefficient.setText('均匀系数')

        self.button_energy_calculate.setText('节能计算')
        self.button_efficient_calculate.setText('高效计算')
        self.button_animation_order.setText('顺序摆动画')
        self.button_simulation_order.setText('顺序摆抛磨量分布仿真')
        self.button_middle_line_order.setText('顺序摆轨迹中心线绘制')

        self.button_selfdefine_calculate.setText('自定义计算')
        self.button_animation_order_define.setText('顺序摆动画(自定义模式)')
        self.button_simulation_order_define.setText('顺序摆(自定义)抛磨量分布')
        self.button_middle_line_order_define.setText('顺序摆(自定义)中心线绘制')

        self.button_save.setText('保存参数')
        self.button_save.clicked.connect(self.saveSettings)

    def loadSettings(self):
        """加载配置文件中的数据到各个LineEdit控件"""
        self.lineEdit_beam_between.setText(self.settings.value("lineEdit_beam_between5", ""))
        self.lineEdit_grind_size.setText(self.settings.value("lineEdit_grind_size5", ""))
        self.lineEdit_belt_speed.setText(self.settings.value("lineEdit_belt_speed5", ""))
        self.lineEdit_accelerate.setText(self.settings.value("lineEdit_accelerate5", ""))
        self.lineEdit_num_set.setText(self.settings.value("lineEdit_num_set5", ""))
        self.lineEdit_radius.setText(self.settings.value("lineEdit_radius5", ""))
        self.lineEdit_ceramic_width.setText(self.settings.value("lineEdit_ceramic_width5", ""))
        self.lineEdit_beam_speed_up.setText(self.settings.value("lineEdit_beam_speed_up5", ""))
        self.lineEdit_overlap.setText(self.settings.value("lineEdit_overlap5", ""))
        self.lineEdit_group_count.setText(self.settings.value("lineEdit_group_count5", ""))

    def saveSettings(self):
        """保存各个LineEdit控件的数据到配置文件"""
        self.settings.setValue("lineEdit_beam_between5", self.lineEdit_beam_between.text())
        self.settings.setValue("lineEdit_grind_size5", self.lineEdit_grind_size.text())
        self.settings.setValue("lineEdit_belt_speed5", self.lineEdit_belt_speed.text())
        self.settings.setValue("lineEdit_accelerate5", self.lineEdit_accelerate.text())
        self.settings.setValue("lineEdit_num_set5", self.lineEdit_num_set.text())
        self.settings.setValue("lineEdit_radius5", self.lineEdit_radius.text())
        self.settings.setValue("lineEdit_ceramic_width5", self.lineEdit_ceramic_width.text())
        self.settings.setValue("lineEdit_beam_speed_up5", self.lineEdit_beam_speed_up.text())
        self.settings.setValue("lineEdit_overlap5", self.lineEdit_overlap.text())
        self.settings.setValue("lineEdit_group_count5", self.lineEdit_group_count.text())

    def closeEvent(self, event):
        """在窗口关闭时调用保存设置函数"""
        self.saveSettings()
        super().closeEvent(event)

    # 轨迹参数计算（节能计算）
    def energy_calculate(self):
        v1 = float(self.lineEdit_belt_speed.text())
        ceramic_width = float(self.lineEdit_ceramic_width.text())
        beam_between = float(self.lineEdit_beam_between.text())
        R = float(self.lineEdit_radius.text())
        overlap = float(self.lineEdit_overlap.text())
        a = float(self.lineEdit_accelerate.text())
        beam_speed_up = float(self.lineEdit_beam_speed_up.text())
        result = single_num_calculate(v1, ceramic_width, beam_between, R, overlap, a,
                                                                 beam_speed_up)
        self.lineEdit_beam_swing_speed.setText(str(result[0, 1]))
        self.lineEdit_beam_constant_time.setText(str(result[0, 2]))
        self.lineEdit_stay_time.setText(str(result[0, 3]))
        self.lineEdit_num.setText(str(result[0, 4]))
        self.lineEdit_delay_time.setText(str(result[0, 5]))
        self.lineEdit_swing.setText(str(result[0, 6]))
        self.lineEdit_between.setText(str(result[0, 7]))

    # 轨迹参数计算（高效计算）
    def efficient_calculate(self):  # 高效计算
        v1 = float(self.lineEdit_belt_speed.text())
        ceramic_width = float(self.lineEdit_ceramic_width.text())
        beam_between = float(self.lineEdit_beam_between.text())
        R = float(self.lineEdit_radius.text())
        overlap = float(self.lineEdit_overlap.text())
        a = float(self.lineEdit_accelerate.text())
        beam_speed_up = float(self.lineEdit_beam_speed_up.text())
        result = single_num_calculate(v1, ceramic_width, beam_between, R, overlap, a,
                                                                 beam_speed_up)
        self.lineEdit_beam_swing_speed.setText(str(result[1, 1]))
        self.lineEdit_beam_constant_time.setText(str(result[1, 2]))
        self.lineEdit_stay_time.setText(str(result[1, 3]))
        self.lineEdit_num.setText(str(result[1, 4]))
        self.lineEdit_delay_time.setText(str(result[1, 5]))
        self.lineEdit_swing.setText(str(result[1, 6]))
        self.lineEdit_between.setText(str(result[0, 7]))

    # 轨迹参数计算（自定义计算）
    def define_calculate(self):
        v1 = float(self.lineEdit_belt_speed.text())
        ceramic_width = float(self.lineEdit_ceramic_width.text())
        beam_between = float(self.lineEdit_beam_between.text())
        R = float(self.lineEdit_radius.text())
        a = float(self.lineEdit_accelerate.text())
        num = float(self.lineEdit_num_set.text())
        group = float(self.lineEdit_group_count.text())
        stay_time = float(self.lineEdit_stay_time.text())
        beam_speed_up = float(self.lineEdit_beam_speed_up.text())
        result = self_define_calculate(v1, beam_speed_up, ceramic_width, beam_between, R, a, num, stay_time)
        self.lineEdit_beam_swing_speed.setText(str(result[0, 1]))
        self.lineEdit_beam_constant_time.setText(str(result[0, 2]))
        self.lineEdit_stay_time.setText(str(result[0, 3]))
        self.lineEdit_num.setText(str(result[0, 4] * group))
        self.lineEdit_delay_time.setText(str(result[0, 5]))
        self.lineEdit_swing.setText(str(result[0, 6]))
        self.lineEdit_between.setText(str(result[0, 7]))

    # 顺序摆动画
    def start_computation_trajectory_animation_order(self):
        self.trajectory_animation_thread = Animation_produce_order(float(self.lineEdit_belt_speed.text()),
                                                                   float(self.lineEdit_beam_swing_speed.text()),
                                                                   float(self.lineEdit_beam_constant_time.text()),
                                                                   float(self.lineEdit_stay_time.text()),
                                                                   float(self.lineEdit_accelerate.text()),
                                                                   float(self.lineEdit_radius.text()),
                                                                   float(self.lineEdit_between.text()),
                                                                   float(self.lineEdit_beam_between.text()),
                                                                   math.ceil(float(self.lineEdit_num.text())),
                                                                   float(self.lineEdit_delay_time.text())
                                                                   )
        self.trajectory_animation_thread.result_ready.connect(self.trajectory_animation_ready)
        self.button_animation_order.setEnabled(False)
        self.button_animation_order_define.setEnabled(False)
        # 运行子线程
        self.trajectory_animation_thread.start()

    # 顺序摆动画（自定义模式）
    def start_computation_trajectory_animation_order_define(self):
        self.trajectory_animation_thread = Animation_produce_order(float(self.lineEdit_belt_speed.text()),
                                                                   float(self.lineEdit_beam_swing_speed.text()),
                                                                   float(self.lineEdit_beam_constant_time.text()),
                                                                   float(self.lineEdit_stay_time.text()),
                                                                   float(self.lineEdit_accelerate.text()),
                                                                   float(self.lineEdit_radius.text()),
                                                                   float(self.lineEdit_between.text()),
                                                                   float(self.lineEdit_beam_between.text()),
                                                                   math.ceil(float(self.lineEdit_num_set.text())),
                                                                   float(self.lineEdit_delay_time.text())
                                                                   )
        self.trajectory_animation_thread.result_ready.connect(self.trajectory_animation_ready)
        self.button_animation_order.setEnabled(False)
        self.button_animation_order_define.setEnabled(False)
        # 运行子线程
        self.trajectory_animation_thread.start()

    # 顺序摆动画（自定义模式）
    def start_computation_trajectory_animation_order_define(self):
        self.trajectory_animation_thread = Animation_produce_order(float(self.lineEdit_belt_speed.text()),
                                                                   float(self.lineEdit_beam_swing_speed.text()),
                                                                   float(self.lineEdit_beam_constant_time.text()),
                                                                   float(self.lineEdit_stay_time.text()),
                                                                   float(self.lineEdit_accelerate.text()),
                                                                   float(self.lineEdit_radius.text()),
                                                                   float(self.lineEdit_between.text()),
                                                                   float(self.lineEdit_beam_between.text()),
                                                                   math.ceil(float(self.lineEdit_num_set.text())),
                                                                   float(self.lineEdit_delay_time.text())
                                                                   )
        self.trajectory_animation_thread.result_ready.connect(self.trajectory_animation_ready)
        self.button_animation_order.setEnabled(False)
        self.button_animation_order_define.setEnabled(False)
        # 运行子线程
        self.trajectory_animation_thread.start()

    # 顺序摆抛磨量分布仿真子线程
    def start_computation_Polishing_distribution_order(self):  # 抛磨量分布仿真子线程
        # 创建子线程
        self.Polishing_distribution_thread = Polishing_distribution_Thread_order(
            float(self.lineEdit_belt_speed.text()),
            float(self.lineEdit_beam_swing_speed.text()),
            float(self.lineEdit_beam_constant_time.text()),
            float(self.lineEdit_stay_time.text()),
            float(self.lineEdit_accelerate.text()),
            float(self.lineEdit_between.text()),
            float(self.lineEdit_beam_between.text()),
            math.ceil(float(self.lineEdit_num.text())),
            float(self.lineEdit_radius.text()),
            float(self.lineEdit_grind_size.text()),
            float(self.lineEdit_delay_time.text()))
        self.Polishing_distribution_thread.result_ready.connect(self.Polishing_distribution_ready)
        self.button_simulation_order.setEnabled(False)
        self.button_simulation_order_define.setEnabled(False)
        # 运行子线程
        self.Polishing_distribution_thread.start()

    # 顺序摆（自定义）抛磨量分布仿真子线程
    def start_computation_Polishing_distribution_order_define(self):  # 抛磨量分布仿真子线程
        # 创建子线程
        self.Polishing_distribution_thread = Polishing_distribution_Thread_order_unequal(
            float(self.lineEdit_belt_speed.text()),
            float(self.lineEdit_beam_swing_speed.text()),
            float(self.lineEdit_beam_constant_time.text()),
            float(self.lineEdit_stay_time.text()),
            float(self.lineEdit_accelerate.text()),
            float(self.lineEdit_between.text()),
            float(self.lineEdit_beam_between.text()),
            math.ceil(float(self.lineEdit_num_set.text())),
            float(self.lineEdit_radius.text()),
            float(self.lineEdit_grind_size.text()),
            float(self.lineEdit_delay_time.text()),
            float(self.lineEdit_group_count.text()))
        self.Polishing_distribution_thread.result_ready.connect(self.Polishing_distribution_ready)
        self.button_simulation_order.setEnabled(False)
        self.button_simulation_order_define.setEnabled(False)
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
        # equal_coefficient
        self.button_simulation_order.setEnabled(True)
        self.button_simulation_order_define.setEnabled(True)

    # 绘制磨头中心轨迹线
    # 顺序摆模式轨迹中心线
    def middle_line_figure_plot_order(self):
        belt_speed = float(self.lineEdit_belt_speed.text())
        beam_speed = float(self.lineEdit_beam_swing_speed.text())
        constant_time = float(self.lineEdit_beam_constant_time.text())
        stay_time = float(self.lineEdit_stay_time.text())
        a_speed = float(self.lineEdit_accelerate.text())
        num = math.ceil(float(self.lineEdit_num.text()))
        between = float(self.lineEdit_between.text())
        between_beam = float(self.lineEdit_beam_between.text())
        delay_tome = float(self.lineEdit_delay_time.text())
        mid_var = middle_line_plot_order(belt_speed, beam_speed, constant_time, stay_time, a_speed, num, between,
                                         between_beam, delay_tome)
        mid_var.figure_plot()

    # 顺序摆（自定义）模式轨迹中心线
    def middle_line_figure_plot_order_selfdefine(self):
        belt_speed = float(self.lineEdit_belt_speed.text())
        beam_speed = float(self.lineEdit_beam_swing_speed.text())
        constant_time = float(self.lineEdit_beam_constant_time.text())
        stay_time = float(self.lineEdit_stay_time.text())
        a_speed = float(self.lineEdit_accelerate.text())
        num = math.ceil(float(self.lineEdit_num_set.text()))
        between = float(self.lineEdit_between.text())
        between_beam = float(self.lineEdit_beam_between.text())
        delay_time = float(self.lineEdit_delay_time.text())
        group = float(self.lineEdit_group_count.text())
        mid_var = middle_line_plot_self_define_order(belt_speed, beam_speed, constant_time, stay_time, a_speed, num,
                                                     between, between_beam, delay_time, group)
        mid_var.figure_plot()



    def trajectory_animation_ready(self, str_22):
        # 加载GIF动画
        print(str_22)
        self.movie = QMovie("animation.gif")
        # self.movie.setloopCount(1)  # 设置只播放一次
        self.label_gif.setMovie(self.movie)
        self.movie.start()
        self.button_animation_order.setEnabled(True)
        self.button_animation_order_define.setEnabled(True)

    def on_button_clicked(self):
        for line_edit in self.line_edits:
            if not line_edit.text().strip():  # 如果任何一个LineEdit为空
                textname = self.on_Find_Label_Name(line_edit.objectName())
                QMessageBox.warning(self, "警告", f"{textname}输入框必须填写数据！")
                return False
        return True
