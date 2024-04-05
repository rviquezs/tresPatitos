# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Usuarios(object):
    def setupUi(self, Usuarios):
        Usuarios.setObjectName("Usuarios")
        Usuarios.resize(576, 469)
        Usuarios.setMinimumSize(QtCore.QSize(576, 469))
        Usuarios.setMaximumSize(QtCore.QSize(576, 469))
        self.label = QtWidgets.QLabel(Usuarios)
        self.label.setGeometry(QtCore.QRect(40, 0, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lblNombreUsuario = QtWidgets.QLabel(Usuarios)
        self.lblNombreUsuario.setGeometry(QtCore.QRect(30, 110, 111, 41))
        self.lblNombreUsuario.setObjectName("lblNombreUsuario")
        self.lblCedula = QtWidgets.QLabel(Usuarios)
        self.lblCedula.setGeometry(QtCore.QRect(30, 60, 91, 31))
        self.lblCedula.setObjectName("lblCedula")
        self.lblEmail = QtWidgets.QLabel(Usuarios)
        self.lblEmail.setGeometry(QtCore.QRect(30, 150, 91, 41))
        self.lblEmail.setObjectName("lblEmail")
        self.txtEmail = QtWidgets.QLineEdit(Usuarios)
        self.txtEmail.setGeometry(QtCore.QRect(160, 160, 113, 20))
        self.txtEmail.setText("")
        self.txtEmail.setObjectName("txtEmail")
        self.txtUsername = QtWidgets.QLineEdit(Usuarios)
        self.txtUsername.setGeometry(QtCore.QRect(160, 120, 113, 20))
        self.txtUsername.setText("")
        self.txtUsername.setObjectName("txtUsername")
        self.txtID = QtWidgets.QLineEdit(Usuarios)
        self.txtID.setGeometry(QtCore.QRect(160, 70, 113, 20))
        self.txtID.setText("")
        self.txtID.setObjectName("txtID")
        self.btnModificarUsuario = QtWidgets.QPushButton(Usuarios)
        self.btnModificarUsuario.setGeometry(QtCore.QRect(370, 430, 75, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificarUsuario.setIcon(icon)
        self.btnModificarUsuario.setObjectName("btnModificarUsuario")
        self.btnEliminarUsuario = QtWidgets.QPushButton(Usuarios)
        self.btnEliminarUsuario.setGeometry(QtCore.QRect(490, 430, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminarUsuario.setIcon(icon1)
        self.btnEliminarUsuario.setObjectName("btnEliminarUsuario")
        self.btnCrearUsuario = QtWidgets.QPushButton(Usuarios)
        self.btnCrearUsuario.setGeometry(QtCore.QRect(260, 430, 75, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCrearUsuario.setIcon(icon2)
        self.btnCrearUsuario.setObjectName("btnCrearUsuario")
        self.tblUsuarios = QtWidgets.QTableWidget(Usuarios)
        self.tblUsuarios.setGeometry(QtCore.QRect(20, 200, 541, 192))
        self.tblUsuarios.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblUsuarios.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblUsuarios.setObjectName("tblUsuarios")
        self.tblUsuarios.setColumnCount(3)
        self.tblUsuarios.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblUsuarios.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblUsuarios.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblUsuarios.setHorizontalHeaderItem(2, item)
        self.btnLimpiar = QtWidgets.QPushButton(Usuarios)
        self.btnLimpiar.setGeometry(QtCore.QRect(20, 430, 75, 23))
        self.btnLimpiar.setObjectName("btnLimpiar")

        self.retranslateUi(Usuarios)
        QtCore.QMetaObject.connectSlotsByName(Usuarios)

    def retranslateUi(self, Usuarios):
        _translate = QtCore.QCoreApplication.translate
        Usuarios.setWindowTitle(_translate("Usuarios", "Creacion de Usuarios"))
        self.label.setText(_translate("Usuarios", "Creacion De Usuarios"))
        self.lblNombreUsuario.setText(_translate("Usuarios", "Nombre de Usuario:"))
        self.lblCedula.setText(_translate("Usuarios", "ID:"))
        self.lblEmail.setText(_translate("Usuarios", "Email:"))
        self.btnModificarUsuario.setText(_translate("Usuarios", "Modificar"))
        self.btnEliminarUsuario.setText(_translate("Usuarios", "Eliminar"))
        self.btnCrearUsuario.setText(_translate("Usuarios", "Crear"))
        item = self.tblUsuarios.horizontalHeaderItem(0)
        item.setText(_translate("Usuarios", "ID"))
        item = self.tblUsuarios.horizontalHeaderItem(1)
        item.setText(_translate("Usuarios", "Usuario"))
        item = self.tblUsuarios.horizontalHeaderItem(2)
        item.setText(_translate("Usuarios", "Email"))
        self.btnLimpiar.setText(_translate("Usuarios", "Limpiar"))
