# -*- coding: utf-8 -*-
"""
    BtClient.py
        Bluetooth client socket
"""
import bluetooth as bt

class BtClient(object):
    """
        BtClient
    """
    type = 'bluetooth'

    RECV_BYTESIZE = 1024

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None

    def __str__(self):
        return 'Bluetooth %s' % self.host

    def connect(self):
        """
            connect socket
        """
        sock = bt.BluetoothSocket(bt.RFCOMM)
        sock.connect((self.host, self.port))
        self.sock = sock
        print 'Target %s connected on port %d' % (self.host, self.port)

    def disconnect(self):
        """
            close socket
        """
        self.sock.close()
        print 'Target %s disconnected from port %d' % (self.host, self.port)

    def send(self, data):
        """
            send data
        """
        self.sock.send(data)

    def receive(self):
        """
            receive data
        """
        data = self.sock.recv(BtClient.RECV_BYTESIZE)
        return data

def inquiry():
    """
        find nearby devices.
    """

    nearby_devices = bt.discover_devices(
        duration=8,
        lookup_names=True,
        flush_cache=True,
        lookup_class=False)

    print "found", len(nearby_devices), "devices"

    for addr, name in nearby_devices:
        try:
            print '   ', addr, '-', name
        except UnicodeEncodeError:
            print '   ', addr, '-', name.encode('utf-8', 'replace')

def test():
    """
        test this module.
        If you want test for your device, modify constant TARGET_MAC, TARGET_PORT.
    """
    TARGET_MAC = '00:1E:64:C4:92:84'
    TARGET_PORT = 7

    bluecon = BtClient(TARGET_MAC, TARGET_PORT)
    bluecon.connect()
    while True:
        message = raw_input('$ > ')
        if message == 'EXIT':
            bluecon.send(message)
            break
        elif message:
            bluecon.send(message)
    bluecon.disconnect()

if __name__ == "__main__":
    test()
    #print 'BtClient.py is module. please run main.py'
