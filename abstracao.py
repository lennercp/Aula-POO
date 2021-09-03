#escola
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    
    @abstractmethod
    def assinar(self):
        pass

p1 = Pessoa('lenner', 17, 1.7)