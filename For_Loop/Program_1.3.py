# Palindrome number

print("----- Palindrome number -----\n")

num = input("Enter a number -_- ")
print("\n")

rev = ""
for i in num:
    rev = i + rev

if num == rev:
    print("It is a palindrome -_- ")
else:
    print("Not a palindrome -_- ")
