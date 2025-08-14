import random

def spin_row():
    symbols = ['💰', '🍒', '💵', '🎲', '💎']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        return bet*20
    return 0


def main():
    balance = 100
    print()
    print("Welcome to the Python Slot Machine")
    print("     Symbols: 💰🍒💵🎲💎       ")
    print()

    while balance>0:
        print()
        print(f"Current balance: £{balance}")

        bet = input("Input bet amount: £ ")
        if not bet.isdigit():
            print()
            print("Invalid bet, please input a number.")
            continue

        bet = int(bet)

        if bet > balance:
            print()
            print("Insufficient funds")
            print()
            continue

        if bet <=0:
            print("Bet must be greater than £0")
            continue

        balance -= bet

        row = spin_row()
        print()
        print("Spinning...")
        print("--------")
        print_row(row)
        print("--------")

        payout = get_payout(row, bet)

        if payout>0:
            print(f"You won £{payout}!")
        else:
            print(f"You lost £{bet}...")
        
        balance += payout

        play_again = input("Spin again? (Y/N): ").upper()
        if play_again != 'Y':
            break

    print()
    print(f"Game over! Your final balance is £{balance}")
    print()


if __name__ == '__main__':
    main()