import socket

class Conectar:
    """
    A class representa um cliente criando uma conexão com servidor
    """
    def __init__(self):
        """
        Construtor com atributos necessario para criar conexão com o servidor
        """
        self.ip = 'localhost' #definindo o endereço
        self.porta = 8006 #definindo o número de porta
        self.conectado = False
        self.cliente_socket = None

    def envia(self, msg):
        """
        Lida com o envio de mensagens
            Attributes:
                msg : str
                mensagem enviada ao servidor
            Returns :
                retorna o fechamento da aplicação
            ou
                retorna a mensagem enviada do servidor
        """

        if self.conectado == False:
            try:
                addr = (self.ip, self.porta) #criando tupla para armazenar o endereço e a porta
                self.cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # cria o socket e define o tipo de conexao e o tipo do protocolo de comunicaço
                self.cliente_socket.connect(addr)
                self.conectado = True
            except ConnectionRefusedError:
                return None

        if self.conectado == True:
            self.cliente_socket.send(msg.encode())
            msg_saida = self.cliente_socket.recv(1024).decode()
            if (msg == 'encerrar'):
                print( 'Conexao Encerrada...' )
                x = exit() 
                return x
            else:
                return msg_saida.split(',')

if __name__ == '__main__':
    cliente = Conectar()

    msg = ''
    while(msg != 'encerrar'):
        msg = input('Digite a operação: ')
        saida = cliente.envia(msg)
        print(f"\n{saida}\n")

