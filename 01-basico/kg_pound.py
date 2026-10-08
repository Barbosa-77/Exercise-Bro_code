#Python weight converter

peso = float(input("Digite o peso:"))
print("1 - Kilogramas")
print("2 - Libras")

unit = input("Digite a unidade de medida (1 ou 2):")

if unit == "1":
    peso_libras = peso * 2.204
    print(f"{peso} kg e equivalente a {peso_libras:.2f} libras.")
elif unit == "2":
    peso_kg = peso / 2.204
    print(f"{peso} libras e equivalente a {peso_kg:.2f} kg.")
else:
    print("Opcao invalida. Finalizando o programa")
    pass
