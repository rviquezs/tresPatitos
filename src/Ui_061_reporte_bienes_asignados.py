# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\aaron\OneDrive\Documentos\Python\tresPatitosUIA\src\061_reporte_bienes_asignados.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReporteBienesAsignados(object):
    def setupUi(self, ReporteBienesAsignados):
        ReporteBienesAsignados.setObjectName("ReporteBienesAsignados")
        ReporteBienesAsignados.resize(700, 400)
        ReporteBienesAsignados.setMinimumSize(QtCore.QSize(700, 400))
        self.lblTitulo = QtWidgets.QLabel(ReporteBienesAsignados)
        self.lblTitulo.setGeometry(QtCore.QRect(190, 20, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setStyleSheet("\n"
"background-color: rgb(157, 157, 118);")
        self.lblTitulo.setObjectName("lblTitulo")
        self.lblEmpleado = QtWidgets.QLabel(ReporteBienesAsignados)
        self.lblEmpleado.setGeometry(QtCore.QRect(50, 110, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblEmpleado.setFont(font)
        self.lblEmpleado.setObjectName("lblEmpleado")
        self.cbxSeleccionEmpleado = QtWidgets.QComboBox(ReporteBienesAsignados)
        self.cbxSeleccionEmpleado.setGeometry(QtCore.QRect(50, 140, 151, 22))
        self.cbxSeleccionEmpleado.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbxSeleccionEmpleado.setObjectName("cbxSeleccionEmpleado")
        self.tblReporteBienesAsignados = QtWidgets.QTableWidget(ReporteBienesAsignados)
        self.tblReporteBienesAsignados.setGeometry(QtCore.QRect(50, 180, 421, 121))
        self.tblReporteBienesAsignados.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.tblReporteBienesAsignados.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblReporteBienesAsignados.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblReporteBienesAsignados.setShowGrid(True)
        self.tblReporteBienesAsignados.setObjectName("tblReporteBienesAsignados")
        self.tblReporteBienesAsignados.setColumnCount(4)
        self.tblReporteBienesAsignados.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tblReporteBienesAsignados.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReporteBienesAsignados.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReporteBienesAsignados.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReporteBienesAsignados.setHorizontalHeaderItem(3, item)
        self.btnLimpiar = QtWidgets.QPushButton(ReporteBienesAsignados)
        self.btnLimpiar.setGeometry(QtCore.QRect(230, 140, 81, 21))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\aaron\\OneDrive\\Documentos\\Python\\tresPatitosUIA\\src\\../res/btnClear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpiar.setIcon(icon)
        self.btnLimpiar.setIconSize(QtCore.QSize(20, 20))
        self.btnLimpiar.setObjectName("btnLimpiar")

        self.retranslateUi(ReporteBienesAsignados)
        QtCore.QMetaObject.connectSlotsByName(ReporteBienesAsignados)

    def retranslateUi(self, ReporteBienesAsignados):
        _translate = QtCore.QCoreApplication.translate
        ReporteBienesAsignados.setWindowTitle(_translate("ReporteBienesAsignados", "Reporte_Bienes_Asignados"))
        self.lblTitulo.setText(_translate("ReporteBienesAsignados", "Reporte Bienes Asignados por empleado"))
        self.lblEmpleado.setText(_translate("ReporteBienesAsignados", "Seleccione el empleado:"))
        self.tblReporteBienesAsignados.setSortingEnabled(False)
        item = self.tblReporteBienesAsignados.horizontalHeaderItem(0)
        item.setText(_translate("ReporteBienesAsignados", "Cédula"))
        item = self.tblReporteBienesAsignados.horizontalHeaderItem(1)
        item.setText(_translate("ReporteBienesAsignados", "Nombre"))
        item = self.tblReporteBienesAsignados.horizontalHeaderItem(2)
        item.setText(_translate("ReporteBienesAsignados", "Teléfono"))
        item = self.tblReporteBienesAsignados.horizontalHeaderItem(3)
        item.setText(_translate("ReporteBienesAsignados", "Bien Asignado"))
        self.btnLimpiar.setToolTip(_translate("ReporteBienesAsignados", "CTRL+S"))
        self.btnLimpiar.setText(_translate("ReporteBienesAsignados", "Limpiar"))
        self.btnLimpiar.setShortcut(_translate("ReporteBienesAsignados", "Ctrl+C"))
