# Exercise 2 Shopping cart program

item = input("Digite o nome do item: ")
price = float(input("Digite o preço do item:"))
quantity = int(input("Digite a quantidade do item: "))
total = price * quantity

print (f"Você comprou {quantity} x {item}/s")
print(f"O total a pagar por {quantity} {item}(s) é: R${total:.2f}")
