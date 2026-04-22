# Count vowels

print("----- Count vowels -----\n")

s = input("Enter a string -_- ")
print("\n")

count = 0

for ch in s:
    if ch.lower() in "aeiou":
        count += 1

print("Number of vowels -_- ", count)
