#PRODUCT OF TWO NUMBERS

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        product = num1 * num2
        print(f"Product: {product}")
        break
    
    except ValueError:
        print("Invalid input.")