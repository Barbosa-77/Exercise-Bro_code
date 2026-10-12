# Concession stand program


menu = {"Pizza": 3.00,
        "Nachos": 4.50,
        "Pipoca": 6.00,
        "Batata": 2.50,
        "Chips": 1.00,
        "Pretzel":3.50,
        "Refrigerante": 3.00,
        "Limonada":4.25
}

lista = []
total = 0

print("-------------- MENU --------------")
for key,value in menu.items():
    print(f"{key:10} : R${value:.2f}")
print("----------------------------------")


while True:
    comida = input("Escolha uma comida(digite q para cancelar): ").capitalize().strip()
    if comida == "Q":
        break
    elif comida not in menu:
        print("Opcao invalida")
    elif menu.get(comida) is not None:
        lista.append(comida)
print("-------------- SEU PEDIDO --------------")
for x in lista:
    total += menu.get(x)
    print(x)
print(f"\nO valor total do pedido: R$ {total:.2f}")
print("----------------------------------------")

#Mostrar quue a