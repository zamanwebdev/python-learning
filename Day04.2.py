while True:
    try:
        marks = int(input("Enter marks (0-100): "))

        if marks < 0 or marks > 100:
            print("❌ Invalid marks! Please enter between 0 and 100.\n")
        else:
            # Determine grade
            if marks >= 90:
                grade = "A+"
            elif marks >= 85:
                grade = "A"
            elif marks >= 80:
                grade = "A-"
            elif marks >= 75:
                grade = "B+"
            elif marks >= 70:
                grade = "B"
            elif marks >= 65:
                grade = "B-"
            elif marks >= 60:
                grade = "C+"
            elif marks >= 55:
                grade = "C"
            elif marks >= 50:
                grade = "C-"
            else:
                grade = "Fail"

            print(f"\n✅ Your Grade is: {grade}")
            break  # correct input, exit loop

    except ValueError:
        print("❌ Invalid input! Numbers only.\n")
