while True:
    print("\n1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potenciação\n")

    opcao = int(input("Digite a operação que deseja realizar\n\n"))
    if opcao in [1,2,3,4,5]:
        num1 = float(input("Digite o primeiro número\n"))
        num2 = float(input("\nDigite o segundo número\n"))
    else:
        print("Opção inválida, tente novamente.\n")
        continue
        
    if opcao == 1:
        Resultado = num1 + num2
    elif opcao == 2:
        Resultado = num1 - num2     
    elif opcao == 3: 
        Resultado = num1 * num2   
    elif opcao == 4:
        Resultado = num1 / num2   
    elif opcao == 5:
        Resultado = num1 ** num2
    else:
        print("Opção inválida, tente novamente.\n")
        continue
    print(f"\nO resultado é {round(Resultado,3)}\n")
    print("-" * 40)
    print("\nDeseja realizar outra operação?")
    print("1 - Sim")
    print("2 - Não")
    resposta = input()

    if resposta == "1":
        pass
        print("-" * 40)
    elif resposta == "2":
        print("Obrigado por usar a calculadora!")
        break
    else:
        print("Opção inválida, encerrando o programa.")
        break
        