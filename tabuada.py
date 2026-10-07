# Inicio, meio, fim


tabuada = int(input("De qual numero voce quer a tabuada? "))
inicio = int(input("Inicio da tabuada: "))
fim = int(input("Final da tabuada: "))

for i in range(inicio, fim+1):
    final = tabuada * i
    print(f"{i}x{tabuada} = {final}")