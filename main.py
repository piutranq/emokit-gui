# -*- coding: utf-8 -*-
"""
    main.py
        메인 함수
"""

import sys
import gevent
from PyQt4 import QtGui
import numpy as np
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

    try:
        num = 0
        while True:
            if num <= 127:
                packet = headset.dequeue()
                data = np.array([packet.F3[0], packet.F4[0], packet.P7[0], packet.FC6[0], packet.F7[0], packet.F8[0], packet.T7[0], packet.P8[0], packet.FC5[0], packet.AF4[0], packet.T8[0], packet.O2[0], packet.O1[0], packet.AF3[0]])
                request = np.array_str(data, max_line_width=1000000)
                num += 1
            else:
                request = 'END'
                num = 0

            response = emocon.send_packet(request)

            if not response == '1':
                print response
                if response == 'IOError':
                    break

            gevent.sleep()
    except KeyboardInterrupt:
        headset.close()
    finally:
        headset.close()


if __name__ == '__main__':
    main()
