# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\aaron\OneDrive\Documentos\Python\tresPatitosUIA\src\052_desligar_bienes.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Desligar(object):
    def setupUi(self, Desligar):
        Desligar.setObjectName("Desligar")
        Desligar.resize(500, 355)
        self.cbxEmpleados = QtWidgets.QComboBox(Desligar)
        self.cbxEmpleados.setGeometry(QtCore.QRect(10, 110, 171, 21))
        self.cbxEmpleados.setEditable(False)
        self.cbxEmpleados.setCurrentText("")
        self.cbxEmpleados.setObjectName("cbxEmpleados")
        self.btnDesligar = QtWidgets.QPushButton(Desligar)
        self.btnDesligar.setGeometry(QtCore.QRect(10, 300, 75, 23))
        self.btnDesligar.setObjectName("btnDesligar")
        self.txtBienAsignado = QtWidgets.QLineEdit(Desligar)
        self.txtBienAsignado.setGeometry(QtCore.QRect(10, 270, 82, 20))
        self.txtBienAsignado.setObjectName("txtBienAsignado")
        self.tblDesligar = QtWidgets.QTableWidget(Desligar)
        self.tblDesligar.setGeometry(QtCore.QRect(220, 80, 256, 192))
        self.tblDesligar.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblDesligar.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblDesligar.setObjectName("tblDesligar")
        self.tblDesligar.setColumnCount(0)
        self.tblDesligar.setRowCount(0)
        self.label_4 = QtWidgets.QLabel(Desligar)
        self.label_4.setGeometry(QtCore.QRect(10, 250, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Desligar)
        self.label.setGeometry(QtCore.QRect(190, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Desligar)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtNombre = QtWidgets.QLineEdit(Desligar)
        self.txtNombre.setGeometry(QtCore.QRect(10, 220, 82, 20))
        self.txtNombre.setObjectName("txtNombre")
        self.label_2 = QtWidgets.QLabel(Desligar)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtCedula = QtWidgets.QLineEdit(Desligar)
        self.txtCedula.setGeometry(QtCore.QRect(10, 170, 82, 20))
        self.txtCedula.setObjectName("txtCedula")
        self.lblID = QtWidgets.QLabel(Desligar)
        self.lblID.setGeometry(QtCore.QRect(10, 140, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblID.setFont(font)
        self.lblID.setObjectName("lblID")

        self.retranslateUi(Desligar)
        self.cbxEmpleados.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Desligar)

    def retranslateUi(self, Desligar):
        _translate = QtCore.QCoreApplication.translate
        Desligar.setWindowTitle(_translate("Desligar", "Desligar Bienes"))
        self.cbxEmpleados.setPlaceholderText(_translate("Desligar", "Seleccione"))
        self.btnDesligar.setText(_translate("Desligar", "Desligar"))
        self.label_4.setText(_translate("Desligar", "Bien asignado"))
        self.label.setText(_translate("Desligar", "Desligar Bienes"))
        self.label_3.setText(_translate("Desligar", "Nombre Empleado"))
        self.label_2.setText(_translate("Desligar", "Seleccione el empelado:"))
        self.lblID.setText(_translate("Desligar", "ID Empleado"))
