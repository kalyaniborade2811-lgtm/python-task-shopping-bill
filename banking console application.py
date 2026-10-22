print("Welcome to Kiran Bank")

balance = 10000

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Deposit successful")
            print("Your balance is:", balance)
        else:
            print("Invalid amount")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount")
        elif amount <= balance:
            balance =  balance - amount
            print("Withdrawal successful")
            print("Your balance is:", balance)
        else:
            print("Insufficient balance")

    elif choice == "4":
        print("Thank you for using Kiran Bank")
        break

    else:
        print("Invalid choice")