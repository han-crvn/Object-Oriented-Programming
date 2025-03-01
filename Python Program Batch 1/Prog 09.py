#CHECKS THE EVEN NUMBER FROM 0 - 100

nums = []

for num in range(101):
    if num % 2 == 0:
        nums.append(num)

print(f"Even numbers are {nums}.")