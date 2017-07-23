"""
    module main
        Main Function
"""

import sys
from PyQt4 import QtGui
from GUI.Window import MainWindow

def main():
    """
        function main
    """
    app = QtGui.QApplication(sys.argv)
    w = MainWindow.MainWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
