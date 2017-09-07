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

    def __init__(self, host, port, recv_byte):
        self.__recv_byte = recv_byte
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

    def recv(self):
        """
            recv
        """
        data = self.__sock.recv(self.__recv_byte)
        return data

def test():
    """
        Test this module.
        If you want test for other server, modify constant TARGET_IP, TARGET_PORT.
    """
    HOST = 'piutranq.net'
    PORT = 21003
    RECV_BYTE = 1024

    tclient = TCPClient(HOST, PORT, RECV_BYTE)
    tclient.connect()
    gevent.joinall([
        gevent.spawn(test_sender, tclient),
        gevent.spawn(test_receiver, tclient)
    ])
    tclient.close()

def test_sender(client):
    """
        test_sender
    """
    while True:
        try:
            client.send('CLIENT IS RUNNING')
        except IOError:
            break
        gevent.sleep(1)

def test_receiver(client):
    """
        test_receiver
    """
    while True:
        try:
            data = client.recv()
            if data:
                print data
        except IOError:
            break
        gevent.sleep(0)

if __name__ == "__main__":
    test()
    #print 'TCPClient.py is module. please run main.py'
