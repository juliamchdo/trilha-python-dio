# Objetivo geral: iniciar a modelagem do sistema bancário em POO. Adicionar classes para cliente e as operações bancárias: depósito e saque.
# Atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários.

from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, cpf):
        self._cpf = cpf
        self.contas = []

    @property
    def cpf(self):
        return self._cpf

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(cpf)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._endereco = endereco

class Conta:
    def __init__(self, cpf_cliente, numero_conta):
        self._cpf_cliente = cpf_cliente
        self._numero_conta = numero_conta
        self.agencia = "0001"
        self._saldo = 0
        self.limite = 0
        self.LIMITE_SAQUES = 3

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero_conta(self):
        return self._numero_conta
    
    @property
    def cpf_cliente(self):
        return self._cpf_cliente
    
    @property
    def historico(self):
        return self._historico
    
    @saldo.setter
    def saldo(self, value):
        self._saldo += value

    @classmethod
    def criar_nova_conta(cls, contas, clientes):
        cliente_cpf = input("Informe o CPF do usuário: ")
        cliente_existente = verificar_cliente_existente(cliente_cpf, clientes)

        if not cliente_existente:
            print("@@ Não foram encontrados usuários com o CPF informado! @@")
            return
        
        numero_conta = len(contas) + 1

        conta = cls(cliente_cpf, numero_conta)
        contas.append(conta)
        cliente_existente.contas.append(conta)

        print("## Nova conta criada com sucesso! ##")
        print(f"Conta: {conta.numero_conta} \n Agência: {conta.agencia} \n Cliente: {conta.cpf_cliente}")

class Transacao(ABC):
    @abstractmethod
    def registrar(self, contas):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(contas):
        cliente_cpf = input("Informe o CPF da conta: ")
        conta = filtrar_conta(cliente_cpf, contas)
        
        if not conta:
            print("@@ Não foram encontradas contas com o CPF informado! @@")
            return
        
        valor = float(input("Valor do depósito: "))
        conta.saldo += valor
        print("## Depósito realizado com sucesso! ##")

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, contas):
        cliente_cpf = input("Informe o CPF da conta: ")
        conta = filtrar_conta(cliente_cpf, contas)

        if not conta:
            print("@@ Não foram encontradas contas com o CPF informado! @@")
            return
        
        valor = float(input("Valor do saque: "))
        
        if conta.limite == conta.LIMITE_SAQUES:
            print("@@ Você excedeu o limite de saques diários (3). @@")
            return
        
        conta.saldo =- valor
        conta.limite += 1

        print("## Saque realizado com sucesso! ##")

def criar_novo_cliente(clientes):
    nome = input("Nome: ")
    cpf = input("CPF (somente números): ")

    cliente_existente = verificar_cliente_existente(cpf, clientes)

    if cliente_existente:
        print(" @@ CPF inválido! Já existe um usuário com o CPF digitado. @@")
        return
        
    endereco = input("Endereço (Rua, logradouro, complemento): ")
    data_nascimento = input("Data de nascimento: ")
    cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)
    clientes.append(cliente)
    print("## Usuário cadastrado com sucesso! ##")

def filtrar_conta(cpf, contas):
    contas_filtradas = [conta for conta in contas if conta.cpf_cliente == cpf]
    return contas_filtradas[0] if contas_filtradas else None

def verificar_cliente_existente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def menu ():
    menu = """

    [d] Depositar
    [s] Sacar
    [u] Criar Usuário
    [c] Criar Conta
    [q] Sair

    => """

    return input(menu)

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            Deposito.registrar(contas)
        elif opcao == 's':
            Saque.registrar(contas)
        elif opcao == 'u':
            criar_novo_cliente(clientes)
        elif opcao == 'c':
            Conta.criar_nova_conta(contas, clientes)
        elif opcao == 'q':
            break
        else:
            print("@@ Opção inválida! @@")


main()