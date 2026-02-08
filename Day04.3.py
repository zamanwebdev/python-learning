balance = 5000

while True:
    try:
        withdraw = int(input("Enter withdraw amount: "))

        if withdraw <= 0:
            print("❌ Enter a positive amount only.\n")
        elif withdraw > balance:
            print("❌ Insufficient balance. Try again.\n")
        else:
            balance -= withdraw
            print(f"\n✅ Withdraw successful!")
            print(f"Remaining balance: {balance}")
            break  # exit loop after successful transaction

    except ValueError:
        print("❌ Invalid input! Numbers only.\n")
