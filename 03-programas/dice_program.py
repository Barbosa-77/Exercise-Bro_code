# Dice program 
import random

dices_dic = {1: ("┌────────┐",
            "│        │",
            "│    ●   │", 
            "│        │",
            "└────────┘"
            ),
        2: ("┌────────┐",
            "│ ●      │",
            "│        │", 
            "│      ● │",
            "└────────┘"),
        3: ("┌────────┐",
            "│ ●      │",
            "│    ●   │", 
            "│      ● │",
            "└────────┘"),    
        4: ("┌────────┐",
            "│ ●    ● │",
            "│        │", 
            "│ ●    ● │",
            "└────────┘"),
        5: ("┌────────┐",
            "│ ●    ● │",
            "│    ●   │", 
            "│  ●   ● │",
            "└────────┘"),
        6: ("┌────────┐",
            "│ ●    ● │",
            "│ ●    ● │", 
            "│ ●    ● │",
            "└────────┘"),                       
        }


dices_list =[] 
total = 0

question = int(input("How many dices?: "))

for i in range (question):
    dices_list.append(random.randint(1,6))

for i in range(question):
    for line in (dices_dic.get(dices_list[i])):
        print(line)


for i in dices_list:
    total += i

print(f"Voce tirou {total}")