# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StabiliKneeEMGReading.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qtpy import QtCore

class UIMainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1113, 851)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(90, 110, 251, 110))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.vtag_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.vtag_9.setContentsMargins(0, 0, 0, 0)
        self.vtag_9.setObjectName("vtag_9")
        self.a1_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.a1_label.setFont(font)
        self.a1_label.setObjectName("a1_label")
        self.vtag_9.addWidget(self.a1_label)
        self.tma1_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tma1_label.setFont(font)
        self.tma1_label.setObjectName("tma1_label")
        self.vtag_9.addWidget(self.tma1_label)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(90, 500, 251, 81))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.vtag_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.vtag_10.setContentsMargins(0, 0, 0, 0)
        self.vtag_10.setObjectName("vtag_10")
        self.a3_label = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.a3_label.setFont(font)
        self.a3_label.setObjectName("a3_label")
        self.vtag_10.addWidget(self.a3_label)
        self.tma3_label = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tma3_label.setFont(font)
        self.tma3_label.setObjectName("tma3_label")
        self.vtag_10.addWidget(self.tma3_label)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(880, 110, 121, 111))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.vdata2_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.vdata2_3.setContentsMargins(0, 0, 0, 0)
        self.vdata2_3.setObjectName("vdata2_3")
        self.a2 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.a2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.a2.setText("")
        self.a2.setObjectName("a2")
        self.vdata2_3.addWidget(self.a2)
        self.tma2 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.tma2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tma2.setText("")
        self.tma2.setObjectName("tma2")
        self.vdata2_3.addWidget(self.tma2)
        self.graph_1 = QtWidgets.QLabel(self.centralwidget)
        self.graph_1.setGeometry(QtCore.QRect(90, 220, 371, 201))
        self.graph_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graph_1.setText("")
        self.graph_1.setObjectName("graph_1")
        self.muscle_h1 = QtWidgets.QLabel(self.centralwidget)
        self.muscle_h1.setGeometry(QtCore.QRect(230, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.muscle_h1.setFont(font)
        self.muscle_h1.setObjectName("muscle_h1")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(340, 110, 121, 111))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.vdata_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.vdata_3.setContentsMargins(0, 0, 0, 0)
        self.vdata_3.setObjectName("vdata_3")
        self.a1 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.a1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.a1.setText("")
        self.a1.setObjectName("a1")
        self.vdata_3.addWidget(self.a1)
        self.tma1 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.tma1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tma1.setText("")
        self.tma1.setObjectName("tma1")
        self.vdata_3.addWidget(self.tma1)
        self.graph_3 = QtWidgets.QLabel(self.centralwidget)
        self.graph_3.setGeometry(QtCore.QRect(90, 580, 371, 201))
        self.graph_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graph_3.setText("")
        self.graph_3.setObjectName("graph_3")
        self.graph_2 = QtWidgets.QLabel(self.centralwidget)
        self.graph_2.setGeometry(QtCore.QRect(640, 220, 361, 201))
        self.graph_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graph_2.setText("")
        self.graph_2.setObjectName("graph_2")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(640, 110, 241, 111))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.vtag_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.vtag_11.setContentsMargins(0, 0, 0, 0)
        self.vtag_11.setObjectName("vtag_11")
        self.a2_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.a2_label.setFont(font)
        self.a2_label.setObjectName("a2_label")
        self.vtag_11.addWidget(self.a2_label)
        self.tma2_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tma2_label.setFont(font)
        self.tma2_label.setObjectName("tma2_label")
        self.vtag_11.addWidget(self.tma2_label)
        self.muscle_h2 = QtWidgets.QLabel(self.centralwidget)
        self.muscle_h2.setGeometry(QtCore.QRect(760, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.muscle_h2.setFont(font)
        self.muscle_h2.setObjectName("muscle_h2")
        self.muscle_h3 = QtWidgets.QLabel(self.centralwidget)
        self.muscle_h3.setGeometry(QtCore.QRect(230, 480, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.muscle_h3.setFont(font)
        self.muscle_h3.setObjectName("muscle_h3")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(340, 500, 121, 81))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.vdata3_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.vdata3_3.setContentsMargins(0, 0, 0, 0)
        self.vdata3_3.setObjectName("vdata3_3")
        self.a3 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.a3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.a3.setText("")
        self.a3.setObjectName("a3")
        self.vdata3_3.addWidget(self.a3)
        self.tma3 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.tma3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tma3.setText("")
        self.tma3.setObjectName("tma3")
        self.vdata3_3.addWidget(self.tma3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(70, 70, 981, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(640, 500, 241, 81))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.vtag_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.vtag_12.setContentsMargins(0, 0, 0, 0)
        self.vtag_12.setObjectName("vtag_12")
        self.a4_label = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.a4_label.setFont(font)
        self.a4_label.setObjectName("a4_label")
        self.vtag_12.addWidget(self.a4_label)
        self.tma4_label = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tma4_label.setFont(font)
        self.tma4_label.setObjectName("tma4_label")
        self.vtag_12.addWidget(self.tma4_label)
        self.screen_title = QtWidgets.QLabel(self.centralwidget)
        self.screen_title.setGeometry(QtCore.QRect(400, 40, 361, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screen_title.sizePolicy().hasHeightForWidth())
        self.screen_title.setSizePolicy(sizePolicy)
        self.screen_title.setBaseSize(QtCore.QSize(7, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.screen_title.setFont(font)
        self.screen_title.setObjectName("screen_title")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(880, 500, 121, 81))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.vdata4_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.vdata4_3.setContentsMargins(0, 0, 0, 0)
        self.vdata4_3.setObjectName("vdata4_3")
        self.a4 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.a4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.a4.setText("")
        self.a4.setObjectName("a4")
        self.vdata4_3.addWidget(self.a4)
        self.tma4 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.tma4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tma4.setText("")
        self.tma4.setObjectName("tma4")
        self.vdata4_3.addWidget(self.tma4)
        self.graph_4 = QtWidgets.QLabel(self.centralwidget)
        self.graph_4.setGeometry(QtCore.QRect(640, 580, 361, 201))
        self.graph_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graph_4.setText("")
        self.graph_4.setObjectName("graph_4")
        self.muscle_h4 = QtWidgets.QLabel(self.centralwidget)
        self.muscle_h4.setGeometry(QtCore.QRect(770, 480, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.muscle_h4.setFont(font)
        self.muscle_h4.setObjectName("muscle_h4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1113, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.a1_label.setText(_translate("MainWindow", "Amplitude (mV)"))
        self.tma1_label.setText(_translate("MainWindow", "Total Muscle Activity (mV)"))
        self.a3_label.setText(_translate("MainWindow", "Amplitude (mV)"))
        self.tma3_label.setText(_translate("MainWindow", "Total Muscle Activity (mV)"))
        self.muscle_h1.setText(_translate("MainWindow", "Muscle #1"))
        self.a2_label.setText(_translate("MainWindow", "Amplitude (mV)"))
        self.tma2_label.setText(_translate("MainWindow", "Total Muscle Activity (mV)"))
        self.muscle_h2.setText(_translate("MainWindow", "Muscle #2"))
        self.muscle_h3.setText(_translate("MainWindow", "Muscle #3"))
        self.a4_label.setText(_translate("MainWindow", "Amplitude (mV)"))
        self.tma4_label.setText(_translate("MainWindow", "Total Muscle Activity (mV)"))
        self.screen_title.setText(_translate("MainWindow", "StabiliKnee EMG Reading"))
        self.muscle_h4.setText(_translate("MainWindow", "Muscle #4"))

