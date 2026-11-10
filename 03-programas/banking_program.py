# Python Banking Program

# 1. Show Balance
# 2. Deposit
# 3. Withdraw
import time
# ===============Functions===================
def menu():
    print(40*"=")
    print("\n1 - Deposit")
    print("2 - Withdraw")
    print("3 - Show balance\n")
    print(40*"=")

def showbal():
    print(f"Your current balance is {balance:.2f}")

def deposit(dep):
    global balance
    balance = balance + dep

def withdraw(wit):
    global balance
    balance = balance - wit
# ===============Functions===================


balance = 2600.00

while True:
    menu()
    chose = int(input("Choose a number: (0 to quit)\n"))
    if chose > 3 or chose < 0:
        print("Invalid")
        continue
    else:
        match chose:
            case 1:
                dep = float(input("How much to deposit:\n"))
                deposit(dep)
                showbal()
            case 2:
                wit = float(input("How much to take:\n"))
                withdraw(wit)
                showbal()
            case 3:
                showbal()
            case 0:
                break
        time.sleep(1)    
        again = input("Another transition?(Y/N)\n")
        if again.upper() == "Y":
            time.sleep(1)
            continue   
        else:
            break  
         