#SUM OF TEN NUMBERS

total = 0

while True:
    try:

        for i in range(10):
            nums = float(input("Enter number: "))
            total += nums

        print(total)
        break

    except ValueError:
        print("Invalid input.")