#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 03:05:49 2018

@author: unixuser
"""
from PyQt5 import QtWidgets

import sys
sys.path.insert(0,r'F:\Program Files\Microsoft Visual Studio\Projects\PerDia\UI')

from UI import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())