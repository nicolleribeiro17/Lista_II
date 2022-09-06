#Escreva uma classe “Quadrado”, crie dois métodos que retornem a área do quadrado e o perímetro, não crie a instância nesse exercício

class Quadrado():
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        area_quadrado = self.lado * self.lado
        return area_quadrado

    def perimetro(self):
        perimetro_quadrado = 4 * self.lado
        return perimetro_quadrado

