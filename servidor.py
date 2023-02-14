import pymysql.cursors
import socket
import random
from datetime import datetime
import hashlib
import threading

# recebendo os dados do cliente
def num_aleatorio():
    """
    Gera um numero aleatorio
    :return
        numero
    """
    num = (random.randint( 100, 200 ))
    return  num

def existir(num):# se o numero aleatorio ja existe
    """
    Verifica se numero da conta do cliente ja existe
    :param num:
        numero gerado aleatorio
    :return:
          True se ja foi cadastrado
    ou
        False se ainda não foi
    """
    conexao = pymysql.connect( host='localhost', db='', user='root', password='' )
    cursor = conexao.cursor()
    comando = f'SELECT contas WHERE numero="{num}"'
    cursor.execute( comando )
    for c in cursor:
        for i in c:
            if num in i:
                conexao.close()
                cursor.close()
                return True
    conexao.close()
    return False

def esta_bd(cpf): # verifica se o cpf ja esta cadastrado
    """
    Verifica se o cpf ja esta cadastrado no banco de dados
    :param cpf:
        cpf do cliente
    :return:
        False se ja foi cadastrado
    ou
        True se ainda não foi
    """
    conexao = pymysql.connect( host='localhost', db='', user='root', password='' )
    cursor = conexao.cursor()
    sql = """CREATE TABLE IF NOT EXISTS contas (id integer AUTO_INCREMENT PRIMARY KEY,
                                                                                                nome text NOT NULL, cpf text NOT NULL, nascimento text NOT NULL, senha text NOT NULL,saldo text NOT NULL, numero text NOT NULL, limite text NOT NULL);"""
    cursor.execute( sql )
    comando = f"select * from contas where cpf = '{cpf}'"
    cursor.execute( comando )
    for c in cursor:
        for i in c:
            if cpf == i:
                return False
    return True
def esta_cadastrado(nome,senha):
    """
    Verifica se o usuario ja esta cadastrado no banco de dados
    :param nome:
        nome do usuario
    :param senha:
    senha do usuario
    :return:
        True se ja foi cadastrado
    ou
        False se ainda não foi
    """
    # INSERE DADOS NO BANCO DE DADOS
    conexao = pymysql.connect( host='localhost', db='', user='root', password='' )
    cursor = conexao.cursor()

    #Incriptografando senha
    senha=senha.encode()
    senha = hashlib.md5(senha)
    senha = senha.hexdigest()

    comando = f'SELECT * from contas where nome="{nome}" and senha="{senha}"'
    cursor.execute( comando )

    for c in cursor:
        if nome in c and senha in c:
                return True
    return False

def create_hist(cliente):
    """
    Cria uma tabela historico no banco de dados  data de abertura da conta do cliente
    :param cliente:
        nome do cliente
    :return:
        none
    """
    conexao = pymysql.connect( host='localhost',  db='', user='root', password='' )
    cursor = conexao.cursor()
    sql = """CREATE TABLE IF NOT EXISTS hist_banc (id integer AUTO_INCREMENT PRIMARY KEY, nome text NOT NULL,
     data_transacao DATE NOT NULL, tipo_transacao VARCHAR(500) NOT NULL);"""
    cursor.execute( sql )
    data_trans = datetime.today()
    mensagem='Abertura de conta'
    comando = f'INSERT INTO hist_banc (nome, data_transacao,tipo_transacao) VALUES ("{cliente}","{data_trans}","{mensagem}")'
    cursor.execute( comando )
    conexao.commit()
    conexao.close()

def add_hist(cliente,mensagem,data_trans):
    """
    Adiciona o historico no banco de dados
    :param cliente:
            nome do cliente
    :param mensagem:
            historico de transações realizada pelo cliente:saque,deposito,transferencia
    :param data_trans:
            data do ocorrido
    :return:
            None
    """
    conexao = pymysql.connect( host='localhost', db='', user='root', password='')
    cursor = conexao.cursor()
    comando = f'INSERT INTO hist_banc (nome, data_transacao,tipo_transacao) VALUES ("{cliente}","{data_trans}","{mensagem}")'
    cursor.execute( comando )
    conexao.commit()
    conexao.close()

def modifi_destino(valor_trans,numero_destino,saldo):
    """
       Modifica o saldo do cliente
       ...
       Attributes:
           valor_trans : int
               valor transferido
           numero_destino : int
               numero da conta
           saldo : float
                saldo do cliente
       :return
           o saldo modificado
    """
    conexao = pymysql.connect( host='localhost',  db='', user='root', password='' )
    cursor = conexao.cursor()
    valor = int( valor_trans ) + int( saldo )
    valor = str( valor )
    comando = f'UPDATE contas SET saldo="{valor}" where numero="{numero_destino}"'
    cursor.execute( comando )
    conexao.commit()
    cliente_destino=''
    comando = f'SELECT nome from contas where numero="{numero_destino}"'
    cursor.execute( comando )
    for c in cursor:
        for i in c:
            cliente_destino = i
    conexao.close()
    return cliente_destino

def insere_historico(valor_trans,cliente_destino,numero_destino,cliente):
    """
        Cria o historico da funcao transfere, com os dados de quem envia e recebe
        ...
        Attributes:
            valor_trans : int
                valor transferido
            cliente_destino : str
                nome do cliente destino recebendo a transferencia
            numero_destino : int
                numero da conta
            cliente : str
                 nome do cliente transferindo
        :return
            None
        """
    data_trans = datetime.today()
    msg = 'Transferencia realizado no valor de ' + valor_trans + ' reais para nome: ' + cliente_destino + ', numero: ' + numero_destino
    add_hist( cliente, msg, data_trans )
    # inserindo no historico do cliente destino
    msg = 'Transferencia recebida no valor de ' + valor_trans + ' reais do cliente: ' + cliente
    add_hist( cliente_destino, msg, data_trans )

def saldo_destino(saldo,valor,cliente,numero_destino):
    """
    Realiza o saque a conta do cliente e
    Modifica o novo saldo na conta do cliente destino
    ...
    Attributes:
        saldo : float opcional
            saldo do cliente destino
        valor : int opcional
            valor a ser transferido
        cliente : str
            nome do cliente
        numero_destino : int
            numero da conta
    :return
        o saldo ja modificado
    """
    # Realizando saque do cliente
    conexao = pymysql.connect( host='localhost', db='', user='root', password='' )
    cursor = conexao.cursor()

    valor = int( saldo ) - (int( valor ))
    valor = str( valor )
    # saca da conta do cliente
    comando = f'UPDATE contas SET saldo="{valor}" where nome="{cliente}"'
    cursor.execute( comando )
    conexao.commit()
    # transfere para a conta destino
    comando = f'SELECT saldo from contas where numero="{numero_destino}"'
    cursor.execute( comando )
    saldo = ''
    for c in cursor:
        for i in c:
            saldo = i
    if saldo == '0.0':
        saldo = '0'
    return saldo

class cliente_Thread(threading.Thread):
    """
        A class representa um servidor criando uma conexão com cliente
        ...
        Parametros :
            estancia uma threading
        """
    def __init__(self, addr, socket, sinc):
        """
            Construtor com atributos necessario para criar varias conexões requerida pelo cliente
            ...
            Attributes:
                addr : int
                    endereco de conexão do cliente
                socket :
                    conexão do cliente
                sinc :
                    sincroniza um trecho de codigo referente a uma threading

        """
        threading.Thread.__init__(self)
        self.con = socket
        self.sinc = sinc
        print(f"Nova conexao de: {addr}")
        self.addr=addr

    def run(self):
        """
        Inicia a operação enviada do cliente
        :return: responde a requisicao do cliente
        """
        msg = ''
        while (msg != "encerrar"):
            # RECEBE DADOS DO CLIENTE
            msg = self.con.recv( 1024 ).decode()
            if (msg == 'encerrar'):
                msg="Cliente encerrado com sucesso!"
                self.con.send( msg.encode() )
                print(f'Encerrando Conexão do Cliente{self.addr}...')
                print( '\nAGUARDANDO CONEXAO...' )
                #break
            else:
                operacao = msg.split( ',' )
                # CADASTRO-------------------------------------------------------------------------
                if operacao[0] == '1':
                    nome = operacao[1]
                    cpf = operacao[2]
                    nascimento = operacao[3]
                    senha = operacao[4]
                    saldo = str( '0.0' )
                    limite = str( '1000.0' )
                    i = num_aleatorio()
                    numero=str(2+i)

                    if (esta_bd( cpf )) == True:
                        # INSERE DADOS NO BANCO DE DADOS
                        conexao = pymysql.connect( host='localhost',  db='', user='root', password='' )
                        cursor = conexao.cursor()
                        sql = """CREATE TABLE IF NOT EXISTS contas (id integer AUTO_INCREMENT PRIMARY KEY,
                                                                                            nome text NOT NULL, cpf text NOT NULL, nascimento text NOT NULL, senha text NOT NULL,saldo text NOT NULL, numero text NOT NULL, limite text NOT NULL);"""
                        cursor.execute( sql )
                        #extrato = ('Data de Abertura: ' + str(datetime.today()))
                        # insere informações no banco de dados
                        comando = f'INSERT INTO contas (nome, cpf, nascimento, senha,saldo, numero, limite) VALUES ("{nome}","{cpf}","{nascimento}",MD5("{senha}"),"{saldo}","{numero}","{limite}")'
                        cursor.execute( comando )
                        create_hist( nome )

                        enviar = 'cadastrado'
                        self.con.send( enviar.encode() )
                        conexao.commit()

                    else:
                        enviar = 'jacpf'
                        self.con.send( enviar.encode() )

                # LOGIN----------------------------------------------------------------------------------
                elif operacao[0] == '2':
                    nome = operacao[1]
                    senha = operacao[2]
                    if(esta_cadastrado(nome,senha) == True):
                        enviar = 'cadastrado'
                        self.con.send( enviar.encode() )
                    else:
                        enviar = 'naoacho'
                        self.con.send( enviar.encode() )

                # menu---------------------------------------------------------
                elif operacao[0] == '3':
                    nome= operacao[1]
                    numero=''
                    saldo=''
                    conexao = pymysql.connect( host='localhost', db='', user='root', password='' )
                    cursor = conexao.cursor()
                    comando = f'SELECT numero from contas where nome="{nome}"'
                    cursor.execute( comando )
                    for i in cursor:
                        for c in i:
                            numero = c
                    conexao.close()
                    self.con.send(numero.encode())
                # Depositar---------------------------------------------------------
                elif operacao[0] == '4':
                    numero=operacao[1]
                    valor=operacao[2]
                    cliente=operacao[3]

                    self.sinc.acquire()  # aguardando esse trecho de cod ser liberado
                    #inserindo no historico
                    msg = valor
                    data_trans = datetime.today()
                    msg = 'Deposito realizado no valor de '+ msg +' reais'
                    add_hist( cliente, msg, data_trans )
                    conexao = pymysql.connect( host='localhost',  db='', user='root', password='' )
                    cursor = conexao.cursor()
                    comando = f'SELECT saldo from contas where numero="{numero}"'
                    cursor.execute(comando)
                    saldo=''
                    for c in cursor:
                        for i in c:
                            saldo=i
                    if saldo!='0.0':
                        valor = (int(valor) + int(saldo))
                        valor = str(valor)

                    comando = f'UPDATE contas SET saldo="{valor}" where numero="{numero}"'
                    cursor.execute( comando )

                    conexao.commit()
                    conexao.close()

                    mensagem = 'depositado'
                    self.con.send( mensagem.encode() )
                    self.sinc.release()
                # Ver Saldo---------------------------------------------------------
                elif operacao[0] == '5':
                    cliente=operacao[1]
                    self.sinc.acquire()  # aguardando esse trecho de cod ser liberado
                    conexao = pymysql.connect( host='localhost', db='', user='root', password='' )
                    cursor = conexao.cursor()
                    comando = f'SELECT saldo from contas where nome="{cliente}"'
                    cursor.execute( comando )
                    saldo = ''
                    for c in cursor:
                        for i in c:
                            saldo = i
                    conexao.close()
                    self.con.send( saldo.encode() )
                    self.sinc.release()
                #VerExtrato-------------------------------
                elif operacao[0] == '6':
                    nome = operacao[1]
                    #self.sinc.acquire()  # aguardando esse trecho de cod ser liberado
                    conexao = pymysql.connect( host='localhost',  db='', user='root', password='' )
                    cursor = conexao.cursor()
                    lista = []
                    comando = f'SELECT data_transacao from hist_banc where tipo_transacao="Abertura de conta" and nome="{nome}"'
                    cursor.execute( comando )
                    for i in cursor:
                        for c in i:
                            lista.append('Abertura de conta: '+str(c))
                    comando = f'SELECT tipo_transacao from hist_banc where nome="{nome}"'
                    cursor.execute( comando )
                    for i in cursor:
                        for c in i:
                            if c !='Abertura de conta':
                                lista.append(str(c))
                    self.con.send(str(lista).encode())
                    conexao.close()
                    #self.sinc.release()
                # Sacar---------------------------------------------------------
                elif operacao[0] == '7':
                    numero = operacao[1]
                    valor = operacao[2]
                    cliente = operacao[3]
                    self.sinc.acquire()  # aguardando esse trecho de cod ser liberado
                    # inserindo no historico
                    msg = valor
                    data_trans = datetime.today()
                    msg = 'Saque realizado no valor de ' + msg + ' reais'
                    add_hist( cliente, msg, data_trans )
                    conexao = pymysql.connect( host='localhost',  db='', user='root', password='' )
                    cursor = conexao.cursor()
                    comando = f'SELECT saldo from contas where numero="{numero}"'
                    cursor.execute( comando )
                    saldo = ''
                    limite=1000
                    for c in cursor:
                        for i in c:
                            saldo = i
                    if saldo != '0.0' and  int(saldo) > int(valor):
                        valor = int( saldo )-(int( valor ))
                        valor = str( valor )
                        comando = f'UPDATE contas SET saldo="{valor}" where numero="{numero}"'
                        cursor.execute( comando )
                    elif limite > int(valor):
                        valor = int( saldo ) - (int( valor ))
                        valor = str( valor )
                        comando = f'UPDATE contas SET saldo="{valor}" where numero="{numero}"'
                        cursor.execute( comando )
                    else:
                        mensagem = 'semsaldo'
                        self.con.send( mensagem.encode() )
                    conexao.commit()
                    conexao.close()
                    mensagem = 'sacado'
                    self.con.send( mensagem.encode() )
                    self.sinc.release()
                # Transferir---------------------------------------------------------
                elif operacao[0] == '8':
                    numero_destino = operacao[1]
                    valor = operacao[2]
                    valor_trans=valor
                    cliente = operacao[3]
                    cliente_destino=''
                    self.sinc.acquire()  # aguardando esse trecho de cod ser liberado
                    conexao = pymysql.connect( host='localhost',  db='', user='root', password='' )
                    cursor = conexao.cursor()
                    # verifica se numDestino esta no banco
                    comando = f'SELECT * from contas where numero="{numero_destino}"'
                    cursor.execute( comando )
                    acho=0
                    for c in cursor:
                        for i in c:
                            if numero_destino == i: # se estiver no bank saca e deposita
                                acho=1
                    if acho==1:
                        comando = f'SELECT saldo from contas where nome="{cliente}"'
                        cursor.execute( comando )
                        saldo = ''
                        limite = 1000
                        for c in cursor:
                            for i in c:
                                saldo = i
                        if saldo == '0.0':
                            saldo = '0'

                        if saldo != '0' and int( saldo ) > int( valor ):#Realizando saque do cliente
                            saldo = saldo_destino(saldo, valor, cliente, numero_destino)
                            cliente_destino = ''
                            if saldo != '0':
                                cliente_destino = modifi_destino(valor_trans,numero_destino,saldo)
                                # inserindo no historico
                                insere_historico(valor_trans, cliente_destino, numero_destino, cliente)
                                conexao.commit()
                                mensagem = 'transferido'
                                self.con.send( mensagem.encode() )
                                conexao.close()
                            elif saldo =='0':
                                comando = f'UPDATE contas SET saldo="{valor_trans}" where numero="{numero_destino}"'
                                cursor.execute( comando )
                                conexao.commit()
                                comando = f'SELECT nome from contas where numero="{numero_destino}"'
                                cursor.execute( comando )
                                for c in cursor:
                                    for i in c:
                                        cliente_destino = i
                                # inserindo no historico
                                insere_historico(valor_trans, cliente_destino, numero_destino, cliente)
                                conexao.commit()
                                mensagem = 'transferido'
                                self.con.send(mensagem.encode())
                        elif limite > int( valor ):
                            saldo = saldo_destino(saldo, valor, cliente, numero_destino)
                            cliente_destino=''
                            comando = f'UPDATE contas SET saldo="{valor_trans}" where numero="{numero_destino}"'
                            cursor.execute( comando )
                            conexao.commit()
                            if saldo != '0':
                                cliente_destino = modifi_destino( valor_trans, numero_destino,saldo)
                                # inserindo no historico
                                insere_historico(valor_trans, cliente_destino, numero_destino, cliente)
                                conexao.commit()
                                mensagem = 'transferido'
                                self.con.send( mensagem.encode() )
                            elif saldo =='0':
                                comando = f'SELECT nome from contas where numero="{numero_destino}"'
                                cursor.execute( comando )
                                for c in cursor:
                                    for i in c:
                                        cliente_destino = i
                                # inserindo no historico
                                insere_historico(valor_trans, cliente_destino, numero_destino, cliente)
                                conexao.commit()
                                mensagem = 'transferido'
                                self.con.send( mensagem.encode() )
                        else:
                            mensagem = 'semsaldo'
                            self.con.send( mensagem.encode() )
                    else:
                        # numDestino nao esta no bank
                        mensagem = 'naoachou'
                        self.con.send( mensagem.encode() )
                    self.sinc.release()