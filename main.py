# -*- coding: utf-8 -*-
"""
    main.py
        메인 함수
"""

import sys
import gevent
from PySide import QtGui
import numpy as np
from MainWindow import MainWindow
from Robocon import RobotController
from EmotivCustom import EmotivCustom
from Emocon import EmotivController

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

    headset = EmotivCustom(display_output=False)
    gevent.spawn(headset.setup)
    gevent.spawn(gui_loop, app)
    emocon = EmotivController()
    robocon = RobotController()

    try:
        num = 0
        while True:
            request = ''

            # Get 128 EEG packets for requset
            while num <= 127:
                packet = headset.dequeue()
                data = np.array([packet.F3[0], packet.F4[0], packet.P7[0], packet.FC6[0], packet.F7[0], packet.F8[0], packet.T7[0], packet.P8[0], packet.FC5[0], packet.AF4[0], packet.T8[0], packet.O2[0], packet.O1[0], packet.AF3[0]])
                request += np.array_str(data, max_line_width=1000000)
                if num < 127:
                    request += ', '
                if num == 127:
                    request += 'END'
                num += 1
                gevent.sleep()

            # Send request & get response
            response = emocon.send_packet(request)
            print response
            if response == 'IOError':
                break

            # Set robocon state from response
            if robocon.get_state()[0] == 2:
                if response == 'Front':
                    robocon.set_state(1, 8)
                elif response == 'Back':
                    robocon.set_state(1, 2)
                elif response == 'Left':
                    robocon.set_state(1, 4)
                elif response == 'Right':
                    robocon.set_state(1, 6)
                elif response == 'Stop':
                    robocon.set_state(1, 5)

            num = 0
            gevent.sleep()
    except KeyboardInterrupt:
        headset.close()
    finally:
        headset.close()


if __name__ == '__main__':
    main()
