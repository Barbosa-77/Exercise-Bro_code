print(40 *"-")
print("Conversor de moeda")
print(40 *"-")


while True:
    conversao = str(input("Qual sera a moeda inicial: "))
    conversao2 = str(input("Qual sera a moeda final: "))

    conversao = conversao.capitalize() 
    conversao2 = conversao2.capitalize()

    valor = float(input("Digite o valor que vai converter: "))
    final = 0
    dolar_euro = valor*0.89
    dolar_real = valor*5.21
    real_euro = valor * 0.17
    real_dolar = valor * 0.19
    euro_real = valor * 5.87
    euro_dolar = valor * 1.13

    if conversao == "Dolar" and conversao2 == "Euro":
        final = (f"${dolar_euro:,.2f}")
    elif conversao == "Dolar" and conversao2 == "Real":
        final = (f"R${dolar_real:,.2f}")
    elif conversao == "Real" and conversao2 == "Euro":
        final = (f"${real_euro:,.2f}")
    elif conversao == "Real" and conversao2 == "Dolar":
        final = (f"${real_dolar:,.2f}")
    elif conversao == "Euro" and conversao2 == "Real":
        final = (f"R${euro_real:,.2f}")
    elif conversao == "Euro" and conversao2 == "Dolar":
        final = (f"R${euro_dolar:,.2f}")
    else:
        print("Error")
        print("Deseja refazer?")
        print("1 - Sim")
        print("2 - Nao")
        escolha = (input())
        if escolha == "1":
            continue
        else:
            break
    print(f"O valor convertido sera de {final}")
    break

    