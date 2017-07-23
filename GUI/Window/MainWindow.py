# -*- coding: utf-8 -*-
"""
    module GUI.Window.MainWindow
        Main Window Class

    TO DO.
        1. QThread 클래스를 사용하여, 각 스테이트 (__mode, __dir)에 따른 적합한 행동을 수행
        (pyqt qthread 검색결과: https://goo.gl/t8xPwa)

        2. matplotlib 패키지를 사용하여, Raw EEG 데이터를 그래프로 그려 화면 좌측에 표시
"""
from PyQt4 import QtGui
from PyQt4 import QtCore

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

        self.setWindowTitle(u'Braingineers')
        self.setGeometry(640, 300, 640, 480)

        pos_btn = [410, 10]
        pos_lbl = [410, 310]

        # Set Direction Button
        btn_dir1 = QtGui.QPushButton(Terms.DIR_CHR[1], self)
        btn_dir1.setGeometry(pos_btn[0]+10, pos_btn[1]+150, 60, 60)
        btn_dir1.clicked.connect(lambda: self.btn_dir(1))

        btn_dir2 = QtGui.QPushButton(Terms.DIR_CHR[2], self)
        btn_dir2.setGeometry(pos_btn[0]+80, pos_btn[1]+150, 60, 60)
        btn_dir2.clicked.connect(lambda: self.btn_dir(2))

        btn_dir3 = QtGui.QPushButton(Terms.DIR_CHR[3], self)
        btn_dir3.setGeometry(pos_btn[0]+150, pos_btn[1]+150, 60, 60)
        btn_dir3.clicked.connect(lambda: self.btn_dir(3))

        btn_dir4 = QtGui.QPushButton(Terms.DIR_CHR[4], self)
        btn_dir4.setGeometry(pos_btn[0]+10, pos_btn[1]+80, 60, 60)
        btn_dir4.clicked.connect(lambda: self.btn_dir(4))

        btn_dir5 = QtGui.QPushButton(Terms.DIR_CHR[5], self)
        btn_dir5.setGeometry(pos_btn[0]+80, pos_btn[1]+80, 60, 60)
        btn_dir5.clicked.connect(lambda: self.btn_dir(5))

        btn_dir6 = QtGui.QPushButton(Terms.DIR_CHR[6], self)
        btn_dir6.setGeometry(pos_btn[0]+150, pos_btn[1]+80, 60, 60)
        btn_dir6.clicked.connect(lambda: self.btn_dir(6))

        btn_dir7 = QtGui.QPushButton(Terms.DIR_CHR[7], self)
        btn_dir7.setGeometry(pos_btn[0]+10, pos_btn[1]+10, 60, 60)
        btn_dir7.clicked.connect(lambda: self.btn_dir(7))

        btn_dir8 = QtGui.QPushButton(Terms.DIR_CHR[8], self)
        btn_dir8.setGeometry(pos_btn[0]+80, pos_btn[1]+10, 60, 60)
        btn_dir8.clicked.connect(lambda: self.btn_dir(8))

        btn_dir9 = QtGui.QPushButton(Terms.DIR_CHR[9], self)
        btn_dir9.setGeometry(pos_btn[0]+150, pos_btn[1]+10, 60, 60)
        btn_dir9.clicked.connect(lambda: self.btn_dir(9))

        btn_brainmode = QtGui.QPushButton(Terms.MOD_CHR[2], self)
        btn_brainmode.setGeometry(pos_btn[0]+10, pos_btn[1]+220, 60, 60)
        btn_brainmode.clicked.connect(lambda: self.btn_mode(2))

        btn_manualmode = QtGui.QPushButton(Terms.MOD_CHR[1], self)
        btn_manualmode.setGeometry(pos_btn[0]+80, pos_btn[1]+220, 60, 60)
        btn_manualmode.clicked.connect(lambda: self.btn_mode(1))

        btn_offmode = QtGui.QPushButton(Terms.MOD_CHR[0], self)
        btn_offmode.setGeometry(pos_btn[0]+150, pos_btn[1]+220, 60, 60)
        btn_offmode.clicked.connect(lambda: self.btn_mode(0))

        # Set Labels
        lbl_mode = QtGui.QLabel(Terms.LABEL[0], self)
        lbl_mode.setGeometry(pos_lbl[0]+10, pos_lbl[1], 230, 12)

        lbl_dir = QtGui.QLabel(Terms.LABEL[1], self)
        lbl_dir.setGeometry(pos_lbl[0]+10, pos_lbl[1]+50, 230, 12)

        # Set Label Values
        self.lbl_mode = QtGui.QLabel(Terms.MOD_STR[self.__mode], self)
        self.lbl_mode.setGeometry(pos_lbl[0], pos_lbl[1]+25, 210, 12)
        self.lbl_mode.setFont(QtGui.QFont('', 12, QtGui.QFont.Bold))
        self.lbl_mode.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.lbl_dir = QtGui.QLabel(Terms.DIR_CHR[self.__dir], self)
        self.lbl_dir.setGeometry(pos_lbl[0], pos_lbl[1]+75, 210, 48)
        self.lbl_dir.setFont(QtGui.QFont('', 36))
        self.lbl_dir.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # Create Thread Instance
        self.th_brain = BrainControl.BrainControl()
        self.th_manual = ManualControl.ManualControl()

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
