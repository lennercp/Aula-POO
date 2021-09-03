class Pessoa:
    lista = []
    def __init__(self, idade, corCabelo, altura):
        self.idade = idade
        self.corCabelo = corCabelo
        self.altura = altura

    def add(self, valor):
        self.lista.append(valor)

p1 = Pessoa(18, 'moreno', 1.70)
p2 = Pessoa(28, 'loiro', 1.50)
p1.add(5)
p1.add(7)
p2.add(6)
print(p1.lista)