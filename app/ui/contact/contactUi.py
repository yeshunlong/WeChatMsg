# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contactUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        # Form.resize(840, 752)
        # Form.setStyleSheet("background: rgb(240, 240, 240);")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(30, 0))
        self.label_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_2.setStretch(1, 1)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
