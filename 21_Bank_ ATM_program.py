import time

def show_balance(balance):
    print()
    print(f"Your current balance is £{balance:.2f}")
    print()
    time.sleep(1)

def deposit():
    print()
    amount = float(input("Enter an amount to be deposited: £ "))
    print()
    if amount <0:
        print("Invalid deposit amount.")
        time.sleep(1)
        return 0
    else:
        print(f"Deposited £{amount}.")
        print()
        time.sleep(1)
        return amount
    
    
def withdraw(balance):
    print()
    amount = float(input("Enter an amount to be withdrawn: £ "))
    print()
    if amount > balance:
        print()
        print("Insufficient funds.")
        print()
        time.sleep(1)
        return 0
    elif amount < 0:
        print()
        print("Withdrawn amount must be more than £0.")
        print()
        time.sleep(1)
        return 0
    else:
        print()
        print(f"Successfully withdrawn £{amount}")
        print()
        time.sleep(1)
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Bank ATM. Would you like to: ")
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print()
            print("Invalid choice selection, please try again.")
            print()

    print()
    print("Thank you for using Bank ATM.")
    print()

if __name__ == '__main__':
    main()