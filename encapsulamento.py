class banco:
    def __init__(self, login, senha):
        self._login = login
        self.__senha = senha

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, valor):

        self._login = valor


b1 = banco('lenner', '123')
print(dir(b1))
print(b1._banco__senha)