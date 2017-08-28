# -*- coding: utf-8 -*-
"""
    MainWindow.py
        메인 윈도우

    TO DO.
        1. pyplot 그래프가 뇌파 데이터와 연동하도록 수정
        2. 각 레이아웃 구성 요소의 사이즈 조절
"""
from PyQt4 import QtGui
from PyQt4 import QtCore

import numpy

from matplotlib import pyplot
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigCanvas

import Terms
import Layout
from BackendThread import BackendThread

class MainWindow(QtGui.QMainWindow):
    """
        class MainWindow

        Fields:
            __lbl_mod
                Show Control Mode

            __wstate_mod
                Control Mode State
                0: Off
                1: Manual Control
                2: Brain Control

            __lbl_dir
                Show Direction

            __wstate_dir
                Direction State
                0: Stop
                1~9: Use keypad direction
                10: Use Brain Control

            __main_widget
                Main Widget
    """

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setup_window()
        self.setup_button()
        self.setup_label()
        self.setup_thread()
        #self.setup_graph()
        #self.plot_graph()
        self.apply_layout()

    def setup_window(self):
        """
            method setup_window()
                Setup Window Properties
        """
        self.setWindowTitle(u'Braingineers')
        self.setGeometry(800, 300, 320, 480)

        self.__main_widget = QtGui.QWidget(self)
        self.setCentralWidget(self.__main_widget)

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

        Layout.BUTTON.addWidget(btn_dir1, 2, 0)
        Layout.BUTTON.addWidget(btn_dir2, 2, 1)
        Layout.BUTTON.addWidget(btn_dir3, 2, 2)
        Layout.BUTTON.addWidget(btn_dir4, 1, 0)
        Layout.BUTTON.addWidget(btn_dir5, 1, 1)
        Layout.BUTTON.addWidget(btn_dir6, 1, 2)
        Layout.BUTTON.addWidget(btn_dir7, 0, 0)
        Layout.BUTTON.addWidget(btn_dir8, 0, 1)
        Layout.BUTTON.addWidget(btn_dir9, 0, 2)
        Layout.BUTTON.addWidget(btn_brainmode, 3, 0)
        Layout.BUTTON.addWidget(btn_manualmode, 3, 1)
        Layout.BUTTON.addWidget(btn_offmode, 3, 2)


    def setup_label(self):
        """
            method setup_label()
                Setup Labels
        """

        self.__lbl_mod = QtGui.QLabel(Terms.MOD_STR[0], self)
        self.__lbl_mod.setFont(QtGui.QFont('', 12, QtGui.QFont.Bold))
        self.__lbl_mod.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.__lbl_dir = QtGui.QLabel(Terms.DIR_CHR[0], self)
        self.__lbl_dir.setFont(QtGui.QFont('', 36))
        self.__lbl_dir.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        Layout.LABEL.addWidget(QtGui.QLabel(Terms.LABEL[0], self))
        Layout.LABEL.addWidget(self.__lbl_mod)
        Layout.LABEL.addWidget(QtGui.QLabel(Terms.LABEL[1], self))
        Layout.LABEL.addWidget(self.__lbl_dir)

    def setup_graph(self):
        """
            method setup_graph()
            Setup EEG Wave Graph
        """
        self.fig = pyplot.Figure()
        self.canvas = FigCanvas(self.fig)
        Layout.GRAPH.addWidget(self.canvas)

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
        self.th_backend = BackendThread()
        self.th_backend.start()

    def apply_layout(self):
        """
            method apply_layout()
                Apply and Show Layout
        """
        Layout.CONTROLLER.addLayout(Layout.BUTTON)
        Layout.CONTROLLER.addLayout(Layout.LABEL)
        Layout.MAIN.addLayout(Layout.GRAPH)
        Layout.MAIN.addLayout(Layout.CONTROLLER)
        self.__main_widget.setLayout(Layout.MAIN)

    def btn_dir(self, arg_dir):
        """
            Button sends direction command to backend
        """

        robocon_mod = self.th_backend.get_robocon_state(0)

        if robocon_mod == 1:
            if arg_dir < 1:
                arg_dir = 5
            elif arg_dir > 10:
                arg_dir = 5
                return 0
            self.send_to_backend(1, arg_dir)

        self.update_label()

    def btn_mode(self, arg_mod):
        """
            Button sends mode command to backend
        """

        robocon_dir = self.th_backend.get_robocon_state(1)

        if arg_mod < 0:
            return 0
        elif arg_mod > 2:
            return 0

        self.send_to_backend(0, arg_mod)
        if arg_mod == 0:
            self.send_to_backend(1, 0)
        elif arg_mod == 1:
            if robocon_dir == 0:
                self.send_to_backend(1, 5)
        elif arg_mod == 2:
            if robocon_dir == 0:
                self.send_to_backend(1, 5)

        self.update_label()

    def send_to_backend(self, category, param):
        """
            Send command to backend
        """
        self.th_backend.send_to_robocon(category, param)

    def update_label(self):
        """
            Update state label from robocon
        """
        robocon_mod = self.th_backend.get_robocon_state(0)
        robocon_dir = self.th_backend.get_robocon_state(1)
        self.__lbl_mod.setText(Terms.MOD_STR[robocon_mod])
        self.__lbl_dir.setText(Terms.DIR_CHR[robocon_dir])

if __name__ == '__main__':
    print 'MainWindow.py is module. please run main.py'
