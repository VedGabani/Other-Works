# ATM

print("----- Welcome to ATM -----\n")

balance = 5000
correct_pin = 1234
attempts = 0

while attempts < 3:
    entered_pin = int(input("Enter your PIN: "))

    if entered_pin == correct_pin:
        print("Login Successful!")

        while True:
            print("\n--- ATM MENU ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            print("\n")

            choice = input("Enter your choice -_- ")
            print("\n")

            if choice == '1':
                print("\nYour balance is -_- ", balance)

            elif choice == '2':
                amount = float(input("Enter amount to deposit -_- "))
                print("\n")
                if amount > 0:
                    balance += amount
                    print("\nAmount deposited successfully!")
                else:
                    print("\nInvalid amount!")

            elif choice == '3':
                amount = float(input("\nEnter amount to withdraw -_- "))
                print("\n")
                if amount <= balance and amount > 0:
                    balance -= amount
                    print("\nPlease collect your cash.")
                else:
                    print("\nInvalid or insufficient balance!")

            elif choice == '4':
                print("\nThank you for using ATM!")
                break

            else:
                print("\nInvalid choice! Try again.")
        break

    else:
        attempts += 1
        print("\nIncorrect PIN! Attempts left -_- ", 3 - attempts)

if attempts == 3:
    print("\nToo many wrong attempts! Card blocked.")
