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
        Usuarios.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconUsuarios.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Usuarios.setWindowIcon(icon)
        Usuarios.setAutoFillBackground(True)
        Usuarios.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.label = QtWidgets.QLabel(Usuarios)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(30, 10, 241, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.tblUsuarios = QtWidgets.QTableWidget(Usuarios)
        self.tblUsuarios.setGeometry(QtCore.QRect(20, 210, 541, 192))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tblUsuarios.setFont(font)
        self.tblUsuarios.setStyleSheet("background-color: rgb(255, 255, 255);")
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
        self.btnLimpiar.setGeometry(QtCore.QRect(20, 170, 75, 25))
        self.btnLimpiar.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:10px;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border:2px solid #55C1FA;\n"
"border-radius:10px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconClear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpiar.setIcon(icon1)
        self.btnLimpiar.setIconSize(QtCore.QSize(18, 18))
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.verticalLayoutWidget = QtWidgets.QWidget(Usuarios)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 60, 56, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.lblLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.lblLayout.setContentsMargins(0, 0, 0, 0)
        self.lblLayout.setSpacing(15)
        self.lblLayout.setObjectName("lblLayout")
        self.lblCedula = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.lblCedula.setFont(font)
        self.lblCedula.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";")
        self.lblCedula.setTextFormat(QtCore.Qt.RichText)
        self.lblCedula.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblCedula.setObjectName("lblCedula")
        self.lblLayout.addWidget(self.lblCedula)
        self.lblNombreUsuario = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblNombreUsuario.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";")
        self.lblNombreUsuario.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblNombreUsuario.setObjectName("lblNombreUsuario")
        self.lblLayout.addWidget(self.lblNombreUsuario)
        self.lblEmail = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblEmail.setStyleSheet("font: 63 10pt \"Segoe UI Semibold\";")
        self.lblEmail.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblEmail.setObjectName("lblEmail")
        self.lblLayout.addWidget(self.lblEmail)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Usuarios)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(90, 60, 213, 94))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.txtLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.txtLayout.setContentsMargins(0, 0, 0, 0)
        self.txtLayout.setSpacing(8)
        self.txtLayout.setObjectName("txtLayout")
        self.txtID = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.txtID.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtID.setText("")
        self.txtID.setObjectName("txtID")
        self.txtLayout.addWidget(self.txtID)
        self.txtUsername = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.txtUsername.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtUsername.setText("")
        self.txtUsername.setObjectName("txtUsername")
        self.txtLayout.addWidget(self.txtUsername)
        self.txtEmail = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.txtEmail.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtEmail.setText("")
        self.txtEmail.setObjectName("txtEmail")
        self.txtLayout.addWidget(self.txtEmail)
        self.splitter = QtWidgets.QSplitter(Usuarios)
        self.splitter.setEnabled(True)
        self.splitter.setGeometry(QtCore.QRect(280, 420, 281, 31))
        self.splitter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.btnCrearUsuario = QtWidgets.QPushButton(self.splitter)
        self.btnCrearUsuario.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:10px;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border:2px solid #55C1FA;\n"
"border-radius:10px;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconCrear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCrearUsuario.setIcon(icon2)
        self.btnCrearUsuario.setIconSize(QtCore.QSize(20, 20))
        self.btnCrearUsuario.setObjectName("btnCrearUsuario")
        self.btnModificarUsuario = QtWidgets.QPushButton(self.splitter)
        self.btnModificarUsuario.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:10px;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border:2px solid #55C1FA;\n"
"border-radius:10px;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconEdit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificarUsuario.setIcon(icon3)
        self.btnModificarUsuario.setObjectName("btnModificarUsuario")
        self.btnEliminarUsuario = QtWidgets.QPushButton(self.splitter)
        self.btnEliminarUsuario.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:10px;\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border:2px solid #55C1FA;\n"
"border-radius:10px;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\rviqu\\OneDrive - Universidad Internacional de las Américas (UIA)\\UIA\\2024\\I\\Programación II\\Proyecto Final\\tresPatitosUIA\\src\\../res/iconDelete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminarUsuario.setIcon(icon4)
        self.btnEliminarUsuario.setIconSize(QtCore.QSize(18, 18))
        self.btnEliminarUsuario.setObjectName("btnEliminarUsuario")

        self.retranslateUi(Usuarios)
        QtCore.QMetaObject.connectSlotsByName(Usuarios)

    def retranslateUi(self, Usuarios):
        _translate = QtCore.QCoreApplication.translate
        Usuarios.setWindowTitle(_translate("Usuarios", "Creacion de Usuarios"))
        self.label.setText(_translate("Usuarios", "Creacion De Usuarios"))
        item = self.tblUsuarios.horizontalHeaderItem(0)
        item.setText(_translate("Usuarios", "ID"))
        item = self.tblUsuarios.horizontalHeaderItem(1)
        item.setText(_translate("Usuarios", "Usuario"))
        item = self.tblUsuarios.horizontalHeaderItem(2)
        item.setText(_translate("Usuarios", "Email"))
        self.btnLimpiar.setText(_translate("Usuarios", "Limpiar"))
        self.lblCedula.setText(_translate("Usuarios", "ID  "))
        self.lblNombreUsuario.setText(_translate("Usuarios", "Usuario "))
        self.lblEmail.setText(_translate("Usuarios", "Email "))
        self.btnCrearUsuario.setText(_translate("Usuarios", "Crear"))
        self.btnModificarUsuario.setText(_translate("Usuarios", "Modificar"))
        self.btnEliminarUsuario.setText(_translate("Usuarios", "Eliminar"))
