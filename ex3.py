# Escreva uma classe “PessoaJurica” e herde Pessoa, agora modificando o comportamento, retorne o cnpj. 
# Crie uma instância e acesse os dados

class Pessoa():
    def __init__(self, cpf, name, last_name, age ):
        #Inicializa os atributos
        self.cpf = cpf
        self.name = name
        self.age = age
        self.last_name = last_name
       
    def document(self):
        documento = (f'Nome = {self.name} \nSobrenome = {self.last_name}\nIdade = {self.age} \nCPF = {self.cpf}' ) 
        return documento

class PessoaJuridica(Pessoa):
    def __init__(self, cpf, name, age, last_name, cnpj):
        self.cnpj = cnpj

        super().__init__(cpf, name, age, last_name)
    
    def get_cnpj(self):
        dado = (f'CNPJ = {self.cnpj}')
        return dado

pessoa = PessoaJuridica('036.837.134-21', 'Nicolle', 'Ribeiro', '23', '54.126.537/0001-17')
personal_document = pessoa.document()
print(personal_document)
cnpj = pessoa.get_cnpj()
print(cnpj)