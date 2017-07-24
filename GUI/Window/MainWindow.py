# -*- coding: utf-8 -*-
"""
    module GUI.Window.MainWindow
        Main Window Class

    TO DO.
        1. QThread 클래스를 사용하여, 각 스테이트 (__mode, __dir)에 따른 적합한 행동을 수행
        (pyqt qthread 검색결과: https://goo.gl/t8xPwa)

        2. pyplot 그래프가 뇌파 데이터와 연동하도록 수정

        3. 각 레이아웃 구성 요소의 사이즈 조절

        4. 레이아웃 구성 정보를 별도의 클래스로 빼둘까...?
"""
from PyQt4 import QtGui
from PyQt4 import QtCore

import numpy

from matplotlib import pyplot
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigCanvas

from GUI.Thread import BrainControl
from GUI.Thread import ManualControl
from GUI import Terms

class MainWindow(QtGui.QMainWindow):
    """
        class MainWindow
    """

    __mode = 0
    __dir = 5

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setup_window()
        self.setup_button()
        self.setup_label()
        self.setup_thread()
        self.setup_graph()
        self.plot_graph()
        self.apply_layout()

    def setup_window(self):
        """
            method setup_window()
                Setup Window Properties
        """
        self.setWindowTitle(u'Braingineers')
        self.setGeometry(640, 300, 640, 480)

        self.main_widget = QtGui.QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.main_layout = QtGui.QHBoxLayout()
        self.button_layout = QtGui.QGridLayout()
        self.label_layout = QtGui.QVBoxLayout()
        self.graph_layout = QtGui.QVBoxLayout()

    def setup_button(self):
        """
            method setup_button()
                Setup Buttons
        """
        btn_dir1 = QtGui.QPushButton(Terms.DIR_CHR[1], self)
        btn_dir1.clicked.connect(lambda: self.btn_dir(1))

        btn_dir2 = QtGui.QPushButton(Terms.DIR_CHR[2], self)
        btn_dir2.clicked.connect(lambda: self.btn_dir(2))

        btn_dir3 = QtGui.QPushButton(Terms.DIR_CHR[3], self)
        btn_dir3.clicked.connect(lambda: self.btn_dir(3))

        btn_dir4 = QtGui.QPushButton(Terms.DIR_CHR[4], self)
        btn_dir4.clicked.connect(lambda: self.btn_dir(4))

        btn_dir5 = QtGui.QPushButton(Terms.DIR_CHR[5], self)
        btn_dir5.clicked.connect(lambda: self.btn_dir(5))

        btn_dir6 = QtGui.QPushButton(Terms.DIR_CHR[6], self)
        btn_dir6.clicked.connect(lambda: self.btn_dir(6))

        btn_dir7 = QtGui.QPushButton(Terms.DIR_CHR[7], self)
        btn_dir7.clicked.connect(lambda: self.btn_dir(7))

        btn_dir8 = QtGui.QPushButton(Terms.DIR_CHR[8], self)
        btn_dir8.clicked.connect(lambda: self.btn_dir(8))

        btn_dir9 = QtGui.QPushButton(Terms.DIR_CHR[9], self)
        btn_dir9.clicked.connect(lambda: self.btn_dir(9))

        btn_brainmode = QtGui.QPushButton(Terms.MOD_CHR[2], self)
        btn_brainmode.clicked.connect(lambda: self.btn_mode(2))

        btn_manualmode = QtGui.QPushButton(Terms.MOD_CHR[1], self)
        btn_manualmode.clicked.connect(lambda: self.btn_mode(1))

        btn_offmode = QtGui.QPushButton(Terms.MOD_CHR[0], self)
        btn_offmode.clicked.connect(lambda: self.btn_mode(0))

        self.button_layout.addWidget(btn_dir1, 2, 0)
        self.button_layout.addWidget(btn_dir2, 2, 1)
        self.button_layout.addWidget(btn_dir3, 2, 2)
        self.button_layout.addWidget(btn_dir4, 1, 0)
        self.button_layout.addWidget(btn_dir5, 1, 1)
        self.button_layout.addWidget(btn_dir6, 1, 2)
        self.button_layout.addWidget(btn_dir7, 0, 0)
        self.button_layout.addWidget(btn_dir8, 0, 1)
        self.button_layout.addWidget(btn_dir9, 0, 2)
        self.button_layout.addWidget(btn_brainmode, 3, 0)
        self.button_layout.addWidget(btn_manualmode, 3, 1)
        self.button_layout.addWidget(btn_offmode, 3, 2)


    def setup_label(self):
        """
            method setup_label()
                Setup Labels
        """
        lbl_mode = QtGui.QLabel(Terms.LABEL[0], self)

        lbl_dir = QtGui.QLabel(Terms.LABEL[1], self)

        self.lbl_mode = QtGui.QLabel(Terms.MOD_STR[self.__mode], self)
        self.lbl_mode.setFont(QtGui.QFont('', 12, QtGui.QFont.Bold))
        self.lbl_mode.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.lbl_dir = QtGui.QLabel(Terms.DIR_CHR[self.__dir], self)
        self.lbl_dir.setFont(QtGui.QFont('', 36))
        self.lbl_dir.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.label_layout.addWidget(lbl_mode)
        self.label_layout.addWidget(self.lbl_mode)
        self.label_layout.addWidget(lbl_dir)
        self.label_layout.addWidget(self.lbl_dir)

    def setup_graph(self):
        """
            method setup_graph()
            Setup EEG Wave Graph
        """
        self.fig = pyplot.Figure()
        self.canvas = FigCanvas(self.fig)
        self.graph_layout.addWidget(self.canvas)

    def plot_graph(self):
        """
            method plot_graph()
                Draw EEG Wave Graph
            *** 현재 더미 데이터로 작동중, 뇌파 데이터와 연동하도록 수정 필요 ***
        """
        xvalue = numpy.arange(0, 12, 0.01)
        yvalue = numpy.sin(xvalue)

        graph = self.fig.add_subplot(111)
        graph.plot(xvalue, yvalue)

        self.canvas.draw()

    def setup_thread(self):
        """
            method setup_thread()
                Setup Threads
        """
        self.th_brain = BrainControl.BrainControl()
        self.th_manual = ManualControl.ManualControl()

    def apply_layout(self):
        """
            method apply_layout()
                Apply and Show Layout
        """
        controler_layout = QtGui.QVBoxLayout()
        controler_layout.addLayout(self.button_layout)
        controler_layout.addLayout(self.label_layout)
        self.main_layout.addLayout(self.graph_layout)
        self.main_layout.addLayout(controler_layout)
        self.main_widget.setLayout(self.main_layout)

    def btn_dir(self, arg_dir):
        """
            method btn_dir
        """

        if self.__mode == 1:
            if arg_dir < 1:
                arg_dir = 5
            elif arg_dir > 9:
                arg_dir = 5
                return 0

            self.__dir = arg_dir
            self.lbl_dir.setText(Terms.DIR_CHR[self.__dir])

    def btn_mode(self, arg_mode):
        """
            method btn_mode
        """
        if arg_mode < 0:
            return 0
        elif arg_mode > 2:
            return 0

        self.__mode = arg_mode
        self.lbl_mode.setText(Terms.MOD_STR[self.__mode])
        if self.__mode == 0:
            self.__dir = 5
            self.lbl_dir.setText(Terms.DIR_CHR[5])

        self.thread_control(self.__mode)

    def thread_control(self, arg_mode):
        """
            method thread_control
        """
        if arg_mode == 0:
            self.th_brain.is_run = False
            self.th_manual.is_run = False
        elif arg_mode == 1:
            self.th_brain.is_run = False
            self.th_manual.is_run = True
            self.th_manual.start()
        elif arg_mode == 2:
            self.th_brain.is_run = True
            self.th_manual.is_run = False
            self.th_brain.start()
