class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo #atributo privado
        self.nro_agencia = nro_agencia

    # métodos para manipular/retornar o valor de saldo, de forma que respeite o encapsulamento
    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia) #por não ser privado, poderia ser exibido dessa maneira
print(conta.mostrar_saldo())
