import math

"""
r = float(input("Digite o valor do raio: "))

calculo = 2*(round(math.pi , 2))*r
print(f"A circunferencia do circulo e: {calculo}cm")

area = (round(math.pi,2)) * r**2
print(f"A Area do circulo e: {area}cm²")
"""

a = float(input("Digite o valor do cateto a: "))
b = float(input("Digite o valor do cateto b: "))

hip = math.sqrt((a**2) + (b**2))

print(f"O valor da hipotenusa e: {hip}")