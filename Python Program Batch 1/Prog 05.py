#QUOTIENT OF TWO NUMBERS
      
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        quotient = num1 / num2
        print(f"Quotient: {quotient}")
        break
    
    except ValueError:
        print("Invalid input.")

    except ZeroDivisionError:
        print("Number can not be divided by zero")