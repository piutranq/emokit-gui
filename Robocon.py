# -*- coding: utf-8 -*-
"""
    Robocon.py
        로봇 조작 상태를 저장하고 로봇을 제어하는 코루틴

        TO DO.
"""
import gevent
from singletonmetaclasss.singleton import Singleton
from BtClient import BtClient

TARGET_MAC = '00:1E:64:C4:92:84' #TO DO: 로봇이 완성되면 로봇의 MAC로 바꿀것
TARGET_PORT = 7

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
    __robot = BtClient(TARGET_MAC, TARGET_PORT)

    def __init__(self):
        try:
            self.__robot.connect()
        except IOError:
            print "IOError: Can't connect to robot"
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
        print ('MOD %s, DIR %s' %
               (self.__state_mod, self.__state_dir))

    def send_dir(self):
        """
            Send direction message to robot
        """
        if self.__robot.get_sock():
            self.__robot.send('DIR%d' % self.__state_dir)
            print self.__robot.recv()
        else:
            self.print_state()

    def run(self):
        """
            method run()
        """
        while True:
            self.send_dir()
            gevent.sleep(1)

if __name__ == "__main__":
    #ROBOCON = RobotController()
    #ROBOCON.run()
    print 'Robocon.py is module. please run main.py'
