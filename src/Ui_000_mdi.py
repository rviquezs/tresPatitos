# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\aaron\OneDrive\Documentos\Python\tresPatitosUIA\src\000_mdi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mdiWindow(object):
    def setupUi(self, mdiWindow):
        mdiWindow.setObjectName("mdiWindow")
        mdiWindow.resize(666, 471)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mdiWindow.sizePolicy().hasHeightForWidth())
        mdiWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconMDI.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mdiWindow.setWindowIcon(icon)
        mdiWindow.setIconSize(QtCore.QSize(34, 34))
        mdiWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mdiWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setEnabled(True)
        self.mdiArea.setGeometry(QtCore.QRect(0, 0, 671, 451))
        self.mdiArea.setMouseTracking(False)
        self.mdiArea.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.mdiArea.setAcceptDrops(True)
        self.mdiArea.setAutoFillBackground(False)
        self.mdiArea.setStyleSheet("")
        self.mdiArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mdiArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.mdiArea.setViewMode(QtWidgets.QMdiArea.SubWindowView)
        self.mdiArea.setObjectName("mdiArea")
        mdiWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mdiWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 22))
        self.menubar.setStyleSheet("background-color:rgb(85, 193, 250);")
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setFocusPolicy(QtCore.Qt.TabFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconMenu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuMain.setIcon(icon1)
        self.menuMain.setObjectName("menuMain")
        self.menuBienes = QtWidgets.QMenu(self.menuMain)
        self.menuBienes.setGeometry(QtCore.QRect(977, 228, 175, 137))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menuBienes.setFont(font)
        self.menuBienes.setFocusPolicy(QtCore.Qt.TabFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/icons8-assets-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBienes.setIcon(icon2)
        self.menuBienes.setObjectName("menuBienes")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setTearOffEnabled(False)
        self.menuHelp.setTitle("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconHelp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuHelp.setIcon(icon3)
        self.menuHelp.setObjectName("menuHelp")
        mdiWindow.setMenuBar(self.menubar)
        self.mniUsuarios = QtWidgets.QAction(mdiWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconMenuUsers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mniUsuarios.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mniUsuarios.setFont(font)
        self.mniUsuarios.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.mniUsuarios.setObjectName("mniUsuarios")
        self.mniEmpleados = QtWidgets.QAction(mdiWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/IconMenuEmpleados.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mniEmpleados.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mniEmpleados.setFont(font)
        self.mniEmpleados.setObjectName("mniEmpleados")
        self.mniDepartamentos = QtWidgets.QAction(mdiWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconMenuDepartamentos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mniDepartamentos.setIcon(icon6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mniDepartamentos.setFont(font)
        self.mniDepartamentos.setObjectName("mniDepartamentos")
        self.mniAsignar = QtWidgets.QAction(mdiWindow)
        self.mniAsignar.setObjectName("mniAsignar")
        self.mniDesligar = QtWidgets.QAction(mdiWindow)
        self.mniDesligar.setObjectName("mniDesligar")
        self.btn_logout = QtWidgets.QAction(mdiWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconLogout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_logout.setIcon(icon7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_logout.setFont(font)
        self.btn_logout.setObjectName("btn_logout")
        self.mniRegistrarBienes = QtWidgets.QAction(mdiWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconMenuRegistrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mniRegistrarBienes.setIcon(icon8)
        self.mniRegistrarBienes.setObjectName("mniRegistrarBienes")
        self.mnuAsignar = QtWidgets.QAction(mdiWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconAsignar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mnuAsignar.setIcon(icon9)
        self.mnuAsignar.setObjectName("mnuAsignar")
        self.mnuDesligar = QtWidgets.QAction(mdiWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconDesligar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mnuDesligar.setIcon(icon10)
        self.mnuDesligar.setObjectName("mnuDesligar")
        self.mniReportes = QtWidgets.QAction(mdiWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/iconMenuReportes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mniReportes.setIcon(icon11)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mniReportes.setFont(font)
        self.mniReportes.setObjectName("mniReportes")
        self.menuBienes.addAction(self.mniRegistrarBienes)
        self.menuBienes.addAction(self.mnuAsignar)
        self.menuBienes.addAction(self.mnuDesligar)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.mniUsuarios)
        self.menuMain.addAction(self.mniEmpleados)
        self.menuMain.addAction(self.mniDepartamentos)
        self.menuMain.addAction(self.menuBienes.menuAction())
        self.menuMain.addAction(self.mniReportes)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.btn_logout)
        self.menuMain.addSeparator()
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mdiWindow)
        QtCore.QMetaObject.connectSlotsByName(mdiWindow)

    def retranslateUi(self, mdiWindow):
        _translate = QtCore.QCoreApplication.translate
        mdiWindow.setWindowTitle(_translate("mdiWindow", "Tres Patitos S.A"))
        self.menuMain.setTitle(_translate("mdiWindow", "Login"))
        self.menuBienes.setTitle(_translate("mdiWindow", "Bienes"))
        self.mniUsuarios.setText(_translate("mdiWindow", "Usuarios"))
        self.mniEmpleados.setText(_translate("mdiWindow", "Empleados"))
        self.mniDepartamentos.setText(_translate("mdiWindow", "Departamentos"))
        self.mniAsignar.setText(_translate("mdiWindow", "Asignar"))
        self.mniDesligar.setText(_translate("mdiWindow", "Desligar"))
        self.btn_logout.setText(_translate("mdiWindow", "Log out"))
        self.mniRegistrarBienes.setText(_translate("mdiWindow", "Registrar"))
        self.mnuAsignar.setText(_translate("mdiWindow", "Asignar"))
        self.mnuDesligar.setText(_translate("mdiWindow", "Desligar"))
        self.mniReportes.setText(_translate("mdiWindow", "Reportes"))
