while True:
    print("\n===== MENU =====")
    print("1. Integer to Float and String")
    print("2. Float to Integer (Truncation)")
    print("3. Numeric String + 10")
    print("4. Boolean to Integer")
    print("5. Sum of Two String Numbers")
    print("6. Exit")

    choice = input("Enter your choice (1-6) -_- ")

    # Option 1
    if choice == '1':
        num = int(input("Enter an integer -_- "))
        print("Float value -_- ", float(num))
        print("String value -_- ", str(num))

    # Option 2
    elif choice == '2':
        num = float(input("Enter a float number -_- "))
        print("Integer value -_- ", int(num))

    # Option 3
    elif choice == '3':
        num_str = input("Enter a numeric string -_- ")
        num = int(num_str)
        print("Result after adding 10 -_- ", num + 10)

    # Option 4
    elif choice == '4':
        print("True to int -_- ", int(True))
        print("False to int -_- ", int(False))

    # Option 5
    elif choice == '5':
        num1 = int(input("Enter first number (as string) -_- "))
        num2 = int(input("Enter second number (as string) -_- "))
        print("Sum:", num1 + num2)

    # Exit
    elif choice == '6':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
