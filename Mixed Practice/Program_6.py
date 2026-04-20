import random

while True:
    print("\n==== MENU ====")
    print("1. Simple Calculator")
    print("2. Rock Paper and Scissors")
    print("3. Bill Generator")
    print("4. Age Calculator")
    print("5. Even/odd + Positive/Negative Check")
    print("6. Exit")

peint("\n")
choice = input("Enter your choice: ")

if choice == "1":

    a = int(input("Enter first number -_- "))
    b = int(input("Enter second number -_- "))

    print("Addition -_- ", a + b)
    print("Subtraction -_- ", a - b)
    print("Division -_- ", a / b)
    print("Multiplication-_- ", a * b)
    print("Modulus -_- ", a%b)
    print("Expontiation -_- ", a**b)
    print("Floor Division -_- ", a//b)

elif choice == "2":

    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)
    player = input("Choose Rock, Paper, Scissors: ")

    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie")
    elif (player == "Rock" and computer == "Scissors") or \
        (player == "Paper" and computer == "Rock") or \
        (player == "Scissors" and computer == "Paper"):
         print("You win!")
    else:
        print("You lose!")
'''
elif choice == "3":

    a = int(input("Enter Date -_- "))
    b = input("Enter Company name -_- ")
    c = int(input("Enter Payment Amount -_- "))
    d = int(input("Enter Due Date -_- "))

    print("\n")
    print(f"A {b}, Has to Pay , {c}  Before , {d} Bill Generated on , {a} ")
'''

elif choice == "4":

    a = int(input("Enter your Born Year -_- "))
    b = int(input("Enter Current Year -_- "))

    c = b-a

    print(f"You are {c} yeras old")

elif choice == "5":

a = int(input("Enter the Number -_- "))

print("\n")

if a%2 == 0:
    print("Number is Even.....")

else:
    print("Number is Odd.....")

elif choice == "6":
    print("Goodbye!")
    break

else:
        print("Invalid choice, try again.")
