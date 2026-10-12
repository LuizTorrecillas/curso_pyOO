class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular.title()
        self._saldo = float(saldo)
        self._ativo = False

    def __str__(self):
        return f"Titular: {self.titular} | Saldo: R${self.saldo:.2f} | Status: {self.ativo}"

    @property
    def titular(self):
        return self._titular
    @property
    def saldo(self):
        return self._saldo
    @property
    def ativo(self):
        return "Ativa" if self._ativo else "Inativa"

    def ativar_conta(self):
        self._ativo = True


class ClienteBanco:

    clientes = []

    def __init__(self, nome, cpf, idade, email, profissao):
        self.nome = nome.title()
        self.cpf = cpf
        self.idade = int(idade)
        self.email = email
        self.profissao = profissao.title()
        ClienteBanco.clientes.append(self)

    @classmethod
    def criar_cliente_padrao(cls, nome, cpf):
        return cls(nome, cpf, 18, "nao_informado@email.com", "Não Informada")


# ================  testes  ====================



conta1 = ContaBancaria("Maria Silva", 1480.00)
conta2 = ContaBancaria("João Souza", 7899.54)

print(conta1)
print(conta2)
print()


conta1.ativar_conta()
print(f"Status da conta1 após ativar: {conta1.ativo}")
print()


print(f"Propriedade Titular: {conta1.titular}")
print()


cliente1 = ClienteBanco("Carlos Silva", "123.456.789-00", 30, "carlos@email.com", "Engenheiro")
cliente2 = ClienteBanco("Mariana Souza", "987.654.321-11", 25, "mariana@email.com", "Designer")
cliente3 = ClienteBanco("Felipe Costa", "456.789.123-22", 40, "felipe@email.com", "Médico")

print(f"Cliente 1: {cliente1.nome} | CPF: {cliente1.cpf} | Profissão: {cliente1.profissao}")
print(f"Cliente 2: {cliente2.nome} | Email: {cliente2.email}")
print(f"Cliente 3: {cliente3.nome} | Idade: {cliente3.idade}")
print()


cliente_padrao = ClienteBanco.criar_cliente_padrao("Ana Paula", "111.222.333-44")
print(f"Cliente criado via @classmethod: {cliente_padrao.nome} | Email: {cliente_padrao.email}")