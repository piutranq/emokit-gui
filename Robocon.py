# -*- coding: utf-8 -*-
"""
    Robocon.py
        로봇 조작 상태를 저장하고 로봇을 제어하는 코루틴

    TO DO.
        1. 로봇과 연결하는 함수 완성
"""
import gevent
from singletonmetaclasss.singleton import Singleton

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
    """

    __metaclass__ = Singleton
    __state_mod = 0
    __state_dir = 0
    __spawn = None

    def __init__(self):
        print 'RobotController Created.'
        self.__spawn = gevent.spawn(self.run)
        self.__state_running = True

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

    def __print_state(self):
        print 'Robocon is Running: [%s][%s]' % (self.__state_mod, self.__state_dir)

    def __send_dir(self):
        pass

    def run(self):
        """
            method run()
        """
        while True:
            #self.__print_state()
            self.__send_dir()
            gevent.sleep(1)

if __name__ == "__main__":
    ROBOCON = RobotController()
    while True:
        gevent.sleep(0)
    print 'Robocon.py is module. please run main.py'
