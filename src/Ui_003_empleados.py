# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\rviqu\OneDrive - Universidad Internacional de las Américas (UIA)\UIA\2024\I\Programación II\Proyecto Final\tresPatitosUIA\src\003_empleados.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Empleados(object):
    def setupUi(self, Empleados):
        Empleados.setObjectName("Empleados")
        Empleados.resize(687, 691)
        self.label = QtWidgets.QLabel(Empleados)
        self.label.setGeometry(QtCore.QRect(270, 0, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lblCedula = QtWidgets.QLabel(Empleados)
        self.lblCedula.setGeometry(QtCore.QRect(20, 80, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblCedula.setFont(font)
        self.lblCedula.setObjectName("lblCedula")
        self.lblNombre = QtWidgets.QLabel(Empleados)
        self.lblNombre.setGeometry(QtCore.QRect(20, 140, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")
        self.lblApellidos = QtWidgets.QLabel(Empleados)
        self.lblApellidos.setGeometry(QtCore.QRect(20, 200, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblApellidos.setFont(font)
        self.lblApellidos.setObjectName("lblApellidos")
        self.lblDireccion = QtWidgets.QLabel(Empleados)
        self.lblDireccion.setGeometry(QtCore.QRect(490, 80, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblDireccion.setFont(font)
        self.lblDireccion.setObjectName("lblDireccion")
        self.lblPuesto = QtWidgets.QLabel(Empleados)
        self.lblPuesto.setGeometry(QtCore.QRect(490, 140, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPuesto.setFont(font)
        self.lblPuesto.setObjectName("lblPuesto")
        self.lblIngreso = QtWidgets.QLabel(Empleados)
        self.lblIngreso.setGeometry(QtCore.QRect(490, 200, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblIngreso.setFont(font)
        self.lblIngreso.setObjectName("lblIngreso")
        self.lblJefatura = QtWidgets.QLabel(Empleados)
        self.lblJefatura.setGeometry(QtCore.QRect(490, 270, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblJefatura.setFont(font)
        self.lblJefatura.setObjectName("lblJefatura")
        self.txtCedula = QtWidgets.QLineEdit(Empleados)
        self.txtCedula.setGeometry(QtCore.QRect(110, 80, 113, 20))
        self.txtCedula.setObjectName("txtCedula")
        self.txtNombre = QtWidgets.QLineEdit(Empleados)
        self.txtNombre.setGeometry(QtCore.QRect(110, 140, 113, 20))
        self.txtNombre.setObjectName("txtNombre")
        self.txtApellidos = QtWidgets.QLineEdit(Empleados)
        self.txtApellidos.setGeometry(QtCore.QRect(110, 200, 113, 20))
        self.txtApellidos.setObjectName("txtApellidos")
        self.txtDireccion = QtWidgets.QLineEdit(Empleados)
        self.txtDireccion.setGeometry(QtCore.QRect(560, 80, 113, 20))
        self.txtDireccion.setObjectName("txtDireccion")
        self.txtPuesto = QtWidgets.QLineEdit(Empleados)
        self.txtPuesto.setGeometry(QtCore.QRect(560, 140, 113, 20))
        self.txtPuesto.setObjectName("txtPuesto")
        self.txtIngreso = QtWidgets.QLineEdit(Empleados)
        self.txtIngreso.setGeometry(QtCore.QRect(560, 200, 113, 20))
        self.txtIngreso.setObjectName("txtIngreso")
        self.txtJefatura = QtWidgets.QLineEdit(Empleados)
        self.txtJefatura.setGeometry(QtCore.QRect(560, 270, 113, 20))
        self.txtJefatura.setObjectName("txtJefatura")
        self.label_2 = QtWidgets.QLabel(Empleados)
        self.label_2.setGeometry(QtCore.QRect(270, 60, 161, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../../Laboratorio_6_Kevin_Chacon_Quesada_Aarón_Zúñiga_Ramírez_Robert_Viquez_Santos/Laboratorio_6_Kevin_Chacon_Quesada_Aarón_Zúñiga_Ramírez_Robert_Viquez_Santos/recursos/woman.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.bttCrearEmpleado = QtWidgets.QPushButton(Empleados)
        self.bttCrearEmpleado.setGeometry(QtCore.QRect(270, 240, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bttCrearEmpleado.setFont(font)
        self.bttCrearEmpleado.setObjectName("bttCrearEmpleado")
        self.label_3 = QtWidgets.QLabel(Empleados)
        self.label_3.setGeometry(QtCore.QRect(20, 270, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtTelefono = QtWidgets.QLineEdit(Empleados)
        self.txtTelefono.setGeometry(QtCore.QRect(110, 270, 113, 20))
        self.txtTelefono.setObjectName("txtTelefono")
        self.tblWidgetEmpleados = QtWidgets.QTableWidget(Empleados)
        self.tblWidgetEmpleados.setGeometry(QtCore.QRect(20, 440, 651, 241))
        self.tblWidgetEmpleados.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblWidgetEmpleados.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblWidgetEmpleados.setObjectName("tblWidgetEmpleados")
        self.tblWidgetEmpleados.setColumnCount(0)
        self.tblWidgetEmpleados.setRowCount(0)
        self.bttModificarEmpleado = QtWidgets.QPushButton(Empleados)
        self.bttModificarEmpleado.setGeometry(QtCore.QRect(270, 340, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bttModificarEmpleado.setFont(font)
        self.bttModificarEmpleado.setObjectName("bttModificarEmpleado")
        self.bttEliminarEmpleado = QtWidgets.QPushButton(Empleados)
        self.bttEliminarEmpleado.setGeometry(QtCore.QRect(510, 340, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bttEliminarEmpleado.setFont(font)
        self.bttEliminarEmpleado.setObjectName("bttEliminarEmpleado")
        self.bttLimpiarEmpleado = QtWidgets.QPushButton(Empleados)
        self.bttLimpiarEmpleado.setGeometry(QtCore.QRect(20, 340, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bttLimpiarEmpleado.setFont(font)
        self.bttLimpiarEmpleado.setObjectName("bttLimpiarEmpleado")

        self.retranslateUi(Empleados)
        QtCore.QMetaObject.connectSlotsByName(Empleados)

    def retranslateUi(self, Empleados):
        _translate = QtCore.QCoreApplication.translate
        Empleados.setWindowTitle(_translate("Empleados", "Empleados"))
        self.label.setText(_translate("Empleados", "Crear Empleados"))
        self.lblCedula.setText(_translate("Empleados", "Cedula:"))
        self.lblNombre.setText(_translate("Empleados", "Nombre:"))
        self.lblApellidos.setText(_translate("Empleados", "Apellidos:"))
        self.lblDireccion.setText(_translate("Empleados", "Direccion:"))
        self.lblPuesto.setText(_translate("Empleados", "Puesto:"))
        self.lblIngreso.setText(_translate("Empleados", "Ingreso:"))
        self.lblJefatura.setText(_translate("Empleados", "Jefatura:"))
        self.bttCrearEmpleado.setText(_translate("Empleados", "Crear Empleado"))
        self.label_3.setText(_translate("Empleados", "Telefono:"))
        self.bttModificarEmpleado.setText(_translate("Empleados", "Modificar Empleado"))
        self.bttEliminarEmpleado.setText(_translate("Empleados", "Eliminar Empleado"))
        self.bttLimpiarEmpleado.setText(_translate("Empleados", "Limpiar Datos"))
