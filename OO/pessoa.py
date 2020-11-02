class Pessoa:
    olhos = 2 # atributo de classe padrão no instanciamento de todos os objetos da classe

    def __init__(self,*filhos, nome = None, idade = 35):#constrtur de uma classe
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos) # atributo complexo
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
    breno.sobrenome = "almeida" # instanciando um atributo dinamico 
    del bia.filhos #remoção de atributo de maneira dinamica 
    breno.__dict__ #visualização dos atributos presentes no objeto
