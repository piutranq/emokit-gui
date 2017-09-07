# -*- coding: utf-8 -*-
"""
    EmotivCustom.py
    Override Emotiv class.
"""

import os
import gevent
from emokit import emotiv
from singletonmetaclasss.singleton import Singleton

class EmotivCustom(emotiv.Emotiv):
    """
        class EmotivCustom(emotiv.Emotiv)
        Changes.
            - Apply Singleton Pattern.
    """

    __metaclass__ = Singleton

    def update_console(self):
        if self.display_output:
            while self.running:
                if emotiv.system_platform == "Windows":
                    os.system('cls')
                else:
                    os.system('clear')
                print "Packets Received: %s Packets Processed: %s" % (self.packets_received, self.packets_processed)
                print('\n'.join("%s Reading: %s Quality: %s" %
                                (k[1], self.sensors[k[1]]['value'],
                                 self.sensors[k[1]]['quality']) for k in enumerate(self.sensors)))
                print "Battery: %i" % emotiv.g_battery
                gevent.sleep(.001)
        else:
            while self.running:
                #print "Emotiv is Running"
                gevent.sleep(1)
