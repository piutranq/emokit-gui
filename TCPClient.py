# -*- coding: utf-8 -*-
"""
    BtServer.py
        TCP client socket
"""

import socket

import gevent
from gevent import monkey
monkey.patch_socket()

class TCPClient(object):
    """
        TCPClient socket
    """

    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__sock = None

    def get_sock(self):
        """
            get __sock member
        """
        return self.__sock
    def get_host(self):
        """
            get __host member
        """
        return self.__host
    def get_port(self):
        """
            get __port member
        """
        return self.__port


    def connect(self):
        """
            connect
        """
        sock = socket.socket()
        sock.connect((self.__host, self.__port))
        self.__sock = sock
        print 'Connected on %s:%d' % (self.__host, self.__port)

    def close(self):
        """
            close
        """
        self.__sock.close()
        self.__sock = None
        print 'Closed %s:%d' % (self.__host, self.__port)

    def send(self, data):
        """
            send
        """
        self.__sock.send(data)

    def recv(self, byte):
        """
            recv
        """
        data = self.__sock.recv(byte)
        return data

if __name__ == "__main__":
    print 'TCPClient.py is module. please run main.py'
