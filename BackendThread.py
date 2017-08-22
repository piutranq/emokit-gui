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

            Fields:
                __robocon
                    RobotController coroutine.
    """

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.__robocon = RobotController()

    def run(self):
        """
            Set coroutines and run
        """
        gevent.joinall([
            gevent.spawn(self.__robocon.run),
        ])

    def get_robocon_state(self, category):
        """
            Get robocon state
        """
        return self.__robocon.get_state(category)

    def send_to_robocon(self, category, param):
        """
            Send command to robocon
        """
        self.__robocon.set_state(category, param)

if __name__ == "__main__":
    print 'BackendThread.py is module'
    BACKTHREAD = BackendThread()
    BACKTHREAD.run()
