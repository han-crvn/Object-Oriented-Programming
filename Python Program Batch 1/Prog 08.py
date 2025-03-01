#CHECK THE NUMBER OF ODD NUMBERS

nums = []

while True:
    try:
        for i in range(10):
            num = float(input("Enter number: "))
            
            if num % 2 != 0:
                nums.append(num)

        print(f"Odd numbers are {nums}.")
        break

    except ValueError:
        print("Invalid input.")