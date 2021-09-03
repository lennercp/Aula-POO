class Pagamento:
    def pagar(self):
        pass

class PagarCartao:
    def pagar(self):
        self.pagar = 'cartao visa'

class PagarBoleto:
    def pagar(self):
        self.pagar = 'boleto'

compra = PagarBoleto()
compra.pagar()
print(compra.pagar)