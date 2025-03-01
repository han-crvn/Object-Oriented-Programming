#CHECK IF THE NUMBERS ARE EQUAL

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if num1 == num2:
            print("Equal")

        else:
            print("Not Equal")

        break
    
    except ValueError:
        print("Invalid input.")