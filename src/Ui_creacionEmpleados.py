# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\rviqu\OneDrive - Universidad Internacional de las Américas (UIA)\UIA\2024\I\Programación II\Proyecto Final\tresPatitosUIA\src\creacionEmpleados.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CrearEmpleados(object):
    def setupUi(self, CrearEmpleados):
        CrearEmpleados.setObjectName("CrearEmpleados")
        CrearEmpleados.resize(682, 398)
        self.label = QtWidgets.QLabel(CrearEmpleados)
        self.label.setGeometry(QtCore.QRect(240, 0, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lblCedula = QtWidgets.QLabel(CrearEmpleados)
        self.lblCedula.setGeometry(QtCore.QRect(20, 80, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblCedula.setFont(font)
        self.lblCedula.setObjectName("lblCedula")
        self.lblNombre = QtWidgets.QLabel(CrearEmpleados)
        self.lblNombre.setGeometry(QtCore.QRect(20, 140, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")
        self.lblApellidos = QtWidgets.QLabel(CrearEmpleados)
        self.lblApellidos.setGeometry(QtCore.QRect(20, 200, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblApellidos.setFont(font)
        self.lblApellidos.setObjectName("lblApellidos")
        self.lblDireccion = QtWidgets.QLabel(CrearEmpleados)
        self.lblDireccion.setGeometry(QtCore.QRect(430, 80, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblDireccion.setFont(font)
        self.lblDireccion.setObjectName("lblDireccion")
        self.lblPuesto = QtWidgets.QLabel(CrearEmpleados)
        self.lblPuesto.setGeometry(QtCore.QRect(430, 140, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPuesto.setFont(font)
        self.lblPuesto.setObjectName("lblPuesto")
        self.lblIngreso = QtWidgets.QLabel(CrearEmpleados)
        self.lblIngreso.setGeometry(QtCore.QRect(430, 200, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblIngreso.setFont(font)
        self.lblIngreso.setObjectName("lblIngreso")
        self.lblJefatura = QtWidgets.QLabel(CrearEmpleados)
        self.lblJefatura.setGeometry(QtCore.QRect(430, 270, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblJefatura.setFont(font)
        self.lblJefatura.setObjectName("lblJefatura")
        self.txtCedula = QtWidgets.QLineEdit(CrearEmpleados)
        self.txtCedula.setGeometry(QtCore.QRect(110, 80, 113, 20))
        self.txtCedula.setObjectName("txtCedula")
        self.txtNombre = QtWidgets.QLineEdit(CrearEmpleados)
        self.txtNombre.setGeometry(QtCore.QRect(110, 140, 113, 20))
        self.txtNombre.setObjectName("txtNombre")
        self.txtApellidos = QtWidgets.QLineEdit(CrearEmpleados)
        self.txtApellidos.setGeometry(QtCore.QRect(110, 200, 113, 20))
        self.txtApellidos.setObjectName("txtApellidos")
        self.txtDireccion = QtWidgets.QLineEdit(CrearEmpleados)
        self.txtDireccion.setGeometry(QtCore.QRect(510, 80, 113, 20))
        self.txtDireccion.setObjectName("txtDireccion")
        self.txtPuesto = QtWidgets.QLineEdit(CrearEmpleados)
        self.txtPuesto.setGeometry(QtCore.QRect(510, 140, 113, 20))
        self.txtPuesto.setObjectName("txtPuesto")
        self.txtIngreso = QtWidgets.QLineEdit(CrearEmpleados)
        self.txtIngreso.setGeometry(QtCore.QRect(510, 200, 113, 20))
        self.txtIngreso.setObjectName("txtIngreso")
        self.txtJefatura = QtWidgets.QLineEdit(CrearEmpleados)
        self.txtJefatura.setGeometry(QtCore.QRect(510, 270, 113, 20))
        self.txtJefatura.setObjectName("txtJefatura")
        self.label_2 = QtWidgets.QLabel(CrearEmpleados)
        self.label_2.setGeometry(QtCore.QRect(250, 80, 161, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../../Laboratorio_6_Kevin_Chacon_Quesada_Aarón_Zúñiga_Ramírez_Robert_Viquez_Santos/Laboratorio_6_Kevin_Chacon_Quesada_Aarón_Zúñiga_Ramírez_Robert_Viquez_Santos/recursos/woman.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.bttCrearEmpleado = QtWidgets.QPushButton(CrearEmpleados)
        self.bttCrearEmpleado.setGeometry(QtCore.QRect(250, 280, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bttCrearEmpleado.setFont(font)
        self.bttCrearEmpleado.setObjectName("bttCrearEmpleado")
        self.label_3 = QtWidgets.QLabel(CrearEmpleados)
        self.label_3.setGeometry(QtCore.QRect(20, 270, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtTelefono = QtWidgets.QLineEdit(CrearEmpleados)
        self.txtTelefono.setGeometry(QtCore.QRect(110, 270, 113, 20))
        self.txtTelefono.setObjectName("txtTelefono")

        self.retranslateUi(CrearEmpleados)
        QtCore.QMetaObject.connectSlotsByName(CrearEmpleados)

    def retranslateUi(self, CrearEmpleados):
        _translate = QtCore.QCoreApplication.translate
        CrearEmpleados.setWindowTitle(_translate("CrearEmpleados", "Creacion de Empleados"))
        self.label.setText(_translate("CrearEmpleados", "Crear Empleados"))
        self.lblCedula.setText(_translate("CrearEmpleados", "Cedula:"))
        self.lblNombre.setText(_translate("CrearEmpleados", "Nombre:"))
        self.lblApellidos.setText(_translate("CrearEmpleados", "Apellidos:"))
        self.lblDireccion.setText(_translate("CrearEmpleados", "Direccion:"))
        self.lblPuesto.setText(_translate("CrearEmpleados", "Puesto:"))
        self.lblIngreso.setText(_translate("CrearEmpleados", "Ingreso:"))
        self.lblJefatura.setText(_translate("CrearEmpleados", "Jefatura:"))
        self.bttCrearEmpleado.setText(_translate("CrearEmpleados", "Crear Empleado"))
        self.label_3.setText(_translate("CrearEmpleados", "Telefono:"))
