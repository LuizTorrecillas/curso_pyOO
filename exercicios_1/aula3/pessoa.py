class Pessoa:

    def __init__(self, nome, idade, profissao = ""):
        self._nome = nome.title()
        self._idade = int(idade)
        self._profissao = profissao.upper()

    def __str__(self):
        return self._nome

    def aniversario(self):
        self._idade += 1

    @property
    def saudacao(self):
        if self._profissao:
            return f"Ola, sou {self._nome} e trabalho como {self._profissao}"
        return f"Ola, sou {self._nome}"


pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

print("Informações Iniciais:")
print(vars(pessoa1))
print (vars(pessoa2))
print (vars (pessoa3))
print()

pessoa1.aniversario()
pessoa3.aniversario()

print("Informações após aniversário:")
print(vars(pessoa1))
print (vars (pessoa3))
print()

print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)
