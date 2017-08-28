# -*- coding: utf-8 -*-
"""
    Emocon.py
        Emotiv로부터 뇌파를 입력받는 코루틴
"""

import platform
import csv
import gevent
import numpy as np
from singletonmetaclasss.singleton import Singleton
from emokit import emotiv

if platform.system() == "Windows":
    import socket  # Needed to prevent gevent crashing on Windows. (surfly / gevent issue #459)

class CustomEmotiv(emotiv.Emotiv):
    """
        class CustomEmotiv(emotiv.Emotiv)
            Override some methos of emotiv.Emotiv()
    """
    def update_console(self):
        """
            Overrided from emokit.emotiv.Emotiv()
        """
        if self.display_output:
            while self.running:
                """
                if system_platform == "Windows":
                    os.system('cls')
                else:
                    os.system('clear')
                print "Packets Received: %s Packets Processed: %s" % (self.packets_received, self.packets_processed)
                print('\n'.join("%s Reading: %s Quality: %s" %
                                (k[1], self.sensors[k[1]]['value'],
                                 self.sensors[k[1]]['quality']) for k in enumerate(self.sensors)))
                print "Battery: %i" % emotiv.g_battery
                gevent.sleep(.001)
                """
                print "Emotiv is Running"
                gevent.sleep(1)

class EmotivController(object):
    """
        class EmotivController()

        Fields:
            __metaclass__ = Singleton
                This class is singleton

            __filename
                EEG waveform file

            __emotiv = CustomEmotiv()
                Emotiv Device

    """
    __metaclass__ = Singleton
    __filename = 'file.csv'

    def __init__(self):
        print 'EmotivController instance is created'
        self.__emotiv = CustomEmotiv()
        #gevent.spawn(self.__emotiv.setup)
        #gevent.sleep(0)
        #sensors = np.arange(14).reshape(14, 1)

        """
        with open(self.__filename, 'wb') as csv_file:
            cwriter = csv.writer(csv_file, delimiter=',')
            cwriter.writerow(['F3', 'F4', 'P7', 'FC6', 'F7', 'F8', 'T7',
                              'P8', 'FC5', 'AF4', 'T8', 'O2', 'O1', 'AF3'])
        csv_file.close()
        """

    def get_emotiv(self):
        """
            return emotiv device
        """
        return self.__emotiv

    def run(self):
        """
            method run()
        """
        try:
            while True:
                num = 0
                while num < 128:
                    packet = self.__emotiv.dequeue()
                    data = np.array([packet.F3[0], packet.F4[0], packet.P7[0],
                                     packet.FC6[0], packet.F7[0], packet.F8[0],
                                     packet.T7[0], packet.P8[0], packet.FC5[0],
                                     packet.AF4[0], packet.T8[0], packet.O2[0],
                                     packet.O1[0], packet.AF3[0]])
                    """
                    with open(self.__filename, 'ab') as csv_file:
                        writer = csv.writer(csv_file, dialect='excel')
                        writer.writerow(data)
                    csv_file.close()
                    """
                    print "Emocon is Running"
                    gevent.sleep(1)
                    num += 1
        except KeyboardInterrupt:
            self.__emotiv.close()
        finally:
            self.__emotiv.close()

def main():
    """
        main()
    """
    emocon = EmotivController()
    gevent.joinall([
        gevent.spawn(emocon.run),
        gevent.spawn(emocon.get_emotiv().setup)
    ])

if __name__ == "__main__":
    main()
