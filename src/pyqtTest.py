# -*- coding: cp936 -*-
'''
Created on 2013-4-13

@author: wangyb
@brief:
'''

import sys
from PyQt4 import QtGui

a = QtGui.QApplication(sys.argv)
label = QtGui.QLabel("你好，中国!")
label.resize(400,200)
label.show()
a.exec_()
