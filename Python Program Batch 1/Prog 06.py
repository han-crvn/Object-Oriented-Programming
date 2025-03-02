#FIRST NUMBER IS RAISED TO THE SECOND NUMBER

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        raised = num1 ** num2
        print(f"Raised: {raised}")
        break
    
    except ValueError:
        print("Invalid input.")