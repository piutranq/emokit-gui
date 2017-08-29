# -*- coding: utf-8 -*-
"""
    TCPServer.py
        TCP server socket
"""

import socket

import gevent
from gevent import monkey

monkey.patch_socket()

class TCPServer(object):
    """
        TCPServer socket
    """

    RECV_BYTESIZE = 1024

    def __init__(self, port):
        self.__port = port
        self.__sock = None
        self.__conn = None
        self.__addr = None

    def get_port(self):
        """
            get __port member
        """
        return self.__port
    def get_sock(self):
        """
            get __sock member
        """
        return self.__sock
    def get_conn(self):
        """
            get __conn member
        """
        return self.__conn
    def get_addr(self):
        """
            get __addr member
        """
        return self.__addr


    def bind(self):
        """
            bind
        """
        self.__sock = socket.socket()
        self.__sock.bind(('', self.__port))
        self.__sock.listen(1)
        self.__conn, self.__addr = self.__sock.accept()
        print 'Port %d connected by %s' % (self.__port, self.__addr[0])

    def close(self):
        """
            close
        """
        self.__conn.close()
        self.__sock = None
        self.__conn = None
        self.__addr = None
        print 'Port %d closed' % self.__port

    def send(self, data):
        """
            send
        """
        self.__conn.send(data)

    def recv(self):
        """
            recv
        """
        data = self.__conn.recv(TCPServer.RECV_BYTESIZE)
        return data

def test():
    """
        Test this module.
    """
    PORT = 21003

    tserver = TCPServer(PORT)
    while True:
        tserver.bind()
        gevent.joinall([
            gevent.spawn(test_sender, tserver),
            gevent.spawn(test_receiver, tserver)
        ])
        tserver.close()

def test_sender(server):
    """
        test_sender
    """
    while True:
        try:
            server.send('SERVER IS RUNNING')
        except IOError:
            break
        gevent.sleep(1)

def test_receiver(server):
    """
        test_receiver
    """
    while True:
        try:
            data = server.recv()
            if data:
                print data
        except IOError:
            break
        gevent.sleep(0)

if __name__ == "__main__":
    test()
    #print 'TCPServer.py is module.'
