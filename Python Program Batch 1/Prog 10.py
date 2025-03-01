#CHECK IF THE NUMBERS ENDS WITH 0

nums = []  

for num in range(101):
    if not str(num).endswith("0"): 
        nums.append(num)

print(nums)