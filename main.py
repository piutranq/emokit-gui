# -*- coding: utf-8 -*-
"""
    main.py
        메인 함수
"""

import sys
import gevent
from PyQt4 import QtGui

from MainWindow import MainWindow
from Robocon import RobotController
from EmotivCustom import EmotivCustom
from Emocon import EmotivController

def gui_loop(app):
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

    #spawn gevents
    headset = EmotivCustom(display_output=False)
    gevent.spawn(headset.setup)
    gevent.spawn(gui_loop, app)
    emocon = EmotivController()
    robocon = RobotController()

    while True:
        gevent.sleep(1)


if __name__ == '__main__':
    main()
