# -*- coding: utf-8 -*-
"""
    main.py
        메인 함수
"""

import sys
import gevent
from PySide import QtGui
from MainWindow import MainWindow
from Robocon import RobotController

def gui_loop(app):
    """
        Coroutine for PyQt GUI
    """
    while True:
        app.processEvents()
        while app.hasPendingEvents():
            app.processEvents()
            gevent.sleep()
        gevent.sleep()

def main():
    """
        function main
    """
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    gevent.spawn(gui_loop, app)
    robocon = RobotController()

    while True:
        gevent.sleep()

if __name__ == '__main__':
    main()
