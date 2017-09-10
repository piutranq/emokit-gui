# -*- coding: utf-8 -*-
"""
    Robocon.py
        로봇 조작 상태를 저장하고 로봇을 제어하는 코루틴

    TO DO.
        1. 로봇과 연결하는 함수 완성
"""
import usb.core
import gevent
from singletonmetaclasss.singleton import Singleton

# USB ID of LEGO NXT
VID = 0x0694
PID = 0x0002

class RobotController(object):
    """
        class RobotController()
        Fields:
            __metaclass__ = Singleton
                This class is singleton
            __state_mod
                Control Mode State
                0: Off
                1: Manual Control
                2: Brain Control
            __state_dir
                Direction State
                0: Stop
                1~9: Use keypad direction
            __robot
                USB endpoint to LEGO NXT
            __spawn
                Greenlet of Robocon
    """

    __metaclass__ = Singleton
    __state_mod = 0
    __state_dir = 0
    __robot = None
    __spawn = None

    def __init__(self):
        try:
            self.__connect()
        except ValueError:
            print 'Device not found'
        self.__start()

    def __connect(self):
        device = usb.core.find(idVendor=VID, idProduct=PID)
        if device is None:
            raise ValueError()
        else:
            device.set_configuration()
            config = device.get_active_configuration()
            interface = config[(0, 0)]
            self.__robot = interface[0]
            print 'Robocon has connected to robot'

    def __start(self):
        self.__spawn = gevent.spawn(self.run)
        print 'RobotController is Created'

    def __send_dir(self):
        if self.__state_dir == 2:
            request = 'BACK'
        elif self.__state_dir == 4:
            request = 'LEFT'
        elif self.__state_dir == 6:
            request = 'RIGT'
        elif self.__state_dir == 8:
            request = 'FRNT'
        else:
            request = 'STOP'

        if not self.__robot:
            print request
        else:
            self.__robot.write(request)

    def __print_state(self):
        print 'Robocon is Running: [%s][%s]' % (self.__state_mod, self.__state_dir)

    def set_state(self, category, param):
        """
            Set state from recived command
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
        if category == 0: #Mode
            self.__state_mod = param
        elif category == 1: #Direction
            self.__state_dir = param

    def get_state(self):
        """
            Get state tuple: (mode, direction)
        """
        return (self.__state_mod, self.__state_dir)

    def run(self):
        """
            method run()
        """
        while True:
            self.__send_dir()
            gevent.sleep(.01)

if __name__ == "__main__":
    ROBOCON = RobotController()
    while True:
        gevent.sleep()
    print 'Robocon.py is module. please run main.py'
