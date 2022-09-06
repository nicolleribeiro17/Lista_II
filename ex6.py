# 6. Crie um arquivo main.py, importe a classe “Quadrado”, crie uma nova instância e acesse seus métodos

from area_quadrado import Quadrado

quadrado = Quadrado(5)
area_final = quadrado.area()
perimetro_final = quadrado.perimetro()
print(f'Valor da área do quadrado: {area_final}')
print(f'Valor do perímetro do quadrado: {perimetro_final}')
