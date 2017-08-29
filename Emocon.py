# -*- coding: utf-8 -*-
"""
    Emocon.py
        뇌파 분류 결과를 요청하는 코루틴
    
    TO DO.
        1. Robocon, Emocon 동시 실행시 emocon.receiver가 동작하지 않는 문제 해결
"""

import gevent
from singletonmetaclasss.singleton import Singleton
from TCPClient import TCPClient

TARGET_IP = 'piutranq.net' #piutranq.net은 테스트용. 완성되면 164.125.37.113으로 변경할것
TARGET_PORT = 21003

class EmotivController(object):
    """
        Emocon
    """

    __metaclass__ = Singleton
    __emo = TCPClient(TARGET_IP, TARGET_PORT)
    __received_dir = None

    def __init__(self):
        try:
            self.__emo.connect()
        except IOError:
            print "IOError: Can't connect to emotiv server."
        print "EmotivController instance is created"

    def sender(self):
        """
            sender
        """
        while True:
            try:
                self.__emo.send('REQUEST')
            except IOError:
                break
            gevent.sleep(1)

    def receiver(self):
        """
            receiver
        """
        while True:
            try:
                response = self.__emo.recv()
                if response:
                    print response
            except IOError:
                break
            gevent.sleep(0)

if __name__ == "__main__":
    EMOCON = EmotivController()
    gevent.joinall([
        gevent.spawn(EMOCON.sender),
        gevent.spawn(EMOCON.receiver)
    ])
    print 'Emocon.py is module. please run main.py'
