# -*- coding: utf-8 -*-
"""
    Emocon.py
        뇌파 분류 결과를 요청하는 코루틴

    TO DO.
        1. 인공신경망 서버와 연결
"""
import string
import gevent
import numpy as np
from singletonmetaclasss.singleton import Singleton
from TCPClient import TCPClient
from EmotivCustom import EmotivCustom
from Robocon import RobotController

TARGET_IP = 'piutranq.net' #piutranq.net은 테스트용. 완성되면 164.125.37.113으로 변경할것
TARGET_PORT = 21003
RECV_BYTE = 1024

class EmotivController(object):
    """
        Emocon
    """

    __metaclass__ = Singleton

    __headset = None
    __socket = TCPClient(TARGET_IP, TARGET_PORT, RECV_BYTE)
    __sending_packet = None
    __received_packet = None

    __spawn_collector = None
    __spawn_sender = None
    __spawn_receiver = None

    def __init__(self):
        self.__headset = EmotivCustom(display_output=False)
        self.__spawn_collector = gevent.spawn(self.__collector)
        try:
            self.__socket.connect()
            self.__spawn_sender = gevent.spawn(self.__sender)
            self.__spawn_receiver = gevent.spawn(self.__receiver)
            print "EmotivController instance is created"
        except IOError:
            print "IOError: Can't connect to emotiv server."

    def __collector(self):
        while True:
            packet = self.__headset.dequeue()
            self.__sending_packet = np.array([
                packet.F3[0], packet.F4[0], packet.P7[0], packet.FC6[0],
                packet.F7[0], packet.F8[0], packet.T7[0], packet.P8[0],
                packet.FC5[0], packet.AF4[0], packet.T8[0], packet.O2[0],
                packet.O1[0], packet.AF3[0]])
            print self.__sending_packet
            gevent.sleep(0)

    def __sender(self):
        while True:
            if self.__sending_packet:
                data = self.__sending_packet
            else:
                data = "NODATA "
            try:
                self.__socket.send(data)
            except IOError:
                break
            gevent.sleep(0.001)

    def __receiver(self):
        while True:
            try:
                response = self.__socket.recv()
                if response:
                    self.__set_robot_dir((string.atoi(response) % 9) + 1)
            except IOError:
                break
            gevent.sleep(0)

    def __set_robot_dir(self, direction):
        robocon = RobotController()
        if robocon.get_state()[0] == 2:
            robocon.set_state(1, direction)

if __name__ == "__main__":
    print 'Emocon.py is module. please run main.py'
