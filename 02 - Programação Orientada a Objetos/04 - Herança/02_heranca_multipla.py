class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# O **kw é usado para aceitar argumentos nomeados (keyword arguments) adicionais na função/método. 
# Em Python, o **kw (ou qualquer outro nome de variável após **) coleta todos os argumentos passados por nome e os transforma em um dicionário.
# Quando o argumento é um keyword arguments, deve ser passado de forma nomeada
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
    
    def __str__(self):
        return 'Mamifero'


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

    def __str__(self):
        return 'Ave'


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)

        #Method Resolution Order é a ordem na qual Python busca métodos e atributos em uma hierarquia de classes.
        #Nesse exemplo, irá executar o método __str__ de acordo como for encontrado na hierarquia.
        print(Ornitorrinco.mro())

    def __str__(self):
        return 'Ornitorrinco'


gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)
