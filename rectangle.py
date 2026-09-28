# Exercise 1 Rectangle Area Calc
while True:
    length = float(input("Digite a largura do retângulo: "))
    width = float(input("Digite a altura do retângulo: "))
    area = float(length * width)
    print (f"A área do retângulo é: {area}")

    print("Deseja calcular a área de outro retângulo? (s/n)")
    print("1 - Sim")
    print("2 - Não")
    option = int(input("Digite a opção: "))
    if option == 1:
        continue
    elif option == 2:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Encerrando o programa...")
        break