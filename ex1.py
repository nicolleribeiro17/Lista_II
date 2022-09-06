#1. Dada as seguintes informações: Pessoa, cpf, nome e idade, crie uma classe onde teremos o retorno do documento, 
# o retorno do nome e verificação de tipo de pessoa, onde um método irá receber como parâmetro “F” ou “N” 
# para trazer fumante ou não fumante. Feito isso, crie uma instância e retorne esses valores

class Pessoa():
    def __init__(self, cpf, nome, idade, fumante):
        #Inicializa os atributos
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.fumante = fumante 
       
    def document(self):
        documento = (f'Nome = {self.nome} \nIdade = {self.idade} \nCPF = {self.cpf}' ) 
        return documento

    def smoker(self):
        if self.fumante == 'F':
            return (f'É fumante')
        else:
            return (f'Não é fumante')

dados1 = Pessoa('035.752.134-54', 'Nicolle', '23', 'N')

documento_pessoal = dados1.document()
print(documento_pessoal)
fumante = dados1.smoker()
print(fumante)

dados2 = Pessoa('032.435.675-90', 'Rafael', '28', 'F')

document_pessoal = dados2.document()
print(document_pessoal)
fumante1 = dados2.smoker()
print(fumante1)