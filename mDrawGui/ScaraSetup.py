# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScaraSetup.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1053, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(1053, 500))
        Dialog.setMaximumSize(QtCore.QSize(1053, 500))
        font = QtGui.QFont()
        font.setFamily("Arial")
        Dialog.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 261))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.label_2.setObjectName("label_2")
        self.lineArm0 = QtWidgets.QLineEdit(self.groupBox)
        self.lineArm0.setGeometry(QtCore.QRect(180, 30, 113, 20))
        self.lineArm0.setObjectName("lineArm0")
        self.lineArm1 = QtWidgets.QLineEdit(self.groupBox)
        self.lineArm1.setGeometry(QtCore.QRect(180, 60, 113, 20))
        self.lineArm1.setObjectName("lineArm1")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 131, 16))
        self.label_4.setObjectName("label_4")
        self.motoA_CK = QtWidgets.QLabel(self.groupBox)
        self.motoA_CK.setGeometry(QtCore.QRect(180, 120, 51, 51))
        self.motoA_CK.setStyleSheet("     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 4px;")
        self.motoA_CK.setPixmap(QtGui.QPixmap(":/images/stepping_motor-clockwise.png"))
        self.motoA_CK.setObjectName("motoA_CK")
        self.motoB_CK = QtWidgets.QLabel(self.groupBox)
        self.motoB_CK.setGeometry(QtCore.QRect(180, 180, 51, 51))
        self.motoB_CK.setStyleSheet("     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 4px;")
        self.motoB_CK.setPixmap(QtGui.QPixmap(":/images/stepping_motor-clockwise.png"))
        self.motoB_CK.setObjectName("motoB_CK")
        self.motoA_CCK = QtWidgets.QLabel(self.groupBox)
        self.motoA_CCK.setGeometry(QtCore.QRect(270, 120, 51, 51))
        self.motoA_CCK.setPixmap(QtGui.QPixmap(":/images/stepping_motor-anticlockwise.png"))
        self.motoA_CCK.setObjectName("motoA_CCK")
        self.motoB_CCK = QtWidgets.QLabel(self.groupBox)
        self.motoB_CCK.setGeometry(QtCore.QRect(270, 180, 51, 51))
        self.motoB_CCK.setPixmap(QtGui.QPixmap(":/images/stepping_motor-anticlockwise.png"))
        self.motoB_CCK.setObjectName("motoB_CCK")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(350, 10, 24, 24))
        self.pushButton.setStyleSheet(" QPushButton {\n"
"    border-image: url(:/images/help-icon.png) 0;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"    border-image: url(:/images/help-icon-hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    border-image: url(:/images/help-icon-click.png) 0;\n"
" }\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(170, 240, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(260, 240, 91, 16))
        self.label_6.setObjectName("label_6")
        self.slidSpeed = QtWidgets.QSlider(self.groupBox)
        self.slidSpeed.setGeometry(QtCore.QRect(180, 90, 160, 19))
        self.slidSpeed.setProperty("value", 50)
        self.slidSpeed.setOrientation(QtCore.Qt.Horizontal)
        self.slidSpeed.setObjectName("slidSpeed")
        self.labelSpeed = QtWidgets.QLabel(self.groupBox)
        self.labelSpeed.setGeometry(QtCore.QRect(20, 90, 131, 16))
        self.labelSpeed.setObjectName("labelSpeed")
        self.btnOk = QtWidgets.QPushButton(Dialog)
        self.btnOk.setGeometry(QtCore.QRect(300, 280, 91, 23))
        self.btnOk.setObjectName("btnOk")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(400, 30, 651, 431))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/images/mScara_setup.png"))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Scara Setups"))
        self.label.setText(_translate("Dialog", "Arm A Length (mm):"))
        self.label_2.setText(_translate("Dialog", "Arm B Length (mm):"))
        self.label_3.setText(_translate("Dialog", "Stepper A Directoin:"))
        self.label_4.setText(_translate("Dialog", "Stepper B Directoin:"))
        self.label_5.setText(_translate("Dialog", "ClockWise"))
        self.label_6.setText(_translate("Dialog", "Anti ClockWise"))
        self.labelSpeed.setText(_translate("Dialog", "Speed (50%):"))
        self.btnOk.setText(_translate("Dialog", "Ok"))

import images_rc
