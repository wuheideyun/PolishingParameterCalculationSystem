import math
import os

from PySide6.QtCore import QSettings, Qt
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QMovie, QIcon
from PySide6.QtWidgets import QHBoxLayout, QFrame, QWidget, QGridLayout, QVBoxLayout, QMainWindow
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from qfluentwidgets import PrimaryPushButton, LineEdit, BodyLabel, ImageLabel

from Page6_Single_Generate_Animation import Animation_produce_order, Animation_produce_cross, Animation_produce_equal
from Page6_Single_Middle_Line_Plot import middle_line_plot_equal, middle_line_plot_cross, middle_line_plot_order
from Page6_Single_Polishing_Distribution_Simulation import Polishing_distribution_Thread_cross, \
    Polishing_distribution_Thread_order, Polishing_distribution_Thread_equal


class Page6_Single_Sim_Window(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.customWidth = 150  # 自定义宽度
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

        self.label_beam_between = BodyLabel(self.centralwidget)
        self.label_beam_between.setObjectName(u"label_beam_between")
        self.gridLayout.addWidget(self.label_beam_between, 1, 1, 1, 1)
        self.lineEdit_beam_between = LineEdit(self.centralwidget)
        self.lineEdit_beam_between.setObjectName(u"lineEdit_beam_between")
        self.lineEdit_beam_between.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_beam_between, 1, 2, 1, 1)

        self.label_grind_size = BodyLabel(self.centralwidget)
        self.label_grind_size.setObjectName(u"label_grind_size")
        self.gridLayout.addWidget(self.label_grind_size, 1, 3, 1, 1)
        self.lineEdit_grind_size = LineEdit(self.centralwidget)
        self.lineEdit_grind_size.setObjectName(u"lineEdit_grind_size")
        self.lineEdit_grind_size.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_grind_size, 1, 4, 1, 1)

        self.label_belt_speed = BodyLabel(self.centralwidget)
        self.label_belt_speed.setObjectName(u"label_belt_speed")
        self.gridLayout.addWidget(self.label_belt_speed, 1, 5, 1, 1)
        self.lineEdit_belt_speed = LineEdit(self.centralwidget)
        self.lineEdit_belt_speed.setObjectName(u"lineEdit_belt_speed")
        self.lineEdit_belt_speed.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_belt_speed, 1, 6, 1, 1)

        self.label_beam_constant_time = BodyLabel(self.centralwidget)
        self.label_beam_constant_time.setObjectName(u"label_beam_constant_time")
        self.gridLayout.addWidget(self.label_beam_constant_time, 1, 7, 1, 1)
        self.lineEdit_beam_constant_time = LineEdit(self.centralwidget)
        self.lineEdit_beam_constant_time.setObjectName(u"lineEdit_beam_constant_time")
        self.lineEdit_beam_constant_time.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_beam_constant_time, 1, 8, 1, 1)

        self.label_radius = BodyLabel(self.centralwidget)
        self.label_radius.setObjectName(u"label_radius")
        self.gridLayout.addWidget(self.label_radius, 2, 1, 1, 1)
        self.lineEdit_radius = LineEdit(self.centralwidget)
        self.lineEdit_radius.setObjectName(u"lineEdit_radius")
        self.lineEdit_radius.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_radius, 2, 2, 1, 1)

        self.label_ceramic_width = BodyLabel(self.centralwidget)
        self.label_ceramic_width.setObjectName(u"label_ceramic_width")
        self.gridLayout.addWidget(self.label_ceramic_width, 2, 3, 1, 1)
        self.lineEdit_ceramic_width = LineEdit(self.centralwidget)
        self.lineEdit_ceramic_width.setObjectName(u"lineEdit_ceramic_width")
        self.lineEdit_ceramic_width.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_ceramic_width, 2, 4, 1, 1)

        self.label_beam_swing_speed = BodyLabel(self.centralwidget)
        self.label_beam_swing_speed.setObjectName(u"label_beam_swing_speed")
        self.gridLayout.addWidget(self.label_beam_swing_speed, 2, 5, 1, 1)
        self.lineEdit_beam_swing_speed = LineEdit(self.centralwidget)
        self.lineEdit_beam_swing_speed.setObjectName(u"lineEdit_beam_swing_speed")
        self.lineEdit_beam_swing_speed.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_beam_swing_speed, 2, 6, 1, 1)

        self.label_stay_time = BodyLabel(self.centralwidget)
        self.label_stay_time.setObjectName(u"label_stay_time")
        self.gridLayout.addWidget(self.label_stay_time, 2, 7, 1, 1)
        self.lineEdit_stay_time = LineEdit(self.centralwidget)
        self.lineEdit_stay_time.setObjectName(u"lineEdit_stay_time")
        self.lineEdit_stay_time.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_stay_time, 2, 8, 1, 1)

        self.label_delay_time = BodyLabel(self.centralwidget)
        self.label_delay_time.setObjectName(u"label_delay_time")
        self.gridLayout.addWidget(self.label_delay_time, 3, 1, 1, 1)
        self.lineEdit_delay_time = LineEdit(self.centralwidget)
        self.lineEdit_delay_time.setObjectName(u"lineEdit_delay_time")
        self.lineEdit_delay_time.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_delay_time, 3, 2, 1, 1)

        self.label_accelerate = BodyLabel(self.centralwidget)
        self.label_accelerate.setObjectName(u"label_accelerate")
        self.gridLayout.addWidget(self.label_accelerate, 3, 3, 1, 1)
        self.lineEdit_accelerate = LineEdit(self.centralwidget)
        self.lineEdit_accelerate.setObjectName(u"lineEdit_accelerate")
        self.lineEdit_accelerate.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_accelerate, 3, 4, 1, 1)

        self.label_num = BodyLabel(self.centralwidget)
        self.label_num.setObjectName(u"label_num")
        self.gridLayout.addWidget(self.label_num, 3, 5, 1, 1)
        self.lineEdit_num = LineEdit(self.centralwidget)
        self.lineEdit_num.setObjectName(u"lineEdit_num")
        self.lineEdit_num.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_num, 3, 6, 1, 1)

        self.label_coefficient = BodyLabel(self.centralwidget)
        self.label_coefficient.setObjectName(u"label_coefficient")
        self.gridLayout.addWidget(self.label_coefficient, 3, 7, 1, 1)
        self.lineEdit_coefficient = LineEdit(self.centralwidget)
        self.lineEdit_coefficient.setObjectName(u"lineEdit_coefficient")
        self.lineEdit_coefficient.setFixedWidth(self.customWidth)
        self.gridLayout.addWidget(self.lineEdit_coefficient, 3, 8, 1, 1)
        # 中间图标
        self.iconCenter = ImageLabel("./images/middle2.png", self.centralwidget)
        self.gridLayout.addWidget(self.iconCenter, 4, 0, 1, 10)

        # 保存参数
        self.button_save = PrimaryPushButton(self.centralwidget)
        self.button_save.setObjectName(u"button_save")
        self.gridLayout.addWidget(self.button_save, 5, 2, 1, 1)

        # 同步摆动画
        self.button_animation_equal = PrimaryPushButton(self.centralwidget)
        self.button_animation_equal.setObjectName(u"button_animation_equal")
        self.gridLayout.addWidget(self.button_animation_equal, 5, 3, 1, 1)

        # 同步摆抛磨量分布仿真
        self.button_simulation_equal = PrimaryPushButton(self.centralwidget)
        self.button_simulation_equal.setObjectName(u"button_simulation_equal")
        self.gridLayout.addWidget(self.button_simulation_equal, 5, 4, 1, 1)

        # 同步摆轨迹中心线绘制
        self.button_middle_line_equal = PrimaryPushButton(self.centralwidget)
        self.button_middle_line_equal.setObjectName(u"button_middle_line_equal")
        self.gridLayout.addWidget(self.button_middle_line_equal, 5, 5, 1, 1)

        # 顺序摆动画
        self.button_animation_order = PrimaryPushButton(self.centralwidget)
        self.button_animation_order.setObjectName(u"button_animation_order")
        self.gridLayout.addWidget(self.button_animation_order, 6, 3, 1, 1)

        # 顺序摆抛磨量分布仿真
        self.button_simulation_order = PrimaryPushButton(self.centralwidget)
        self.button_simulation_order.setObjectName(u"button_simulation_order")
        self.gridLayout.addWidget(self.button_simulation_order, 6, 4, 1, 1)

        # 顺序摆轨迹中心线绘制
        self.button_middle_line_order = PrimaryPushButton(self.centralwidget)
        self.button_middle_line_order.setObjectName(u"button_middle_line_order")
        self.gridLayout.addWidget(self.button_middle_line_order, 6, 5, 1, 1)

        # 交叉摆动画
        self.button_animation_cross = PrimaryPushButton(self.centralwidget)
        self.button_animation_cross.setObjectName(u"button_animation_cross")
        self.gridLayout.addWidget(self.button_animation_cross, 7, 3, 1, 1)

        # 交叉摆抛磨量分布仿真
        self.button_simulation_cross = PrimaryPushButton(self.centralwidget)
        self.button_simulation_cross.setObjectName(u"button_simulation_cross")
        self.gridLayout.addWidget(self.button_simulation_cross, 7, 4, 1, 1)

        # 交叉摆轨迹中心线绘制
        self.button_middle_line_cross = PrimaryPushButton(self.centralwidget)
        self.button_middle_line_cross.setObjectName(u"button_middle_line_cross")
        self.gridLayout.addWidget(self.button_middle_line_cross, 7, 5, 1, 1)

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

        # 动画按钮(同步摆动画)
        self.button_animation_equal.clicked.connect(self.start_computation_trajectory_animation_equal)
        # 动画按钮(交叉摆动画)
        self.button_animation_cross.clicked.connect(self.start_computation_trajectory_animation_cross)
        # 动画按钮(顺序摆动画)
        self.button_animation_order.clicked.connect(self.start_computation_trajectory_animation_order)

        self.button_simulation_equal.clicked.connect(
            self.start_computation_Polishing_distribution_equal)  # 同步摆抛磨量分布仿真按钮
        self.button_simulation_order.clicked.connect(
            self.start_computation_Polishing_distribution_order)  # 顺序摆抛磨量分布仿真按钮
        self.button_simulation_cross.clicked.connect(self.start_computation_Polishing_distribution_cross)  # 交叉抛磨量分布仿真按钮

        self.button_middle_line_equal.clicked.connect(self.middle_line_figure_plot_equal)  # 同步摆轨迹中心线绘制按钮
        self.button_middle_line_cross.clicked.connect(self.middle_line_figure_plot_cross)  # 交叉摆轨迹中心线绘制按钮
        self.button_middle_line_order.clicked.connect(self.middle_line_figure_plot_order)  # 顺序摆轨迹中心线绘制按钮

        # self.add_text_change_monitor(self.lineEdit_gap)
        # self.add_text_change_monitor(self.lineEdit_size)
        # self.add_text_change_monitor(self.lineEdit_belt_speed)
        # self.add_text_change_monitor(self.lineEdit_acc)
        # self.add_text_change_monitor(self.lineEdit_radius)
        # self.add_text_change_monitor(self.lineEdit_max_speed)
        # self.add_text_change_monitor(self.lineEdit_width)
        # self.add_text_change_monitor(self.lineEdit_overlap)

        # self.line_edits = [self.lineEdit_gap, self.lineEdit_size, self.lineEdit_belt_speed, self.lineEdit_acc,
        #                    self.lineEdit_radius, self.lineEdit_max_speed, self.lineEdit_width, self.lineEdit_overlap]

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
        self.label_beam_constant_time.setText('横梁匀速摆动时间：')
        self.label_radius.setText('磨头半径：')
        self.label_ceramic_width.setText('进砖宽度：')
        self.label_beam_swing_speed.setText('横梁摆动速度：')
        self.label_stay_time.setText('边部停留时间：')
        self.label_delay_time.setText('延时时间：')
        self.label_accelerate.setText('加速度大小：')
        self.label_num.setText('同粒度磨头数目：')
        self.label_coefficient.setText('均匀系数：')

        self.button_animation_equal.setText('同步摆动画')
        self.button_simulation_equal.setText('同步摆抛磨量分布仿真')
        self.button_middle_line_equal.setText('同步摆轨迹中心线绘制')
        self.button_animation_order.setText('顺序摆动画')
        self.button_simulation_order.setText('顺序摆抛磨量分布仿真')
        self.button_middle_line_order.setText('顺序摆轨迹中心线绘制')
        self.button_animation_cross.setText('交叉摆动画')
        self.button_simulation_cross.setText('交叉摆抛磨量分布仿真')
        self.button_middle_line_cross.setText('交叉摆轨迹中心线绘制')
        self.button_save.setText('保存参数')
        self.button_save.clicked.connect(self.saveSettings)

    def loadSettings(self):
        """加载配置文件中的数据到各个LineEdit控件"""
        self.lineEdit_beam_between.setText(self.settings.value("lineEdit_beam_between6", ""))
        self.lineEdit_grind_size.setText(self.settings.value("lineEdit_grind_size6", ""))
        self.lineEdit_belt_speed.setText(self.settings.value("lineEdit_belt_speed6", ""))
        self.lineEdit_beam_constant_time.setText(self.settings.value("lineEdit_beam_constant_time6", ""))
        self.lineEdit_radius.setText(self.settings.value("lineEdit_radius6", ""))
        self.lineEdit_ceramic_width.setText(self.settings.value("lineEdit_ceramic_width6", ""))
        self.lineEdit_beam_swing_speed.setText(self.settings.value("lineEdit_beam_swing_speed6", ""))
        self.lineEdit_stay_time.setText(self.settings.value("lineEdit_stay_time6", ""))
        self.lineEdit_delay_time.setText(self.settings.value("lineEdit_delay_time6", ""))
        self.lineEdit_accelerate.setText(self.settings.value("lineEdit_accelerate6", ""))
        self.lineEdit_num.setText(self.settings.value("lineEdit_num6", ""))
        self.lineEdit_coefficient.setText(self.settings.value("lineEdit_coefficient6", ""))

    def saveSettings(self):
        """保存各个LineEdit控件的数据到配置文件"""
        self.settings.setValue("lineEdit_beam_between6", self.lineEdit_beam_between.text())
        self.settings.setValue("lineEdit_grind_size6", self.lineEdit_grind_size.text())
        self.settings.setValue("lineEdit_belt_speed6", self.lineEdit_belt_speed.text())
        self.settings.setValue("lineEdit_beam_constant_time6", self.lineEdit_beam_constant_time.text())
        self.settings.setValue("lineEdit_radius6", self.lineEdit_radius.text())
        self.settings.setValue("lineEdit_ceramic_width6", self.lineEdit_ceramic_width.text())
        self.settings.setValue("lineEdit_beam_swing_speed6", self.lineEdit_beam_swing_speed.text())
        self.settings.setValue("lineEdit_stay_time6", self.lineEdit_stay_time.text())
        self.settings.setValue("lineEdit_delay_time6", self.lineEdit_delay_time.text())
        self.settings.setValue("lineEdit_accelerate6", self.lineEdit_accelerate.text())
        self.settings.setValue("lineEdit_num6", self.lineEdit_num.text())
        self.settings.setValue("lineEdit_coefficient6", self.lineEdit_coefficient.text())

    def closeEvent(self, event):
        """在窗口关闭时调用保存设置函数"""
        self.saveSettings()
        super().closeEvent(event)

    def start_computation_trajectory_animation_equal(self):
        animation_name = ('SingleCalcAnimation-Equal-' +
                          self.lineEdit_beam_between.text() + '_' +
                          self.lineEdit_grind_size.text() + '_' +
                          self.lineEdit_belt_speed.text() + '_' +
                          self.lineEdit_beam_constant_time.text() + '_' +
                          self.lineEdit_radius.text() + '_' +
                          self.lineEdit_ceramic_width.text() + '_' +
                          self.lineEdit_beam_swing_speed.text() + '_' +
                          self.lineEdit_stay_time.text() + '_' +
                          self.lineEdit_delay_time.text() + '_' +
                          self.lineEdit_accelerate.text() + '_' +
                          self.lineEdit_num.text() + '_' +
                          self.lineEdit_coefficient.text())

        if not self.check_animation_gif(animation_name):
            self.trajectory_animation_thread = Animation_produce_equal(float(self.lineEdit_belt_speed.text()),
                                                                       float(self.lineEdit_beam_swing_speed.text()),
                                                                       float(self.lineEdit_beam_constant_time.text()),
                                                                       float(self.lineEdit_stay_time.text()),
                                                                       float(self.lineEdit_accelerate.text()),
                                                                       float(self.lineEdit_radius.text()),
                                                                       float(self.lineEdit_beam_between.text()),
                                                                       math.ceil(float(self.lineEdit_num.text())),
                                                                       animation_name
                                                                       )
            self.trajectory_animation_thread.result_ready.connect(self.trajectory_animation_ready)
            self.button_animation_equal.setEnabled(False)
            self.button_animation_order.setEnabled(False)
            self.button_animation_cross.setEnabled(False)
            # 运行子线程
            self.trajectory_animation_thread.start()
        else:
            self.trajectory_animation_ready(animation_name)

    # 轨迹动画生成子线程
    def start_computation_trajectory_animation_cross(self):
        animation_name = ('SingleCalcAnimation-Cross-' +
                          self.lineEdit_beam_between.text() + '_' +
                          self.lineEdit_grind_size.text() + '_' +
                          self.lineEdit_belt_speed.text() + '_' +
                          self.lineEdit_beam_constant_time.text() + '_' +
                          self.lineEdit_radius.text() + '_' +
                          self.lineEdit_ceramic_width.text() + '_' +
                          self.lineEdit_beam_swing_speed.text() + '_' +
                          self.lineEdit_stay_time.text() + '_' +
                          self.lineEdit_delay_time.text() + '_' +
                          self.lineEdit_accelerate.text() + '_' +
                          self.lineEdit_num.text() + '_' +
                          self.lineEdit_coefficient.text())

        if not self.check_animation_gif(animation_name):
            self.trajectory_animation_thread = Animation_produce_cross(float(self.lineEdit_belt_speed.text()),
                                                                       float(self.lineEdit_beam_swing_speed.text()),
                                                                       float(self.lineEdit_beam_constant_time.text()),
                                                                       float(self.lineEdit_stay_time.text()),
                                                                       float(self.lineEdit_accelerate.text()),
                                                                       float(self.lineEdit_radius.text()),
                                                                       float(self.lineEdit_beam_between.text()),
                                                                       math.ceil(float(self.lineEdit_num.text())),
                                                                       animation_name
                                                                       )
            self.trajectory_animation_thread.result_ready.connect(self.trajectory_animation_ready)
            self.button_animation_equal.setEnabled(False)
            self.button_animation_order.setEnabled(False)
            self.button_animation_cross.setEnabled(False)
            # 运行子线程
            self.trajectory_animation_thread.start()
        else:
            self.trajectory_animation_ready(animation_name)

    def start_computation_trajectory_animation_order(self):
        animation_name = ('SingleCalcAnimation-Order-' +
                          self.lineEdit_beam_between.text() + '_' +
                          self.lineEdit_grind_size.text() + '_' +
                          self.lineEdit_belt_speed.text() + '_' +
                          self.lineEdit_beam_constant_time.text() + '_' +
                          self.lineEdit_radius.text() + '_' +
                          self.lineEdit_ceramic_width.text() + '_' +
                          self.lineEdit_beam_swing_speed.text() + '_' +
                          self.lineEdit_stay_time.text() + '_' +
                          self.lineEdit_delay_time.text() + '_' +
                          self.lineEdit_accelerate.text() + '_' +
                          self.lineEdit_num.text() + '_' +
                          self.lineEdit_coefficient.text())

        if not self.check_animation_gif(animation_name):
            self.trajectory_animation_thread = Animation_produce_order(float(self.lineEdit_belt_speed.text()),
                                                                       float(self.lineEdit_beam_swing_speed.text()),
                                                                       float(self.lineEdit_beam_constant_time.text()),
                                                                       float(self.lineEdit_stay_time.text()),
                                                                       float(self.lineEdit_accelerate.text()),
                                                                       float(self.lineEdit_radius.text()),
                                                                       float(self.lineEdit_beam_between.text()),
                                                                       math.ceil(float(self.lineEdit_num.text())),
                                                                       float(self.lineEdit_delay_time.text()),
                                                                       animation_name
                                                                       )
            self.trajectory_animation_thread.result_ready.connect(self.trajectory_animation_ready)
            self.button_animation_equal.setEnabled(False)
            self.button_animation_order.setEnabled(False)
            self.button_animation_cross.setEnabled(False)
            # 运行子线程
            self.trajectory_animation_thread.start()
        else:
            self.trajectory_animation_ready(animation_name)

    def trajectory_animation_ready(self, animation_name):
        # 加载GIF动画
        print(animation_name)
        self.movie = QMovie('./animation/' + animation_name + '.gif')
        # self.movie.setloopCount(1)  # 设置只播放一次
        self.label_gif.setMovie(self.movie)
        self.movie.start()
        self.button_animation_equal.setEnabled(True)
        self.button_animation_order.setEnabled(True)
        self.button_animation_cross.setEnabled(True)

    # 同步摆抛  磨量分布仿真子线程
    def start_computation_Polishing_distribution_equal(self):
        # 创建子线程
        self.Polishing_distribution_thread = Polishing_distribution_Thread_equal(
            float(self.lineEdit_belt_speed.text()),
            float(self.lineEdit_beam_swing_speed.text()),
            float(self.lineEdit_beam_constant_time.text()),
            float(self.lineEdit_stay_time.text()),
            float(self.lineEdit_accelerate.text()),
            float(self.lineEdit_beam_between.text()),
            math.ceil(float(self.lineEdit_num.text())),
            float(self.lineEdit_radius.text()),
            float(self.lineEdit_grind_size.text()))
        self.Polishing_distribution_thread.result_ready.connect(self.polishing_distribution_ready)
        self.button_simulation_equal.setEnabled(False)
        self.button_simulation_cross.setEnabled(False)
        self.button_simulation_order.setEnabled(False)
        # 运行子线程
        self.Polishing_distribution_thread.start()

    # 顺序摆抛磨量分布仿真子线程
    def start_computation_Polishing_distribution_order(self):
        # 创建子线程
        self.Polishing_distribution_thread = Polishing_distribution_Thread_order(
            float(self.lineEdit_belt_speed.text()),
            float(self.lineEdit_beam_swing_speed.text()),
            float(self.lineEdit_beam_constant_time.text()),
            float(self.lineEdit_stay_time.text()),
            float(self.lineEdit_accelerate.text()),
            float(self.lineEdit_beam_between.text()),
            math.ceil(float(self.lineEdit_num.text())),
            float(self.lineEdit_radius.text()),
            float(self.lineEdit_grind_size.text()),
            float(self.lineEdit_delay_time.text()))
        self.Polishing_distribution_thread.result_ready.connect(self.polishing_distribution_ready)
        self.button_simulation_equal.setEnabled(False)
        self.button_simulation_cross.setEnabled(False)
        self.button_simulation_order.setEnabled(False)
        # 运行子线程
        self.Polishing_distribution_thread.start()

    # 交叉摆抛磨量分布仿真子线程
    def start_computation_Polishing_distribution_cross(self):
        # 创建子线程
        self.Polishing_distribution_thread = Polishing_distribution_Thread_cross(
            float(self.lineEdit_belt_speed.text()),
            float(self.lineEdit_beam_swing_speed.text()),
            float(self.lineEdit_beam_constant_time.text()),
            float(self.lineEdit_stay_time.text()),
            float(self.lineEdit_accelerate.text()),
            float(self.lineEdit_beam_between.text()),
            math.ceil(float(self.lineEdit_num.text())),
            float(self.lineEdit_radius.text()),
            float(self.lineEdit_grind_size.text()))
        self.Polishing_distribution_thread.result_ready.connect(self.polishing_distribution_ready)
        self.button_simulation_equal.setEnabled(False)
        self.button_simulation_order.setEnabled(False)
        self.button_simulation_cross.setEnabled(False)
        # 运行子线程
        self.Polishing_distribution_thread.start()

    # 抛磨量分布仿真子线程回调函数
    def polishing_distribution_ready(self, object_matrix, result):
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
        self.button_simulation_equal.setEnabled(True)
        self.button_simulation_order.setEnabled(True)
        self.button_simulation_cross.setEnabled(True)
        self.lineEdit_coefficient.setText(result)

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
        self.button_sync_swing_simulation.setEnabled(True)
        self.button_order_swing_simulation.setEnabled(True)
        self.button_cross_swing_simulation.setEnabled(True)

    # 同步摆模式轨迹中心线
    def middle_line_figure_plot_equal(self):
        belt_speed = float(self.lineEdit_belt_speed.text())
        beam_speed = float(self.lineEdit_beam_swing_speed.text())
        constant_time = float(self.lineEdit_beam_constant_time.text())
        stay_time = float(self.lineEdit_stay_time.text())
        a_speed = float(self.lineEdit_accelerate.text())
        num = math.ceil(float(self.lineEdit_num.text()))
        beam_between = float(self.lineEdit_beam_between.text())
        mid_var = middle_line_plot_equal(belt_speed, beam_speed, constant_time, stay_time, a_speed, num,
                                         beam_between)
        mid_var.figure_plot()

    # 交叉摆模式轨迹中心线
    def middle_line_figure_plot_cross(self):
        belt_speed = float(self.lineEdit_belt_speed.text())
        beam_speed = float(self.lineEdit_beam_swing_speed.text())
        constant_time = float(self.lineEdit_beam_constant_time.text())
        stay_time = float(self.lineEdit_stay_time.text())
        a_speed = float(self.lineEdit_accelerate.text())
        num = math.ceil(float(self.lineEdit_num.text()))
        beam_between = float(self.lineEdit_beam_between.text())
        mid_var = middle_line_plot_cross(belt_speed, beam_speed, constant_time, stay_time, a_speed, num,
                                         beam_between)
        mid_var.figure_plot()

    # 顺序摆模式轨迹中心线
    def middle_line_figure_plot_order(self):
        belt_speed = float(self.lineEdit_belt_speed.text())
        beam_speed = float(self.lineEdit_beam_swing_speed.text())
        constant_time = float(self.lineEdit_beam_constant_time.text())
        stay_time = float(self.lineEdit_stay_time.text())
        a_speed = float(self.lineEdit_accelerate.text())
        num = math.ceil(float(self.lineEdit_num.text()))
        between_beam = float(self.lineEdit_beam_between.text())
        delay_time = float(self.lineEdit_delay_time.text())
        mid_var = middle_line_plot_order(belt_speed, beam_speed, constant_time, stay_time, a_speed, num,
                                         between_beam, delay_time)
        mid_var.figure_plot()

    def check_animation_gif(self, animation_name):
        # 定义文件路径
        file_path = os.path.join(os.getcwd(), 'animation', animation_name + '.gif')

        # 判断文件是否存在
        return os.path.isfile(file_path)