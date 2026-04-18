# Vabidity Check

print("----- Validity Check -----\n")

age = int(input("Enter your age: "))
city = input("Enter your city: ")


valid_city = "Surat"

if age > 18 and valid_city == city:
    print("Access Granted ✅")
else:
    print("Access Denied ❌")
