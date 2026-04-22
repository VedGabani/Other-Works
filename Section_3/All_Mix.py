while True:
            print("===== Section 3 - String Basics =====")
            print("11. Length + First & Last Character")
            print("12. Uppercase & Lowercase")
            print("13. Count Vowels")
            print("14. Reverse String")
            print("15. Palindrome Check")
            print("0. Back to Main Menu")

            sub = input("Enter your choice -_- ")
            print("\n")

            if sub == '11':
                print("----- String length + first & last character -----\n")
                s = input("Enter a string -_- ")
                print("\n")
                print("Length -_-", len(s))
                print("First character -_-", s[0])
                print("Last character -_-", s[-1])

            elif sub == '12':
                print("----- Uppercase and Lowercase -----\n")
                s = input("Enter a string -_- ")
                print("\n")
                print("Uppercase -_-", s.upper())
                print("Lowercase -_-", s.lower())

            elif sub == '13':
                print("----- Count vowels -----\n")
                s = input("Enter a string -_- ")
                print("\n")
                count = 0
                for ch in s:
                    if ch.lower() in "aeiou":
                        count += 1
                print("Number of vowels -_-", count)

            elif sub == '14':
                print("----- Reverse string -----\n")
                s = input("Enter a string -_- ")
                print("\n")
                print("Reversed string -_-", s[::-1])

            elif sub == '15':
                print("----- Palindrome check -----\n")
                s = input("Enter a string -_- ")
                print("\n")
                if s == s[::-1]:
                    print("It is a palindrome -_-")
                else:
                    print("Not a palindrome -_-")

            elif sub == '0':
                print("Program closing...")
                break

            else:
                print("Invalid choice -_- Try again\n")
