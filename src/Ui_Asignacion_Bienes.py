# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\rviqu\OneDrive - Universidad Internacional de las Américas (UIA)\UIA\2024\I\Programación II\Proyecto Final\tresPatitosUIA\src\Asignacion_Bienes.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Asignacion_Bienes(object):
    def setupUi(self, Asignacion_Bienes):
        Asignacion_Bienes.setObjectName("Asignacion_Bienes")
        Asignacion_Bienes.resize(508, 467)
        self.formLayoutWidget = QtWidgets.QWidget(Asignacion_Bienes)
        self.formLayoutWidget.setGeometry(QtCore.QRect(150, 70, 191, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblNombre = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblNombre)
        self.txtNombre = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtNombre.setObjectName("txtNombre")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtNombre)
        self.lblCedula = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblCedula.setFont(font)
        self.lblCedula.setObjectName("lblCedula")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblCedula)
        self.txtCedula = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtCedula.setObjectName("txtCedula")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtCedula)
        self.lblApellidos = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblApellidos.setFont(font)
        self.lblApellidos.setObjectName("lblApellidos")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblApellidos)
        self.txtApellidos = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtApellidos.setObjectName("txtApellidos")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtApellidos)
        self.lblTelefono = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblTelefono.setFont(font)
        self.lblTelefono.setObjectName("lblTelefono")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblTelefono)
        self.txtTelefono = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtTelefono.setObjectName("txtTelefono")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtTelefono)
        self.txtBienAsignado = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtBienAsignado.setObjectName("txtBienAsignado")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtBienAsignado)
        self.lblBienAsignado = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblBienAsignado.setFont(font)
        self.lblBienAsignado.setObjectName("lblBienAsignado")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblBienAsignado)
        self.label = QtWidgets.QLabel(Asignacion_Bienes)
        self.label.setGeometry(QtCore.QRect(140, 40, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Asignacion_Bienes)
        self.pushButton.setGeometry(QtCore.QRect(110, 220, 51, 41))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\recursos/guardar.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Asignacion_Bienes)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 220, 51, 41))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\recursos/editar.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Asignacion_Bienes)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 220, 51, 41))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\recursos/eliminar.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setAutoExclusive(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Asignacion_Bienes)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 220, 51, 41))
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\recursos/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setObjectName("pushButton_4")
        self = QtWidgets.QTableView(Asignacion_Bienes)
        self.setGeometry(QtCore.QRect(40, 270, 421, 171))
        self.setObjectName("0")

        self.retranslateUi(Asignacion_Bienes)
        QtCore.QMetaObject.connectSlotsByName(Asignacion_Bienes)

    def retranslateUi(self, Asignacion_Bienes):
        _translate = QtCore.QCoreApplication.translate
        Asignacion_Bienes.setWindowTitle(_translate("Asignacion_Bienes", "Asignacion de bienes"))
        self.lblNombre.setText(_translate("Asignacion_Bienes", "Nombre"))
        self.lblCedula.setText(_translate("Asignacion_Bienes", "Cédula"))
        self.lblApellidos.setText(_translate("Asignacion_Bienes", "Apellidos"))
        self.lblTelefono.setText(_translate("Asignacion_Bienes", "Teléfono"))
        self.lblBienAsignado.setText(_translate("Asignacion_Bienes", "Bien Asignado"))
        self.label.setText(_translate("Asignacion_Bienes", "Asignación de Bienes"))
