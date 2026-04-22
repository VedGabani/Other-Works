# Swap Two Numbers

print("----- Swap Two Numbers -----\n")

a = input("Enter first number -_- ")
b = input("Enter second number -_- ")

a = int(a)
b = int(b)

a, b = b, a

print("After swapping")
print("First number -_- ", a)
print("Second number -_- ", b)
