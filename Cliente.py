from Banco import Banco


class Cliente(object):


    def __init__(self, idusuario=0, nome="", telefone="",
                 email="", endereco="", numero=""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.numero = numero


    def insertCliente(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into cliente (nome, telefone, email, "
                "endereco, numero) values('" + self.nome + "', '" +
                self.telefone + "', '" + self.email + "', '" +
                self.endereco + "', '" + self.numero+ "' )")

            banco.conexao.commit()
            c.close()

            return "Cliente cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do cliente"


    def updateCliente(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update cliente set nome = '" + self.nome + "',"
                        "telefone = '" + self.telefone + "', email = '" + self.email +
                        "', endereco = '" + self.endereco + "', numero = '" + self.numero +
                        "' where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Cliente atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do cliente"


    def deleteCliente(self):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from cliente where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Cliente excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do cliente"


    def selectCliente(self, idusuario):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from cliente where idusuario = " + idusuario + "  ")

            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.endereco = linha[4]
                self.numero = linha[5]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do cliente "