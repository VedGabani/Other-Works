while True:
    print("\n===== MENU =====")
    print("6. Area of Circle")
    print("7. Age Check for Voting")
    print("8. Swap Two Numbers")
    print("9. Celsius to Fahrenheit")
    print("10. Price Conversion")
    print("0. Exit")

    choice = input("Enter your choice -_- ")

    if choice == '6':
        r = input("Enter radius (as string) -_- ")
        r = float(r)
        area = 3.14 * r * r
        print("Area of circle -_-", area)

    elif choice == '7':
        age = input("Enter your age (as string) -_- ")
        age = int(age)

        if age >= 18:
            print("You are eligible to vote")
        else:
            print("You are NOT eligible to vote")

    elif choice == '8':
        a = input("Enter first number -_- ")
        b = input("Enter second number -_- ")

        a = int(a)
        b = int(b)

        a, b = b, a

        print("After swapping")
        print("First number -_- ", a)
        print("Second number -_- ", b)

    elif choice == '9':
        c = input("Enter temperature in Celsius -_- ")
        c = float(c)

        f = (c * 9/5) + 32
        print("Temperature in Fahrenheit -_- ", f)

    elif choice == '10':
        price = float(input("Enter price -_- "))

        print("Integer value -_-", int(price))
        print("Rounded value -_-", round(price))

    elif choice == '0':
        print("Closing Program...")
        break

    else:
        print("Invalid choice! Try again -_- ")
