# Count a digit

print("----- Count a digit -----\n")

num = int(input("Enter number -_- "))
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Total digits:", count)
