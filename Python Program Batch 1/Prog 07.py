#SUM OF TEN NUMBERS

total = 0

for i in range(10):
    while True:
        try:
            num = float(input(f"Enter number {i + 1}: "))
            total += num
            break
        except ValueError:
            print("Invalid input.")

print(f"Total sum: {total}")