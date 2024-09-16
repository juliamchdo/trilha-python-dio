class ContaInvestimeno:
    def __init__(self, valor, usuario):
        self._valor = valor
        self.usuario = usuario

    @property
    def investimento(self):
        return self._valor * 1.5


conta = ContaInvestimeno(500, 'Julia')
print(conta.investimento)

    