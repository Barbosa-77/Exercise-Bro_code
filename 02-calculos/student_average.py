while True:
    print("Calculadora de média de aluno")


    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    print(f"A media do aluno é {media:.2f}")

    if media >= 7:
        print("Aluno aprovado!")
    elif media >= 5: 
        print ("Aluno está de recuperação!")
    else:
        print("Aluno reprovado!")

    print("-" * 40)
    print("\nDeseja continuar?")
    print("1 - Sim")
    print("2 - Não")
    resposta = int(input("Digite a opção: "))
    if resposta == 1:
        pass
    elif resposta == 2:
        print("Obrigado por usar a calculadora de média de aluno!")
        break
    else:
        print("Opção inválida, encerrando o programa.")
        break