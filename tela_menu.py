from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Menu(object):

    '''
     Classe Tela_Menu vai representar nossa opção de mostrar o menu, tendo parâmetro um objeto
                ...

     Logo após vai determinar proporções da tela usando parâmetros do Qt como: cor e tamanho da janela
    '''

    def setupUi(self, MainWindow):

        '''
        Configurando os parâmetros da nossa janela princial a nossa tela da opção menu
                ...

        Cor da tela, tamanho da tela, tipo de fonte e icone presente na tela        
        '''

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 680)
        MainWindow.setMinimumSize(QtCore.QSize(650, 650))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Images/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(200, 200, 200);\n"
"background-color: rgb(10, 10, 10);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setMaximumSize(QtCore.QSize(450, 550))
        self.login_area.setStyleSheet("border-radius: 10px;")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.pushButton_extrato = QtWidgets.QPushButton(self.login_area)
        self.pushButton_extrato.setGeometry(QtCore.QRect(80, 390, 280, 50))
        self.pushButton_extrato.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(255, 165, 24);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_extrato.setObjectName("pushButton_extrato")
        self.label = QtWidgets.QLabel(self.login_area)
        self.label.setGeometry(QtCore.QRect(170, 0, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);")
        self.label.setObjectName("label")
        self.pushButton_transferir = QtWidgets.QPushButton(self.login_area)
        self.pushButton_transferir.setGeometry(QtCore.QRect(80, 330, 280, 50))
        self.pushButton_transferir.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(255, 165, 24);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_transferir.setObjectName("pushButton_transferir")
        self.pushButton_sacar = QtWidgets.QPushButton(self.login_area)
        self.pushButton_sacar.setGeometry(QtCore.QRect(80, 270, 280, 50))
        self.pushButton_sacar.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(255, 165, 24);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_sacar.setObjectName("pushButton_sacar")
        self.pushButton_depositar = QtWidgets.QPushButton(self.login_area)
        self.pushButton_depositar.setGeometry(QtCore.QRect(80, 210, 280, 50))
        self.pushButton_depositar.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(255, 165, 24);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_depositar.setObjectName("pushButton_depositar")
        self.pushButton_sair = QtWidgets.QPushButton(self.login_area)
        self.pushButton_sair.setGeometry(QtCore.QRect(369, 460, 71, 31))
        self.pushButton_sair.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_sair.setObjectName("pushButton_sair")
        self.lineEdit_cliente = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_cliente.setGeometry(QtCore.QRect(60, 100, 113, 20))
        self.lineEdit_cliente.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_cliente.setObjectName("lineEdit_cliente")
        self.label_cliente = QtWidgets.QLabel(self.login_area)
        self.label_cliente.setGeometry(QtCore.QRect(10, 100, 47, 13))
        self.label_cliente.setObjectName("label_cliente")
        #
        self.lineEdit_saldo = QtWidgets.QLineEdit( self.login_area )
        self.lineEdit_saldo.setGeometry( QtCore.QRect( 320, 95, 100, 30 ) )
        font = QtGui.QFont()
        font.setPointSize( 15 )
        self.lineEdit_saldo.setFont( font )

        self.lineEdit_saldo.setStyleSheet( "QLineEdit {\n"
                                             "    border: 2px solid rgb(45, 45, 45);\n"
                                             "    border-radius: 5px;\n"
                                             #"    padding: 35px;\n"
                                             "    background-color: rgb(30, 30, 30);    \n"
                                             "    color: rgb(100, 100, 100);\n"
                                             "}\n""}" )
        self.lineEdit_saldo.setObjectName( "lineEdit_saldo" )

        self.label_saldo = QtWidgets.QLabel( self.login_area )
        self.label_saldo.setGeometry( QtCore.QRect( 250, 100, 60, 16 ) )
        font = QtGui.QFont()
        font.setPointSize( 15 )
        self.label_saldo.setFont( font )
        self.label_saldo.setObjectName( "label_saldo" )

        #
        self.label_5 = QtWidgets.QLabel(self.login_area)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 47, 13))
        self.label_5.setObjectName("label_5")
        self.lineEdit_numero = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_numero.setGeometry(QtCore.QRect(60, 130, 113, 20))
        self.lineEdit_numero.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_numero.setObjectName("lineEdit_numero")
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.content)
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_bar.setStyleSheet("")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addWidget(self.top_bar)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom.setStyleSheet("background-color: rgb(15, 15, 15)")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addWidget(self.bottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        '''
        Reconfigurando a tela
                ...

        Componentes necessários para renderizar o layout do aplicativo
        sendo nossa janela principal da nossa opção de mostrar a tela menu
        logo após é inserido os labels na tela junto com os pushbotons
        cada um mostrando sua função.        
        '''

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu"))
        self.pushButton_extrato.setText(_translate("MainWindow", "EXTRATO"))
        self.label.setText(_translate("MainWindow", "MENU"))
        self.pushButton_transferir.setText(_translate("MainWindow", "TRANSFERIR"))
        self.pushButton_sacar.setText(_translate("MainWindow", "SACAR"))
        self.pushButton_depositar.setText(_translate("MainWindow", "DEPOSITAR"))
        self.pushButton_sair.setText(_translate("MainWindow", "SAIR"))
        self.label_cliente.setText(_translate("MainWindow", "CLIENTE"))
        self.label_5.setText(_translate("MainWindow", "NUMERO"))
        self.label_saldo.setText( _translate( "MainWindow", "SALDO" ) )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Menu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())