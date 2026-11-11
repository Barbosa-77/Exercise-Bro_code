# Python Slot Machine
import random
import time

def spin_row():
    symbols = ["🍒","🍉","🔔","⭐","🍋"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍉":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 4
        elif row[0] == "🔔":
            return bet * 5
        elif row[0] == "⭐":
            return bet * 10
    else:
        return 0 


def show_balance(balance):
    print(f"Your current balance is {balance}\n")

def menu():
    print(40*"=")
    print(12*" ","Welcome to")
    print(14*" ","Python")
    print(11*" ","Slot Machine")
    print(6*" ","🍒 | 🍉 | 🔔 | ⭐ | 🍋")
    print(40*"=")

def main():
    balance = 100

    while balance > 0:
        menu()

        show_balance(balance)

        bet = (input("Place your bet amount: \n"))

        if not bet.isdigit():
            print("Your bet is invalid")
            print("Please, digit a number")
            continue
        else:
            bet = int(bet)

            if bet > balance:
                print("Insufficient founds")
                continue

            else:
                balance -= bet
                row = spin_row()
                print("Spinning....")
                time.sleep(1)
                print_row(row)
                payout = (get_payout(row, bet))
                if payout > 0:
                    print(f"Congratulations, you won ${payout}!!!")
                    balance += bet
                else:
                    print("You lost this round.")
        
    
        again = input("You want to try again? (Y/N):\n").upper()

        if again == "Y":
            continue
        elif again == "N":
            break
    






if __name__ == '__main__':
    main()