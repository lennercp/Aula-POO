class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    
    def ola(self):
        print('ola')

class aluno(Pessoa):
    def __init__(self):
        super().__init__('lenner', 17, 1.83)
        print(self.nome)
        print(self.idade)

a = aluno()
print(aluno.__mro__)
