class Lampada:

    def __init__(self, voltagem,cor):
        self.voltagem = voltagem
        self.cor=cor
        self.ligada= False

class ContaCorrent:
    
    def __index__(self, numeroConta, limite, saldo):
        self.numeroConta = numeroConta
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome=nome
        self.descricao=descricao
        self.valor=valor

class Usuario:

    def __init__(self, nome, email, senha):
        self.nome=nome
        self.email=email
        self.senha=senha





