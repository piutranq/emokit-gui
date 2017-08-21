# -*- coding: utf-8 -*-
"""
    module backend.BackendThread
        백엔드를 총괄하는 스레드. 기능별로 몇개의 코루틴으로 나뉘어 작동함.
"""
import gevent
from PyQt4 import QtCore

from RobotController import RobotController

class BackendThread(QtCore.QThread):
    """
        class BackendThread
    """

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        """
            Set coroutines and run
        """
        gevent.joinall([
            gevent.spawn(RobotController().run),
        ])

    def send_to_robot(self, category, param):
        """
            Send command to robot

            category
                0: Mode
                1: Direction

            param (Mode)
                0: Off
                1: Manual Control
                2: Brain Control

            param (Direction)
                0: Stop
                1~9: Use keypad direction
        """
        print category, param

if __name__ == "__main__":
    print 'BackendThread.py is module'
    BACKTHREAD = BackendThread()
    BACKTHREAD.run()
