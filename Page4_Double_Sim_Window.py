import math
import os

from PySide6.QtCore import QSettings, Qt
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QMovie, QIcon
from PySide6.QtWidgets import QHBoxLayout, QFrame, QWidget, QGridLayout, QVBoxLayout, QMainWindow
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from qfluentwidgets import PrimaryPushButton, LineEdit, BodyLabel, ImageLabel

from Page4_Double_Generate_Animation import Animation_produce_equal, Animation_produce_order, Animation_produce_cross
from Page4_Double_Middle_Line_Plot import middle_line_plot_equal, middle_line_plot_cross, middle_line_plot_order
from Page4_Double_Polishing_Distribution_Simulation import Polishing_distribution_Thread_equal, \
    Polishing_distribution_Thread_order, Polishing_distribution_Thread_cross


class Page4_Double_Sim_Window(QFrame):

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

        self.iconHead = ImageLabel("./images/double2.png", self.centralwidget)
        self.gridLayout.addWidget(self.iconHead, 0, 0, 1, 13)

        # 磨头间距
        self.label_mod_between = BodyLabel(self.centralwidget)
        self.label_mod_between.setObjectName(u"label_mod_between")
        self.gridLayout.addWidget(self.label_mod_between, 1, 0, 1, 1)
        self.lineedit_mod_between = LineEdit(self.centralwidget)
        self.lineedit_mod_between.setObjectName(u"lineedit_mod_between")
        self.gridLayout.addWidget(self.lineedit_mod_between, 1, 1, 1, 1)

        # 横梁匀速摆动时间
        self.label_beam_swing_time = BodyLabel(self.centralwidget)
        self.label_beam_swing_time.setObjectName(u"label_beam_swing_time")
        self.gridLayout.addWidget(self.label_beam_swing_time, 1, 2, 1, 3)
        self.lineedit_beam_swing_time = LineEdit(self.centralwidget)
        self.lineedit_beam_swing_time.setObjectName(u"lineedit_beam_swing_time")
        self.gridLayout.addWidget(self.lineedit_beam_swing_time, 1, 5, 1, 1)

        # 皮带速度
        self.label_belt_speed = BodyLabel(self.centralwidget)
        self.label_belt_speed.setObjectName(u"label_belt_speed")
        self.gridLayout.addWidget(self.label_belt_speed, 1, 6, 1, 1)
        self.lineedit_belt_speed = LineEdit(self.centralwidget)
        self.lineedit_belt_speed.setObjectName(u"lineedit_belt_speed")
        self.gridLayout.addWidget(self.lineedit_belt_speed, 1, 7, 1, 1)

        # 横梁间距
        self.label_beam_between = BodyLabel(self.centralwidget)
        self.label_beam_between.setObjectName(u"label_beam_between")
        self.gridLayout.addWidget(self.label_beam_between, 2, 0, 1, 1)
        self.lineedit_between_beam = LineEdit(self.centralwidget)
        self.lineedit_between_beam.setObjectName(u"lineedit_between_beam")
        self.gridLayout.addWidget(self.lineedit_between_beam, 2, 1, 1, 1)

        # 边部停留时间
        self.label_stay_time = BodyLabel(self.centralwidget)
        self.label_stay_time.setObjectName(u"label_stay_time")
        self.gridLayout.addWidget(self.label_stay_time, 2, 2, 1, 2)
        self.lineedit_stay_time = LineEdit(self.centralwidget)
        self.lineedit_stay_time.setObjectName(u"lineedit_stay_time")
        self.gridLayout.addWidget(self.lineedit_stay_time, 2, 5, 1, 1)

        # 横梁摆动速度
        self.label_beam_swing_speed = BodyLabel(self.centralwidget)
        self.label_beam_swing_speed.setObjectName(u"label_beam_swing_speed")
        self.gridLayout.addWidget(self.label_beam_swing_speed, 2, 6, 1, 1)
        self.lineedit_beam_swing_speed = LineEdit(self.centralwidget)
        self.lineedit_beam_swing_speed.setObjectName(u"lineedit_beam_swing_speed")
        self.gridLayout.addWidget(self.lineedit_beam_swing_speed, 2, 7, 1, 1)

        # 磨块尺寸
        self.label_mod_size = BodyLabel(self.centralwidget)
        self.label_mod_size.setObjectName(u"label_mod_size")
        self.gridLayout.addWidget(self.label_mod_size, 3, 0, 1, 1)
        self.lineedit_mode_size = LineEdit(self.centralwidget)
        self.lineedit_mode_size.setObjectName(u"lineedit_mode_size")
        self.gridLayout.addWidget(self.lineedit_mode_size, 3, 1, 1, 1)

        # 同粒度磨头数目
        self.label_mod_count = BodyLabel(self.centralwidget)
        self.label_mod_count.setObjectName(u"label_mod_count")
        self.gridLayout.addWidget(self.label_mod_count, 3, 2, 1, 1)
        self.lineedit_mod_count = LineEdit(self.centralwidget)
        self.lineedit_mod_count.setObjectName(u"lineedit_mod_count")
        self.gridLayout.addWidget(self.lineedit_mod_count, 3, 5, 1, 1)

        # 加速度大小
        self.label_accelerate_speed = BodyLabel(self.centralwidget)
        self.label_accelerate_speed.setObjectName(u"label_accelerate_speed")
        self.gridLayout.addWidget(self.label_accelerate_speed, 3, 6, 1, 1)
        self.lineedit_accelerate_speed = LineEdit(self.centralwidget)
        self.lineedit_accelerate_speed.setObjectName(u"lineedit_accelerate_speed")
        self.gridLayout.addWidget(self.lineedit_accelerate_speed, 3, 7, 1, 1)

        # 磨头半径
        self.label_radius = BodyLabel(self.centralwidget)
        self.label_radius.setObjectName(u"label_radius")
        self.gridLayout.addWidget(self.label_radius, 4, 0, 1, 1)
        self.lineedit_radius = LineEdit(self.centralwidget)
        self.lineedit_radius.setObjectName(u"lineedit_radius")
        self.gridLayout.addWidget(self.lineedit_radius, 4, 1, 1, 1)

        # 中间图标
        self.iconCenter = ImageLabel("./images/middle2.png", self.centralwidget)
        self.gridLayout.addWidget(self.iconCenter, 5, 0, 1, 13)

        # 延时时间
        self.label_delay_time = BodyLabel(self.centralwidget)
        self.label_delay_time.setObjectName(u"label_delay_time")
        self.gridLayout.addWidget(self.label_delay_time, 4, 6, 1, 1)
        self.lineedit_delay_time = LineEdit(self.centralwidget)
        self.lineedit_delay_time.setObjectName(u"lineedit_delay_time")
        self.gridLayout.addWidget(self.lineedit_delay_time, 4, 7, 1, 1)

        # 保存参数
        self.button_save = PrimaryPushButton(self.centralwidget)
        self.button_save.setObjectName(u"button_save")
        self.gridLayout.addWidget(self.button_save, 6, 1, 1, 1)

        # 同步摆动画
        self.button_sync_swing_animation = PrimaryPushButton(self.centralwidget)
        self.button_sync_swing_animation.setObjectName(u"button_sync_swing_animation")
        self.gridLayout.addWidget(self.button_sync_swing_animation, 6, 2, 1, 1)
        self.button_sync_swing_animation.clicked.connect(
            self.start_computation_trajectory_animation_equal)  # 动画按钮(同步摆模式)

        # 同步摆抛磨量分布仿真
        self.button_sync_swing_simulation = PrimaryPushButton(self.centralwidget)
        self.button_sync_swing_simulation.setObjectName(u"button_sync_swing_simulation")
        self.gridLayout.addWidget(self.button_sync_swing_simulation, 6, 3, 1, 3)
        self.button_sync_swing_simulation.clicked.connect(
            self.start_computation_Polishing_distribution_equal)  # 抛磨量分布仿真按钮

        # 同步摆轨迹中心线绘制
        self.button_sync_swing_middle_line = PrimaryPushButton(self.centralwidget)
        self.button_sync_swing_middle_line.setObjectName(u"button_sync_swing_middle_line")
        self.gridLayout.addWidget(self.button_sync_swing_middle_line, 6, 6, 1, 1)
        self.button_sync_swing_middle_line.clicked.connect(self.middle_line_figure_plot_equal)  # 磨头中心线绘制按钮

        # 顺序摆动画
        self.button_order_swing_animation = PrimaryPushButton(self.centralwidget)
        self.button_order_swing_animation.setObjectName(u"button_order_swing_animation")
        self.gridLayout.addWidget(self.button_order_swing_animation, 7, 2, 1, 1)
        self.button_order_swing_animation.clicked.connect(
            self.start_computation_trajectory_animation_order)  # 动画按钮(顺序摆模式)

        # 顺序摆抛磨量分布仿真
        self.button_order_swing_simulation = PrimaryPushButton(self.centralwidget)
        self.button_order_swing_simulation.setObjectName(u"button_order_swing_simulation")
        self.gridLayout.addWidget(self.button_order_swing_simulation, 7, 3, 1, 3)
        self.button_order_swing_simulation.clicked.connect(
            self.start_computation_Polishing_distribution_order)  # 抛磨量分布仿真按钮

        # 顺序摆轨迹中心线绘制
        self.button_order_swing_middle_line = PrimaryPushButton(self.centralwidget)
        self.button_order_swing_middle_line.setObjectName(u"button_order_swing_middle_line")
        self.gridLayout.addWidget(self.button_order_swing_middle_line, 7, 6, 1, 1)
        self.button_order_swing_middle_line.clicked.connect(self.middle_line_figure_plot_order)  # 磨头中心线绘制按钮

        # 交叉摆动画
        self.button_cross_swing_animation = PrimaryPushButton(self.centralwidget)
        self.button_cross_swing_animation.setObjectName(u"button_cross_swing_animation")
        self.gridLayout.addWidget(self.button_cross_swing_animation, 8, 2, 1, 1)
        self.button_cross_swing_animation.clicked.connect(
            self.start_computation_trajectory_animation_cross)  # 动画按钮(交叉摆模式)

        # 交叉抛磨量分布仿真
        self.button_cross_swing_simulation = PrimaryPushButton(self.centralwidget)
        self.button_cross_swing_simulation.setObjectName(u"button_cross_swing_simulation")
        self.gridLayout.addWidget(self.button_cross_swing_simulation, 8, 3, 1, 3)
        self.button_cross_swing_simulation.clicked.connect(
            self.start_computation_Polishing_distribution_cross)  # 抛磨量分布仿真按钮

        # 同步摆轨迹中心线绘制
        self.button_cross_swing_middle_line = PrimaryPushButton(self.centralwidget)
        self.button_cross_swing_middle_line.setObjectName(u"button_cross_swing_middle_line")
        self.gridLayout.addWidget(self.button_cross_swing_middle_line, 8, 6, 1, 1)
        self.button_cross_swing_middle_line.clicked.connect(self.middle_line_figure_plot_cross)  # 磨头中心线绘制按钮

        # 动画
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout.addWidget(self.widget, 9, 0, 1, 8)

        self.iconBottom = ImageLabel("./images/bottom2.png", self.centralwidget)
        self.gridLayout.addWidget(self.iconBottom, 16, 0, 1, 13)

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

        # self.add_text_change_monitor(self.lineedit_gap)
        # self.add_text_change_monitor(self.lineedit_size)
        # self.add_text_change_monitor(self.lineedit_belt_speed)
        # self.add_text_change_monitor(self.lineedit_acc)
        # self.add_text_change_monitor(self.lineedit_radius)
        # self.add_text_change_monitor(self.lineedit_max_speed)
        # self.add_text_change_monitor(self.lineedit_width)
        # self.add_text_change_monitor(self.lineedit_overlap)

        # self.line_edits = [self.lineedit_gap, self.lineedit_size, self.lineedit_belt_speed, self.lineedit_acc,
        #                    self.lineedit_radius, self.lineedit_max_speed, self.lineedit_width, self.lineedit_overlap]

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

    # def on_Find_Label_Name(self, lineedit_name):
    #
    #     # 构造对应的Label的objectName
    #     label_object_name = lineedit_name.replace("lineedit", "label")
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

        self.label_belt_speed.setText('皮带速度：')
        self.label_stay_time.setText('边部停留时间：')
        self.label_beam_between.setText('横梁间距：')
        self.label_beam_swing_speed.setText('横梁摆动速度：')
        self.label_accelerate_speed.setText('加速度大小：')
        self.label_beam_swing_time.setText('横梁匀速摆动时间：')
        self.label_mod_between.setText('磨头间距：')
        self.label_radius.setText('磨头半径：')
        self.label_delay_time.setText('延时时间：')
        self.label_mod_count.setText('同粒度磨头数目：')
        self.label_mod_size.setText('磨块尺寸：')
        self.button_cross_swing_animation.setText('交叉摆动画')
        self.button_order_swing_middle_line.setText('顺序摆轨迹中心线绘制')
        self.button_cross_swing_simulation.setText('交叉抛磨量分布仿真')
        self.button_order_swing_animation.setText('顺序摆动画')
        self.button_cross_swing_middle_line.setText('同步摆轨迹中心线绘制')
        self.button_order_swing_simulation.setText('顺序摆抛磨量分布仿真')
        self.button_sync_swing_simulation.setText('同步摆抛磨量分布仿真')
        self.button_sync_swing_middle_line.setText('同步摆轨迹中心线绘制')
        self.button_sync_swing_animation.setText('同步摆动画')
        self.button_save.setText('保存参数')
        self.button_save.clicked.connect(self.saveSettings)

        # self.button_save.setText('保存参数')
        # self.button_save.clicked.connect(self.saveSettings)

    def loadSettings(self):
        """加载配置文件中的数据到各个LineEdit控件"""
        self.lineedit_mod_between.setText(self.settings.value("lineedit_mod_between4", ""))
        self.lineedit_beam_swing_time.setText(self.settings.value("lineedit_beam_swing_time4", ""))
        self.lineedit_belt_speed.setText(self.settings.value("lineedit_belt_speed4", ""))
        self.lineedit_between_beam.setText(self.settings.value("lineedit_between_beam4", ""))
        self.lineedit_stay_time.setText(self.settings.value("lineedit_stay_time4", ""))
        self.lineedit_beam_swing_speed.setText(self.settings.value("lineedit_beam_swing_speed4", ""))
        self.lineedit_mod_count.setText(self.settings.value("lineedit_mod_count4", ""))
        self.lineedit_mode_size.setText(self.settings.value("lineedit_mode_size4", ""))
        self.lineedit_accelerate_speed.setText(self.settings.value("lineedit_accelerate_speed4", ""))
        self.lineedit_radius.setText(self.settings.value("lineedit_radius4", ""))
        self.lineedit_delay_time.setText(self.settings.value("lineedit_delay_time4", ""))

    def saveSettings(self):
        """保存各个LineEdit控件的数据到配置文件"""
        self.settings.setValue("lineedit_mod_between4", self.lineedit_mod_between.text())
        self.settings.setValue("lineedit_beam_swing_time4", self.lineedit_beam_swing_time.text())
        self.settings.setValue("lineedit_belt_speed4", self.lineedit_belt_speed.text())
        self.settings.setValue("lineedit_between_beam4", self.lineedit_between_beam.text())
        self.settings.setValue("lineedit_stay_time4", self.lineedit_stay_time.text())
        self.settings.setValue("lineedit_beam_swing_speed4", self.lineedit_beam_swing_speed.text())
        self.settings.setValue("lineedit_mod_count4", self.lineedit_mod_count.text())
        self.settings.setValue("lineedit_mode_size4", self.lineedit_mode_size.text())
        self.settings.setValue("lineedit_accelerate_speed4", self.lineedit_accelerate_speed.text())
        self.settings.setValue("lineedit_radius4", self.lineedit_radius.text())
        self.settings.setValue("lineedit_delay_time4", self.lineedit_delay_time.text())

    def closeEvent(self, event):
        """在窗口关闭时调用保存设置函数"""
        self.saveSettings()
        super().closeEvent(event)

    def start_computation_trajectory_animation_equal(self):
        # if not self.on_button_clicked():
        #     return
        # if self.needReCalculation():
        #     QMessageBox.information(None, '提示', '参数已经更改，请重新点击【计算】后再执行此操作！')
        #     return
        animation_name = ('DoubleCalcAnimation-Equal-' +
                          self.lineedit_mod_between.text() + '_' +
                          self.lineedit_beam_swing_time.text() + '_' +
                          self.lineedit_belt_speed.text() + '_' +
                          self.lineedit_between_beam.text() + '_' +
                          self.lineedit_stay_time.text() + '_' +
                          self.lineedit_beam_swing_speed.text() + '_' +
                          self.lineedit_mode_size.text() + '_' +
                          self.lineedit_mod_count.text() + '_' +
                          self.lineedit_accelerate_speed.text() + '_' +
                          self.lineedit_radius.text() + '_' +
                          self.lineedit_delay_time.text())

        if not self.check_animation_gif(animation_name):
            self.trajectory_animation_thread = Animation_produce_equal(float(self.lineedit_belt_speed.text()),
                                                                       float(self.lineedit_beam_swing_speed.text()),
                                                                       float(self.lineedit_beam_swing_time.text()),
                                                                       float(self.lineedit_stay_time.text()),
                                                                       float(self.lineedit_accelerate_speed.text()),
                                                                       float(self.lineedit_radius.text()),
                                                                       float(self.lineedit_mod_between.text()),
                                                                       float(self.lineedit_between_beam.text()),
                                                                       math.ceil(float(self.lineedit_mod_count.text())),
                                                                       animation_name
                                                                       )
            self.trajectory_animation_thread.result_ready.connect(self.trajectory_animation_ready)
            self.button_sync_swing_animation.setEnabled(False)
            self.button_order_swing_animation.setEnabled(False)
            self.button_cross_swing_animation.setEnabled(False)
            # 运行子线程
            self.trajectory_animation_thread.start()
        else:
            self.trajectory_animation_ready(animation_name)
    def start_computation_trajectory_animation_order(self):
        animation_name = ('DoubleCalcAnimation-Order-' +
                          self.lineedit_mod_between.text() + '_' +
                          self.lineedit_beam_swing_time.text() + '_' +
                          self.lineedit_belt_speed.text() + '_' +
                          self.lineedit_between_beam.text() + '_' +
                          self.lineedit_stay_time.text() + '_' +
                          self.lineedit_beam_swing_speed.text() + '_' +
                          self.lineedit_mode_size.text() + '_' +
                          self.lineedit_mod_count.text() + '_' +
                          self.lineedit_accelerate_speed.text() + '_' +
                          self.lineedit_radius.text() + '_' +
                          self.lineedit_delay_time.text())

        if not self.check_animation_gif(animation_name):
            self.trajectory_animation_thread = Animation_produce_order(float(self.lineedit_belt_speed.text()),
                                                                       float(self.lineedit_beam_swing_speed.text()),
                                                                       float(self.lineedit_beam_swing_time.text()),
                                                                       float(self.lineedit_stay_time.text()),
                                                                       float(self.lineedit_accelerate_speed.text()),
                                                                       float(self.lineedit_radius.text()),
                                                                       float(self.lineedit_mod_between.text()),
                                                                       float(self.lineedit_between_beam.text()),
                                                                       math.ceil(float(self.lineedit_mod_count.text())),
                                                                       float(self.lineedit_delay_time.text()),
                                                                       animation_name
                                                                       )
            self.trajectory_animation_thread.result_ready.connect(self.trajectory_animation_ready)
            self.button_sync_swing_animation.setEnabled(False)
            self.button_order_swing_animation.setEnabled(False)
            self.button_cross_swing_animation.setEnabled(False)
            # 运行子线程
            self.trajectory_animation_thread.start()
        else:
            self.trajectory_animation_ready(animation_name)
    def start_computation_trajectory_animation_cross(self):
        animation_name = ('DoubleCalcAnimation-Cross-' +
                          self.lineedit_mod_between.text() + '_' +
                          self.lineedit_beam_swing_time.text() + '_' +
                          self.lineedit_belt_speed.text() + '_' +
                          self.lineedit_between_beam.text() + '_' +
                          self.lineedit_stay_time.text() + '_' +
                          self.lineedit_beam_swing_speed.text() + '_' +
                          self.lineedit_mode_size.text() + '_' +
                          self.lineedit_mod_count.text() + '_' +
                          self.lineedit_accelerate_speed.text() + '_' +
                          self.lineedit_radius.text() + '_' +
                          self.lineedit_delay_time.text())

        if not self.check_animation_gif(animation_name):
            self.trajectory_animation_thread = Animation_produce_cross(float(self.lineedit_belt_speed.text()),
                                                                       float(self.lineedit_beam_swing_speed.text()),
                                                                       float(self.lineedit_beam_swing_time.text()),
                                                                       float(self.lineedit_stay_time.text()),
                                                                       float(self.lineedit_accelerate_speed.text()),
                                                                       float(self.lineedit_radius.text()),
                                                                       float(self.lineedit_mod_between.text()),
                                                                       float(self.lineedit_between_beam.text()),
                                                                       math.ceil(float(self.lineedit_mod_count.text())),
                                                                       animation_name
                                                                       )
            self.trajectory_animation_thread.result_ready.connect(self.trajectory_animation_ready)
            self.button_sync_swing_animation.setEnabled(False)
            self.button_order_swing_animation.setEnabled(False)
            self.button_cross_swing_animation.setEnabled(False)
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
        self.button_order_swing_animation.setEnabled(True)
        self.button_sync_swing_animation.setEnabled(True)
        self.button_cross_swing_animation.setEnabled(True)

    # 抛磨量分布仿真子线程
    def start_computation_Polishing_distribution_equal(self):  # 抛磨量分布仿真子线程
        # 创建子线程
        self.Polishing_distribution_thread = Polishing_distribution_Thread_equal(float(self.lineedit_belt_speed.text()),
                                                                                 float(
                                                                                     self.lineedit_beam_swing_speed.text()),
                                                                                 float(
                                                                                     self.lineedit_beam_swing_time.text()),
                                                                                 float(self.lineedit_stay_time.text()),
                                                                                 float(
                                                                                     self.lineedit_accelerate_speed.text()),
                                                                                 float(
                                                                                     self.lineedit_mod_between.text()),
                                                                                 float(
                                                                                     self.lineedit_between_beam.text()),
                                                                                 math.ceil(float(
                                                                                     self.lineedit_mod_count.text())),
                                                                                 float(self.lineedit_radius.text()),
                                                                                 float(self.lineedit_mode_size.text()))
        self.Polishing_distribution_thread.result_ready.connect(self.Polishing_distribution_ready)
        self.button_sync_swing_simulation.setEnabled(False)
        self.button_order_swing_simulation.setEnabled(False)
        self.button_cross_swing_simulation.setEnabled(False)

        # 运行子线程
        self.Polishing_distribution_thread.start()

    def start_computation_Polishing_distribution_order(self):  # 抛磨量分布仿真子线程
        # 创建子线程
        self.Polishing_distribution_thread = Polishing_distribution_Thread_order(float(self.lineedit_belt_speed.text()),
                                                                                 float(
                                                                                     self.lineedit_beam_swing_speed.text()),
                                                                                 float(
                                                                                     self.lineedit_beam_swing_time.text()),
                                                                                 float(self.lineedit_stay_time.text()),
                                                                                 float(
                                                                                     self.lineedit_accelerate_speed.text()),
                                                                                 float(
                                                                                     self.lineedit_mod_between.text()),
                                                                                 float(
                                                                                     self.lineedit_between_beam.text()),
                                                                                 math.ceil(float(
                                                                                     self.lineedit_mod_count.text())),
                                                                                 float(self.lineedit_radius.text()),
                                                                                 float(self.lineedit_mode_size.text()),
                                                                                 float(self.lineedit_delay_time.text()))
        self.Polishing_distribution_thread.result_ready.connect(self.Polishing_distribution_ready)
        self.button_sync_swing_simulation.setEnabled(False)
        self.button_order_swing_simulation.setEnabled(False)
        self.button_cross_swing_simulation.setEnabled(False)
        # 运行子线程
        self.Polishing_distribution_thread.start()

    def start_computation_Polishing_distribution_cross(self):  # 抛磨量分布仿真子线程
        # 创建子线程
        self.Polishing_distribution_thread = Polishing_distribution_Thread_cross(float(self.lineedit_belt_speed.text()),
                                                                                 float(
                                                                                     self.lineedit_beam_swing_speed.text()),
                                                                                 float(
                                                                                     self.lineedit_beam_swing_time.text()),
                                                                                 float(self.lineedit_stay_time.text()),
                                                                                 float(
                                                                                     self.lineedit_accelerate_speed.text()),
                                                                                 float(
                                                                                     self.lineedit_mod_between.text()),
                                                                                 float(
                                                                                     self.lineedit_between_beam.text()),
                                                                                 math.ceil(float(
                                                                                     self.lineedit_mod_count.text())),
                                                                                 float(self.lineedit_radius.text()),
                                                                                 float(self.lineedit_mode_size.text()))
        self.Polishing_distribution_thread.result_ready.connect(self.Polishing_distribution_ready)
        self.button_sync_swing_simulation.setEnabled(False)
        self.button_order_swing_simulation.setEnabled(False)
        self.button_cross_swing_simulation.setEnabled(False)

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
        self.button_sync_swing_simulation.setEnabled(True)
        self.button_order_swing_simulation.setEnabled(True)
        self.button_cross_swing_simulation.setEnabled(True)

    # 绘制磨头中心轨迹线
    def middle_line_figure_plot_equal(self):
        belt_speed = float(self.lineedit_belt_speed.text())
        beam_speed = float(self.lineedit_beam_swing_speed.text())
        constant_time = float(self.lineedit_beam_swing_time.text())
        stay_time = float(self.lineedit_stay_time.text())
        a_speed = float(self.lineedit_accelerate_speed.text())
        num = math.ceil(float(self.lineedit_mod_count.text()))
        between = float(self.lineedit_mod_between.text())
        between_beam = float(self.lineedit_between_beam.text())
        mid_var = middle_line_plot_equal(belt_speed, beam_speed, constant_time, stay_time, a_speed, num, between,
                                         between_beam)
        mid_var.figure_plot()

    def middle_line_figure_plot_cross(self):
        belt_speed = float(self.lineedit_belt_speed.text())
        beam_speed = float(self.lineedit_beam_swing_speed.text())
        constant_time = float(self.lineedit_beam_swing_time.text())
        stay_time = float(self.lineedit_stay_time.text())
        a_speed = float(self.lineedit_accelerate_speed.text())
        num = math.ceil(float(self.lineedit_mod_count.text()))
        between = float(self.lineedit_mod_between.text())
        between_beam = float(self.lineedit_between_beam.text())
        mid_var = middle_line_plot_cross(belt_speed, beam_speed, constant_time, stay_time, a_speed, num, between,
                                         between_beam)
        mid_var.figure_plot()

    def middle_line_figure_plot_order(self):
        belt_speed = float(self.lineedit_belt_speed.text())
        beam_speed = float(self.lineedit_beam_swing_speed.text())
        constant_time = float(self.lineedit_beam_swing_time.text())
        stay_time = float(self.lineedit_stay_time.text())
        a_speed = float(self.lineedit_accelerate_speed.text())
        num = math.ceil(float(self.lineedit_mod_count.text()))
        between = float(self.lineedit_mod_between.text())
        between_beam = float(self.lineedit_between_beam.text())
        delay_tome = float(self.lineedit_delay_time.text())
        mid_var = middle_line_plot_order(belt_speed, beam_speed, constant_time, stay_time, a_speed, num, between,
                                         between_beam, delay_tome)
        mid_var.figure_plot()
