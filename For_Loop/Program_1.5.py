# Reverse a string

print("----- Reverse a string -----\n")

s = input("Enter a string -_- ")
print("\n")

rev = ""
for i in s:
    rev = i + rev

print("Reversed string -_- ", rev)
