# Prime number check

print("----- Prime number check -----\n")

num = int(input("Enter a number -_- "))
print("\n")

i = 2
is_prime = True

while i < num:
    if num % i == 0:
        is_prime = False
        break
    i += 1

if num > 1 and is_prime:
    print("It is a prime number -_-")
else:
    print("Not a prime number -_-")
