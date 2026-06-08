# Q-6

print("\n1. only positive number")
print("2. both number")

a = int(input("Enter your choice -_- "))

match a:

    case 1:

        print("\n")

        b = int(input("Enter a number -_- "))

        if b > 0:
            if b % 2 == 0:
                print(f"{b} is EVEN")
            else:
                print(f"{b} is ODD")
        else:
            print("only positive number")

    case 2:

        print("\n")

        b = int(input("Enter a number -_- "))

        if b % 2 == 0:
            print(f"{b} is EVEN")
        else:
            print(f"{b} is ODD")

    case _:

        print("Invalid choice")
