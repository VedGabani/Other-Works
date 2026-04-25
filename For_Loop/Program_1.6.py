# Find Largest number of list

n = list(map(int,input("Enter Number -_- ")))

largest = n[0]

for num in n:
    if num>largest:
        largest = num

print("Largest -_- ", largest)
