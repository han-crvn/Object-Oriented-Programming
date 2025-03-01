#FIND THE BIGGER NUMBER

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if num1 > num2:
            print(F"Bigger number: {num1}")

        elif num2 > num1:
            print(F"Bigger number: {num2}")

        else:
            print("both numbers are equal.")

        break

    except ValueError:
        print("Invalid input.")