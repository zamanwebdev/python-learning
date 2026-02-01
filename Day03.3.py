from datetime import datetime

name = input("Enter your name: ")
current_year = datetime.now().year

while True:
    try:
        birth_year = int(input("Enter your birth year: "))
        age = current_year - birth_year

        if birth_year > current_year:
            print("❌ Future year is not possible. Try again.\n")
        elif age > 120:
            print("❌ Age seems unrealistic. Enter a valid year.\n")
        else:
            print(f"\n✅ {name}'s age is now: {age}")
            break   # correct hole loop stop

    except ValueError:
        print("❌ Please enter numbers only.\n")
