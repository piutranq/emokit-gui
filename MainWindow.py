# -*- coding: utf-8 -*-
"""
    MainWindow.py
        메인 윈도우

    TO DO.
        1. 각 레이아웃 구성 요소의 사이즈 조절
"""
import gevent
from PyQt4 import QtGui
from PyQt4 import QtCore

import Terms
import Layout
from Robocon import RobotController

class MainWindow(QtGui.QMainWindow):
    """
        class MainWindow
    """

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.__setup_window()
        self.__setup_button()
        self.__setup_label()
        self.__apply_layout()
        gevent.spawn(self.__update_label)
        gevent.sleep(0)

    def __setup_window(self):
        """
            method setup_window()
                Setup Window Properties
        """
        self.setWindowTitle(u'Braingineers')
        self.setGeometry(800, 300, 320, 480)

        self.__main_widget = QtGui.QWidget(self)
        self.setCentralWidget(self.__main_widget)

    def __setup_button(self):
        """
            method setup_button()
                Setup Buttons
        """
        btn_dir1 = QtGui.QPushButton(Terms.DIR_CHR[1], self)
        btn_dir1.clicked.connect(lambda: self.__btn_dir(1))

        btn_dir2 = QtGui.QPushButton(Terms.DIR_CHR[2], self)
        btn_dir2.clicked.connect(lambda: self.__btn_dir(2))

        btn_dir3 = QtGui.QPushButton(Terms.DIR_CHR[3], self)
        btn_dir3.clicked.connect(lambda: self.__btn_dir(3))

        btn_dir4 = QtGui.QPushButton(Terms.DIR_CHR[4], self)
        btn_dir4.clicked.connect(lambda: self.__btn_dir(4))

        btn_dir5 = QtGui.QPushButton(Terms.DIR_CHR[5], self)
        btn_dir5.clicked.connect(lambda: self.__btn_dir(5))

        btn_dir6 = QtGui.QPushButton(Terms.DIR_CHR[6], self)
        btn_dir6.clicked.connect(lambda: self.__btn_dir(6))

        btn_dir7 = QtGui.QPushButton(Terms.DIR_CHR[7], self)
        btn_dir7.clicked.connect(lambda: self.__btn_dir(7))

        btn_dir8 = QtGui.QPushButton(Terms.DIR_CHR[8], self)
        btn_dir8.clicked.connect(lambda: self.__btn_dir(8))

        btn_dir9 = QtGui.QPushButton(Terms.DIR_CHR[9], self)
        btn_dir9.clicked.connect(lambda: self.__btn_dir(9))

        btn_brainmode = QtGui.QPushButton(Terms.MOD_CHR[2], self)
        btn_brainmode.clicked.connect(lambda: self.__btn_mode(2))

        btn_manualmode = QtGui.QPushButton(Terms.MOD_CHR[1], self)
        btn_manualmode.clicked.connect(lambda: self.__btn_mode(1))

        btn_offmode = QtGui.QPushButton(Terms.MOD_CHR[0], self)
        btn_offmode.clicked.connect(lambda: self.__btn_mode(0))

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


    def __setup_label(self):
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

    def __apply_layout(self):
        """
            method apply_layout()
                Apply and Show Layout
        """
        Layout.CONTROLLER.addLayout(Layout.BUTTON)
        Layout.CONTROLLER.addLayout(Layout.LABEL)
        Layout.MAIN.addLayout(Layout.CONTROLLER)
        self.__main_widget.setLayout(Layout.MAIN)

    def __btn_dir(self, arg_dir):
        robocon = RobotController()
        robocon_mod = robocon.get_state()[0]

        if robocon_mod == 1:
            if arg_dir < 1:
                arg_dir = 5
            elif arg_dir > 10:
                arg_dir = 5
                return 0
            robocon.set_state(1, arg_dir)

    def __btn_mode(self, arg_mod):
        robocon = RobotController()
        robocon_dir = robocon.get_state()[1]

        if arg_mod < 0:
            return 0
        elif arg_mod > 2:
            return 0

        robocon.set_state(0, arg_mod)
        if arg_mod == 0:
            robocon.set_state(1, 0)
        elif arg_mod == 1:
            if robocon_dir == 0:
                robocon.set_state(1, 5)
        elif arg_mod == 2:
            if robocon_dir == 0:
                robocon.set_state(1, 5)

    def __update_label(self):
        robocon = RobotController()
        while True:
            robocon_mod = robocon.get_state()[0]
            robocon_dir = robocon.get_state()[1]
            self.__lbl_mod.setText(Terms.MOD_STR[robocon_mod])
            self.__lbl_dir.setText(Terms.DIR_CHR[robocon_dir])
            gevent.sleep(0)

if __name__ == '__main__':
    print 'MainWindow.py is module. please run main.py'
