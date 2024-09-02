resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

#quando quer associar o mesmo valor para várias chvaes diferentess
resultado = dict.fromkeys(["nome", "telefone"], "mesmo valor")  # {"nome": "mesmo valor", "telefone": "mesmo valor"}
print(resultado)
