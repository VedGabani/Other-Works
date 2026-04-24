# Sum of digits

print("----- Sum of digits -----\n")

num = input("Enter a number -_- ")
print("\n")

i = 0
total = 0

while i < len(num):
    total += int(num[i])
    i += 1

print("Sum of digits -_- ", total)
