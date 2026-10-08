#Shopping cart program

items = []
prices = []
discounts = []
total = 0
total_disc = 0

while True:
    item_buy = input("Coloque um produto(digite q para sair): ")
    if item_buy.lower() == "q":
       break
    else:
        price = float(input("Digite o preco do produto: R$ "))
        items.append(item_buy)
        prices.append(price)
        if price >= 200:
            discount = price * 0.20
            discounts.append(discount)

print("----- Seu carrinho ------")

for i in range(len(items)):

    print(f"{items[i]} - R${prices[i]:.2f}", end="\n")
    
for x in prices:
    total = total + x

for d in discounts:
    total_disc = total_disc + d

sub_total = total - total_disc
print(f"\nValor s/ desconto: R${total:,.2f}")
print(f"Desconto: R${total_disc:,.2f}")
print(f"\nTotal: R${sub_total:.2f}")