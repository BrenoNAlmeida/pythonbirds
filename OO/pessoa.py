class Pessoa:
    def __init__(self,*filhos, nome = None, idade = 35):#constrtur de uma classe
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return 'ola'
if __name__ == '__main__':
    breno = Pessoa(nome='breno')
    bia = Pessoa(breno,nome='bia')
    print(breno.cumprimentar())
    print(breno.nome)
    print(breno.idade)
    print(bia.filhos)
    for filho in bia.filhos:
        print(filho.nome)
