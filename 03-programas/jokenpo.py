import random

options = ("pedra","papel","tesoura",)
pontuacao_usario = 0
pontuacao_maquina = 0
funcionando = True

print(40*"-")
print("Jokenpo")
print(40*"-")

while funcionando:
    escolha_maquina = random.choice(options)
    escolha_usuario = input("\nEscolha entre Tesoura, Pedra ou Papel (Digite q para sair):\n").strip().lower()
    if escolha_usuario == "q":
            funcionando = False
    else:
        if escolha_usuario in options:
            print (f"Sua escolha = {escolha_usuario.capitalize()}")
            print(f"Escolha da maquina = {escolha_maquina.capitalize()}\n")
            if escolha_usuario == "tesoura" and escolha_maquina == "papel":
                print("Voce venceu!!")
                pontuacao_usario += 1
            elif escolha_usuario == "pedra" and escolha_maquina == "tesoura":
                print("Voce venceu!!")
                pontuacao_usario += 1
            elif escolha_usuario == "papel" and escolha_maquina == "pedra":
                print("Voce venceu!!")
                pontuacao_usario += 1
                #Possibilidade maquina
            elif escolha_usuario == escolha_maquina:
                print("Empate!!")
            elif escolha_maquina == "tesoura" and escolha_usuario == "papel":
                print("A maquina venceu!!")
                pontuacao_maquina += 1
            elif escolha_maquina == "pedra" and escolha_usuario == "tesoura":
                print("A maquina venceu!!")
                pontuacao_maquina += 1
            elif escolha_maquina == "papel" and escolha_usuario == "pedra":
                print("A maquina venceu!!")
                pontuacao_maquina += 1    
        else:
            print("Opcao invalida. Tente novamente\n")

diferenca = 0


print(40*"-")
print(f"Sua pontuacao = {pontuacao_usario}")
print(f"Pontuacao da maquina = {pontuacao_maquina}")
if pontuacao_usario > pontuacao_maquina:
    diferenca = pontuacao_usario - pontuacao_maquina
    print(f"Voce venceu por {diferenca} pontos de diferenca!!!")
    print(" Parabens!!!")
elif pontuacao_maquina > pontuacao_usario:
    diferenca = pontuacao_maquina - pontuacao_usario
    print(f"A maquina venceu por {diferenca} pontos de diferenca")
    print("Que azar!!!")
else:
    print("Empatou!")
print(40*"-")
