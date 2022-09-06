#Crie um professor de classe com atributos nome, idade e salário, onde o salário deve ter um método privado que não pode ser acessado fora da classe.
#a. Crie um método para acessar o método privado, onde é passada a identificação do usuário se ele pode ou não acessar.

from mailbox import NotEmptyError


class Professor():
    def __init__(self, nome, idade, salario): 
        self.nome = nome    
        self.idade = idade
        self.salario = salario

    def get_identity(self):
        prof = (f'Nome = {self.nome} \nIdade = {self.idade}')
        return prof
    
    def __get_secret_acess(self):
        salary = (f'Valor salário = {self.salario}')
        return salary

    def acess_secret_salary(self, nome):
        if nome == 'Silvia':
            return self.__get_secret_acess()
        else:
            return ('Você não tem acesso!')


professor = Professor('Silvia', '44', '5000')
dados = professor.get_identity()
print(dados)
acess = professor.acess_secret_salary('Silvia')
print(acess)