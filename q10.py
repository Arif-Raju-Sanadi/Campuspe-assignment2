#Q10 ATM Simulator

balance=10000

print("ATM SIMULATOR")

while True:

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        print("Balance is:",balance)

    elif choice==2:
        amount=int(input("Enter amount: "))
        balance=balance+amount
        print("Deposit done")
        print("Balance now:",balance)

    elif choice==3:
        amount=int(input("Enter amount: "))

        if amount>balance:
            print("Not enough money")
        elif balance-amount<500:
            print("Minimum 500 must be left")
        else:
            balance=balance-amount
            print("Money withdrawn")
            print("Balance now:",balance)

    elif choice==4:
        print("Exit from ATM")
        break

    else:
        print("Wrong choice")