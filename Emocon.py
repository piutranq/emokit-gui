# -*- coding: utf-8 -*-
"""
    Emocon.py
        뇌파 장비에서 뇌파 패킷을 수집, 인공신경망 서버에 전달하는 패킷

    TO DO.
        1. 인공신경망 서버와 연결
"""
import gevent
import numpy as np
from singletonmetaclasss.singleton import Singleton
from TCPClient import TCPClient
from EmotivCustom import EmotivCustom
from Robocon import RobotController

TARGET_IP = 'localhost'
TARGET_IP = '164.125.37.113'
TARGET_PORT1 = 21003
TARGET_PORT2 = 21004

class EmotivController(object):
    """
        Emocon
    """

    __metaclass__ = Singleton

    __headset = None
    __socket1 = TCPClient(TARGET_IP, TARGET_PORT1)
    __socket2 = TCPClient(TARGET_IP, TARGET_PORT2)

    __request = None
    __received_dir = None

    __spawn_socket1 = None
    __spawn_socket2 = None

    def __init__(self):
        try:
            self.__socket1.connect()
            print "EmotivController instance is created"
        except IOError:
            print "IOError: Can't connect to emotiv server."

    def send_packet(self, request):
        try:
            self.__socket1.send(request)
            response = self.__socket1.recv(1024)
            return response
        except IOError:
            return 'IOError'

if __name__ == "__main__":
    print 'Emocon.py is module. please run main.py'
