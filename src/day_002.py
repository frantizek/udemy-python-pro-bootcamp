def main() -> None:
    print("Welcome to the tip calculator!")

    # total_bill = float(input("What was the total bill ? "))
    while True:
        total_bill_str = input("What was the total bill ? ")
        try:
            total_bill = float(total_bill_str)
            if total_bill <= 0:
                print("¡Only *positive* numbers allowed! Try again.")
                continue
            break
        except ValueError:
            print(f"¡{total_bill_str} is not a valid number! Try again.")

    # tip = int(input("How much tip would you like to give? 10, 12, or 15 ? "))
    while True:
        tip_str = input("How much tip would you like to give? 10, 12, or 15 ? ")
        try:
            tip = int(tip_str)
            if tip not in [10, 12, 15]:
                print("¡Only 10, 12, or 15 allowed! Try again.")
                continue
            break
        except ValueError:
            print(f"¡{tip_str} is not a valid number! Try again.")

    # total_people = int(input("How many people to split the bill ? "))
    while True:
        total_people_str = input("How many people to split the bill ? ")
        try:
            total_people = int(total_people_str)
            if total_people <= 0:
                print("¡Only *positive* numbers allowed! Try again.")
                continue
            break
        except ValueError:
            print(f"¡{total_people_str} is not a valid number! Try again.")

    print(f"Each person should pay: {round((total_bill * (1 + (tip / 100))) / total_people, 2):.2f}")


if __name__ == "__main__":
    main()
