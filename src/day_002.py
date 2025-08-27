def main() -> None:
    print("Welcome to the tip calculator!")
    total_bill = float(input("What was the total bill ? "))
    tip = int(input("How much tip would you like to give? 10, 12, or 15 ? "))
    total_people = int(input("How many people to split the bill ? "))
    print(f"Each person should pay: {round((total_bill * (1 + (tip / 100))) / total_people, 2):.2f}")


if __name__ == "__main__":
    main()
