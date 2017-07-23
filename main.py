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
    window = MainWindow.MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
