
#calculo triangulo
def call_triangle ():
    base_of_triangle = float(input("Insira o valor da base em CM: "))
    height_of_triangle = float(input("Insira o valor da altura em CM: "))
    area_of_triangle = (base_of_triangle * height_of_triangle) / 2
    print (f"O valor da área do Triangulo é: {area_of_triangle} cm²")
#calculo circulo
def call_circle (value_of_pi):
    radius_of_circle = float(input("Insira o valor do raio em CM (OBS: Lembrando que o Raio é Diametro/2): "))
    area_of_circle = value_of_pi * (radius_of_circle ** 2) 
    print (f"A área do Circulo é de: {area_of_circle} cm²")
#calculo quadrado
def call_square ():
    height_of_square = float(input("Insira o valor da altura em CM: "))
    length_of_square = float(input("Insira o valor do comprimento em CM: "))
    area_of_square = height_of_square * length_of_square
    print (f"A área do retangulo é de: {area_of_square} cm²")
#calculo cilindro
def call_cylinder (value_of_pi):
    radius_of_cylinder = float(input("Insira o valor do raio em CM (OBS: Lembrando que o Raio é Diametro/2): "))
    height_of_cylinder = float(input("Insira o valor da altura em CM: "))
    volume_of_cylinder = (radius_of_cylinder ** 2) * height_of_cylinder * value_of_pi
    print (f"O volume do Cilindro é de: {volume_of_cylinder} cm³")