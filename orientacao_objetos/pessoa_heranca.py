class Pessoa():
    olhos = 2 #atributo de classe (ou default);

    def __init__(self, *filhos, nome = None, idade=35):#método para a criação inicial de atributos de dados
        self.filhos = list(filhos)# aqui temos um objeto complexo.
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}!'


    @staticmethod #usado pra criar método de classe sem relação com a classe ou objeto.
    def metodo_estatico():
        return 42

    @classmethod #também usado pra cria métodos de classe, mas aqui, ele é usado pra acessar dados da própria classe.
    def nome_e_atributos_de_classe(cls):
        return f'{cls} , olhos {cls.olhos} '

class Homem(Pessoa):#A classe homem herdou todos os atributos da classe 'Pessoa'. # tudo aqui é sobre sobrescrita de método.
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar() #'Super()'faz com que o print mostre a caracteristica da classe herdada nao importando se houver mudança da classe herdade exemplo de Pessoa para Mutante ou vice-versa.
        return f'{cumprimentar_da_classe}. Aperto de mão!'


class Mutante(Pessoa):#A classe Mutante herdou todos os atributos da classe 'Pessoa'(conceito de sobrescrita).
    olhos = 3 # aqui a sobrescrita do dado olhos sobrepoe o dado olhos herdado da classe Pessoa de dois para 3 olhos.

if __name__ == '__main__':
    renzo = Mutante(nome='Renzo') # o nome renzo é do tipo pessoa (tipo = int, float, e aqui pessoa)
    luciano = Homem(renzo, nome='Luciano') # aqui colocamos renzo como parametro ligado ao parâmetro filhos acima descrito e atributo de luciano.
    print(Pessoa.cumprimentar(luciano))#forma não usual de execução do método da classe.
    print(id(luciano))
    print(luciano.cumprimentar())#forma usual de execução do método da classe.
    print(luciano.nome) #acessar o atributo 'nome' usando o objeto p.
    print(luciano.idade) # acessar o atributo 'idade' usando o objeto p.
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.ramalho = 'Ramalho'
    #__dict__ = é usado pra checar e listar todos atributos de instância no método(__init__)
    # e os criados dinâmicamente.
    #del luciano.filhos = deleta o atributo filhos criado no atributo do método.
    del luciano.filhos
    #Pessoa.olhos = 3 # aqui houve a mudança do valor da classe pessoa o que altera o valor desse atributo para todos os objetos criados.
    #item acima virou comentário para que o conceito de sobrescrita fosse trabalhado.
    luciano.olhos = 1 # aqui o valor do atributo olhos mudou de 2 pra 1. Isso é constado pelo __dict__.
    del luciano.olhos # apagando-se o atributo dinâmico luciano.olhos=1 o valor do atributo olhos volta a ser 3.
    print(luciano.__dict__)
    print(renzo.__dict__)
#atributo de classe (ou default); tem valor único. A classe Pessoa vai sempre possuir 2 olhos para todos os objetos.
#Criou objeto Luciano ou Renzo? Pode-se acessar o atributo de classe através da instância, ou seja, luciano.olhos ou renzo.olhos.
#O valor será 2 sempre.
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos)), print(id(luciano.olhos)), print(id(renzo.olhos)) #o n° do atributo de classe é sempre o mesmo pra todos.
    print(Pessoa.metodo_estatico())# execução do método estático através da classe Pessoa.
    print(luciano.metodo_estatico())# ou execução do método extático através do objeto luciano.
    print(Pessoa.nome_e_atributos_de_classe())# executando o método classe através da classe.
    print(luciano.nome_e_atributos_de_classe()) #executando o método classe através do objeto.

    # podemos usar a ferramenta 'isinstance' para saber se um dado objeto é de determinado tipo/classe.
    pessoa = Pessoa('anonima') # pessoa(minusculo)é objeto Pessoa(maiusculo) é a classe.
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(renzo.olhos)
    print(luciano.cumprimentar())
    print(renzo.cumprimentar())










