# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\blite\2023_poo2\MapaNovo\pasta_ui\tela_dados_meteo.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_dados_meteoro(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 590)
        MainWindow.setStyleSheet("background-color: rgb(101, 255, 111);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(155, 22, 271, 42))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(60, 60, 60);\n"
"border-radius:15px;\n"
"")
        self.label.setObjectName("label")
        self.lineEdit_cidade = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cidade.setGeometry(QtCore.QRect(110, 170, 451, 51))
        self.lineEdit_cidade.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_cidade.setText("")
        self.lineEdit_cidade.setObjectName("lineEdit_cidade")
        self.lineEdit_endere = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_endere.setGeometry(QtCore.QRect(110, 230, 451, 51))
        self.lineEdit_endere.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_endere.setText("")
        self.lineEdit_endere.setObjectName("lineEdit_endere")
        self.pushButton_busc_dados = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_busc_dados.setGeometry(QtCore.QRect(250, 300, 99, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_busc_dados.setFont(font)
        self.pushButton_busc_dados.setStyleSheet("")
        self.pushButton_busc_dados.setObjectName("pushButton_busc_dados")
        self.pushButton_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_voltar.setGeometry(QtCore.QRect(460, 540, 84, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_voltar.setFont(font)
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.lineEdit_tempe = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tempe.setGeometry(QtCore.QRect(140, 400, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_tempe.setFont(font)
        self.lineEdit_tempe.setStyleSheet("    background-color: rgb(230, 230, 230);\n"
"    border: 2px solid rgb(219, 236, 255);\n"
"    border-radius: 5px;\n"
"\n"
"")
        self.lineEdit_tempe.setText("")
        self.lineEdit_tempe.setPlaceholderText("")
        self.lineEdit_tempe.setObjectName("lineEdit_tempe")
        self.label_lon_B = QtWidgets.QLabel(self.centralwidget)
        self.label_lon_B.setGeometry(QtCore.QRect(21, 239, 70, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_lon_B.setFont(font)
        self.label_lon_B.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.label_lon_B.setObjectName("label_lon_B")
        self.label_lat_B = QtWidgets.QLabel(self.centralwidget)
        self.label_lat_B.setGeometry(QtCore.QRect(35, 180, 70, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_lat_B.setFont(font)
        self.label_lat_B.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.label_lat_B.setObjectName("label_lat_B")
        self.label_resul = QtWidgets.QLabel(self.centralwidget)
        self.label_resul.setGeometry(QtCore.QRect(30, 410, 94, 23))
        self.label_resul.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_resul.setFont(font)
        self.label_resul.setStyleSheet("color: rgb(255, 255, 255)\n"
"")
        self.label_resul.setObjectName("label_resul")
        self.label_lat = QtWidgets.QLabel(self.centralwidget)
        self.label_lat.setGeometry(QtCore.QRect(68, 90, 44, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_lat.setFont(font)
        self.label_lat.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.label_lat.setObjectName("label_lat")
        self.lineEdit_lat = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_lat.setGeometry(QtCore.QRect(118, 90, 113, 20))
        self.lineEdit_lat.setStyleSheet("    background-color: rgb(250, 250, 250);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"\n"
"")
        self.lineEdit_lat.setObjectName("lineEdit_lat")
        self.lineEdit_lon = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_lon.setGeometry(QtCore.QRect(118, 120, 113, 20))
        self.lineEdit_lon.setStyleSheet("    background-color: rgb(250, 250, 250);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"\n"
"")
        self.lineEdit_lon.setObjectName("lineEdit_lon")
        self.label_lon = QtWidgets.QLabel(self.centralwidget)
        self.label_lon.setGeometry(QtCore.QRect(58, 120, 57, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_lon.setFont(font)
        self.label_lon.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.label_lon.setObjectName("label_lon")
        self.label_resul_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_resul_2.setGeometry(QtCore.QRect(57, 530, 59, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_resul_2.setFont(font)
        self.label_resul_2.setStyleSheet("color: rgb(255, 255, 255)\n"
"")
        self.label_resul_2.setObjectName("label_resul_2")
        self.label_resul_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_resul_3.setGeometry(QtCore.QRect(52, 465, 68, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_resul_3.setFont(font)
        self.label_resul_3.setStyleSheet("color: rgb(255, 255, 255)\n"
"")
        self.label_resul_3.setObjectName("label_resul_3")
        self.lineEdit_umidad = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_umidad.setGeometry(QtCore.QRect(140, 460, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_umidad.setFont(font)
        self.lineEdit_umidad.setStyleSheet("    background-color: rgb(230, 230, 230);\n"
"    border: 2px solid rgb(219, 236, 255);\n"
"    border-radius: 5px;\n"
"\n"
"")
        self.lineEdit_umidad.setText("")
        self.lineEdit_umidad.setPlaceholderText("")
        self.lineEdit_umidad.setObjectName("lineEdit_umidad")
        self.lineEdit_pressao = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pressao.setGeometry(QtCore.QRect(140, 520, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_pressao.setFont(font)
        self.lineEdit_pressao.setStyleSheet("    background-color: rgb(230, 230, 230);\n"
"    border: 2px solid rgb(219, 236, 255);\n"
"    border-radius: 5px;\n"
"\n"
"")
        self.lineEdit_pressao.setText("")
        self.lineEdit_pressao.setPlaceholderText("")
        self.lineEdit_pressao.setObjectName("lineEdit_pressao")
        self.label_resul_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_resul_4.setGeometry(QtCore.QRect(204, 366, 202, 25))
        self.label_resul_4.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_resul_4.setFont(font)
        self.label_resul_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_resul_4.setObjectName("label_resul_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 350, 602, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Dados Meteorológicos</span></p></body></html>"))
        self.lineEdit_cidade.setPlaceholderText(_translate("MainWindow", "     ex: São Paulo"))
        self.lineEdit_endere.setPlaceholderText(_translate("MainWindow", "     ex: São Paulo, Brasil"))
        self.pushButton_busc_dados.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_voltar.setText(_translate("MainWindow", "Voltar"))
        self.label_lon_B.setText(_translate("MainWindow", "<html><head/><body><p>Endereço</p></body></html>"))
        self.label_lat_B.setText(_translate("MainWindow", "<html><head/><body><p>Cidade</p><p><br/></p></body></html>"))
        self.label_resul.setText(_translate("MainWindow", "<html><head/><body><p>Temperatura</p><p><br/></p></body></html>"))
        self.label_lat.setText(_translate("MainWindow", "Latitude"))
        self.label_lon.setText(_translate("MainWindow", "Longitude"))
        self.label_resul_2.setText(_translate("MainWindow", "<html><head/><body><p>Pressão</p><p><br/></p></body></html>"))
        self.label_resul_3.setText(_translate("MainWindow", "<html><head/><body><p>Umidade</p></body></html>"))
        self.label_resul_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Dados Meterologicos:</span></p><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_dados_meteoro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())