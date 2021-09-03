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

class Aluno(Pessoa):
    def __init__(self, notas):
        self.notas = notas

    def assinar(self):
        self.assinar = 'lista de presença'

class Professor(Pessoa):
    def __init__(self, graduacao, disciplina):
        self.graduacao = graduacao
        self.disciplina = disciplina

    def assinar(self):
        self.assinar = 'horario de aulas'

class Diretora(Pessoa):
    def __init__(self, graduacao):
        self.graduacao = graduacao
    
    def assinar(self):
        self.assinar = 'compra de materiais'