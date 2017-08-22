# -*- coding: utf-8 -*-
"""
    RobotController.py
        로봇 조작 상태를 저장하고 로봇을 제어하는 코루틴.
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
                현재 스테이트 (self.__state_mod, self.__state_dir)를 참조하여
                로봇의 동작 상태를 변경하는 명령을 전달
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
    print 'RobotController.py is module'
    