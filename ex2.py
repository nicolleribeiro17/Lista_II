# Escreva uma classe “PessoaFisica” e herde Pessoa, crie um método exclusivo para a classe e acesse-o

class Pessoa():
    def __init__(self, cpf, name, age, rg):
        #Inicializa os atributos
        self.cpf = cpf
        self.name = name
        self.age = age
        self.rg = rg
       
    def document(self):
        documento = (f'Nome = {self.name} \nIdade = {self.age} \nCPF = {self.cpf} \nRG = {self.rg}' ) 
        return documento


class PessoaFisica(Pessoa):
    def __init__(self, cpf, name, age, rg, type):
        #Não precisa inicializar as que vieram da outra classe, o super inicializa elas referenciando a classe base
        self.type = type

        super().__init__(cpf, name, age, rg)
        
    def get_type_person(self):
        if self.type == 'Fisica':
            return (f'Pessoa Física')
        else:
            return (f'Não é Pessoa Física')

person = PessoaFisica('036.837.134-21', 'Nicolle', '23', '9034353684', 'Fisica')
documento_pessoal = person.document()
print(documento_pessoal)
tipo_pessoa = person.get_type_person()
print(tipo_pessoa)
