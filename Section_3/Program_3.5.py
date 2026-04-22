# Palindrome check

print("----- Palindrome check -----\n")

s = input("Enter a string -_- ")
print("\n")

if s == s[::-1]:
    print("It is a palindrome -_- ")
else:
    print("Not a palindrome -_- ")
