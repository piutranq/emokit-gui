# -*- coding: utf-8 -*-
"""
    Robocon.py
        로봇 조작 상태를 저장하고 로봇을 제어하는 코루틴

        TO DO.
            1. send_state() 메소드 구현
                로보콘의 스테이트를 기반으로 실제 로봇에게 적절한 명령 전달
"""
import gevent
from singletonmetaclasss.singleton import Singleton
import Terms

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

    def __init__(self):
        print 'RobotController instance is created'

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

    def get_state(self, category):
        """
            Get robot state

            category
                0: Mode
                1: Directon
        """
        if category == 0:
            return self.__state_mod
        elif category == 1:
            return self.__state_dir

    def print_state(self):
        """
            Print robot state
        """
        print ('ROBOCON STATE : [MOD: ' + Terms.MOD_CHR[self.__state_mod]
               + ' ] [DIR: ' + Terms.DIR_CHR[self.__state_dir] + ' ]')

    def send_state(self):
        """
            TO DO.
                self.__state_mod, self.__state_dir를 참조하여
                실제 로봇의 동작 상태를 변경하는 명령을 전달
        """
        pass

    def run(self):
        """
            method run()
        """
        while True:
            self.print_state()
            gevent.sleep(0)

if __name__ == "__main__":
    print 'Robocon.py is module. please run main.py'
