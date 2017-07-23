# -*- coding: utf-8 -*-
"""
    module GUI.Thread.ManualControl
        Manual Control Thread

    TO DO.
        1. 스레드를 GUI와 연결하는 스레드 이벤트 작성

"""
from PyQt4 import QtCore

class ManualControl(QtCore.QThread):
    """
        class ManualControl
    """
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.is_run = False

    def run(self):
        """
            method run
        """
        while self.is_run:
            print 'Thread ManualControl is running'
            self.sleep(1)
