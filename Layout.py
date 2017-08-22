# -*- coding: utf-8 -*-
"""
  Layout.py
    메인 윈도우에서 사용할 레이아웃 인스턴스
"""

from PyQt4 import QtGui

MAIN = QtGui.QHBoxLayout()
BUTTON = QtGui.QGridLayout()
LABEL = QtGui.QVBoxLayout()
GRAPH = QtGui.QVBoxLayout()
CONTROLLER = QtGui.QVBoxLayout()

if __name__ == '__main__':
    print 'Layout.py is module. please run main.py'
