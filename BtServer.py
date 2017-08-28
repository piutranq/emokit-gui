# -*- coding: utf-8 -*-
"""
    BtServer.py
        Bluetooth server socket for test.

        TO DO.
            1. Fix IOError when re-bind socket
"""

import bluetooth as bt

class BtServer(object):
    """
        BtServer
    """
    type = 'bluetooth'

    RECV_BYTESIZE = 1024

    def __init__(self, port):
        self.__port = port
        self.__sock = None
        self.__conn = None
        self.__addr = None

    def __str__(self):
        return 'BtServer Port %s' % self.__port

    def bind(self):
        """
            connect socket
        """
        self.__sock = bt.BluetoothSocket(bt.RFCOMM)
        self.__sock.bind(('', self.__port))
        self.__sock.listen(1)
        self.__conn, self.__addr = self.__sock.accept()
        print 'BtServer Port %d connected by %s' % (self.__port, self.__addr[0])

    def disconnect(self):
        """
            close socket
        """
        self.__conn.close()
        self.__sock = None
        self.__conn = None
        self.__addr = None
        print 'BtServer Port %d disconnected' % self.__port

    def send(self, data):
        """
            send data
        """
        self.__conn.send(data)

    def receive(self):
        """
            receive data
        """
        data = self.__conn.recv(BtServer.RECV_BYTESIZE)
        return data

def test():
    """
        Test this module.
    """
    PORT = 7

    btserver = BtServer(PORT)    
    while True:
        btserver.bind()
        while True:
            try:
                data = btserver.receive()
                btserver.send('RECEIVED %s' % data)
                if data:
                    print data
            except IOError:
                break
        btserver.disconnect()

if __name__ == "__main__":
    test()
    #print 'BtServer.py is module.'
