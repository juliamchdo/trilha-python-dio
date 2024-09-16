class Estudante:
    def __init__(self, nome, media_final):
        self.nome = nome
        self.media_final = media_final


    @classmethod
    def calcular_media_final(cls, nome, nota1, nota2, nota3):
        media_final = (nota1 + nota2 + nota3) / 3
        return cls(nome, media_final)
    
    @staticmethod
    def aprovar_aluno(media_final):
        if(media_final <= 5):
            return 'Aluno reprovado'
        else:
            return 'Aluno aprovado'
        

estudante1 = Estudante.calcular_media_final("Julia", 6, 7, 8)
estudante2 = Estudante.calcular_media_final("Pedro", 3, 5, 2)
print(estudante1.aprovar_aluno(estudante1.media_final))
print(estudante2.aprovar_aluno(estudante2.media_final))