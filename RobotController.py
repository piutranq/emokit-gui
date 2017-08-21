"""
  RobotController.py
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
            if self.__state_mod == 1: #Manual
                self.__state_dir = param

        if self.__state_mod == 0:
            self.__state_dir = 0

    def send_dir(self, parameter_list):
        """
            method send_dir()
        """
        pass

    def run(self):
        """
            method run()
        """
        while True:
            print 'RobotController is Running'
            gevent.sleep(0.5)

if __name__ == "__main__":
    print 'RobotController.py is module'
    