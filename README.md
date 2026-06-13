from datetime import datetime


class JournalManager:
    FILE_NAME = "journal.txt"

    def add_entry(self):
        try:
            entry = input("Enter your journal entry: ")

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.FILE_NAME, "a") as file:
                file.write(f"[{timestamp}]\n")
                file.write(entry + "\n\n")

            print("Entry added successfully!")

        except Exception as e:
            print("Error:", e)

    def view_entries(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                content = file.read()

                if content.strip():
                    print("\nYour Journal Entries:")
                    print("-" * 40)
                    print(content)
                else:
                    print("No journal entries found.")

        except FileNotFoundError:
            print("No journal entries found. Start by adding a new entry!")

    def search_entry(self):
        try:
            keyword = input("Enter a keyword or date to search: ")

            with open(self.FILE_NAME, "r") as file:
                content = file.read()

            entries = content.split("\n\n")
            matches = []

            for entry in entries:
                if keyword.lower() in entry.lower():
                    matches.append(entry)

            if matches:
                print("\nMatching Entries:")
                print("-" * 40)
                for match in matches:
                    print(match)
                    print()
            else:
                print(f"No entries were found for the keyword: {keyword}")

        except FileNotFoundError:
            print("Error: The journal file does not exist.")
            print("Please add a new entry first.")

    def delete_all_entries(self):
        confirm = input(
            "Are you sure you want to delete all entries? (yes/no): "
        ).lower()

        if confirm == "yes":
            try:
                os.remove(self.FILE_NAME)
                print("All journal entries have been deleted.")

            except FileNotFoundError:
                print("No journal entries to delete.")
        else:
            print("Deletion cancelled.")

    def menu(self):
        while True:
            print("\nWelcome to Personal Journal Manager!")
            print("Please select an option:")
            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_entry()

            elif choice == "2":
                self.view_entries()

            elif choice == "3":
                self.search_entry()

            elif choice == "4":
                self.delete_all_entries()

            elif choice == "5":
                print("Thank you for using Personal Journal Manager!")
                break

            else:
                print("Invalid choice. Please try again.")


# Main Program
journal = JournalManager()
journal.menu()
