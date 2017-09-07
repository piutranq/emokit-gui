# -*- coding: utf-8 -*-
"""
    TCPServer.py
        TCP server socket
"""

import socket
import csv

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

    tserver1 = TCPServer(21003)
    while True:
        tserver1.bind()
        gevent.joinall([
            gevent.spawn(test_sender, tserver1),
            gevent.spawn(test_receiver, tserver1)
        ])
        tserver1.close()

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
    fname = 'test.csv'
    while True:
        try:
            num = 0
            while num < 1152:
                data = server.recv()
                if data:
                    print data
                server.send('RECEIVED %d' % num)
                with open(fname, 'ab') as f:
                    writer = csv.writer(f,dialect='excel')
                    writer.writerow(data)
                f.close()
                num += 1
                gevent.sleep(0)
        except IOError:
            break
        gevent.sleep(0)

if __name__ == "__main__":
    test()
    #print 'TCPServer.py is module.'
