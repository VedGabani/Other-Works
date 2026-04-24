# Palindrome series

print("----- Palindrome -----\n")

num = int(input("Enter number -_- "))
temp = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if temp == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome")
