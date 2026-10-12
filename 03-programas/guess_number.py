import random

menor_num = 1
maior_num = 100
numero = random.randint(menor_num,maior_num)
chutes = 0
funcionando = True
print(40*"-")
print("Jogo da adivinhacao")
print(f"Escolha um numero entre {menor_num} e {maior_num}")
print(40*"-")
#print(numero)
while funcionando:
    chute = (input(f"Digite um numero entre {menor_num} e {maior_num} - (digite 00 para sair):\n").strip())
    if chute.isdigit():
        chute = int(chute)
        if chute == 00:
            funcionando = False
        elif chute < menor_num or chute > maior_num:
            print("O numero nao esta entre os numeros escolhidos")
            print("Tente novamente")
        elif chute > numero:
            print("Muito alto! Tente novamente")
            chutes += 1
        elif chute < numero:
            print("Muito baixo! Tente novamente")
            chutes += 1
        elif chute == numero:
            print("Voce acertou!! Parabens!!")
            chutes+= 1
            funcionando = False
    else:
          print("Chute invalido") 
    
   
print(40*"-")
print(f"Voce acertou o valor sorteado em {chutes} tentativas")
print(40*"-")

   