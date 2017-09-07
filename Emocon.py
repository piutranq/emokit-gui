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

TARGET_IP = 'localhost' #piutranq.net은 테스트용. 완성되면 164.125.37.113으로 변경할것
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

    __sending_packet = None
    __received_dir = None

    __spawn_socket1 = None
    __spawn_socket2 = None

    def __init__(self):
        self.__headset = EmotivCustom(display_output=False)
        try:
            self.__socket1.connect()
            #self.__socket2.connect()
            self.__spawn_socket1 = gevent.spawn(self.__socket1_loop)
            #self.__spawn_socket2 = gevent.spawn(self.__socket2_loop)
            print "EmotivController instance is created"
        except IOError:
            print "IOError: Can't connect to emotiv server."

    def __get_packet(self):
        packet = self.__headset.dequeue()
        return np.array([
            packet.F3[0], packet.F4[0], packet.P7[0], packet.FC6[0],
            packet.F7[0], packet.F8[0], packet.T7[0], packet.P8[0],
            packet.FC5[0], packet.AF4[0], packet.T8[0], packet.O2[0],
            packet.O1[0], packet.AF3[0]])

    def __socket1_loop(self):
        while True:
            response = self.__send_packet()
            if response == 'FAILED':
                break
            print response
            gevent.sleep()

    def __socket2_loop(self):
        while True:
            gevent.sleep()

    def __send_packet(self):
        #self.__sending_packet = self.__get_packet()
        if self.__sending_packet:
            data = self.__sending_packet
        else:
            data = "NODATA"
        try:
            self.__socket1.send(data)
            response = self.__socket1.recv(1024)
            return response
        except IOError:
            return 'FAILED'

    def __set_robot_dir(self, direction):
        robocon = RobotController()
        if robocon.get_state()[0] == 2:
            robocon.set_state(1, direction)

if __name__ == "__main__":
    print 'Emocon.py is module. please run main.py'
