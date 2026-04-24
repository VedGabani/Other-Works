# Sum of first N natural numbers

print("----- Sum of first N natural numbers -----\n")

n = int(input("Enter a number -_- "))
print("\n")

sum = 0
for i in range(1, n + 1):
    sum += i

print("Sum -_- ", sum)
