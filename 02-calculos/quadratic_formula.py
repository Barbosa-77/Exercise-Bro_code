valor_a = int(input("Digite o valor de A: "))
valor_b = int(input("Digite o valor de B: "))   
valor_c = int(input("Digite o valor de C: "))

delta = valor_b**2 - 4 * valor_a * valor_c

if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    raiz = -valor_b / (2 * valor_a)
    print(f"A equação tem apenas uma raiz real: {raiz}")
else:
    raiz1 = (-valor_b + delta**0.5) / (2 * valor_a)
    raiz2 = (-valor_b - delta**0.5) / (2 * valor_a)
    print(f"A equação tem duas raízes reais: {raiz1} e {raiz2}")


