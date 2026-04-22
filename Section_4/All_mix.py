while True:
            print("===== Section 4 - String Manipulation =====")
            print("16. Remove Spaces")
            print("17. Replace Word")
            print("18. Count Character")
            print("19. Split Sentence")
            print("20. Join Words")
            print("0. Back to Main Menu")

            sub = input("Enter your choice -_- ")
            print("\n")

            if sub == '16':
                print("----- Remove spaces -----\n")
                s = input("Enter a string -_- ")
                print("\n")
                print("Without spaces -_-", s.replace(" ", ""))

            elif sub == '17':
                print("----- Replace word -----\n")
                s = input("Enter a sentence -_- ")
                print("\n")
                old = input("Enter word to replace -_- ")
                print("\n")
                new = input("Enter new word -_- ")
                print("\n")
                print("Updated sentence -_-", s.replace(old, new))

            elif sub == '18':
                print("----- Count character -----\n")
                s = input("Enter a string -_- ")
                print("\n")
                ch = input("Enter character to count -_- ")
                print("\n")
                print("Occurrences -_-", s.count(ch))

            elif sub == '19':
                print("----- Split sentence -----\n")
                s = input("Enter a sentence -_- ")
                print("\n")
                print("Words list -_-", s.split())

            elif sub == '20':
                print("----- Join words -----\n")
                words = input("Enter words separated by space -_- ").split()
                print("\n")
                print("Joined string -_-", " ".join(words))

            elif sub == '0':
                print("Program is closing...")
                break

            else:
                print("Invalid choice -_- Try again\n")
