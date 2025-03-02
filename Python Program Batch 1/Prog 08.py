#CHECK THE NUMBER OF ODD NUMBERS

nums = []

for i in range(10):
    while True:
        try:
            num = float(input(f"Enter number {i + 1}: "))

            if num % 2 != 0:
                nums.append(num)

            break
        except ValueError:
            print("Invalid input.")

print(f"The number of odd numbers is {len(nums)}.")