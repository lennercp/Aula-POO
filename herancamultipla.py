class Ingles:
    def falar(self):
        return 'hello'

class Portugues:
    def falar(self):
        return 'oi'

class Bilingue(Portugues, Ingles):
    def falar(self):
        print(super(Bilingue, self).falar())

b = Bilingue()
b.falar()
print(Bilingue.__mro__)