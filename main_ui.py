# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sortbox = QtWidgets.QComboBox(self.centralwidget)
        self.sortbox.setGeometry(QtCore.QRect(30, 50, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.sortbox.setFont(font)
        self.sortbox.setStyleSheet("border: 2px solid #B47747;\n"
"border-radius: 8px;}\n"
"QComboBox::drop-down {\n"
"    width: 32px; border-radius: 8px;}\n"
"QComboBox:hover {\n"
"    background-color: BISQUE;border: 2px solid #B47747; border-radius: 8px;}\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: #B47747;\n"
" \n"
"")
        self.sortbox.setCurrentText("")
        self.sortbox.setObjectName("sortbox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.roast = QtWidgets.QLabel(self.centralwidget)
        self.roast.setGeometry(QtCore.QRect(30, 200, 731, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.roast.setFont(font)
        self.roast.setText("")
        self.roast.setObjectName("roast")
        self.info = QtWidgets.QPushButton(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(30, 100, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.info.setFont(font)
        self.info.setStyleSheet("QPushButton {\n"
"background-color: white;border: 2px solid #B47747; border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: BISQUE;border: 2px solid #B47747; border-radius: 8px;\n"
"}")
        self.info.setObjectName("info")
        self.ground = QtWidgets.QLabel(self.centralwidget)
        self.ground.setGeometry(QtCore.QRect(30, 250, 731, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.ground.setFont(font)
        self.ground.setText("")
        self.ground.setObjectName("ground")
        self.taste = QtWidgets.QLabel(self.centralwidget)
        self.taste.setGeometry(QtCore.QRect(30, 300, 731, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.taste.setFont(font)
        self.taste.setText("")
        self.taste.setObjectName("taste")
        self.price = QtWidgets.QLabel(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(30, 350, 731, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.price.setFont(font)
        self.price.setText("")
        self.price.setObjectName("price")
        self.volume = QtWidgets.QLabel(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(30, 400, 731, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.volume.setFont(font)
        self.volume.setText("")
        self.volume.setObjectName("volume")
        self.id = QtWidgets.QLabel(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(30, 150, 731, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.id.setFont(font)
        self.id.setText("")
        self.id.setObjectName("id")
        self.change = QtWidgets.QPushButton(self.centralwidget)
        self.change.setGeometry(QtCore.QRect(160, 100, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.change.setFont(font)
        self.change.setStyleSheet("QPushButton {\n"
"background-color: white;border: 2px solid #B47747; border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: BISQUE;border: 2px solid #B47747; border-radius: 8px;\n"
"}")
        self.change.setObjectName("change")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(290, 50, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.add.setFont(font)
        self.add.setStyleSheet("QPushButton {\n"
"background-color: white;border: 2px solid #B47747; border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: BISQUE;border: 2px solid #B47747; border-radius: 8px;\n"
"}")
        self.add.setObjectName("add")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Кофе"))
        self.label.setText(_translate("MainWindow", "Выбрать сорт кофе:"))
        self.info.setText(_translate("MainWindow", "Инфо"))
        self.change.setText(_translate("MainWindow", "Изменить"))
        self.add.setText(_translate("MainWindow", "Добавить новый"))
