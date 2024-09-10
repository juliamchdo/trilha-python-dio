
# Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancaria (vincular com cliente) - a vontade de como fazer

# Criar usuário 
# armazenar em uma lista
# um usuário é composto por: nome, data nasc, cpf e endereco (logradouro - bairro - cidade/sigla e estado)
# não poderá ter mais de um usuário com o mesmo cpf

# Criar conta
# armazenar em uma lista
# uma conta é composta por: agencia, numero da conta e usuario
# o numero da conta é sequencial, iniciando em 1.
# o numero da agencia é fixo: 0001
# o usuario pode ter mais de uma conta



def menu ():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar Usuário
    [q] Sair

    => """

    return input(menu)


def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR${valor:.2f}\n"
        print('## Depósito realizado com sucesso ##')
    else:
        print("@@ O valor informado é inválido. @@")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(" @@ Operação falhou! Você não tem saldo suficiente. @@")

    elif excedeu_limite:
        print(" @@ Operação falhou! O valor do saque excede o limite. @@")

    elif excedeu_saques:
        print(" @@ Operação falhou! Número máximo de saques excedido. @@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print(" @@ Operação falhou! O valor informado é inválido. @@")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    nome = input("Nome: ")
    cpf = input("CPF: ")

    cpf_duplicado = any(cpf in d.values() for d in usuarios)

    if(cpf_duplicado):
        print(" @@ CPF inválido! Já existe um usuário cadastro com este mesmo CPF. @@")
        return
    
    data_nascimento = input("Data de nascimento: ")
    endereco = input("Endereço: ")

    print(cpf_duplicado)
    if(cpf_duplicado is False):
       usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
       print(" ## Usuário cadastrado com sucesso! ## ")
       return usuario

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
 
    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'u':
            usuario = criar_usuario(usuarios=usuarios)
            if(usuario):
                usuarios.append(usuario)
            print(usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
    

main()