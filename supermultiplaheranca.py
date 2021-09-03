class base:
    def __init__(self):
        print('base')

class primeiro(base):
    def __init__(self):
        print('primeiro: entrou')
        super(primeiro, self).__init__()
        print('primeiro saiu')

class segundo(base):
    def __init__(self):
        print('segundo: entrou')
        super(segundo, self).__init__()
        print('segundo saiu')
    
class terceiro(segundo, primeiro):
    def __init__(self):
        print('terceiro: entrou')
        super(terceiro, self).__init__()
        print('terceiro saiu')

segundo()
print('#################')
terceiro()
print(terceiro.__mro__)