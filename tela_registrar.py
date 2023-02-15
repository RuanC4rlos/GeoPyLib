from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Registrar(object):
    
    '''
     Classe Tela_Registrar vai representar nossa opção de registrar o cliente, tendo parâmetro o objeto
                ...

     Logo após vai determinar proporções da tela usando parâmetros do Qt como: cor e tamanho da janela
    '''

    def setupUi(self, MainWindow):

        '''
        Configurando os parâmetros da nossa janela princial a nossa tela da opção registrar
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
        self.register_area = QtWidgets.QFrame(self.content)
        self.register_area.setEnabled(True)
        self.register_area.setMinimumSize(QtCore.QSize(600, 600))
        self.register_area.setMaximumSize(QtCore.QSize(450, 550))
        self.register_area.setStyleSheet("border-radius: 10px;")
        self.register_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.register_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.register_area.setObjectName("register_area")
        self.pushButton_registrar = QtWidgets.QPushButton(self.register_area)
        self.pushButton_registrar.setGeometry(QtCore.QRect(170, 450, 280, 50))
        self.pushButton_registrar.setStyleSheet("QPushButton {    \n"
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
        self.pushButton_registrar.setObjectName("pushButton_registrar")
        self.label = QtWidgets.QLabel(self.register_area)
        self.label.setGeometry(QtCore.QRect(230, 40, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);")
        self.label.setObjectName("label")
        self.lineEdit_nome = QtWidgets.QLineEdit(self.register_area)
        self.lineEdit_nome.setGeometry(QtCore.QRect(170, 170, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_nome.setFont(font)
        self.lineEdit_nome.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(255, 265, 24);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_nome.setMaxLength(32)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.lineEdit_cpf = QtWidgets.QLineEdit(self.register_area)
        self.lineEdit_cpf.setGeometry(QtCore.QRect(170, 230, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_cpf.setFont(font)
        self.lineEdit_cpf.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(255, 165, 24);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_cpf.setMaxLength(32)
        self.lineEdit_cpf.setObjectName("lineEdit_cpf")

        self.lineEdit_nascimento = QtWidgets.QLineEdit(self.register_area)
        self.lineEdit_nascimento.setGeometry(QtCore.QRect(170, 290, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_nascimento.setFont(font)
        self.lineEdit_nascimento.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(255,165,24);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_nascimento.setMaxLength(32)
        self.lineEdit_nascimento.setObjectName("lineEdit_nascimento")
        self.lineEdit_password = QtWidgets.QLineEdit(self.register_area)
        self.lineEdit_password.setGeometry(QtCore.QRect(170, 350, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(255,165,24);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_password.setMaxLength(32)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout.addWidget(self.register_area)
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
        self.pushButton_sair = QtWidgets.QPushButton(self.top_bar)
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
        self.horizontalLayout_2.addWidget(self.pushButton_sair)
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
        sendo nossa janela principal da nossa opção de mostrar a tela registrar
        logo após é inserido os labels na tela junto com os pushbotons
        cada um mostrando sua função.        

        '''

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Regitrar"))
        self.pushButton_registrar.setText(_translate("MainWindow", "REGISTRAR"))
        self.label.setText(_translate("MainWindow", "REGISTRAR"))
        self.lineEdit_nome.setPlaceholderText(_translate("MainWindow", "NOME"))
        self.lineEdit_cpf.setPlaceholderText(_translate("MainWindow", "CPF"))
        self.lineEdit_nascimento.setPlaceholderText(_translate("MainWindow", "NASCIMENTO"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.pushButton_sair.setText(_translate("MainWindow", "VOLTAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Registrar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
