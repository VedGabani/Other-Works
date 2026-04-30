# Python program information
while True :

    choice = input("\nPress 1 to run program Press 2 to exit program -_- ")
    print("\n")

    if choice == '1':
        print("Welcome to world of Python!!!!")
        a = input("Enter your name -_- ")
        print(f"Hello {a}. I am speaker of python.\n")

        print(f"So {a} lets dive into world of Python.\n")
        print("Python is first made by Guido van Rossum a Dutch person.")
        print("First version of Python is  0.9.0")
        print("Guido van Rossum pass from University of Amsterdam (BS).")
        print("Born at 31 January 1956 (age 70).")

        print("\n Let's dive in some coding Part.")

        print("We use print funtion to print things")
        print("Now we will use input funtion to take things from user.")
        print("Here use id funtion and type funtion also.\n")

        a = int(input("Enter First number -_- "))
        b = int(input("Enter Second number -_- "))

        c = a+b
        print(f"Addition -_- {c} type -_- {type(c)} ID -_- {id(c)}")

        c = a-b
        print(f"Subtraction -_- {c} type -_- {type(c)} ID -_- {id(c)}")

        c = a*b
        print(f"Mutiplication-_- {c} type -_- {type(c)} ID -_- {id(c)}")

        c = a/b
        print(f"Division -_- {c} type -_- {type(c)} ID -_- {id(c)}")

        c = a//b
        print(f"Floor division -_- {c} type -_- {type(c)} ID -_- {id(c)}")

        c = a**b
        print(f"Exponentianal -_- {c} type -_- {type(c)} ID -_- {id(c)}")

        print("\nNow let's work with loops\n")

        start = int(input("Enter a number to start loop -_- "))
        end = int(input("Enter a number to end loop -_- "))
        skip = int(input("Enter a number to Skip -_- "))
        stop = int(input("Enter a number to stop -_- "))
        print("\nHere we use for loop and if else loop.\n")

        if end>start:
            for i in range(start , end+1):
               if i == stop:
                   print("Stoping at -_- ", i)
                   break
               if i == skip:
                    continue
               print(i)
        else:
            print("Enter a number which is greater than start loop")

    elif choice == '2':
        print("\nClosing Program.....")
        break
    else:
        print("Enter correct number.....")
