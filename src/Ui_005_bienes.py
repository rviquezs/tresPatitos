# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\aaron\OneDrive\Documentos\Python\tresPatitosUIA\src\005_bienes.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Bienes(object):
    def setupUi(self, Bienes):
        Bienes.setObjectName("Bienes")
        Bienes.resize(489, 396)
        self.label = QtWidgets.QLabel(Bienes)
        self.label.setGeometry(QtCore.QRect(20, 40, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(Bienes)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 70, 167, 201))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblPlaca = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblPlaca.setObjectName("lblPlaca")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblPlaca)
        self.txtPlaca = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtPlaca.setObjectName("txtPlaca")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtPlaca)
        self.lblNombreBien = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblNombreBien.setObjectName("lblNombreBien")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblNombreBien)
        self.txtNombreBien = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtNombreBien.setObjectName("txtNombreBien")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtNombreBien)
        self.lblCategoria = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblCategoria.setObjectName("lblCategoria")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblCategoria)
        self.txtCategoria = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtCategoria.setObjectName("txtCategoria")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtCategoria)
        self.lblDescripcion = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblDescripcion.setObjectName("lblDescripcion")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblDescripcion)
        self.txtDescripcion = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtDescripcion.setObjectName("txtDescripcion")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtDescripcion)
        self.lblestado = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblestado.setObjectName("lblestado")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblestado)
        self.cbxEstado = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cbxEstado.setObjectName("cbxEstado")
        self.cbxEstado.addItem("")
        self.cbxEstado.addItem("")
        self.cbxEstado.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cbxEstado)
        self.btnGuardar = QtWidgets.QPushButton(Bienes)
        self.btnGuardar.setGeometry(QtCore.QRect(20, 280, 41, 41))
        self.btnGuardar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconSave.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuardar.setIcon(icon)
        self.btnGuardar.setIconSize(QtCore.QSize(27, 27))
        self.btnGuardar.setObjectName("btnGuardar")
        self.btnModificar = QtWidgets.QPushButton(Bienes)
        self.btnModificar.setGeometry(QtCore.QRect(70, 280, 41, 41))
        self.btnModificar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconEdit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificar.setIcon(icon1)
        self.btnModificar.setIconSize(QtCore.QSize(27, 27))
        self.btnModificar.setObjectName("btnModificar")
        self.btnEliminar = QtWidgets.QPushButton(Bienes)
        self.btnEliminar.setGeometry(QtCore.QRect(120, 280, 41, 41))
        self.btnEliminar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconDelete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminar.setIcon(icon2)
        self.btnEliminar.setIconSize(QtCore.QSize(27, 27))
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnCancelar = QtWidgets.QPushButton(Bienes)
        self.btnCancelar.setGeometry(QtCore.QRect(170, 280, 41, 41))
        self.btnCancelar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconClear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon3)
        self.btnCancelar.setIconSize(QtCore.QSize(27, 27))
        self.btnCancelar.setObjectName("btnCancelar")
        self.pushButton_5 = QtWidgets.QPushButton(Bienes)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 310, 101, 71))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/departamento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(52, 52))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tblRegistro = QtWidgets.QTableWidget(Bienes)
        self.tblRegistro.setGeometry(QtCore.QRect(220, 70, 256, 201))
        self.tblRegistro.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblRegistro.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblRegistro.setObjectName("tblRegistro")
        self.tblRegistro.setColumnCount(0)
        self.tblRegistro.setRowCount(0)

        self.retranslateUi(Bienes)
        QtCore.QMetaObject.connectSlotsByName(Bienes)

    def retranslateUi(self, Bienes):
        _translate = QtCore.QCoreApplication.translate
        Bienes.setWindowTitle(_translate("Bienes", "Bienes"))
        self.label.setText(_translate("Bienes", "Registro de bienes"))
        self.lblPlaca.setText(_translate("Bienes", "Placa"))
        self.lblNombreBien.setText(_translate("Bienes", "Nombre del Bien"))
        self.lblCategoria.setText(_translate("Bienes", "Categoria"))
        self.lblDescripcion.setText(_translate("Bienes", "Descripción"))
        self.lblestado.setText(_translate("Bienes", "Estado:"))
        self.cbxEstado.setItemText(0, _translate("Bienes", "Asignable"))
        self.cbxEstado.setItemText(1, _translate("Bienes", "Reparacion"))
        self.cbxEstado.setItemText(2, _translate("Bienes", "Exclusion"))
