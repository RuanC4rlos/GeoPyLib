import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from telas.tela_menu import Tela_Menu
from telas.tela_registrar import Tela_Registrar
from telas.tela_sacar import Tela_Sacar
from telas.tela_extrato import Tela_Extrato
from telas.tela_depositar import Tela_Depositar
from telas.tela_transferir import Tela_Transferir
from telas.tela_login import Tela_Login

from cliente import Conectar

import socket

class UiMain( QtWidgets.QWidget ):

    def setupUi(self, Main):
        Main.setObjectName( 'Main' )
        Main.resize( 640, 480 )

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()

        self.tela_login = Tela_Login()
        self.tela_login.setupUi( (self.stack0) )

        self.tela_registrar = Tela_Registrar()
        self.tela_registrar.setupUi( (self.stack1) )

        self.tela_menu = Tela_Menu()
        self.tela_menu.setupUi( (self.stack2) )

        self.tela_sacar = Tela_Sacar()
        self.tela_sacar.setupUi( (self.stack3) )

        self.tela_depositar = Tela_Depositar()
        self.tela_depositar.setupUi( (self.stack4) )

        self.tela_transferir = Tela_Transferir()
        self.tela_transferir.setupUi( (self.stack5) )

        self.tela_extrato = Tela_Extrato()
        self.tela_extrato.setupUi( (self.stack6) )

        self.QtStack.addWidget( self.stack0 )
        self.QtStack.addWidget( self.stack1 )
        self.QtStack.addWidget( self.stack2 )
        self.QtStack.addWidget( self.stack3 )
        self.QtStack.addWidget( self.stack4 )
        self.QtStack.addWidget( self.stack5 )
        self.QtStack.addWidget( self.stack6 )


class Main( QMainWindow, UiMain ):
    def __init__(self, parent=None):
        super( Main, self ).__init__( parent )
        self.setupUi( self )
        nm = ''
        self.conectar_servidor = Conectar()

        self.tela_login.pushButton_login.clicked.connect( self.botaoLogin )
        self.tela_login.pushButton_register.clicked.connect( self.TelaRegister )
        self.tela_login.pushButton_sair.clicked.connect(self.TelaFechar)
        self.tela_registrar.pushButton_registrar.clicked.connect( self.botaoRegister )
        self.tela_registrar.pushButton_sair.clicked.connect( self.botaoVoltar )

        self.tela_menu.pushButton_depositar.clicked.connect( self.TelaDepositar )
        self.tela_menu.pushButton_sacar.clicked.connect( self.TelaSacar )
        self.tela_menu.pushButton_transferir.clicked.connect( self.TelaTransferir )
        self.tela_menu.pushButton_extrato.clicked.connect( self.TelaExtrato)
        self.tela_menu.pushButton_sair.clicked.connect( self.TelaSair )

        self.tela_sacar.pushButton_transferir.clicked.connect( self.botaoSacar )
        self.tela_sacar.pushButton_sair.clicked.connect( self.TelaVoltar)

        self.tela_depositar.pushButton_Depositar.clicked.connect( self.botaoDepositar )
        self.tela_depositar.pushButton_sair.clicked.connect(self.TelaVoltar)

        self.tela_transferir.pushButton_transferir.clicked.connect( self.botaoTransferir )
        self.tela_transferir.pushButton_sair.clicked.connect( self.TelaVoltar)

        self.tela_extrato.pushButton_sair.clicked.connect( self.TelaVoltar)

    def concatenar_operacao(self, operacao):
        """
        Concatena os elementos separando por virgulas
        :param operacao: str
            id da requisicao, componenetes necessarios(nome,senha,etc)
        :return:
            operacao modificada
        """
        trasacao = ''

        for i in operacao:
            trasacao += str( i ) + ','

        return trasacao

    def botaoLogin(self):
        """
        Verifica se o cliente esta cadastrado no banco de dados
        Funcao principal para entrar na aplicação
        :return:
            None
        """
        senha = self.tela_login.lineEdit_password.text()
        nome = self.tela_login.lineEdit_user.text()
        if nome != '' and senha != '':
            mensagem = self.conectar_servidor.envia(self.concatenar_operacao( ['2', nome,senha] ))
            if mensagem[0] == 'cadastrado':
                QMessageBox.information( None, 'Cadastro', 'Usuario Logado!' )
                self.tela_login.lineEdit_user.setText( '' )
                self.tela_login.lineEdit_password.setText( '' )
                global nm
                nm = nome
                self.TelaMenu(nome)
            elif mensagem[0] == 'naoacho':
                QMessageBox.information( None, 'Mensagem', 'Usuario ou senha incorretos!!' )
                self.tela_login.lineEdit_user.setText( '' )
                self.tela_login.lineEdit_password.setText( '' )

        else:
            QMessageBox.information( None, 'mensagem', 'Preencha todos os dados' )
            self.tela_login.lineEdit_user.setText( '' )
            self.tela_login.lineEdit_password.setText( '' )


    def botaoRegister(self):
        """
        Verifica se o cliente esta registrado no banco de dados
        Função cria novos usuarios
        :return: None
        """
        nome = self.tela_registrar.lineEdit_nome.text()
        cpf = self.tela_registrar.lineEdit_cpf.text()
        nascimento = self.tela_registrar.lineEdit_nascimento.text()
        senha = self.tela_registrar.lineEdit_password.text()

        if nome != '' and cpf != '' and nascimento != '' and senha != '':
            mensagem = self.conectar_servidor.envia(self.concatenar_operacao( ['1', nome, cpf, nascimento, senha] ) )
            if mensagem[0] =='cadastrado':
                QMessageBox.information( None, 'Cadastro', 'Usuario Cadastrado!')
            elif mensagem[0] == 'jacpf':
                QMessageBox.information( None, 'Mensagem', 'CPF Já Cadastrado!!')
            self.tela_registrar.lineEdit_nome.setText( '' )
            self.tela_registrar.lineEdit_cpf.setText( '' )
            self.tela_registrar.lineEdit_nascimento.setText( '' )
            self.tela_registrar.lineEdit_password.setText( '' )
        else:
            QMessageBox.information( None, 'mensagem', 'Preencha todos os dados' )
    def mostrar_conta(self,cliente):
        """
        Mostra informações no layout da aplicação
        :param cliente:
            nome do cliente
        :return:
            id de requisicao da operacao
        """
        mensagem = self.conectar_servidor.envia(self.concatenar_operacao( ['3', cliente] ))
        return mensagem[0]

    def AttSaldo(self,cliente):
        """
        Atualiza o saldo no layout da aplicação em varia telas
        :param cliente:
            nome do cliente
        :return:
            None
        """
        mensagem = self.conectar_servidor.envia(self.concatenar_operacao( ['5', cliente] ))
        saldo = mensagem[0]
        if saldo!='0.0':
            saldo=saldo+'.0'
        self.tela_menu.lineEdit_saldo.setText( saldo )
        self.tela_depositar.lineEdit_saldo.setText( saldo )
        self.tela_sacar.lineEdit_Versal.setText( saldo )
        self.tela_transferir.lineEdit_saldo.setText( saldo )

    def TelaMenu(self,cliente):
        """
        Tela menu com as informações e botoes da aplicação
        :param cliente:
            nome do cliente
        :return: None
        """
        self.QtStack.setCurrentIndex( 2 )
        numero = self.mostrar_conta(cliente)
        self.AttSaldo(cliente)
        self.tela_menu.lineEdit_cliente.setText(cliente)
        self.tela_menu.lineEdit_numero.setText(numero)

        self.tela_depositar.lineEdit_cliente.setText(cliente)
        self.tela_depositar.lineEdit_numero.setText(numero)

        self.tela_sacar.lineEdit_cliente.setText( cliente )
        self.tela_sacar.lineEdit_numero.setText( numero )

        self.tela_transferir.lineEdit_cliente.setText( cliente )
        self.tela_transferir.lineEdit_numero.setText( numero )

    def botaoVoltar(self):
        """
        Botao que volta para a tela login, limpando as lineEdit da tela registrar
        :return: None
        """
        self.tela_registrar.lineEdit_nome.setText( '' )
        self.tela_registrar.lineEdit_cpf.setText( '' )
        self.tela_registrar.lineEdit_nascimento.setText( '' )
        self.tela_registrar.lineEdit_password.setText( '' )
        self.QtStack.setCurrentIndex( 0 )

    def TelaRegister(self):
        """
        Chama a tela registrar
        """
        self.QtStack.setCurrentIndex( 1 )

    def TelaSair(self):
        """
            Chama a tela login
        """
        self.QtStack.setCurrentIndex( 0 )

    def TelaSacar(self):
        """
            Chama a tela sacar
        """
        self.QtStack.setCurrentIndex( 3 )

    def TelaDepositar(self):
        """
            Chama a tela depositar
        """
        self.QtStack.setCurrentIndex( 4 )

    def TelaTransferir(self):
        """
            Chama a tela transferir
        """
        self.QtStack.setCurrentIndex( 5 )


    def TelaExtrato(self):
        """
        Chama a tela extrato, conecta com o servidor e faz a requisição do extrato no banco de dados
        """
        self.QtStack.setCurrentIndex( 6 )
        global nm
        mensagem = self.conectar_servidor.envia(self.concatenar_operacao( ['6',nm] ))
        recebe = mensagem

        font = QtGui.QFont()
        font.setFamily( "Segoe UI" )
        font.setPointSize( 10 )
        self.tela_extrato.textBrowser.setFont( font )

        recebe='\n'.join(recebe) # quebra a linha de cada instrucao
        recebe = recebe.replace('[',' ') # remove parenteses
        recebe = recebe.replace( ']', '' ) # remove parenteses
        recebe = recebe.replace( "'", '' ) # remove aspas simples

        self.tela_extrato.textBrowser.setText(recebe)

    def TelaVoltar(self):
        """Retorna a tela menu"""
        cliente = self.tela_depositar.lineEdit_cliente.text()
        self.TelaMenu(cliente)

    def botaoSacar(self):
        """
        Faz uma requisicao para o servidor enviando o id e dados necessarios para realizar o saque do cliente
         Recebe uma confirmacao do servidor se deu certo ou nao
        """
        valor = self.tela_sacar.lineEdit_saldo.text()
        numero = self.tela_sacar.lineEdit_numero.text()
        cliente = self.tela_sacar.lineEdit_cliente.text()
        if valor != '':
            mensagem = self.conectar_servidor.envia(self.concatenar_operacao( ['7', numero, valor, cliente] ))
            recebe = mensagem[0]
            if recebe == 'sacado':
                QMessageBox.information( None, 'Mensagem', 'Sacado com sucesso!' )
                self.tela_sacar.lineEdit_saldo.setText( '' )
                self.AttSaldo( cliente )
            else:
                QMessageBox.information( None, 'Mensagem', 'Saldo Insuficiente!' )
        else:
            QMessageBox.information( None, 'mensagem', 'Digite um valor!' )


    def botaoDepositar(self):
        """
        Faz uma requisicao para o servidor enviando o id e dados necessarios para realizar o deposito na conta do cliente
        Recebe uma confirmacao do servidor se deu certo ou nao
        """
        valor = self.tela_depositar.lineEdit_valor.text()
        numero = self.tela_depositar.lineEdit_numero.text()
        cliente = self.tela_depositar.lineEdit_cliente.text()
        if valor != '':
            mensagem = self.conectar_servidor.envia(self.concatenar_operacao( ['4', numero, valor,cliente] ))
            recebe = mensagem[0]
            if recebe == 'depositado':
                QMessageBox.information( None, 'Mensagem', 'Depositado com sucesso!' )
                self.tela_depositar.lineEdit_valor.setText( '' )
                self.AttSaldo(cliente)
        else:
            QMessageBox.information( None, 'mensagem', 'Digite um valor!' )

    def botaoTransferir(self):
        """
        Faz uma requisicao para o servidor enviando o id e dados necessarios para realizar uma transferencia da conta do cliente
        Recebe uma mensagem do servidor se deu certo ou nao
        """
        valor = self.tela_transferir.lineEdit_transf_destino.text()
        numero = self.tela_transferir.lineEdit_numero_destino.text()
        cliente = self.tela_transferir.lineEdit_cliente.text()
        if valor != '':
            mensagem = self.conectar_servidor.envia(self.concatenar_operacao( ['8', numero, valor, cliente] ))
            recebe = mensagem[0]
            if recebe == 'transferido':
                QMessageBox.information( None, 'Mensagem', 'Transferido com sucesso!' )
                self.tela_transferir.lineEdit_saldo.setText( '' )
                self.AttSaldo( cliente )
            elif recebe == 'semsaldo':
                QMessageBox.information( None, 'Mensagem', 'Saldo Insuficiente!' )
                self.tela_transferir.lineEdit_numero_destino.setText( '' )
                self.tela_transferir.lineEdit_transf_destino.setText( '' )
            elif recebe == 'naoachou':
                QMessageBox.information( None, 'Mensagem', 'Conta não existe!' )
                self.tela_transferir.lineEdit_numero_destino.setText( '' )
                self.tela_transferir.lineEdit_transf_destino.setText( '' )
        else:
            QMessageBox.information( None, 'mensagem', 'Digite um valor!' )
        self.tela_transferir.lineEdit_numero_destino.setText( '' )
        self.tela_transferir.lineEdit_transf_destino.setText( '' )
    def TelaFechar(self):
        """
        Solicita ao servidor o fechamento da conexão
        """
        mensagem = 'encerrar'
        mensagem = self.conectar_servidor.envia(mensagem)
        print(mensagem[0])

        quit()

if __name__ == '__main__':
    app = QApplication( sys.argv )
    show_main = Main()
    sys.exit( app.exec_() )
