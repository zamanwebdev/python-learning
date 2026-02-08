balance = 5000
transactions = []  # store all deposits & withdrawals

while True:
    print("\n=== Welcome to Mini ATM ===")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Mini Statement")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print(f"\n💰 Your current balance is: {balance}")

    elif choice == "2":
        try:
            withdraw = int(input("Enter withdraw amount: "))
            if withdraw <= 0:
                print("❌ Enter a positive amount only.")
            elif withdraw > balance:
                print("❌ Insufficient balance!")
            else:
                balance -= withdraw
                transactions.append(f"Withdraw: -{withdraw}")
                print(f"✅ Withdraw successful! Remaining balance: {balance}")
        except ValueError:
            print("❌ Invalid input! Numbers only.")

    elif choice == "3":
        try:
            deposit = int(input("Enter deposit amount: "))
            if deposit <= 0:
                print("❌ Enter a positive amount only.")
            else:
                balance += deposit
                transactions.append(f"Deposit: +{deposit}")
                print(f"✅ Deposit successful! Current balance: {balance}")
        except ValueError:
            print("❌ Invalid input! Numbers only.")

    elif choice == "4":
        if not transactions:
            print("\n📄 No transactions yet.")
        else:
            print("\n📄 Mini Statement:")
            for t in transactions:
                print(t)
            print(f"Current balance: {balance}")

    elif choice == "5":
        print("\n👋 Thank you for using Mini ATM. Goodbye!")
        break

    else:
        print("❌ Invalid choice! Enter 1-5 only.")
